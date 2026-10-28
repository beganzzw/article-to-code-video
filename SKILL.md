---
name: article-to-code-video
description: 将长文、技术深度文章或行业报告拆解并转化为代码驱动视频（Remotion/React/Canvas 代码动画与终端渲染）的一体化导演级流水线。深度融合 anything2explainer 的工业质检与 lemo-opuscar 的电影级导演语法及多风格矩阵（极简白板手绘、暗色科技发布、瑞士动态排版、工程简报墙、视觉调查案卷、黑底流光MG）。涵盖事实零脑补解构、非对称大纲、媒介原生大招（Native Move）、活人口语旁白、程序化音效（sfx.py）与本地一键渲染成片。触发词：文章转视频、文章做成视频、代码做视频、文章拆成视频讲解、文章讲解视频、技术文章转视频、Remotion 视频拆解。
version: 1.3.0
display_name: "文章转代码视频拆解"
display_name_en: "Article to Code-Video"
description_zh: "将长文/技术文章端到端转化为代码驱动动画视频的导演级流水线，内置 6 大视觉风格预设、Remotion 4 模板、程序化音效与人话脚本规范"
description_en: "Director-grade pipeline to deconstruct articles into code-driven animated videos with 6 style presets, built-in Remotion 4 template, procedural foley, and human narration"
visibility: "public"
---

# 文章转代码视频讲解 (Article to Code-Video)

本技能是一个**端到端全闭环的导演级代码视频创作系统**。输入一篇长文、技术博客、深度报告或工程文章，直接输出为**用真实代码驱动渲染的高质量科技解说视频（Remotion / React / Canvas 动画）**。

本技能深度融合了两大开源标杆的精髓：
- **`anything2explainer` 的工业化工程管线**：Remotion 4 渲染底座、词级 TTS 时间轴自动生成（`tts_build.py`）、持续动作与落位停留质检标尺；
- **`lemo-opuscar` 的电影级导演语法与多风格美学**：6 大经典代码制片风格预设（`style-presets.md`）、媒介原生大招（One Native Move）、2D 相机运镜语法、阅读时间硬公式与程序化物理音效合成器（`sfx.py`）。

---

## 六大视觉风格路由（支持按文章调性选择或自定义派生）

动笔前先根据文章调性或用户指定匹配风格（详见 `references/style-presets.md`）：
1. **`whiteboard`（极简白板手绘风）**：暖白无限画布 + 单线手绘笔触 + 擦除 7% 残影 + 相机沿线漫游（零硬切），最适合技术科普、概念辟谣与原理推导；
2. **`dark-keynote`（暗色科技发布风）**：Apple/Linear 质感，近黑舞台 + 3% 细网格 + 唯一品牌高亮色（问题红色在转折后永久消失），最适合架构升级与性能对比；
3. **`swiss-motion`（瑞士动态排版风）**：暖灰纸张 + 12 列网格 + 唯一信号色 + 极端字号反差 + 裁纸刀切线坍缩（无弹性回弹），最适合方法论与清单法则；
4. **`briefing-board`（工程简报墙风）**：搪瓷白板墙 + 证据卡/磁吸钉 + 印章裁定 + 尾声第一次拉远展示整面架构海报（Whole-Wall Reveal），最适合系统复盘与选型；
5. **`visual-investigation`（视觉调查案卷风）**：档案灯台 + 荧光笔划原句证据 + 红线串联因果链，最适合故障溯源与论文深扒；
6. **`cyber-mg`（黑底流光 MG 风 · 默认模板）**：点阵波/星点黑底 + 亮紫 HUD 胶囊 + 扫光高光 + 章节进度条。

---

## 核心交付阶段

### 阶段一：材料解构与标尺设定（Benchmark & Zero Hallucination）
- 抽取三样硬材料：真实撞墙痛点、反直觉方案、实测数据与真实踩坑案例；
- **先立标尺（Benchmark First）**：针对所选风格与题材明确构图、运镜与色彩参考；
- **事实零脑补铁律（Zero Hallucination）**：不仅解说词观点与案例必须 100% 出自原文，**连画面代码框里的函数名、参数、报错提示也必须严守原文字面表述**，严禁自行编造原文未提及的业务名称或数字。

