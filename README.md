# Article to Code-Video (文章转代码视频)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> 将长文、技术博客与深度报告，端到端转化为**代码驱动渲染（Remotion / React 代码动效）的工业级科技解说视频**的 AI Agent Skill。

---

## 💡 为什么做这个项目？

传统的“文章转视频”工具往往面临两极分化的尴尬：
1. **文案层面充满“AI味”**：自动生成的解说词充斥着“第一、第二、第三”等长展开的对称骨架，以及“分野/宿命/生态/赋能”等评论腔，听起来毫无活人感；
2. **画面层面沦为“PPT念稿”**：要么是拼凑无意义的素材库贴片，要么是毫无动态细节的静态幻灯片。

**代码编写视频（Programmatic Video）的精髓在于：用真实的代码逻辑、动态架构图、运行控制台、代码 Diff、数据打点和流程模拟，把抽象的技术思想原汁原味地演出来。**

`article-to-code-video` 将**硬核长文解构方法论、去 AI 味口语化叙事、与工业级 Remotion 4 渲染工程**深度融合为一套开箱即用的一体化 Skill。

---

## ✨ 核心特性

- 🎯 **深度材料解构**：不按原文流水账复述，重点提炼技术演进中的**现实痛点、反直觉解法、硬核数据与踩坑案例**。
- 🗣️ **去 AI 味活人解说**：破除结构对称，允许段落长短悬殊；剔除假大空书面腔，采用第一人称工程师对话感，结尾利落收在务实工程准则上。
- 🧱 **六大技术特化动效组件**：
  - `<ArchitectureGraph />`：微服务与 Agent 拓扑流光图
  - `<TelephoneGameLoss />`：模拟传话游戏，演示长文本穿越多层 Agent 时的字词瓦解与丢包
  - `<CodeDiffViewer />`：IDE 语法高亮与代码平滑折叠/替换对比
  - `<ConsoleLatencyTracker />`：终端日志打字机滚动与耗时红色报警器
  - `<ProgressiveDisclosureVisualizer />`：动态检索与工具/技能按需加载
  - `<DecisionMatrix />`：红绿卡片技术选型决策边界
- 🛑 **四大确认门禁（Stop Points）**：
  - **门禁 1 · 时长与语言**：写大纲前先定档（2-3 分钟精简版，3-5 分钟深度版），倒推字数；
  - **门禁 2 · 解说词定稿**：配音与写帧前必须定稿，防止改词引发全片时间轴骨牌效应；
  - **门禁 3 · 配音引擎选型**：支持 edge-tts / kokoro 生成毫秒级词级对齐时间轴；
  - **门禁 4 · 前 30 秒样片预览**：只写前 30 秒快速打样核实验收，满意后再推进全片。
- 🎬 **工业级动效标准**：
  - 严禁「入场即停」与「落位即切」，必须有持续微动作支撑；
  - 末拍元素落位后预留 30–45 帧（1–1.5 秒）稳定期；
  - 每镜头唯一主角，光只跟主角，杜绝满屏碎屑乱飞。
- 📦 **自包含开箱即用**：内置完整的 Remotion 4 项目模板、TTS 时间轴生成脚本、HUD 覆盖层及渲染流水线。

---

## 📂 仓库结构

```text
article-to-code-video/
├── SKILL.md                          # Skill 核心入口与调度协议
├── LICENSE                           # MIT 开源协议
├── README.md                         # 项目说明文档
├── references/                       # 规则与最佳实践手册
│   ├── workflow.md                   # 带 4 大门禁的五步端到端 SOP
│   ├── narration-rules.md            # 去 AI 味与口语化台词铁律
│   ├── code-components.md            # 六大技术动效组件库规范
│   ├── composition-and-light.md      # 构图比例与光效质量标尺
│   ├── motion-vocabulary.md          # 动效公式与帧数字典
│   ├── style-guide.md                # 调色板与画布安全区
│   ├── lessons.md                    # 避坑指南与质检经验
│   └── case-study-anthropic.md       # Anthropic 智能体折叠实战范例
└── template/                         # 内置开箱即用的 Remotion 4 工程
    ├── package.json
    ├── scripts/
    │   ├── tts_build.py              # 配音与生成 timeline.ts / subs.ts
    │   ├── preview.sh                # 前 30 秒样片快速预览
    │   └── render.sh                 # 全片多核并发渲染 MP4
    └── src/
        ├── common/                   # 点阵波/星点/字幕/进度条底座
        ├── overlay/                  # HUD 胶囊、章节卡、流程轨
        ├── fx.tsx                    # 扫光、光环、舞台光线
        └── ui.tsx                    # 常用科技矢量图元库
```

---

## 🚀 快速使用

### 安装到你的 AI Agent 环境

无论是 **Claude Code**、**WorkBuddy AI** 还是其他支持 Agent Skill 协议的编程助手，只需将本仓库克隆至技能目录：

```bash
# 安装为用户级 Skill
git clone https://github.com/beganzzw/article-to-code-video.git ~/.workbuddy-ai/skills/article-to-code-video

# 或者在 Claude Code 中
git clone https://github.com/beganzzw/article-to-code-video.git ~/.claude/skills/article-to-code-video
```

### 触发使用

在对话中输入任意文章、链接或技术主题：

> *"用 article-to-code-video 把这篇文章拆解并制作成代码视频讲解：https://example.com/blog/..."*

智能体将自动加载本 Skill，严格执行：
1. **解构材料**并呈递**非对称大纲**（停下等待你确认时长与角度）；
2. 撰写**去 AI 味逐字口播稿**（停下等待你确认定稿）；
3. 运行内置脚本生成**配音音频与时间轴**；
4. 编写并渲染**前 30 秒样片**供你验收；
5. 本地并发渲染导出完整的 1080p MP4 视频。

---

## 🛠️ 本地运行与开发依赖

- **Node.js**: >= 18.0.0
- **Python**: >= 3.10（用于运行 `tts_build.py` 生成时间轴）
- **FFmpeg**: 用于音视频合成与编码

---

## 🙏 致谢

- 视觉风格与工程管线借鉴致敬了开源项目 [`Vincentwei1021/anything2explainer`](https://github.com/Vincentwei1021/anything2explainer) 与 Remotion 社区生态。

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。
