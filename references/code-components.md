# 代码驱动视频视觉组件库与设计规范 (Code Components)

代码编写视频的核心优势在于**可编程、高精度、高保真**。每个场景不是一张静态 PPT，而是一个接收状态与参数的 React/Remotion 组件。

以下是技术类文章拆解时最高频的六大视觉组件模式：

---

## 1. 架构流转拓扑 (`<ArchitectureGraph />`)

用于展示系统架构、Agent 调用链、数据流向。

* **视觉特征**：
  * 暗色科技背景（如 `#0d1117`），圆角卡片节点；
  * 节点之间有发光动效连线（SVG path 带 `strokeDashoffset` 动画）；
  * 数据包以光点形式在节点间跳跃传输。
* **常用 Props 约定**：
  ```tsx
  interface Node {
    id: string;
    label: string;
    role: "orchestrator" | "subagent" | "tool" | "main";
    status?: "active" | "waiting" | "error";
  }
  interface Connection {
    from: string;
    to: string;
    activeFrame?: number;
    latencyMs?: number;
  }
  ```

---

## 2. 传话游戏丢失模拟 (`<TelephoneGameLoss />`)

用于直观呈现多层 Agent 间的信息衰减或上下文有损传递。

* **视觉特征**：
  * 左侧展示初始完整的 User Prompt（长文本，带高亮关键约束）；
  * 中间经过“Agent A 摘要”卡片，部分字词泛红并淡出瓦解；
  * 右侧展示经过两次传递后，主模型拿到的一小截残缺总结，形成强烈视觉落差。
* **常用 Props 约定**：
  ```tsx
  interface TelephoneGameLossProps {
    originalPrompt: string;
    intermediateSummary: string;
    finalDistortedContext: string;
    lostKeywords: string[]; // 动态做红字划线或粉碎动画
  }
  ```

---

## 3. 代码重构与差分对比 (`<CodeDiffViewer />`)

用于展示代码层面的真实改变，比如从臃肿的编排器重构成轻量的主循环。

* **视觉特征**：
  * 真实 IDE / VS Code 风格窗口（带红黄绿三色控制按钮、文件名标签）；
  * 基于 Prism 或 Highlight.js 做语法高亮；
  * 利用平滑的高度与透明度插值，展示旧代码被折叠/删除（红色背景浅层高亮），新代码插入（绿色背景浅层高亮）。
* **常用 Props 约定**：
  ```tsx
  interface CodeDiffProps {
    fileName: string;
    oldCode: string;
    newCode: string;
    highlightLines?: number[];
    progress: number; // Remotion interpolate 控制的演变进度 (0 ~ 1)
  }
  ```

---

## 4. 终端打点与延迟监视器 (`<ConsoleLatencyTracker />`)

用于展示运行时日志滚动与直观的延迟耗时。

* **视觉特征**：
  * 仿真实终端窗口（Monospace 等宽字体，前缀 `$`）；
  * 实时打字机效果输出运行时调用日志；
  * 右上角挂载一个醒目的计时器 HUD（如 `Elapsed: 4.2s`，耗时过长时数字变红闪烁）。
* **常用 Props 约定**：
  ```tsx
  interface ConsoleLatencyTrackerProps {
    logs: Array<{ text: string; timeOffsetFrames: number; level?: "info" | "warn" | "error" }>;
    finalLatencySec: number;
    compareLatencySec?: number; // 对比项（如单循环对比多智能体）
  }
  ```

---

## 5. 渐进式加载动态视窗 (`<ProgressiveDisclosureVisualizer />`)

用于演示“只先加载名字，用到了再搜出完整能力”的技术机理。

* **视觉特征**：
  * 左侧是极小的 System Prompt 视窗（Token 占用仅 15%）；
  * 右侧是待命的技能/工具索引库；
  * 当中间的光标发出 `ToolSearch("orders")` 时，右侧对应模块以粒子或卡片展开的方式动态注入左侧上下文。

---

## 6. 决策边界与踩坑红线卡 (`<DecisionMatrix />`)

用于演示“什么时候能用、什么时候绝不能用”的边界划分。

* **视觉特征**：
  * 双栏对比或红绿盾牌卡片；
  * 绿色卡片：并入主循环的最佳场景（带绿色 Checkmark）；
  * 红色卡片：必须保留独立子 Agent 的红线场景（带黄色/红色 Warning 图标）；
  * 避免密集文字，每个维度提炼成 4-8 个字的一句话要点。