### 阶段二：非对称大纲设计与【门禁 1 · 时长、语言与风格定档】
- 拒绝骨架对称，挑一两个最致命的点讲透；段落之间允许硬切，绝不用“综上所述”、“接下来我们看”等假过渡；
- **设计至少一个「媒介原生大招 (One Native Move)」**：在认知高潮处放入只有代码动画能实现的视觉动作（如一拍磁吸对齐 Snap-Grid、橡皮擦倒擦回滚、或全墙终极拉远揭示）；
- 确认时长档位（1 分钟短视频约 350 字，3–5 分钟深度版约 1200 字）、语言与视觉风格。

### 阶段三：视觉场景、相机语法与代码组件映射
- 全片组合使用至少 **4 种不同语义的运镜**（跟线运镜 Ride the line、极近特写定格、阶梯式对比构图、全墙拉远揭示）；
- 绑定具体 React/Remotion 代码动效组件（`<ArchitectureGraph />`、`<TelephoneGameLoss />`、`<CodeDiffViewer />`、`<ConsoleLatencyTracker />`、`<ProgressiveDisclosureVisualizer />`、`<DecisionMatrix />`）。

### 阶段四：活人口语旁白创作与【门禁 2 & 门禁 3 · 文案定稿与配音音效】
- 严格遵循 `references/narration-rules.md`：第一人称工程师口吻，长短句交错，彻底消灭“分野/宿命/生态/赋能”等评论腔；
- 调用内置 `template/scripts/tts_build.py` 自动跑出毫秒级词级对齐时间轴；
- 可选搭配 `template/scripts/sfx.py` 合成物理动作音效（`click`、`whoosh`、`thump`、`ding`），在转折前留出真实留白（Silence），母带响度对齐 **-14 LUFS**。

### 阶段五：代码分镜工程、抽帧视觉质检与【门禁 4 · 样片预览】
- **动效与阅读时间硬标准**：
  - 持续动作 + 末拍 30–45 帧稳定期（严禁入场即停/落位即切）；
  - 画面文字停留时间满足 `中文字符 ÷ 4.5 + 英文字符 ÷ 15 + 1.5s`，字幕停留 `≥ max(1.8s, 语音 + 0.6s)`；
- **强制抽帧视觉自检（Still Frame Visual QC）**：全片渲染前必须用 `npx remotion still` 抽取每幕满态关键帧并用 `Read` 肉眼检查，确保零文字溢出、零箭头穿模、所有卡片顶部胶囊严格水平居中；
- 本地并发渲染导出 16:9 横版母版与 9:16 竖屏短视频版 MP4。

---

## 内置资产与参考文档

- `template/`：**内置可直接编译运行的 Remotion 4 项目模板**
  - `template/scripts/tts_build.py`：自动 TTS 配音与生成 `timeline.ts`、`subs.ts`
  - `template/scripts/sfx.py`：程序化物理音效合成器与混音工具（吸收自 `lemo-opuscar`）
  - `template/scripts/preview.sh` / `render.sh`：样片快速预览与全片高保真并发渲染
  - `template/src/overlay/`：科技感 HUD 胶囊、底部章节进度条、片头片尾
  - `template/src/fx.tsx` / `ui.tsx`：扫光、光环、舞台光线、常用矢量图元
- `references/director-grammar.md`：电影级代码视频导演法则（标尺、原生大招、相机语法、阅读时间公式、声音设计）
- `references/style-presets.md`：六大经典代码视频视觉风格预设库与自定义风格派生指南
- `references/workflow.md`：带 4 大门禁的五步全闭环标准作业 SOP
- `references/narration-rules.md`：去 AI 味、口语化人话旁白编写与破绽规避铁律
- `references/code-components.md`：六大技术代码动效组件库规范
- `references/composition-and-light.md` & `motion-vocabulary.md`：构图光效标尺与动效帧数公式
- `references/style-guide.md` & `lessons.md`：排版安全区规范与避坑质检汇总
- `references/case-study-anthropic.md`：Anthropic 智能体折叠实战标杆范例
