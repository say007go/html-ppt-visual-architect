# HTML implementation guidance

## Deliverable shape

Prefer one self-contained HTML file with inline CSS and JavaScript. Local assets are acceptable only when they materially improve the result. Avoid remote fonts, CDNs, or third-party chart libraries by default; the deck should open offline.

Use semantic slide markup, a unique `data-layout` value per page, an explicit `data-density="dense|standard|spacious"`, and `data-coupling="integrated|diagram-led|parallel"`. Keep page-specific CSS names semantic, such as `.governance-rights-field`, `.year-workstream-map`, or `.strategy-pressure-landscape`.

## Canvas and shell

- Use a fixed 16:9 `.slide` with `aspect-ratio: 16 / 9`.
- Use container query units where supported so typography and geometry scale with the slide.
- Keep the slide boundary clipped, but treat hidden overflow as a defect rather than a design technique.
- Keep header, lead, footer, and safe areas consistent; body compositions may differ freely.
- Use the denser shell only when the source requires it. Do not let a large header consume space needed by the content.

## CSS architecture

Separate design tokens, global shell and typography, shared micro-primitives, and page-specific compositions.

Do not create universal `.card-grid`, `.three-cols`, `.four-cards`, or named diagram-page templates. Reuse primitives and tokens; originate the composition.

Use CSS Grid for macro structure, Flexbox for one-dimensional alignment, and SVG for connection logic. Repeated elements must be governed by a shared layout or formula. Avoid multiple hard-coded `left/top` values when a grid, track, transform, or calculated polar placement would be more exact.

CSS Grid may implement an asymmetric editorial page, but do not expose every track as a bordered cell. Use gaps, open fields, selective rules, and differentiated proportions so the visible language follows the argument rather than the implementation technology.

For `diagram-led` pages, keep the core graphic and interpretation as separate semantic containers. The graphic should contain only labels needed to understand its primary visual structure; long rules, examples, and evidence belong in the interpretation container unless they change a mark, axis, boundary, stage, scale, or relationship.

Translate the visual blueprint into implementation layers rather than starting with DOM components:

`background fields and boundaries → axes/routes/connectors → structural marks or nodes → direct labels → annotations and evidence`

Use the implementation primitive that matches the visual variable: CSS Grid/Flex for aligned tracks and editorial zoning; SVG for exact paths, scales, boundaries, and calculated geometry; HTML for wrapping explanatory text. Do not express every visual grammar as absolutely positioned rectangles.

## QA annotations

Add lightweight hooks to help browser validation:

```html
<main class="slide-body">
  <div class="page-specific-composition" data-qa="primary">
    <article data-qa="node">...</article>
    <span data-qa="label">...</span>
  </div>
</main>
```

- `data-qa="primary"`: the main composition whose body coverage should be inspected;
- `data-qa="node"`: a bounded semantic node;
- `data-qa="label"`: a free-standing annotation or connector label, not ordinary text inside its own node;
- `data-qa-ignore`: intentionally excluded decorative or invisible elements.

These hooks do not determine the visual design. They make overlap and utilization checks more reliable.

The coupling attribute records the chosen information-responsibility strategy for deck-level review. It does not authorize a reusable page shell. Two `diagram-led` pages should still differ when their visual grammar, interpretation dimensions, or reading paths differ.

## SVG rules

- Set a `viewBox`; use responsive width and height.
- Add `<title>` and `<desc>` to meaningful diagrams.
- Use `<defs>` for reusable markers, gradients, masks, and filters.
- Use `vector-effect="non-scaling-stroke"` for fine rules when appropriate.
- Align paths precisely to node centers or edges and keep routing clear of unrelated content.
- Keep text in HTML when it needs to wrap. Overlay HTML labels on SVG geometry when necessary.
- Calculate repeated coordinates programmatically or from a documented formula. Do not approximate equal spacing manually.
- Keep one coordinate system for each coherent visual field. If a second visual grammar overlays the first, document the shared anchors or intersections that join them.
- Use one connector family for one relationship family. A return path, cross-cutting control rail, and primary process route must remain visually distinguishable.
- For quantitative or temporal graphics, derive mark positions from a documented scale. Never space unequal values evenly unless the encoding is explicitly ordinal.
- Draw fields, boundaries, and routes before nodes; draw labels and annotations after structural marks so the visual hierarchy remains stable.

## Charts and tables

Build quantitative charts only from supplied data. Annotate the implication beside the relevant mark. Remove redundant axes, legends, borders, and gridlines.

Use a table only for genuine row/column comparison. Keep entries concise but preserve qualifiers. If the source is categorical or incomplete, use a qualitative framework rather than fabricated scale.

## Interaction and encoding

The supplied runtime supports keyboard navigation, fullscreen, slide indexing, print separation, and `?qa=1`. Interaction is secondary; the deck must read correctly as a scrollable page and as a PDF.

Always include `<meta charset="utf-8">` as the first metadata element. Use the bundled UTF-8 server for review.

## Responsiveness

Optimize for presentation dimensions first. On narrow screens, scale the slide as one canvas rather than reflowing it into a mobile website. Reflow would alter the intended composition.

## Review loop

1. Run `content_coverage.py` against the source and resolve missing literals or suspiciously low units.
2. Run `static_lint.py` and fix structural findings.
3. Open through `serve.py` with `?qa=1` and inspect browser measurements.
4. Capture every slide at presentation size. Inspect the image, not only the live DOM.
5. Review first in grayscale or low-attention mode for hierarchy, then in color for finish.
6. Verify that the rendered visual still performs its declared perceptual task and that every visual variable carries its intended meaning.
7. Fix content fit, unexplained whitespace, weak focal points, misaligned geometry, awkward Chinese breaks, repeated compositions, accidental table language, and topology used where another grammar would be more truthful.
8. On `diagram-led` or `parallel` pages, inspect the graphic and interpretation separately, then together; remove duplicated copy and restore any missing semantic link.
9. Re-run all checks after material edits.

Source-code validity is necessary but insufficient. The rendered slide is the artifact.
