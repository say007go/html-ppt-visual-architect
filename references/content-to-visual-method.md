# Content-to-visual method

This method converts page copy into a content-faithful visual argument. It is a decision system, not a layout catalog.

## 1. Establish a content contract

Before composing, decompose each page into atomic source units. An atomic unit is the smallest statement that would change the meaning if removed: a claim, condition, example, number, output, exception, actor, stage, or mechanism.

Create a private ledger:

| Source unit | Role | Fidelity | Allowed treatment | Final carrier |
|---|---|---|---|---|
| exact number, date, name, commitment | evidence / constraint | exact | reposition only | metric, label, annotation |
| unique claim with qualifier | claim | semantic | shorten syntax, preserve qualifier | node, band, direct text |
| explanation of how something works | mechanism | semantic | structure into steps or connectors | path, layer, bracket |
| example or application scene | evidence | semantic | shorten, never generalize beyond source | callout, footnote, side rail |
| repeated context | context | mergeable | merge into lead or one surviving node | lead, shared label |
| unresolved content | placeholder | exact status | keep visibly unresolved | placeholder treatment |

Default to preserving every unique unit. Visual simplicity does not authorize content deletion.

### The coverage test

At the end, every ledger row must be visibly represented, legitimately merged with an identified equivalent, or disclosed as omitted because of a user-approved constraint.

Run `scripts/content_coverage.py` as a recall check. It cannot determine semantic equivalence, but it catches silent loss of numbers, named concepts, and whole source passages.

## 2. Derive the page's governing idea

Write one sentence answering: “What should the audience believe or decide after this page?” Put that judgment in the title or lead without changing the source's intent.

Separate content roles:

- **claim**: the conclusion or position;
- **mechanism**: how or why it works;
- **evidence**: numbers, examples, standards, or constraints;
- **implication**: what must be done or what follows.

One page may contain many units but should still have one governing claim. Multiple equal claims need an organizing relationship, not automatic deletion.

## 3. Build a visual-semantic model

First state the perceptual task: what must the audience see faster or more accurately than prose allows. Then identify the content atoms and semantic dimensions that control the visual model.

Actors or concepts may become nodes when connection or ownership matters, but not every page is a graph. Time, quantity, comparison, containment, position, distribution, and evidence may instead require axes, marks, boundaries, scales, fields, or annotations.

Relationships and dimensions may include:

- contains / governs / supports;
- precedes / triggers / transforms;
- compares / contrasts / substitutes;
- owns / decides / executes / supervises;
- inputs / outputs / depends on;
- reinforces / feeds back / constrains;
- measures / proves / qualifies / excepts.

Mark one semantic dimension as primary. A second dimension may become a rail, overlay, boundary, foundation, return path, evidence strip, or sublayer. Do not flatten a genuinely cross-cutting dimension into prose, but do not let secondary structure destroy the main reading path.

Meaning, visual variables, and forms are separate axes. “Five stages that reinforce one another” is meaning; a ring is only one possible geometry. The same meaning could become a return path, staged belt, orbit, or integrated mechanism field depending on truthfulness, text capacity, and emphasis.

For any substantive visual field, use [visual-semantic-synthesis.md](visual-semantic-synthesis.md) to map the perceptual task to visual variables, compose primary and secondary grammars, and define the geometry handoff.

## 4. Distribute responsibility between graphic and text

Classify each source unit by whether it changes the visual structure:

| Responsibility | Question | Preferred treatment |
|---|---|---|
| structural | Would removing this change a node, edge, boundary, layer, axis, or sequence? | encode in the core graphic |
| interpretive | Does it explain how the structure is configured, governed, operated, or understood? | structured interpretation field, side rail, or attached explanation |
| evidence | Does it prove, quantify, exemplify, or qualify the claim? | evidence strip, metric, example, or callout |
| implication | Does it state the decision, output, action, or consequence? | conclusion band, focal statement, or outcome field |

Then choose the coupling mode:

- **integrated**: graphic and detail must be read together because each detail belongs to a specific node, stage, or mark;
- **diagram-led**: the graphic is a compact, independently readable framework; separate text explains shared rules, operating dimensions, methods, examples, evidence, or implications;
- **parallel**: graphic and narrative provide two complementary views of the same judgment, such as model plus evidence or trend plus interpretation.

Use `diagram-led` when details do not alter the visual structure, apply across several marks or regions, repeat across the framework, or would force the graphic to become text-heavy. The interpretation zone may sit right, left, below, above, or partly inside an open field; do not turn “diagram-led” into a fixed left-diagram/right-text template.

For separated modes, preserve semantic linkage through one or more of:

- matching dimension names;
- numbered references used sparingly;
- shared color roles;
- a bracket, rail, or leader line;
- spatial alignment with the affected level;
- explicit wording such as “范围维”“动作维”“证据”“实施参数”.

Apply the three-part independence test:

1. Without the interpretation text, can the graphic still communicate the core structure?
2. Without the graphic, can the text still explain its assigned dimension?
3. Together, do they add understanding rather than repeat the same wording?

## 5. Write the visual thesis

A visual thesis describes meaning, direction, and emphasis:

- “Three strategic pressures converge into one talent imperative; each pressure retains its evidence and training implication.”
- “A role transition crosses four operating challenges, then resolves into four linked capability upgrades.”
- “A strategy-to-platform stack moves from group strategy through talent engineering to technical foundations, with service enablement as a vertical rail.”

Reject “use five cards,” “make a nice diagram,” or “place text in three columns.” Those describe containers, not arguments.

Also reject “use a loop,” “use an architecture diagram,” or “use a timeline” when the form was chosen before the perceptual task and visual variables. A valid thesis explains what the chosen position, direction, boundary, scale, or connection makes visible.

