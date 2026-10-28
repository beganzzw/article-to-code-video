---
name: article-to-code-video
description: 将长文、技术深度文章或行业报告拆解并转化为代码驱动视频（Remotion/React 代码动画与终端渲染）的一体化完整流水线。内置 Remotion 4 脚手架模板、TTS 词级时间戳工具与工业级质检标尺。涵盖原文核心事实与冲突点提取、非对称视频大纲设计、专业代码动效组件映射（架构图、代码 Diff、控制台打点、动态图表）、纯正活人口语旁白编写、4 大确认门禁体系与本地一键渲染成片。触发词：文章转视频、文章做成视频、代码做视频、文章拆成视频讲解、文章讲解视频、技术文章转视频、Remotion 视频拆解。
version: 1.2.0
display_name: "文章转代码视频拆解"
display_name_en: "Article to Code-Video"
description_zh: "将长文/技术文章端到端转化为代码驱动动画视频（Remotion/React）的完整流水线，内嵌开箱即用的渲染模板与人话脚本规范"
description_en: "End-to-end pipeline to deconstruct articles into code-driven animated videos with built-in Remotion 4 template, human narration, and motion standards"
visibility: "public"
---

# 文章转代码视频讲解 (Article to Code-Video)

本技能是一个**端到端全闭环的一体化代码视频创作系统**。输入一篇长文、技术博客、深度报告或工程文章，直接输出为**用真实代码驱动渲染的高质量科技解说视频（Remotion / React 动画）**。

无需在不同工具和技能之间跳转，本技能**自带开箱即用的 Remotion 4 渲染工程模板、自动配音对齐工具（`tts_build.py`）、科技感 HUD 覆盖层与工业级动效质检规范**。

---

## 核心交付阶段

### 阶段一：材料解构（提炼真实冲突、反直觉解法与实测数据）
- 不按原文段落流水账复述，抽取三样硬材料：真实撞墙痛点、反直觉方案、实测数据与真实踩坑案例；
- **事实零脑补铁律（Zero Hallucination）**：不仅解说词观点与案例必须 100% 出自原文，**连画面代码框里的函数名、参数、报错提示也必须严守原文字面表述**（例如原文写 `order lookup tool` 和 `shipping specialist`，代码框就用 `order_lookup_tool()` 和 `ask_shipping_specialist()`，严禁自行编造原文没提过的“仓储运力核验”或“$500金额”等虚构业务细节）。

### 阶段二：非对称大纲设计与【门禁 1 · 时长语言定档】
- 拒绝骨架对称，挑一两个最致命的点讲透；段落之间允许硬切，绝不用“综上所述”、“接下来我们看”等假过渡；
- 确认时长档位（2-3 分钟精简版，或 3-5 分钟标准版），字数与分镜严格受时长倒推约束。

### 阶段三：视觉场景与代码组件映射
解说段落绑定具体 React/Remotion 组件：
- `<ArchitectureGraph />`：微服务/Agent 拓扑图与调用流光；
- `<TelephoneGameLoss />`：长文本穿越多层 Agent 时的字词瓦解与丢包模拟；
- `<CodeDiffViewer />`：IDE 语法高亮与代码平滑折叠/替换；
- `<ConsoleLatencyTracker />`：终端日志打字机滚动与耗时红色报警器；
- `<ProgressiveDisclosureVisualizer />`：动态检索与 Skills/MCP Tools 挂载。

### 阶段四：活人口语旁白创作与【门禁 2 & 门禁 3 · 文案定稿与配音】
- 严格遵循 `references/narration-rules.md`：第一人称工程师口吻，长短句交错；
- 彻底消灭“分野/宿命/生态/赋能”等评论腔，严禁通篇“不是 A 而是 B”；
- 空行分段对齐镜头分块，用户确认逐字稿后调用内置 `template/scripts/tts_build.py` 自动跑出毫秒级词级对齐时间轴。

### 阶段五：代码分镜工程与【门禁 4 · 30秒样片预览】
- 复制内嵌的 `template/` 作为项目基础，生成具体的分镜组件；
- 严守动效三铁律：持续动作（打字机、流光、慢推）+ 末拍 30-45 帧稳定期（严禁入场即停/落位即切），光只跟主角；
- 调用 `scripts/preview.sh 30` 快速导出前 30 秒样片，确认无误后并行构建剩余镜头并全片渲染 MP4。

---

## 四个核心确认门禁（严格执行）

1. **门禁 1 · 时长与语言（写大纲前确认）**：
   - 确定预期时长（如 2-3 分钟约 700 字，3-5 分钟约 1200 字）与语言（中/英）。
2. **门禁 2 · 解说词与章节定稿（配音与写帧之前确认）**：
   - 将完整逐字旁白、章节分段及字数贴给用户确认。定稿后帧号硬编码，避免改词引发连锁反应。
3. **门禁 3 · 配音引擎选型（时间轴生成前确认）**：
   - 默认免费高质量 TTS：中文 edge-tts（`zh-CN-YunxiNeural` 原速），英文 kokoro；用户若有自备音色则按需替换。
4. **门禁 4 · 前 30 秒样片预览（全片大面积编写前确认）**：
   - 优先编写片头与第 1 镜头代码，快速测渲前 30 秒样片给用户确认，画风节奏满意后再推进全片。

---

## 内置资产与参考文档

- `template/`：**内置可直接编译运行的 Remotion 4 项目模板**
  - `template/scripts/tts_build.py`：自动 TTS 配音与生成 `timeline.ts`、`subs.ts`
  - `template/scripts/preview.sh`：快速预览前 N 秒样片
  - `template/scripts/render.sh`：全片高保真并发渲染为 MP4
  - `template/src/overlay/`：科技感 HUD 胶囊、底部章节进度条、片头片尾
  - `template/src/fx.tsx` / `ui.tsx`：扫光、光环、舞台光线、常用矢量图元
- `references/workflow.md`：带 4 大门禁的五步全闭环标准作业 SOP
- `references/narration-rules.md`：去 AI 味、口语化人话旁白编写与破绽规避铁律
- `references/code-components.md`：六大技术代码动效组件库规范
- `references/composition-and-light.md`：构图与光效标尺
- `references/motion-vocabulary.md`：动效词汇表与帧数公式
- `references/style-guide.md`：视觉与排版安全区规范
- `references/lessons.md`：踩坑与质检经验汇总
- `references/case-study-anthropic.md`：Anthropic 智能体折叠实战标杆范例
