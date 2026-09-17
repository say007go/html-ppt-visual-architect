# Red consulting-deck design system

The theme is red-led, not red-saturated. Treat it as a token system that supports many page geometries, not as a page template.

## 1. Core tokens

```css
:root {
  --paper: #f1edec;
  --surface: #fffdfc;
  --surface-2: #f7f2f2;
  --surface-3: #eee7e7;
  --ink: #211a1b;
  --ink-2: #514749;
  --ink-3: #7c7072;
  --rule: #ddd3d5;
  --rule-strong: #c7b8bb;
  --red-950: #450b14;
  --red-900: #64111d;
  --red-800: #821827;
  --red-700: #a61e2d;
  --red-600: #bf3241;
  --red-300: #d99099;
  --red-100: #f1dadd;
  --red-050: #faf0f1;
  --gold: #9a742f;
  --gold-wash: #f5edda;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
}
```

Suggested page proportion: 65–75% warm whites and neutrals, 15–25% red washes and rules, 5–10% saturated or deep red. Use gold only for a genuinely separate meaning such as risk, assurance, or milestone.

## 2. Color roles

- `red-950/900`: chapter backgrounds, anchor nodes, final conclusions;
- `red-800/700`: active paths, decisive connectors, key figures, section markers;
- `red-100/050`: grouped zones, background fields, comparison sides;
- graphite: sustained reading text;
- neutral rules: alignment and structure.

Do not assign multiple reds as arbitrary categories. A shade change must encode hierarchy, intensity, stage, status, or emphasis. Pair color with position, label, border, or pattern so meaning survives grayscale.

## 3. Typography and density

Suggested font stacks:

- title: `"Source Han Serif SC", "Songti SC", STSong, SimSun, serif`;
- body: `"Noto Sans CJK SC", "Microsoft YaHei", "PingFang SC", Arial, sans-serif`;
- numbers and compact technical labels: `"IBM Plex Mono", "Cascadia Mono", monospace`.

At a 1200 × 675 slide:

| Role | Spacious | Standard | Dense |
|---|---:|---:|---:|
| title | 34–40 px | 30–36 px | 28–34 px |
| lead | 17–19 px | 15–18 px | 14–16 px |
| body primary | 16–19 px | 14–17 px | 12.5–15.5 px |
| annotation | 13–15 px | 12–14 px | 12–13 px |

Important content must not fall below 12 px. Long Chinese text normally needs 1.35–1.6 line height; use the tighter end only when line length and grouping remain clear.

Density is controlled by hierarchy, syntax compression, table economy, and carrier choice—not by shrinking everything. Dense pages should still expose three levels clearly: governing point, structural labels, supporting detail.

## 4. Grid and spatial rules

- Use a 12-column mental grid with 40–56 px outside margins at 1200 px width.
- Treat the grid as invisible infrastructure, not the visible result. A page may be precisely aligned without looking like a spreadsheet.
- Use a 4px or 8px spacing rhythm. Exact exceptions are allowed when required by mathematical geometry, but repeated gaps must be identical.
- Align the title, lead, and body to a shared left anchor unless the page concept deliberately breaks it.
- Every major element must align to at least one visible or inferred anchor: another edge, baseline, centerline, grid track, axis, or radius.
- Distinguish module spacing from internal spacing. The gap between semantic groups should normally be at least 1.5× the gap within a group.
- The main composition should normally occupy 65–85% of the usable body bounding area. Treat lower use as a warning to inspect unexplained whitespace, not as an automatic failure.
- Avoid large accidental voids. Empty space must separate levels, protect a focal point, route connectors, or establish deliberate asymmetry.
- Do not spread sparse content to every edge merely to hit an occupancy target.

### Editorial zoning and asymmetry

- Use asymmetry to establish hierarchy: one dominant graphic field and one smaller interpretation field often feels more authored than equal columns.
- For a diagram-led page, a core graphic commonly uses about 55–72% of the body and interpretation uses about 24–40%. These are capacity heuristics, never a fixed left/right template.
- The interpretation field may be a right or left rail, a bottom essay band, two stacked explanations, an inset, or open text aligned to a graphic level.
- Keep interpretation panels fewer and larger than ordinary modules. Two meaningful explanation zones are usually stronger than five small cards when the text describes shared dimensions.
- Preserve a clear gutter or boundary between structural and interpretive responsibilities, then reconnect them through labels, alignment, color, or a small number of leaders.
- Avoid full-body vertical and horizontal rules unless their axes encode real comparison, time, ownership, or status.

## 5. Geometry standards

These standards apply to all diagram families rather than prescribing a particular diagram:

- Repeated peers use common dimensions unless text load or semantic importance justifies a documented difference.
- Repeated positions come from CSS Grid/Flex tracks or calculated coordinates, never a list of arbitrary offsets.
- Parallel lines share endpoints, spacing, and direction.
- Circular or orbital arrangements use a common center, explicit radius, and equal or meaningfully weighted angles.
- Connector endpoints meet node edges or centers precisely; do not leave visible gaps or overshoot.
- Connector labels sit on a clear local background and do not cross unrelated nodes or text.
- A connector may be straight, orthogonal, curved, or radial according to meaning and surrounding geometry. Consistency within one diagram matters more than a universal connector style.
- If an annotation touches a node, its ownership must be unmistakable through alignment, proximity, leader line, or shared field.
- Any intentional asymmetry must strengthen reading order or emphasis; otherwise rebalance it.

## 6. Shape language

- Default corner radius: 0–4 px. Large pill radii are for tags and status only.
- Default shadow: none. Use a subtle shadow only when depth communicates foreground/background.
- Prefer hairline rules, filled bands, brackets, open fields, and direct labels over bordered rectangles everywhere.
- Use arrowheads only when direction might otherwise be ambiguous.
- Use SVG for exact connector geometry; keep wrapping text in HTML when practical.
- Use icons only when they reduce reading time. Avoid decorative icon grids, emoji, and icon-plus-card repetition.

## 7. Layout primitives, not templates

The reusable layer may include shell, safe area, spacing tokens, text roles, metric styles, line, bracket, node, label, tag, evidence note, field, band, axis, rail, route, boundary, table/chart styling, connector markers, and accessibility helpers.

Do not add reusable “three-card page,” “five-stage ring page,” or “left-text-right-diagram page” components. Those are compositions and must be derived per page.

Do not add “diagram with two explanation cards” as a page component either. Reuse only the underlying rail, field, heading, note, and connector primitives; let the content determine orientation, proportion, number of interpretation zones, and graphic topology.

## 8. Page atmosphere and deck rhythm

Light pages should feel analytical and calm. Dark red pages are punctuation: cover, chapter break, major synthesis, or conclusion. Red should create a narrative pulse rather than saturate every page.

Across the deck, vary background weight, primary direction, symmetry, focal position, and graphic-text coupling according to the storyline. Maintain stable typography, margins, footer, line behavior, and color semantics.

## 9. Accessibility and print

- Maintain strong contrast for body text.
- Never use color as the sole differentiator.
- Verify grayscale value contrast.
- Define `@media print` so each slide prints on a separate landscape page with no browser chrome.
