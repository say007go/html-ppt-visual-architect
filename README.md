# HTML PPT Visual Architect

**HTML PPT 视觉架构师 · Consulting-Grade Presentation Design Skill**

> 将逐页演示文稿文案转化为高密度、视觉语义驱动、离线安全且可继续编辑的 HTML 演示稿。  
> Turn page-by-page presentation copy into dense, consulting-grade, semantically structured, self-contained HTML slides that remain editable, printable, and reviewable.

![Version](https://img.shields.io/badge/version-1.0.0-1f6feb)
![Output](https://img.shields.io/badge/output-self--contained%20HTML-f2cc60)
![Design](https://img.shields.io/badge/design-semantic%20visual%20architecture-a61e2d)

**Skill name:** <code>html-ppt-visual-architect</code>  
**中文名称：** HTML PPT 视觉架构师  
**作者 / Author：** 圣婴

### 语言选择 / Language Selection

- [中文文档 / Chinese Documentation](#zh)
- [English Documentation / 英文文档](#en)

---

<a id="zh"></a>

## 中文

### 1. 项目概述

<code>html-ppt-visual-architect</code> 是一个面向多模态 AI Agent 的咨询级 HTML 演示稿设计 skill。

它适用于用户已经准备好逐页文案、项目大纲或页面内容，希望将其转化为高站位、高信息密度、具有明确视觉论证关系的演示页面。

这个 skill 的核心不是套用一个固定模板，而是把每一页当作一个需要解决的“内容—语义—空间—视觉”系统：

- 先保留并梳理原始事实、数字、机制、案例和结论；
- 再识别页面需要让观众看懂的核心关系；
- 根据感知任务选择视觉语法、信息载体和阅读路径；
- 用 HTML、CSS 和 SVG 构建页面；
- 最后通过内容覆盖检查、静态结构检查、浏览器 QA 和渲染复核完成交付。

最终输出是一个自包含的 HTML 演示稿，可在浏览器中打开、打印和继续编辑，也可交给后续工具转换为 PPTX 或 PDF。

### 2. 它解决的问题

普通的自动排版工具往往在以下场景中失效：

- 页面信息密度高，无法同时容纳标题、总领段、证据、机制和行动含义；
- 所有内容都被压缩成重复的卡片墙、三栏布局或节点连线图；
- 图形好看，但没有表达真实的因果、层级、时间、边界或比较关系；
- 为了留白而静默删掉数字、限定条件、案例和关键事实；
- 页面之间看似整齐，实则每页都使用相同的布局，缺乏内容驱动的节奏；
- HTML 生成后没有覆盖检查、溢出检查或视觉复核。

本 skill 通过“内容与排版解耦、视觉语义先于形式、渲染结果优先于源代码”的方法，处理这些问题。

### 3. 核心价值

#### 3.1 保留事实，不牺牲信息密度

skill 会先建立内容台账，将每条源内容区分为：

- **关键字面事实**：数字、日期、名称、承诺、法规表述、阶段数量和明确输出；
- **独特主张**：需要保留原意与限定条件的判断；
- **支撑细节**：可以压缩，但必须靠近其支持的主张；
- **真实重复**：可以合并，并记录保留位置；
- **占位符**：继续显式保留，等待用户补充。

默认策略是保留信息。页面空间不足时，优先重组结构、压缩语法、改用更高效的载体或拆分信息责任，而不是为了制造空白直接删除内容。

#### 3.2 让视觉形式表达真实语义

页面中的位置、方向、边界、大小、颜色、连线、邻近关系和层级，都必须承担明确的信息责任。

例如：

- 时间关系使用时间轴、阶段带或回路；
- 层级关系使用嵌套、树形或阶梯；
- 因果关系使用方向和连接；
- 比较关系使用共享轴、矩阵或平行结构；
- 约束关系使用边界、护栏、括号或覆盖层；
- 证据关系使用标注、数据对象或支撑带。

图形不是装饰，卡片也不是默认答案。只有当形状能够表达分组、顺序、方向、规模、归属、依赖、边界、优先级、时间或状态时，才应使用它。

#### 3.3 形成真正的页面论证

每一页都必须具有：

- 结论式标题；
- 紧随标题的总领段；
- 可在三秒内识别的主要视觉论点；
- 与主论点匹配的证据、机制、例子或行动含义；
- 明确的阅读路径；
- 不依赖演讲者口头补充也能理解的结构。

图形和文字可以采用整合、图形主导或平行协同的不同关系，但必须各自承担清晰的信息责任，避免重复表达。

#### 3.4 让整套 deck 既统一又不千篇一律

全局使用稳定的红色咨询风格系统、字体、间距、画布和组件规范；局部页面则根据语义选择不同的视觉语法和空间拓扑。

因此，统一性来自：

- 颜色角色；
- 字体和层级；
- 画布与边距；
- 对齐锚点；
- 线条和形状语言；
- 页眉、页脚和导航行为。

差异性来自：

- 页面结论；
- 信息责任；
- 视觉语法；
- 图形与文字的耦合方式；
- 重点区域和阅读顺序。

#### 3.5 输出可交付、可预览、可验证的 HTML

输出不是代码片段，也不是设计说明，而是一个可以直接打开的 HTML 文件或完整 HTML deck：

- CSS、JavaScript 和必要资源可以内联或本地加载；
- 页面具备 16:9 画布和打印行为；
- 支持键盘翻页与全屏预览；
- 支持 <code>?qa=1</code> 显示浏览器端 QA 面板；
- 支持静态检查、内容覆盖检查和浏览器渲染检查；
- 优先保证离线可用，减少未经审查的远程依赖。

### 4. 核心特点

| 特点 | 具体能力 | 使用价值 |
| --- | --- | --- |
| 内容与排版解耦 | 先建立内容台账和语义模型，再决定页面形式 | 避免为了版式牺牲事实 |
| 视觉语义驱动 | 根据感知任务、视觉变量和信息关系选择图形语法 | 让图形真正表达业务逻辑 |
| 高密度排版 | 通过连续场、路径、层级、表格、注释和结构化文字承载信息 | 适合咨询、政企和企业培训场景 |
| 页面级原创构图 | 每页从语义关系推导独特布局，不机械套用模板 | 保持 deck 节奏和内容适配度 |
| 三种耦合模式 | integrated、diagram-led、parallel | 明确图形与文字各自的责任 |
| 自包含 HTML | 原生 HTML、CSS、SVG，离线安全且便于修改 | 易于预览、打印和后续转换 |
| 红色咨询设计系统 | 统一色彩角色、密度模式、网格、几何和形状行为 | 建立稳定的专业视觉识别 |
| 内容覆盖检查 | 对照 Markdown 源稿检查页面数量、文字覆盖和关键字面事实 | 降低漏文案和漏数字风险 |
| 浏览器端 QA | 检查标题、总领段、溢出、裁切、字号、SVG 和图形标签关系 | 在交付前发现结构性问题 |
| 双层视觉复核 | 先审线框结构，再审字体、红色强调、连线、几何和节奏 | 避免只看代码或只看装饰 |

### 5. 标准工作流程

~~~mermaid
flowchart LR
    A[逐页文案<br/>Page-by-page copy] --> B[内容台账<br/>Content ledger]
    B --> C[语义模型<br/>Semantic model]
    C --> D[空间架构<br/>Spatial system]
    D --> E[HTML / CSS / SVG]
    E --> F[Coverage + Static Lint]
    F --> G[Browser QA + Render Review]
    G -. 定向修复 .-> D
~~~

#### 第一步：Normalize without reducing

识别页面边界、标题、总领段、主张、证据、案例、数字、脚注和占位符，建立内容台账，明确哪些内容必须逐字保留、哪些内容允许压缩，以及最终由哪个信息载体承接。

#### 第二步：Model meaning before form

为每一页明确：

- 页面统领结论；
- 原子主张与证据；
- 时间、层级、因果、归属、比较、规模、边界、反馈和例外关系；
- 观众需要优先感知的任务；
- 结构信息、解释信息、证据信息和行动含义的责任分配。

#### 第三步：Solve the page as a spatial system

建立构图台账，规划：

- 页面标题和总领段；
- 信息组及其重要性；
- 主次语义维度；
- 视觉变量和视觉语法；
- 图形与文字的耦合方式；
- 空间区域、信息载体、阅读路径和焦点；
- 页面密度模式、几何锚点和独特视觉签名。

在低保真阶段至少比较两个有实质差异的构图候选。差异应来自编码方式或视觉语法，而不仅是换颜色或重新排列卡片。

#### 第四步：Build a page-specific visual argument

让页面结论在三秒内可识别，主感知任务在小字阅读前就能理解。每个图形必须说明它表达的关系，每条连线必须有明确起点、终点和语义目的。

当长篇解释文字不会改变图形节点或连线时，优先采用 <code>diagram-led</code>；当图形与结构化文字需要分别成立并共同支持判断时，采用 <code>parallel</code>；当结构和细节必须在同一语义归属下理解时，采用 <code>integrated</code>。

#### 第五步：Build the global shell

从 <code>assets/deck-core.css</code> 和 <code>assets/deck-runtime.js</code> 开始，或将其内联到一个自包含 HTML 文件中。

每页遵循统一的语义契约：

~~~html
<section class="slide" id="slide-01"
         data-layout="unique-semantic-name"
         data-density="dense"
         data-coupling="diagram-led">
  <header class="slide-head">
    <div class="slide-kicker">章节 · 页面类型</div>
    <h2 class="slide-title">结论式标题</h2>
    <p class="slide-lead">承上启下的总领段，概括本页核心主旨。</p>
  </header>
  <main class="slide-body">
    <div data-qa="primary">页面专属构图</div>
  </main>
  <footer class="slide-foot"><span>项目名</span><span>01</span></footer>
</section>
~~~

#### 第六步：Validate content before admiring the layout

有源 Markdown 文稿时，运行内容覆盖检查，查找缺失的关键字面事实和覆盖率较低的源内容单元。检查器是召回辅助，不代替人工判断语义等价、合理改写和真实重复。

#### 第七步：Render and inspect

用本地 UTF-8 服务打开 HTML，逐页查看正常演示尺寸，生成页面截图或缩略图，并通过 <code>?qa=1</code> 查看浏览器 QA 报告。

#### 第八步：Perform a two-pass visual review

**线框复核：** 关注内容覆盖、阅读路径、面积分配、对齐锚点、文字容量、图形与文字责任，以及无法解释的空白。

**完成度复核：** 关注字体、红色强调、线宽、连线、几何、中文换行、对比度和整套 deck 的节奏。

对于 <code>diagram-led</code> 和 <code>parallel</code> 页面，分别隐藏图形和解释文字，确认两者单独成立；恢复后确认组合产生新增理解，而不是重复表达。

### 6. 图形与文字的三种耦合模式

| 模式 | 适用逻辑 | 页面表现 |
| --- | --- | --- |
| <code>integrated</code> | 结构和细节最好在同一语义归属下共同理解 | 信息沿流程、目标链、时间轴或机制结构直接展开 |
| <code>diagram-led</code> | 一个简洁图形承担主结构，文字承担规则、范围、机制、证据或例子 | 图形先建立框架，解释区补充判断所需的信息 |
| <code>parallel</code> | 图形和结构化叙述分别成立，并共同支持比较、诊断或决策 | 两个阅读面并行推进，但必须围绕同一判断 |

### 7. 适用场景

- 将企业培训方案、咨询报告、管理汇报和技术方案的逐页文案转化为 HTML deck；
- 设计高文字密度、多层级语义和复杂信息关系的单页；
- 将时间、层级、因果、约束、比较、治理和路线图表达为真实视觉结构；
- 在浏览器中预览、打印或继续编辑演示稿；
- 生成适合后续转换为 PPTX/PDF 的自包含 HTML；
- 对已有 HTML deck 做内容覆盖、结构 lint 和浏览器 QA；
- 建立稳定的红色咨询级 HTML 演示稿底座。

### 8. 使用方式

#### 在 Codex 中使用

将 skill 文件夹放入 Codex skills 目录：

~~~text
%USERPROFILE%\.codex\skills\html-ppt-visual-architect\
~~~

然后使用 <code>$html-ppt-visual-architect</code>，提供逐页文案、页面大纲或结构化内容。例如：

~~~text
请使用 html-ppt-visual-architect，将以下逐页文案转化为一套高密度、红色咨询级、自包含 HTML 演示稿。
保留数字、日期、名称、机制、案例和限定条件。
每页使用结论式标题和总领段，并根据页面感知任务选择独特的视觉语法。
避免机械使用卡片墙、三栏布局和节点连线图。
完成内容覆盖检查、静态检查和浏览器端 QA，并说明未解决的占位符。
~~~

#### 本地预览

在包含 HTML deck 的文件夹中启动 UTF-8 本地服务：

~~~powershell
python scripts/serve.py <deck-folder> --port 8765
~~~

然后打开：

~~~text
http://127.0.0.1:8765/
~~~

在 URL 后加入 <code>?qa=1</code> 可以显示浏览器端 QA 面板。

#### 静态结构检查

~~~powershell
python scripts/static_lint.py <deck.html>
~~~

该检查会关注：

- 是否存在 UTF-8 声明；
- 是否存在 <code>section.slide</code>；
- 每页是否有唯一 ID、标题、总领段和布局签名；
- <code>data-density</code> 与 <code>data-coupling</code> 是否有效；
- 是否存在过多重复布局；
- 是否存在卡片堆叠而缺乏关系图形；
- SVG 是否缺少 <code>viewBox</code>、<code>title</code> 或 <code>desc</code>；
- 是否存在未经审查的远程依赖。

#### 内容覆盖检查

如果源文稿使用 <code>## P1</code>、<code>## P2</code> 等页面标题，可以运行：

~~~powershell
python scripts/content_coverage.py <source.md> <deck.html>
~~~

检查结果包括页面数量、加权页面覆盖率、低覆盖源内容单元和缺失关键字面事实。

### 9. 仓库结构

~~~text
html-ppt-visual-architect/
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── deck-core.css
│   └── deck-runtime.js
├── references/
│   ├── content-to-visual-method.md
│   ├── html-implementation.md
│   ├── qa-rubric.md
│   ├── red-design-system.md
│   ├── reference-derived-insights.md
│   └── visual-semantic-synthesis.md
└── scripts/
    ├── content_coverage.py
    ├── serve.py
    └── static_lint.py
~~~

- <code>SKILL.md</code>：Agent 的主流程、输出标准和生产步骤；
- <code>agents/openai.yaml</code>：skill 在 OpenAI/Codex 环境中的界面名称、品牌色和默认提示词；
- <code>assets/deck-core.css</code>：画布、色彩、字体、密度、布局基础和组件样式；
- <code>assets/deck-runtime.js</code>：翻页、全屏、键盘导航和浏览器端 QA；
- <code>references/</code>：内容建模、视觉语义、红色设计系统、HTML 实现和验收规则；
- <code>scripts/</code>：内容覆盖、UTF-8 本地服务和静态结构检查工具。

### 10. 质量标准

一个合格的 HTML deck 应同时满足：

1. 每页都有结论式标题和紧随其后的总领段；
2. 原始数字、日期、名称、机制、案例、限定条件和输出要求没有被静默删除；
3. 每页的视觉语法由实际语义和感知任务驱动；
4. 图形、标签、连线、边界和文字之间的关系可解释；
5. 页面使用统一的视觉系统，但没有机械复制同一种布局；
6. HTML 使用 UTF-8、16:9 画布，并具备稳定的打印和预览行为；
7. 页面没有影响阅读的溢出、裁切、遮挡或字号过小问题；
8. SVG 具备必要的 <code>viewBox</code>、<code>title</code> 和 <code>desc</code>；
9. 页面没有未经审查的远程资源依赖，或已明确说明其必要性；
10. 内容覆盖、静态 lint 和浏览器 QA 结果已经复核；
11. 未解决的占位符、合并内容和近似处理已经披露。

### 11. 范围与边界

本 skill 的默认任务是**根据已有逐页文案设计 HTML 演示稿**。

适合使用其他 skill 或工作流的任务包括：

- 从零提炼主题、研究内容或编写完整逐页文案；
- 普通企业网站、后台系统或交互产品开发；
- 不受输入文案约束的开放式文案创作；
- 只要求把现有 PPTX 或 PDF 原样转成可编辑文件；
- 只要求制作一张视觉海报，而不是一套可阅读的演示页面。

本仓库提供的是 Agent skill、HTML/CSS/JavaScript 底座和 QA 脚本，不是独立运行的 OCR 工具，也不是完整的 PPTX 导出器。最终 PPTX/PDF 转换能力取决于后续使用的转换环境。

### 12. 已知限制

- 过短、过长或结构不清晰的逐页文案会影响页面结论和信息分配；
- 缺少字体时，中文换行、字宽和整体密度可能发生变化；
- 浏览器端 QA 可以发现结构和几何风险，但不能替代专业设计判断；
- 内容覆盖检查是召回辅助，不能自动判断所有语义改写是否等价；
- 自包含 HTML 对外部资源依赖较少，但复杂字体、图片或转换工具仍可能需要额外资源；
- HTML 转 PPTX/PDF 需要单独的转换流程，转换后仍应重新做视觉 QA；
- 页面允许使用图形化表达，但图形必须有语义责任，不能以装饰替代论证。

### 13. 资源与许可证

本仓库当前未声明统一的开源许可证。公开发布前，请根据你的授权意图补充 <code>LICENSE</code> 文件，并确认使用的字体、图标、图片和其他第三方资源符合相应许可证。

如果 HTML deck 使用外部资源，请优先下载并本地化，记录来源、版本、许可证和使用边界，确保离线交付时行为可预期。

### 14. 作者

**圣婴**

欢迎通过 Issue 或 Pull Request 提交页面案例、内容覆盖问题、视觉语义问题、浏览器 QA 结果和改进建议。

---

<a id="en"></a>

## English

### 1. Overview

<code>html-ppt-visual-architect</code> is a consulting-grade HTML presentation design skill for multimodal AI agents.

Use it when page-by-page copy, a presentation outline, or structured slide content already exists and needs to become a high-authority, information-dense, visually argued HTML deck.

The skill does not route every page through a fixed template. It treats each page as a content, semantic, spatial, and visual system:

- Preserve and organize facts, numbers, mechanisms, examples, and conclusions;
- Identify the relationship the audience must perceive;
- Select visual grammars, information carriers, and reading paths from that perceptual task;
- Build the page with HTML, CSS, and SVG;
- Validate coverage, structure, browser behavior, and rendered quality before delivery.

The output is a self-contained HTML presentation that can be opened, printed, and edited in a browser, then passed to a separate toolchain for PPTX or PDF conversion.

### 2. The Problem It Solves

Generic auto-layout tools often fail when:

- The page contains dense copy, evidence, mechanisms, and implications at the same time;
- Everything is reduced to repeated card grids, three-column layouts, or node-link diagrams;
- A diagram looks polished but does not encode the actual causal, temporal, hierarchical, boundary, or comparative relationship;
- Numbers, qualifiers, examples, or constraints are silently removed to create whitespace;
- Every page uses the same layout, creating a mechanically uniform deck;
- Generated HTML is delivered without coverage, overflow, or visual review.

This skill addresses those failure modes through content-layout separation, visual semantics before form, and rendered output as the final quality reference.

### 3. Core Value

#### 3.1 Preserve facts without sacrificing density

The workflow builds a content ledger and classifies source units as:

- **Critical literals:** numbers, dates, names, commitments, regulatory wording, stage counts, and explicit outputs;
- **Unique claims:** meanings and qualifiers that must remain intact;
- **Supporting detail:** compressible material that must stay near the claim it supports;
- **True repetition:** mergeable content whose surviving location is recorded;
- **Placeholders:** visibly unresolved content awaiting user input.

Preservation is the default. When space is tight, restructure, compress syntax, choose denser carriers, or redistribute responsibility before deleting content.

#### 3.2 Make visual form carry real meaning

Position, direction, boundary, size, color, connection, proximity, and hierarchy must carry an explicit information responsibility.

For example:

- Use timelines, phase bands, or loops for temporal relationships;
- Use nesting, trees, or steps for hierarchy;
- Use direction and connectors for causality;
- Use shared axes, matrices, or parallel structures for comparison;
- Use boundaries, guardrails, brackets, or overlays for constraints;
- Use annotations, evidence objects, or support bands for proof.

Graphics are not decoration, and cards are not the default answer. A shape should communicate grouping, order, direction, magnitude, ownership, dependency, boundary, priority, time, or status.

#### 3.3 Build a genuine page-level argument

Every page should have:

- A conclusion-led title;
- A lead paragraph immediately after the title;
- A primary visual argument recognizable within three seconds;
- Evidence, mechanisms, examples, or implications tied to that argument;
- A deliberate reading path;
- Enough explanation to be understood without a presenter.

Graphics and text may be integrated, diagram-led, or parallel, but each must have a distinct information responsibility.

#### 3.4 Create a deck that is coherent without being repetitive

The global shell stabilizes the red consulting visual system, typography, spacing, canvas, and component behavior. Local composition varies with the page’s semantic structure and perceptual task.

Consistency comes from:

- Color roles;
- Typography and hierarchy;
- Canvas and margins;
- Alignment anchors;
- Line and shape language;
- Header, footer, and navigation behavior.

Variation comes from the page conclusion, information responsibility, visual grammar, coupling mode, focal area, and reading order.

#### 3.5 Deliver HTML that can be previewed and verified

The output is a working HTML deck rather than a code excerpt:

- CSS, JavaScript, and necessary assets can be inlined or kept local;
- Slides use a 16:9 canvas and print behavior;
- Keyboard navigation and fullscreen preview are supported;
- <code>?qa=1</code> exposes the browser QA panel;
- Coverage checks, static lint, and browser review are available;
- Offline delivery is preferred, with remote dependencies treated as explicit exceptions.

### 4. Key Features

| Feature | What it does | Practical value |
| --- | --- | --- |
| Content-layout separation | Builds a content ledger and semantic model before choosing the page form | Protects facts from layout-driven deletion |
| Visual-semantic reasoning | Selects grammars from perceptual tasks, visual variables, and relationships | Makes graphics carry business meaning |
| High-density composition | Uses fields, paths, layers, tables, annotations, and structured text | Fits serious consulting and enterprise materials |
| Page-specific composition | Derives a distinct layout from each page’s semantics | Maintains deck rhythm and content fit |
| Three coupling modes | Supports integrated, diagram-led, and parallel relationships | Clarifies graphic and text responsibilities |
| Self-contained HTML | Uses native HTML, CSS, and SVG with local or inline assets | Easy to preview, print, edit, and hand off |
| Red consulting design system | Defines color roles, density modes, grid, geometry, and shape behavior | Provides a consistent professional visual language |
| Content coverage audit | Checks page count, text coverage, and critical literals against source Markdown | Reduces omissions and dropped numbers |
| Browser-side QA | Checks titles, leads, overflow, clipping, text size, SVGs, and label-node collisions | Finds structural defects before release |
| Two-pass visual review | Separates wireframe review from finish review | Prevents decoration from masking weak structure |

### 5. Standard Workflow

~~~mermaid
flowchart LR
    A[Page-by-page copy] --> B[Content ledger]
    B --> C[Semantic model]
    C --> D[Spatial system]
    D --> E[HTML / CSS / SVG]
    E --> F[Coverage + Static Lint]
    F --> G[Browser QA + Render Review]
    G -. targeted repair .-> D
~~~

#### Step 1: Normalize without reducing

Identify page boundaries, titles, leads, claims, evidence, examples, numbers, notes, and placeholders. Record what must remain verbatim, what may be compressed, and which carrier will own each source unit.

#### Step 2: Model meaning before form

For every page, define the governing conclusion, atomic claims, evidence, sequence, hierarchy, causality, ownership, comparison, time, magnitude, boundaries, feedback, exceptions, and the perceptual task the audience must complete.

Assign responsibility across structural information, interpretation, evidence, and implication before choosing geometry.

#### Step 3: Solve the page as a spatial system

Create a composition ledger covering:

- Title and lead;
- Information groups and importance;
- Primary and secondary semantic dimensions;
- Visual variables and visual grammars;
- Graphic-text coupling;
- Spatial zones, carriers, reading path, and focal point;
- Density mode, geometry system, and unique signature.

Generate at least two meaningfully different low-fidelity candidates. Change the encoding or visual grammar, not merely the color or card order.

#### Step 4: Build a page-specific visual argument

Make the conclusion visible within three seconds and the primary perceptual task understandable before the small text is read. Every graphic must state the relationship it encodes, and every connector must have a clear source, destination, and semantic purpose.

Use <code>diagram-led</code> when explanatory text does not change the graphic’s nodes or edges. Use <code>parallel</code> when a graphic and structured narrative must each stand on their own. Use <code>integrated</code> when structure and detail belong to the same semantic owner.

#### Step 5: Build the global shell

Start from <code>assets/deck-core.css</code> and <code>assets/deck-runtime.js</code>, or inline them into one self-contained HTML file.

Each slide follows a semantic contract:

~~~html
<section class="slide" id="slide-01"
         data-layout="unique-semantic-name"
         data-density="dense"
         data-coupling="diagram-led">
  <header class="slide-head">
    <div class="slide-kicker">Chapter · Page type</div>
    <h2 class="slide-title">Conclusion-led title</h2>
    <p class="slide-lead">Lead paragraph stating the governing message.</p>
  </header>
  <main class="slide-body">
    <div data-qa="primary">Page-specific composition</div>
  </main>
  <footer class="slide-foot"><span>Project</span><span>01</span></footer>
</section>
~~~

#### Step 6: Validate content before admiring the layout

When a Markdown source is available, run the coverage checker and investigate missing critical literals and low-coverage source units. The checker supports recall; it is not a semantic-equivalence judge.

#### Step 7: Render and inspect

Serve the deck with UTF-8 headers, inspect every page at presentation size, capture screenshots or a contact sheet, and use <code>?qa=1</code> to view the browser QA report.

#### Step 8: Perform a two-pass visual review

**Wireframe pass:** review content coverage, reading path, area allocation, alignment anchors, text capacity, graphic-text responsibility, and unexplained whitespace.

**Finish pass:** review typography, red emphasis, line weights, connector routes, geometry, CJK wrapping, contrast, and deck rhythm.

For <code>diagram-led</code> and <code>parallel</code> pages, hide the interpretation and confirm that the graphic still communicates its structure; hide the graphic and confirm that the text still explains its assigned dimension; restore both and confirm that the combination adds meaning rather than duplication.

### 6. Graphic-Text Coupling Modes

| Mode | Logic | Page behavior |
| --- | --- | --- |
| <code>integrated</code> | Structure and detail are best understood under the same semantic owner | Information unfolds directly along a process, target chain, timeline, or mechanism |
| <code>diagram-led</code> | A concise graphic owns the main structure while text owns rules, scope, mechanisms, evidence, or examples | The graphic establishes the framework and interpretation zones complete the judgment |
| <code>parallel</code> | A graphic and structured narrative remain independently readable and jointly support a comparison, diagnosis, or decision | Two reading surfaces advance in parallel around one judgment |

### 7. Typical Use Cases

- Turn training proposals, consulting reports, management updates, and technical plans into HTML decks;
- Design dense pages with multi-level semantics and complex information relationships;
- Express time, hierarchy, causality, constraints, comparison, governance, and roadmaps as meaningful visual structures;
- Preview, print, or continue editing a presentation in a browser;
- Produce self-contained HTML suitable for later PPTX/PDF conversion;
- Audit an existing HTML deck for content coverage, structure, and browser QA;
- Establish a reusable red consulting-grade HTML presentation foundation.

### 8. Usage

#### In Codex

Place the skill folder in the Codex skills directory:

~~~text
%USERPROFILE%\.codex\skills\html-ppt-visual-architect\
~~~

Invoke <code>$html-ppt-visual-architect</code> with page-by-page copy, a slide outline, or structured content. For example:

~~~text
Use html-ppt-visual-architect to turn the following page-by-page copy into a dense, red, consulting-grade, self-contained HTML presentation.
Preserve numbers, dates, names, mechanisms, examples, and qualifiers.
Use conclusion-led titles and lead paragraphs, and derive a page-specific visual grammar from each perceptual task.
Avoid mechanical card grids, three-column defaults, and node-link diagrams.
Run content coverage, static lint, and browser QA, and disclose unresolved placeholders.
~~~

#### Local preview

Start the UTF-8 local server from the folder containing the deck:

~~~powershell
python scripts/serve.py <deck-folder> --port 8765
~~~

Open:

~~~text
http://127.0.0.1:8765/
~~~

Append <code>?qa=1</code> to display the browser-side QA panel.

#### Static structural lint

~~~powershell
python scripts/static_lint.py <deck.html>
~~~

The linter checks:

- UTF-8 declaration;
- Presence of <code>section.slide</code>;
- Unique slide IDs, titles, leads, and layout signatures;
- Valid <code>data-density</code> and <code>data-coupling</code> values;
- Excessive layout repetition;
- Card-heavy pages without detected relational graphics;
- SVG <code>viewBox</code>, <code>title</code>, and <code>desc</code>;
- Unreviewed remote dependencies.

#### Content coverage audit

If the source uses headings such as <code>## P1</code> and <code>## P2</code>, run:

~~~powershell
python scripts/content_coverage.py <source.md> <deck.html>
~~~

The result reports page count, weighted page coverage, low-coverage source units, and missing critical literals.

### 9. Repository Structure

~~~text
html-ppt-visual-architect/
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── deck-core.css
│   └── deck-runtime.js
├── references/
│   ├── content-to-visual-method.md
│   ├── html-implementation.md
│   ├── qa-rubric.md
│   ├── red-design-system.md
│   ├── reference-derived-insights.md
│   └── visual-semantic-synthesis.md
└── scripts/
    ├── content_coverage.py
    ├── serve.py
    └── static_lint.py
~~~

- <code>SKILL.md</code> contains the agent workflow, output standard, and production sequence;
- <code>agents/openai.yaml</code> defines the skill’s OpenAI/Codex display name, brand color, and default prompt;
- <code>assets/deck-core.css</code> defines canvas, color, typography, density, layout, and component foundations;
- <code>assets/deck-runtime.js</code> provides navigation, fullscreen behavior, keyboard controls, and browser QA;
- <code>references/</code> contains content modeling, visual semantics, red design system, HTML implementation, and acceptance guidance;
- <code>scripts/</code> provides content coverage, UTF-8 serving, and static structural checks.

### 10. Quality Standard

A successful HTML deck should satisfy all of the following:

1. Every page has a conclusion-led title followed by a lead paragraph;
2. Numbers, dates, names, mechanisms, examples, qualifiers, and explicit outputs are not silently removed;
3. Each page’s visual grammar is derived from its semantics and perceptual task;
4. The relationships among graphics, labels, connectors, boundaries, and text are explainable;
5. The visual system is consistent without mechanically repeating one layout;
6. The HTML uses UTF-8, a 16:9 canvas, and stable preview and print behavior;
7. No material overflow, clipping, collision, or unreadably small text remains;
8. Meaningful SVGs provide the required <code>viewBox</code>, <code>title</code>, and <code>desc</code>;
9. Remote dependencies are absent, localized, or explicitly justified;
10. Coverage, static lint, and browser QA results have been reviewed;
11. Unresolved placeholders, merged content, and approximations are disclosed.

### 11. Scope and Boundaries

The default task is **designing an HTML presentation from existing page-by-page copy**.

Use another skill or workflow for:

- Researching a topic or authoring the complete page-by-page copy from scratch;
- General websites, dashboards, or interactive product development;
- Open-ended copywriting without a source content contract;
- Direct image/PDF-to-editable-PPTX reconstruction;
- A single poster or illustration rather than a readable presentation deck.

This repository contains the agent skill, the HTML/CSS/JavaScript foundation, and QA scripts. It is not a standalone OCR tool or a complete PPTX exporter. PPTX/PDF conversion depends on the downstream conversion environment and should be visually rechecked after conversion.

### 12. Known Limitations

- Very short, very long, or poorly structured copy can weaken page conclusions and information allocation;
- Missing fonts can change CJK wrapping, text width, and overall density;
- Browser QA detects structural and geometric risks but does not replace design judgment;
- Coverage auditing supports recall and cannot determine every semantic paraphrase automatically;
- Self-contained HTML minimizes external dependencies, but complex fonts, images, or conversion tools may still require additional assets;
- HTML-to-PPTX/PDF conversion requires a separate pipeline and a fresh visual QA pass;
- Graphics are welcome only when they carry semantic responsibility rather than decorative surface.

### 13. Assets and Licensing

This repository does not currently declare a single open-source license. Before public distribution, add a <code>LICENSE</code> file that matches your intended terms and verify that fonts, icons, images, and other third-party assets comply with their licenses.

When a deck uses external resources, prefer downloading and localizing them. Record source, version, license, and usage boundaries so offline delivery remains predictable.

### 14. Author

**圣婴**

Issues and Pull Requests are welcome for page examples, coverage problems, visual-semantic problems, browser QA findings, and workflow improvements.

