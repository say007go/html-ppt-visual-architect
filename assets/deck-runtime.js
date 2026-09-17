(() => {
  "use strict";

  const slides = () => Array.from(document.querySelectorAll(".slide"));
  const px = (value) => Number.isFinite(value) ? value : 0;

  function nearestSlideIndex() {
    const all = slides();
    const middle = window.scrollY + window.innerHeight / 2;
    let best = 0;
    let distance = Infinity;
    all.forEach((slide, index) => {
      const center = slide.offsetTop + slide.offsetHeight / 2;
      const delta = Math.abs(center - middle);
      if (delta < distance) {
        distance = delta;
        best = index;
      }
    });
    return best;
  }

  function goTo(index) {
    const all = slides();
    const target = all[Math.max(0, Math.min(index, all.length - 1))];
    if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function isVisible(element) {
    const style = getComputedStyle(element);
    const rect = element.getBoundingClientRect();
    return style.display !== "none" && style.visibility !== "hidden" &&
      Number(style.opacity || 1) > 0 && rect.width > 0 && rect.height > 0;
  }

  function visibleTextElements(slide) {
    const selector = "h1,h2,h3,h4,h5,h6,p,li,span,td,th,text";
    return Array.from(slide.querySelectorAll(selector)).filter(isVisible);
  }

  function intersectionArea(a, b) {
    const width = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
    const height = Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
    return width * height;
  }

  function outside(rect, boundary, tolerance = 1.5) {
    return rect.left < boundary.left - tolerance || rect.top < boundary.top - tolerance ||
      rect.right > boundary.right + tolerance || rect.bottom > boundary.bottom + tolerance;
  }

  function clippedByAncestor(element, slide) {
    const rect = element.getBoundingClientRect();
    let ancestor = element.parentElement;
    while (ancestor && ancestor !== slide.parentElement) {
      const style = getComputedStyle(ancestor);
      const clipsX = ["hidden", "clip", "auto", "scroll"].includes(style.overflowX);
      const clipsY = ["hidden", "clip", "auto", "scroll"].includes(style.overflowY);
      if (clipsX || clipsY) {
        const box = ancestor.getBoundingClientRect();
        if ((clipsX && (rect.left < box.left - 1 || rect.right > box.right + 1)) ||
            (clipsY && (rect.top < box.top - 1 || rect.bottom > box.bottom + 1))) {
          return true;
        }
      }
      if (ancestor === slide) break;
      ancestor = ancestor.parentElement;
    }
    return false;
  }

  function inspectPrimary(slide, number, findings) {
    const body = slide.querySelector(".slide-body");
    const primaries = Array.from(slide.querySelectorAll('[data-qa="primary"]')).filter(isVisible);
    if (primaries.length !== 1) {
      findings.push({ level: "warning", slide: number, message: `expected one primary composition; found ${primaries.length}` });
      return;
    }
    if (!body) return;
    const bodyRect = body.getBoundingClientRect();
    const primaryRect = primaries[0].getBoundingClientRect();
    const widthRatio = Math.min(primaryRect.right, bodyRect.right) - Math.max(primaryRect.left, bodyRect.left);
    const heightRatio = Math.min(primaryRect.bottom, bodyRect.bottom) - Math.max(primaryRect.top, bodyRect.top);
    const widthUse = Math.max(0, widthRatio) / Math.max(1, bodyRect.width);
    const heightUse = Math.max(0, heightRatio) / Math.max(1, bodyRect.height);
    const areaUse = Math.max(0, widthUse * heightUse);
    if (areaUse < 0.38 || widthUse < 0.62 || heightUse < 0.50) {
      findings.push({
        level: "warning",
        slide: number,
        message: `primary composition uses only ${Math.round(widthUse * 100)}% width × ${Math.round(heightUse * 100)}% height; inspect unexplained whitespace`,
      });
    }
  }

  function inspectGeometry(slide, number, findings) {
    const nodes = Array.from(slide.querySelectorAll('[data-qa="node"]')).filter(isVisible);
    const labels = Array.from(slide.querySelectorAll('[data-qa="label"]')).filter(isVisible);
    let collisions = 0;
    labels.forEach((label) => {
      const labelRect = label.getBoundingClientRect();
      nodes.forEach((node) => {
        if (node.contains(label) || label.contains(node)) return;
        if (intersectionArea(labelRect, node.getBoundingClientRect()) > 4) collisions += 1;
      });
    });
    if (collisions) {
      findings.push({ level: "warning", slide: number, message: `${collisions} free-standing label/node overlaps detected` });
    }
  }

  function runDeckQA() {
    const findings = [];
    const layoutCounts = new Map();
    const couplingCounts = new Map();

    slides().forEach((slide, index) => {
      const number = index + 1;
      const title = slide.querySelector(".slide-title");
      const lead = slide.querySelector(".slide-lead");
      const layout = (slide.dataset.layout || "").trim();
      const density = (slide.dataset.density || "").trim();
      const coupling = (slide.dataset.coupling || "").trim();
      const overflowX = slide.scrollWidth - slide.clientWidth;
      const overflowY = slide.scrollHeight - slide.clientHeight;
      const slideRect = slide.getBoundingClientRect();

      if (!title || !title.textContent.trim()) findings.push({ level: "error", slide: number, message: "missing slide title" });
      if (!lead || !lead.textContent.trim()) findings.push({ level: "error", slide: number, message: "missing lead paragraph" });
      if (!layout) findings.push({ level: "error", slide: number, message: "missing data-layout signature" });
      if (layout) layoutCounts.set(layout, (layoutCounts.get(layout) || 0) + 1);
      if (!["dense", "standard", "spacious"].includes(density)) {
        findings.push({ level: "warning", slide: number, message: "data-density should be dense, standard, or spacious" });
      }
      if (!["integrated", "diagram-led", "parallel"].includes(coupling)) {
        findings.push({ level: "warning", slide: number, message: "data-coupling should be integrated, diagram-led, or parallel" });
      } else {
        couplingCounts.set(coupling, (couplingCounts.get(coupling) || 0) + 1);
      }
      if (overflowX > 2 || overflowY > 2) {
        findings.push({ level: "error", slide: number, message: `slide overflow ${Math.ceil(overflowX)}px × ${Math.ceil(overflowY)}px` });
      }

      if (lead) {
        const length = lead.textContent.replace(/\s+/g, "").length;
        if (length < 18) findings.push({ level: "warning", slide: number, message: "lead may be too thin to govern the page" });
        if (length > 120) findings.push({ level: "warning", slide: number, message: "lead is long; verify body capacity" });
      }

      const textElements = visibleTextElements(slide);
      const smallText = textElements.filter((element) => px(parseFloat(getComputedStyle(element).fontSize)) < 12);
      if (smallText.length) findings.push({ level: "warning", slide: number, message: `${smallText.length} visible text elements below 12px` });

      const outsideText = textElements.filter((element) => outside(element.getBoundingClientRect(), slideRect));
      if (outsideText.length) findings.push({ level: "error", slide: number, message: `${outsideText.length} text elements extend outside the slide` });

      const clippedText = textElements.filter((element) => {
        // Browsers often report 1–3 px of glyph/line-box slop for CJK headings
        // and large numerals. Treat only material overflow as clipping.
        // SVGTextElement client/scroll metrics are unreliable under a scaled
        // viewBox or transformed group; bounding boxes and ancestor clipping
        // remain meaningful, but self-overflow metrics do not.
        const isSvgText = element.namespaceURI === "http://www.w3.org/2000/svg";
        if (!isSvgText && element.clientWidth > 0 && element.scrollWidth - element.clientWidth > 4) return true;
        if (!isSvgText && element.clientHeight > 0 && element.scrollHeight - element.clientHeight > 4) return true;
        return clippedByAncestor(element, slide);
      });
      if (clippedText.length) findings.push({ level: "error", slide: number, message: `${clippedText.length} text elements may be clipped` });

      const cards = slide.querySelectorAll(".card,[class*='card-'],[class*='-card']").length;
      const relational = slide.querySelectorAll("svg,.timeline,.axis,.layer,.tree,.matrix,.flow,.route,.loop,.stack,.swimlane,.bracket,.connector,.band,.field,.rail").length;
      if (cards >= 5 && relational === 0) {
        findings.push({ level: "warning", slide: number, message: "card-heavy page has no detected relational graphic" });
      }

      slide.querySelectorAll("svg").forEach((svg) => {
        if (!svg.getAttribute("viewBox")) findings.push({ level: "warning", slide: number, message: "SVG missing viewBox" });
        if (!svg.querySelector("title") || !svg.querySelector("desc")) {
          findings.push({ level: "warning", slide: number, message: "meaningful SVG should include title and desc" });
        }
      });

      inspectPrimary(slide, number, findings);
      inspectGeometry(slide, number, findings);
    });

    layoutCounts.forEach((count, layout) => {
      if (count > 1) findings.push({ level: "warning", slide: "deck", message: `layout signature '${layout}' repeats ${count} times` });
    });
    if (slides().length >= 4 && couplingCounts.size === 1) {
      const only = couplingCounts.keys().next().value;
      findings.push({ level: "warning", slide: "deck", message: `all slides use coupling mode '${only}'; review deck rhythm` });
    }

    const errors = findings.filter((finding) => finding.level === "error").length;
    const warnings = findings.filter((finding) => finding.level === "warning").length;
    const report = { slideCount: slides().length, errors, warnings, findings };
    window.__deckQAReport = report;
    return report;
  }

  function renderQAPanel(report) {
    document.querySelector(".deck-qa-panel")?.remove();
    const panel = document.createElement("aside");
    panel.className = "deck-qa-panel";
    panel.setAttribute("role", "status");
    const statusClass = report.errors ? "qa-error" : report.warnings ? "qa-warning" : "qa-pass";
    const statusText = report.errors ? `${report.errors} errors` : report.warnings ? `${report.warnings} warnings` : "all automated checks passed";
    panel.innerHTML = `<h3>Deck QA · ${report.slideCount} slides</h3><div class="${statusClass}">${statusText}</div>`;
    if (report.findings.length) {
      const list = document.createElement("ul");
      report.findings.forEach((finding) => {
        const item = document.createElement("li");
        item.className = finding.level === "error" ? "qa-error" : "qa-warning";
        item.textContent = `S${finding.slide}: ${finding.message}`;
        list.appendChild(item);
      });
      panel.appendChild(list);
    }
    document.body.appendChild(panel);
  }

  document.addEventListener("keydown", (event) => {
    if (["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement?.tagName)) return;
    const index = nearestSlideIndex();
    if (["ArrowDown", "ArrowRight", "PageDown", " "].includes(event.key)) {
      event.preventDefault();
      goTo(index + 1);
    } else if (["ArrowUp", "ArrowLeft", "PageUp"].includes(event.key)) {
      event.preventDefault();
      goTo(index - 1);
    } else if (event.key === "Home") {
      event.preventDefault();
      goTo(0);
    } else if (event.key === "End") {
      event.preventDefault();
      goTo(slides().length - 1);
    } else if (event.key.toLowerCase() === "f") {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen?.();
      else document.exitFullscreen?.();
    }
  });

  slides().forEach((slide, index) => {
    if (!slide.id) slide.id = `slide-${String(index + 1).padStart(2, "0")}`;
    slide.setAttribute("aria-label", slide.getAttribute("aria-label") || `Slide ${index + 1}`);
  });

  window.__deckQA = runDeckQA;
  if (new URLSearchParams(location.search).has("qa")) renderQAPanel(runDeckQA());
})();
