#!/usr/bin/env python3
"""Compare page-by-page Markdown source with visible HTML slide text.

This is a conservative recall checker, not a semantic-equivalence judge. It
flags critical literals that disappear and source units whose character-ngram
coverage is low after wording edits.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


PAGE_RE = re.compile(r"^\s*##\s+P(\d+)\b\s*(.*)$", re.I)
TABLE_RULE_RE = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*$")
NUMBER_RE = re.compile(
    r"(?<![A-Za-z0-9])\d+(?:\.\d+)?(?:[—-]\d+(?:\.\d+)?)?"
    r"(?:%|年|个月|月|周|天|次|项|个|家|国|地区|港口|岁|度)?",
)
QUOTE_RE = re.compile(r"[“\"]([^”\"]{2,40})[”\"]")
ACRONYM_RE = re.compile(r"\b[A-Z][A-Z0-9-]{1,11}\b")


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return "".join(ch for ch in text if ch.isalnum() or ch in "%")


def split_sentences(text: str) -> list[str]:
    return [part.strip(" \t:：-—") for part in re.split(r"[。；;！？!?]+", text) if part.strip(" \t:：-—")]


def markdown_units(source: str) -> list[dict]:
    pages: list[dict] = []
    current: dict | None = None

    for raw in source.splitlines():
        page_match = PAGE_RE.match(raw)
        if page_match:
            current = {"number": int(page_match.group(1)), "units": []}
            pages.append(current)
            title = re.sub(r"^[：:]\s*", "", page_match.group(2)).strip()
            if title:
                current["units"].append(title)
            continue
        if current is None:
            continue

        line = raw.strip()
        if not line or line == "---" or TABLE_RULE_RE.match(line):
            continue
        if line.startswith("|") and line.endswith("|"):
            cells = [cell.strip() for cell in line.strip("|").split("|") if cell.strip()]
            if cells:
                current["units"].append("；".join(cells))
            continue

        line = re.sub(r"^#{1,6}\s+", "", line)
        line = re.sub(r"^[-*+]\s+", "", line)
        line = re.sub(r"^\d+[.)、]\s*", "", line)
        current["units"].extend(split_sentences(line))

    for page in pages:
        seen: set[str] = set()
        clean: list[str] = []
        for unit in page["units"]:
            key = normalize(unit)
            if len(key) < 4 or key in seen:
                continue
            seen.add(key)
            clean.append(unit)
        page["units"] = clean
    return pages


class SlideTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, bool]] = []
        self.slides: list[list[str]] = []
        self.current: list[str] | None = None
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs_raw: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs_raw)
        classes = set((attrs.get("class") or "").split())
        starts_slide = tag == "section" and "slide" in classes
        if starts_slide:
            self.current = []
            self.slides.append(self.current)
        if tag in {"script", "style", "noscript"}:
            self.skip_depth += 1
        self.stack.append((tag, starts_slide))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
        for index in range(len(self.stack) - 1, -1, -1):
            stack_tag, starts_slide = self.stack[index]
            if stack_tag == tag:
                if starts_slide:
                    self.current = None
                del self.stack[index:]
                break

    def handle_data(self, data: str) -> None:
        if self.current is not None and not self.skip_depth and data.strip():
            self.current.append(data.strip())


def html_slides(source: str) -> list[str]:
    parser = SlideTextParser()
    parser.feed(source)
    return [" ".join(parts) for parts in parser.slides]


def ngram_counter(text: str, size: int = 2) -> Counter[str]:
    if len(text) < size:
        return Counter(text)
    return Counter(text[index : index + size] for index in range(len(text) - size + 1))


def recall_score(unit: str, slide: str) -> float:
    source = normalize(unit)
    target = normalize(slide)
    if not source:
        return 1.0
    if source in target:
        return 1.0
    size = 2 if len(source) >= 8 else 1
    wanted = ngram_counter(source, size)
    available = ngram_counter(target, size)
    matched = sum(min(count, available[token]) for token, count in wanted.items())
    return matched / max(1, sum(wanted.values()))


def critical_literals(units: list[str]) -> list[str]:
    found: list[str] = []
    for unit in units:
        found.extend(NUMBER_RE.findall(unit))
        found.extend(match.group(1) for match in QUOTE_RE.finditer(unit))
        found.extend(ACRONYM_RE.findall(unit))
    seen: set[str] = set()
    result: list[str] = []
    for literal in found:
        key = normalize(literal)
        if len(key) < 2 or key in seen:
            continue
        seen.add(key)
        result.append(literal)
    return result


def audit(markdown: Path, html: Path, min_page: float, min_unit: float) -> dict:
    pages = markdown_units(markdown.read_text(encoding="utf-8"))
    slides = html_slides(html.read_text(encoding="utf-8"))
    result = {
        "source": str(markdown),
        "deck": str(html),
        "source_pages": len(pages),
        "slides": len(slides),
        "min_page_coverage": min_page,
        "min_unit_coverage": min_unit,
        "page_results": [],
        "errors": [],
    }
    if len(pages) != len(slides):
        result["errors"].append(f"page-count mismatch: source={len(pages)}, deck={len(slides)}")

    for index, page in enumerate(pages):
        slide_text = slides[index] if index < len(slides) else ""
        unit_results = []
        weighted_sum = 0.0
        weight_total = 0
        for unit in page["units"]:
            score = recall_score(unit, slide_text)
            weight = min(80, max(4, len(normalize(unit))))
            weighted_sum += score * weight
            weight_total += weight
            if score < min_unit:
                unit_results.append({"score": round(score, 3), "text": unit})
        coverage = weighted_sum / max(1, weight_total)
        literals = critical_literals(page["units"])
        normalized_slide = normalize(slide_text)
        missing_literals = [literal for literal in literals if normalize(literal) not in normalized_slide]
        page_result = {
            "page": page["number"],
            "coverage": round(coverage, 3),
            "source_units": len(page["units"]),
            "low_coverage_units": unit_results,
            "missing_critical_literals": missing_literals,
        }
        result["page_results"].append(page_result)
        if coverage < min_page:
            result["errors"].append(f"P{page['number']}: coverage {coverage:.1%} below {min_page:.0%}")
        if missing_literals:
            result["errors"].append(f"P{page['number']}: missing critical literals: {', '.join(missing_literals)}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Markdown-to-HTML slide content recall.")
    parser.add_argument("source", type=Path, help="Page-by-page Markdown source")
    parser.add_argument("deck", type=Path, help="Generated HTML deck")
    parser.add_argument("--min-page", type=float, default=0.72, help="Minimum weighted page coverage")
    parser.add_argument("--min-unit", type=float, default=0.50, help="Threshold for listing weak source units")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    for path in (args.source, args.deck):
        if not path.is_file():
            print(f"ERROR: file not found: {path}")
            return 2
    result = audit(args.source, args.deck, args.min_page, args.min_unit)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Source pages: {result['source_pages']} | Deck slides: {result['slides']}")
        for page in result["page_results"]:
            print(
                f"P{page['page']}: coverage={page['coverage']:.1%} | "
                f"units={page['source_units']} | weak={len(page['low_coverage_units'])} | "
                f"missing_literals={len(page['missing_critical_literals'])}"
            )
            for literal in page["missing_critical_literals"]:
                print(f"  MISSING LITERAL: {literal}")
            for unit in page["low_coverage_units"][:8]:
                print(f"  LOW {unit['score']:.0%}: {unit['text']}")
            if len(page["low_coverage_units"]) > 8:
                print(f"  ... {len(page['low_coverage_units']) - 8} more low-coverage units")
        if result["errors"]:
            print("FAIL:")
            for error in result["errors"]:
                print(f"  {error}")
        else:
            print("PASS: no page fell below the coverage gate and all critical literals were found.")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