## 6. Budget space from information weight

For each semantic group estimate its importance, text load, relationship load, and evidence load. Allocate area accordingly. A long mechanism cannot live in the same-sized box as a two-word label. A decisive conclusion deserves more visual weight even if its text is short.

Use a page capacity sketch before styling:

```text
fixed shell = title + lead + footer
usable body = slide area - shell - safe margins
primary composition = normally 65–85% of usable body
supporting evidence = normally 15–35%, attached to its semantic owner
```

These are review ranges, not templates. A deliberate full-width table or single hero number may fall outside them.

### Density modes

- **dense**: detailed source, procurement content, mechanisms, evidence, or a user preference for high information density; preserve detail through hierarchy and compact carriers;
- **standard**: moderate detail and one main relationship;
- **spacious**: cover, chapter divider, single decision, or deliberate synthesis.

Do not infer `spacious` from a desire to make the slide look premium. Premium pages can be dense and disciplined.

## 7. Generate structural alternatives

Create at least two low-fidelity candidates. Change the perceptual encoding or spatial argument, not decoration. Useful transformations include:

- hierarchy as vertical stack versus nested landscape;
- sequence as horizontal route versus multi-track timeline;
- convergence as funnel versus diagonal pressure field;
- governance as central control tree versus decision-rights matrix with a control spine;
- loop as circular return path versus linear stages with an explicit feedback arc;
- portfolio as matrix versus shared platform with differentiated roles.

For multi-dimensional content, vary which semantic dimension becomes the primary skeleton and how the second dimension appears as an overlay, axis, field, foundation, boundary, or annotation. Do not assume a node-link topology is the neutral default.

When both are viable, change coupling as well as geometry: compare a deeply integrated candidate with a concise core graphic plus an interpretation field. This comparison is especially important when the integrated candidate produces many same-sized cells.

Select using five criteria:

1. source-unit coverage;
2. semantic accuracy;
3. reading-path clarity;
4. space utilization and text capacity;
5. contrast with adjacent slides.

Also test semantic gain: if structured prose or a true table communicates the same point with equal speed and less interpretation risk, do not force a graphic.

## 8. Choose information carriers

Do not equate content units with cards. Choose the carrier that communicates the unit's role:

- direct text for a claim that needs no boundary;
- band or field for a shared foundation;
- node for an actor, stage, or bounded object;
- connector for dependency, flow, delegation, or return;
- bracket for scope, aggregation, or common ownership;
- axis for progression, comparison, time, or maturity;
- nested frame for inclusion, platform, or governance boundary;
- table for true row/column comparison;
- annotation or evidence strip for proof, qualifier, exception, or example;
- metric treatment for supplied quantitative evidence.

If more than half the slide is equal rounded rectangles, redesign unless equality and modular independence are the actual message.

## 9. Detect accidental table language

A page may look like a table even without a `<table>`. Warning signs include:

- equal-width columns and equal-height rows dominating the body;
- full-height separators turning every idea into a cell;
- the same visual weight for claims, evidence, actions, and outputs;
- repeated rectangles whose position does not encode comparison or sequence;
- multiple adjacent pages using the same orthogonal grid rhythm.

Grid is legitimate when its axes carry meaning: time × workstream, role × permission, stage × output, or a true comparison. If the grid exists only to keep boxes tidy, replace it with an asymmetric anchor, core graphic plus interpretation, nested field, route, hierarchy, direct labels, or another relationship-bearing composition.

Do not pursue randomness. The goal is controlled editorial asymmetry: one strong visual center, a secondary explanatory zone, and stable alignment beneath the apparent freedom.

## 10. Use one dominant reading path

- left → right: cause, process, transformation;
- top → bottom: hierarchy, strategy deployment;
- center → outward: platform, ecosystem;
- outside → center: convergence, diagnosis;
- clockwise: recurring mechanism;
- foreground → background: priority, horizon.

Secondary content must attach to the item it explains. Avoid detached notes that force the viewer to guess the correspondence.

## 11. Design repeated geometry as a system

Repeated elements must share a computed rule:

- grid tracks for aligned peers;
- a common baseline or axis for stages;
- equal angular increments and a common radius for radial arrangements;
- consistent start/end anchors for parallel flows;
- shared columns for comparisons;
- documented offsets for intentional hierarchy.

Do not independently position repeated nodes by eye. Irregular geometry reads as accidental even when the conceptual idea is strong.

Geometry follows the selected visual grammar. Quantitative marks require a common scale; temporal elements require a common time axis; containment requires continuous boundaries; cross-cutting relationships require a visibly continuous rail or field; feedback requires a distinct return route. Do not solve every grammar with boxes and connectors.

## 12. Plan deck rhythm

Track each page's layout signature. Vary direction, density, symmetry, anchor, background weight, and graphic family only when the content supports it. Adjacent pages should not repeat the same geometry unintentionally, but originality is not random novelty.

Also vary coupling rhythm. Do not let every page embed all text in the primary graphic, and do not let every page become a main graphic with the same right-hand explanation rail. Repeat a coupling mode only because the content requires it.

The page sequence should escalate from context to diagnosis, solution, execution, evidence, and conclusion as appropriate to the source.

## 13. Edit for fit without changing substance

- Move repeated context into the lead.
- Turn noun lists into parallel labels.
- Split long syntax into heading + explanation + qualifier.
- Attach details to the relevant node or stage.
- Use abbreviated labels only when the full wording remains nearby.
- Preserve exact numbers, dates, contractual terms, regulatory language, outputs, exceptions, and control conditions.
- Never create fake data to justify a chart.

The page remains auditable when a reviewer can locate: why it matters, what acts on what, what is controlled, what is produced, and where conditions or exceptions apply.
