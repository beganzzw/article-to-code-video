# Article to Code-Video (文章转代码视频 · 导演级工作流)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> 将长文、技术博客与深度报告，端到端转化为**代码驱动渲染（Remotion / React / Canvas 动效）的工业级科技解说视频**的 AI Agent Skill。
> 深度融合 [`anything2explainer`](https://github.com/Vincentwei1021/anything2explainer) 的工业级质检管线与 [`lemo-opuscar`](https://github.com/lemomo-ai/lemo-opuscar) 的电影级导演语法与多风格美学。

---

## 💡 为什么做这个项目？

传统的“文章转视频”工具往往面临两极分化的尴尬：
1. **文案层面充满“AI味”**：自动生成的解说词充斥着“第一、第二、第三”等长展开的对称骨架，以及“分野/宿命/生态/赋能”等评论腔，听起来毫无活人感；
2. **画面层面沦为“PPT念稿”**：要么是拼凑无意义的素材库贴片，要么是单一死板的静态模板。

**代码编写视频（Programmatic Video）的精髓在于：用真实的代码逻辑、动态架构图、运行控制台、代码 Diff、2D 相机漫游和物理音效，把抽象的技术思想像一部纪录短片一样演出来。**

---

## 🎨 内置六大代码视频视觉风格 (`references/style-presets.md`)

支持根据文章调性自由选择或派生属于你自己的专属风格：

| 风格代码 (Slug) | 中文名称 | 视觉与运镜核心特征 | 最适配的文章类型 |
| :--- | :--- | :--- | :--- |
| **`whiteboard`** | **极简白板手绘** | 暖白无限画布 + 单线手绘笔触 + 擦除残影 + 相机沿线漫游（零硬切） | 技术科普、概念辟谣、原理推导 |
| **`dark-keynote`** | **暗色科技发布** | Apple/Linear 质感，近黑舞台 + 3% 细网格 + 唯一品牌色 + 磁吸网格对齐 | 架构升级、新框架发布、性能实测 |
| **`swiss-motion`** | **瑞士动态排版** | 暖灰纸张 + 12列严谨网格 + 唯一信号色 + 极端字号反差 + 裁纸刀坍缩 | 方法论总结、设计规范、清单法则 |
| **`briefing-board`** | **工程简报墙** | 搪瓷白板墙 + 真实证据卡/磁吸钉 + 印章裁定 + 终局第一次全景拉远 | 系统工程复盘、多方案选型对比 |
| **`visual-investigation`** | **视觉调查案卷** | 档案灯台 + 荧光笔划原句证据 + 时间线刻度 + 红线因果链 | 故障溯源、论文深扒、安全分析 |
| **`cyber-mg`** | **黑底流光 MG** | 点阵波/星点黑底 + 亮紫胶囊 HUD + 三轮扫光高光 + 章节进度条 | 通用硬核工程解说、Agent 机制拆解 |

---

## ✨ 核心特性

- 🎯 **深度材料解构 & 事实零脑补铁律（Zero Hallucination）**：
  提炼现实痛点、反直觉解法与实测数据；不仅口播台词 100% 忠于原文，**连画面代码框里的函数名、参数、报错提示也严守原文字面表述**。
- 🎬 **电影级导演语法 (`references/director-grammar.md`)**：
  - **媒介原生大招 (One Native Move)**：高潮处必有一处只有代码能实现的动作（如一拍磁吸网格 Snap-Grid、橡皮擦倒擦回滚时间、全墙终极拉远揭示 Whole-Wall Reveal）；
  - **2D 相机运镜语法**：跟线运镜（Ride the line）、极近特写定格、对数空间连续拉远、阶梯式对比构图；
  - **阅读时间硬公式**：画面文字静止可读时长严格满足 `中文字符 ÷ 4.5 + 英文字符 ÷ 15 + 1.5s`。
- 🗣️ **去 AI 味活人解说 (`references/narration-rules.md`)**：
  破除结构对称，允许段落长短悬殊；剔除书面评论腔，采用第一人称工程师对话感。
- 🔊 **程序化物理音效与混音 (`template/scripts/sfx.py`)**：
  可见动作皆有声（`click` 吸附、`whoosh` 横扫、`thump` 盖章、`ding` 指标亮起），转折前设置真实留白（Silence），母带统一对齐 **-14 LUFS**。
- 🛑 **四大确认门禁 + 抽帧视觉自检（Still Frame Visual QC）**：
  全片渲染前强制通过 `remotion still` 抽取每幕关键帧检查排版，杜绝文字溢出、穿模或偏置。

---

## 📂 仓库结构

```text
article-to-code-video/
├── SKILL.md                          # Skill 核心入口与调度协议 (v1.3.0)
├── LICENSE                           # MIT 开源协议
├── README.md                         # 项目说明文档
├── references/                       # 导演、风格与工程规范手册
│   ├── director-grammar.md           # 电影级导演法则（标尺/原生大招/相机语法/阅读公式/声音）
│   ├── style-presets.md              # 六大经典代码视频风格预设库与自定义风格派生指南
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
    │   ├── sfx.py                    # 程序化物理音效合成器与混音工具
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

```bash
# 安装到 WorkBuddy AI
git clone https://github.com/beganzzw/article-to-code-video.git ~/.workbuddy-ai/skills/article-to-code-video

# 或者安装到 Claude Code
git clone https://github.com/beganzzw/article-to-code-video.git ~/.claude/skills/article-to-code-video
```

在对话中直接指定文章与你想要的风格：
> *"用 article-to-code-video 的【极简白板手绘 / 暗色科技发布 / 瑞士动态排版】风格，把这篇文章做成代码视频讲解：https://..."*

---

## 🙏 致谢

- 导演方法论、多风格体系与程序化音效致敬并吸收自 [`lemomo-ai/lemo-opuscar`](https://github.com/lemomo-ai/lemo-opuscar)；
- Remotion 工程管线与动效质检标尺借鉴自 [`Vincentwei1021/anything2explainer`](https://github.com/Vincentwei1021/anything2explainer)。

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。
