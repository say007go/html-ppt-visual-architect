#!/usr/bin/env python3
"""Static structural checks for HTML PPT decks. Uses only the Python standard library."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


RELATIONAL_TOKENS = {
    "timeline", "axis", "layer", "tree", "matrix", "flow", "route", "loop",
    "stack", "swimlane", "bracket", "connector", "architecture", "orbit",
    "funnel", "flywheel", "path", "spine", "landscape", "roadmap",
}


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[dict] = []
        self.slides: list[dict] = []
        self.meta_charset = False
        self.external_urls: list[str] = []

    @staticmethod
    def class_tokens(attrs: dict[str, str | None]) -> set[str]:
        return set((attrs.get("class") or "").split())

    def handle_starttag(self, tag: str, raw_attrs: list[tuple[str, str | None]]) -> None:
        attrs = dict(raw_attrs)
        classes = self.class_tokens(attrs)
        parent_slide = next((item["slide"] for item in reversed(self.stack) if item["slide"] is not None), None)
        slide = parent_slide

        if tag == "section" and "slide" in classes:
            slide = {
                "number": len(self.slides) + 1,
                "id": (attrs.get("id") or "").strip(),
                "layout": (attrs.get("data-layout") or "").strip(),
                "density": (attrs.get("data-density") or "").strip(),
                "coupling": (attrs.get("data-coupling") or "").strip(),
                "title": [],
                "lead": [],
                "cards": 0,
                "relational": 0,
                "primary": 0,
                "nodes": 0,
                "labels": 0,
                "svgs": [],
            }
            self.slides.append(slide)

        if tag == "meta" and (attrs.get("charset") or "").lower() == "utf-8":
            self.meta_charset = True

        if slide is not None:
            qa_role = (attrs.get("data-qa") or "").strip()
            if qa_role == "primary":
                slide["primary"] += 1
            elif qa_role == "node":
                slide["nodes"] += 1
            elif qa_role == "label":
                slide["labels"] += 1
            if "card" in classes or any(token.startswith("card-") or token.endswith("-card") for token in classes):
                slide["cards"] += 1
            if tag == "svg":
                slide["relational"] += 1
                slide["svgs"].append(attrs)
            if classes.intersection(RELATIONAL_TOKENS) or any(any(key in token for key in RELATIONAL_TOKENS) for token in classes):
                slide["relational"] += 1

        for attr_name in ("src", "href"):
            value = attrs.get(attr_name)
            if value and urlparse(value).scheme in {"http", "https"}:
                self.external_urls.append(value)

        self.stack.append({"tag": tag, "classes": classes, "slide": slide})

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                return

    def handle_data(self, data: str) -> None:
        if not data.strip() or not self.stack:
            return
        slide = next((item["slide"] for item in reversed(self.stack) if item["slide"] is not None), None)
        if slide is None:
            return
        active_classes = set().union(*(item["classes"] for item in self.stack))
        if "slide-title" in active_classes:
            slide["title"].append(data)
        if "slide-lead" in active_classes:
            slide["lead"].append(data)


def clean_text(parts: list[str]) -> str:
    return re.sub(r"\s+", " ", " ".join(parts)).strip()


def lint(path: Path) -> tuple[list[str], list[str], DeckParser]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"File is not valid UTF-8: {exc}"], warnings, DeckParser()

    parser = DeckParser()
    parser.feed(source)

    if not re.search(r"<!doctype\s+html", source, re.I):
        warnings.append("Missing <!doctype html>.")
    if not parser.meta_charset:
        errors.append("Missing <meta charset=\"utf-8\">.")
    if not parser.slides:
        errors.append("No <section class=\"slide\"> elements found.")

    ids = Counter(slide["id"] for slide in parser.slides if slide["id"])
    layouts = Counter(slide["layout"] for slide in parser.slides if slide["layout"])
    couplings = Counter(slide["coupling"] for slide in parser.slides if slide["coupling"])
    card_heavy = 0

    for slide in parser.slides:
        number = slide["number"]
        title = clean_text(slide["title"])
        lead = clean_text(slide["lead"])
        if not slide["id"]:
            errors.append(f"S{number}: missing unique id.")
        if not slide["layout"]:
            errors.append(f"S{number}: missing data-layout signature.")
        if slide["density"] not in {"dense", "standard", "spacious"}:
            warnings.append(f"S{number}: set data-density to dense, standard, or spacious.")
        if slide["coupling"] not in {"integrated", "diagram-led", "parallel"}:
            warnings.append(f"S{number}: set data-coupling to integrated, diagram-led, or parallel.")
        if slide["primary"] != 1:
            warnings.append(f"S{number}: expected one data-qa='primary' composition; found {slide['primary']}.")
        if not title:
            errors.append(f"S{number}: missing .slide-title text.")
        if not lead:
            errors.append(f"S{number}: missing .slide-lead text.")
        elif len(re.sub(r"\s+", "", lead)) < 18:
            warnings.append(f"S{number}: lead may be too short to govern the page.")
        elif len(re.sub(r"\s+", "", lead)) > 105:
            warnings.append(f"S{number}: lead may be too long for quick scanning.")

        if slide["cards"] >= 5 and slide["relational"] == 0:
            card_heavy += 1
            warnings.append(f"S{number}: {slide['cards']} cards and no detected relational graphic.")

        if slide["labels"] and not slide["nodes"]:
            warnings.append(f"S{number}: QA labels exist without QA nodes; geometry checks will be incomplete.")

        for svg in slide["svgs"]:
            if not svg.get("viewbox"):
                warnings.append(f"S{number}: SVG missing viewBox.")

    for slide_id, count in ids.items():
        if count > 1:
            errors.append(f"Duplicate slide id '{slide_id}' appears {count} times.")
    for layout, count in layouts.items():
        if count > 1:
            warnings.append(f"Layout signature '{layout}' repeats {count} times.")

    if len(parser.slides) >= 4 and len(couplings) == 1:
        only = next(iter(couplings), "unset")
        warnings.append(f"All slides use coupling mode '{only}'; review whether deck rhythm needs another valid mode.")

    analytical_count = max(1, len(parser.slides) - 2)
    if card_heavy / analytical_count > 1 / 3:
        errors.append("More than one third of analytical pages appear card-heavy without relational graphics.")

    if parser.external_urls:
        unique_urls = sorted(set(parser.external_urls))
        warnings.append(f"Remote dependencies detected ({len(unique_urls)}); verify that offline delivery is intentional.")

    return errors, warnings, parser


def main() -> int:
    argument_parser = argparse.ArgumentParser(description="Lint an HTML PPT deck for structural quality checks.")
    argument_parser.add_argument("html", type=Path, help="Path to the HTML deck")
    args = argument_parser.parse_args()

    if not args.html.is_file():
        print(f"ERROR: file not found: {args.html}")
        return 2

    errors, warnings, parsed = lint(args.html)
    print(f"Deck: {args.html}")
    print(f"Slides: {len(parsed.slides)} | Errors: {len(errors)} | Warnings: {len(warnings)}")
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN: {message}")
    if not errors and not warnings:
        print("PASS: static checks completed with no findings.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
