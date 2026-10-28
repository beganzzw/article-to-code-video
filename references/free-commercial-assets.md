# 免费可商用素材源白名单与拉取规范 (Free Commercial Assets)

在代码驱动视频中，除了纯代码绘制的几何组件外，适当引入**真实的硬件/历史档案照片、开源技术栈矢量图标、免版权实拍 B-roll 视频与真实乐器采样**，能让画面的纪实感与专业度成倍提升（尤其在 `briefing-board` 工程简报墙、`visual-investigation` 视觉调查、`cyber-mg` 实拍混剪风格中）。

本规范整理了 **100% 免费可商用** 的六大类素材源，并提供内置脚本 `template/scripts/fetch_assets.py` 免 Key 一键拉取。

---

## 一、六大类免费可商用素材白名单

### 1. 开源矢量图标与技术 Logo（MIT / CC0 / Apache 2.0）
* **Iconify 开源图标中心（首选，免 Key 直接通过 API 拉取 SVG）**：
  * 接口格式：`https://api.iconify.design/<collection>/<name>.svg`
  * 推荐图标集：
    * `lucide`（MIT，极简现代线性图标，如 `lucide:cpu`, `lucide:database`, `lucide:git-branch`, `lucide:terminal`）
    * `tabler`（MIT，5000+ 工程与系统架构图标）
    * `simple-icons`（CC0，主流科技品牌与开源项目 Logo，如 `simple-icons:anthropic`, `simple-icons:docker`, `simple-icons:kubernetes`, `simple-icons:github`）
    * `ph`（Phosphor Icons，MIT，支持 duotone 双色调风格）
* **手绘人物与插画**：
  * **Open Peeps**（CC0 公有领域）：手绘简笔半身/全身人物组件库，极度契合 `whiteboard` 极简白板风格。
  * **unDraw**（unDraw 开源商用许可）：可自定义主色调的扁平科技插画 SVG。

### 2. 真实实物照片、历史档案与科学影像（Public Domain / CC0 / CC BY）
* **Wikimedia Commons（维基共享资源）**：
  * 通过 API 查询并严格校验 `extmetadata.LicenseShortName`；
  * **直接可用（无附加条件）**：`CC0`、`Public domain`；
  * **署名即可商用**：`CC BY 3.0`、`CC BY 4.0`（须在项目 `CREDITS.md` 与片尾注明作者与来源）；
  * **需谨慎或询问用户**：`CC BY-SA`（要求同协议传染共享）。
* **Smithsonian Open Access（史密森尼学会开放档案）**：数百万张 2D/3D 历史与科技器物高清扫描图，全部 **CC0**。
* **NASA Image and Video Library**：航空航天、卫星遥感、地球观测实拍影像，属公有领域（Public Domain）。

### 3. 免版权实拍视频 B-roll（配合 `<FootageTrack />` 使用）
* **Mixkit**（Mixkit Free License）：科技机房、代码屏幕、城市延时、实验室实拍视频，免费用于商业视频项目且无需署名。
* **Pexels Videos / Pixabay Videos**：免费可商用高清 MP4 素材，下载后放入 `public/assets/<slug>/`，通过 `FootageTrack` 挂载并自动叠加暗角调色（`DarkGrade`）与运动模糊（`DirBlur`）。

### 4. 免费商用乐器采样与音效库（CC0 / Public Domain）
* **内置程序化物理音效 (`template/scripts/sfx.py`)**：100% 纯代码合成（`click`, `clack`, `whoosh`, `thump`, `ding`, `pop`, `rumble`），零版权风险。
* **VCSL (Versilian Community Sample Library)**：**CC0** 真实乐器采样库（马林巴琴、颤音琴、钟琴、拨弦、打击乐）。
* **VSCO 2 Community Edition**：**CC0** 管弦乐与室内乐采样。
* **Freesound.org（筛选 CC0 标签）**：环境底噪（机房风扇、白板教室环境音、打字机声）。

### 5. 开源免费商用字体（SIL Open Font License 1.1）
* **已内置于 `template/public/fonts/`**：
  * `NotoSansSC.ttf`（思源黑体，正文与大标题）
  * `Audiowide-Regular.ttf`（宽体科技大字）
  * `Exo2-Italic.ttf`（斜体技术副标）
  * `Orbitron[wght].ttf`（几何数字与 HUD）
* **推荐按需扩展的 OFL 字体**：
  * **霞鹜文楷 / LXGW Marker Gothic**：极适合 `whiteboard` 与 `briefing-board` 风格的手写马克笔中文字体；
  * **JetBrains Mono / Fira Code**：代码 Diff 与终端组件专用等宽字体。

---

## 二、内置自动拉取工具 (`template/scripts/fetch_assets.py`)

无需注册任何账号或配置 API Key，直接通过命令行拉取开源图标或公有领域高清图片，并自动登记 `CREDITS.md`：

```bash
# 1. 拉取开源 SVG 图标（支持指定颜色与尺寸）
python scripts/fetch_assets.py --icon lucide:cpu --color "#2A5CB3" --out public/assets/icons/cpu.svg
python scripts/fetch_assets.py --icon simple-icons:anthropic --color "#FFFFFF" --out public/assets/icons/anthropic.svg

# 2. 搜索并下载 Wikimedia Commons 上的免费商用（CC0 / Public Domain / CC BY）图片
python scripts/fetch_assets.py --wikimedia "punched card computer" --limit 2 --out-dir public/assets/photos/
```

---

## 三、合规铁律

1. **绝不把 AI 生成的假图当成“真实历史/实物证据”**：在 `briefing-board`（工程简报墙）与 `visual-investigation`（视觉调查）风格中，凡是作为事实证据展示的照片，必须来自真实可查的开源档案；若找不到可商用照片，直接用代码画成手绘线稿（Sketch）。
2. **自动登记 `CREDITS.md`**：凡使用了 `CC BY` 素材，必须由 `fetch_assets.py` 自动将作者、来源链接与许可证写入项目根目录的 `CREDITS.md`。
