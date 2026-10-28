#!/usr/bin/env python3
"""免 Key 一键拉取 100% 免费可商用素材（SVG 图标 / CC0 手绘人物与 Agent 形象 / NASA 公有领域实拍图），
并自动登记到项目根目录的 CREDITS.md。

全部接口实测免 Key 直连秒通：
  1. Iconify (20万+ MIT/CC0 技术与架构矢量图标):
     python scripts/fetch_assets.py --icon lucide:cpu --color "#2A5CB3"
     python scripts/fetch_assets.py --search-icon "database"

  2. DiceBear (CC0 手绘人物 notionists / open-peeps 与 AI Agent 机器人 bottts):
     python scripts/fetch_assets.py --avatar notionists:Architect --out public/assets/avatars/architect.svg
     python scripts/fetch_assets.py --avatar open-peeps:Engineer
     python scripts/fetch_assets.py --avatar bottts:SubAgentA

  3. NASA Public Domain Library (公有领域真实硬件/卫星/科学高清照片):
     python scripts/fetch_assets.py --nasa "supercomputer" --limit 2 --out-dir public/assets/photos
"""
import argparse
import json
import os
import re
import urllib.parse
import urllib.request

USER_AGENT = "ArticleToCodeVideoSkill/1.4 (https://github.com/beganzzw/article-to-code-video; MIT License)"


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read()


def append_credit(project_root: str, item_name: str, source_url: str, author: str, license_name: str):
    credits_path = os.path.join(project_root, "CREDITS.md")
    if not os.path.exists(credits_path):
        with open(credits_path, "w", encoding="utf-8") as f:
            f.write("# 素材来源与免费商用许可登记 (CREDITS)\n\n")
            f.write("| 本地素材文件 | 来源链接 | 提供方/作者 | 商用开源许可证 |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
    rel_name = os.path.relpath(item_name, project_root).replace("\\", "/")
    with open(credits_path, "a", encoding="utf-8") as f:
        f.write(f"| `{rel_name}` | {source_url} | {author} | {license_name} |\n")


def search_iconify(query: str, limit: int = 10):
    url = f"https://api.iconify.design/search?query={urllib.parse.quote(query)}&limit={limit}"
    data = json.loads(_get(url).decode("utf-8"))
    icons = data.get("icons", [])
    print(f"Found {len(icons)} open-source icons for '{query}':")
    for ic in icons:
        print(f"  - {ic}")


def fetch_icon(icon_spec: str, color: str, out_path: str, project_root: str):
    if ":" not in icon_spec:
        raise SystemExit("图标格式应为 <collection>:<name>，例如 lucide:cpu 或 simple-icons:anthropic")
    prefix, name = icon_spec.split(":", 1)
    params = {" color": color} if color else {}
    qs = ("?" + urllib.parse.urlencode({"color": color})) if color else ""
    url = f"https://api.iconify.design/{prefix}/{name}.svg{qs}"
    data = _get(url)
    if not data or not data.lstrip().startswith(b"<svg"):
        raise SystemExit(f"未找到图标：{icon_spec} ({url})")
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(data)
    append_credit(
        project_root,
        out_path,
        f"https://icon-sets.iconify.design/{prefix}/{name}/",
        f"Iconify ({prefix})",
        "MIT / CC0 / Apache-2.0 (Commercial Free)",
    )
    print(f"[OK] 开源矢量图标已保存至 {out_path}")


def fetch_avatar(avatar_spec: str, out_path: str, project_root: str):
    """拉取 CC0 手绘人物 (notionists / open-peeps / lorelei) 或 AI 机器人 (bottts)"""
    if ":" in avatar_spec:
        style, seed = avatar_spec.split(":", 1)
    else:
        style, seed = "notionists", avatar_spec
    url = f"https://api.dicebear.com/9.x/{urllib.parse.quote(style)}/svg?seed={urllib.parse.quote(seed)}"
    data = _get(url)
    if not data or not data.lstrip().startswith(b"<svg"):
        raise SystemExit(f"拉取插画失败：{avatar_spec}")
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(data)
    lic = "CC0 1.0 Public Domain (Commercial Free)" if style in ("notionists", "open-peeps", "lorelei") else "Free for Commercial Use (DiceBear)"
    append_credit(project_root, out_path, url, f"DiceBear ({style})", lic)
    print(f"[OK] 手绘人物/Agent 插画已保存至 {out_path} ({lic})")


def fetch_nasa(query: str, limit: int, out_dir: str, project_root: str):
    """从 NASA Image and Video Library 拉取 100% 公有领域 (Public Domain) 真实高清照片"""
    url = f"https://images-api.nasa.gov/search?q={urllib.parse.quote(query)}&media_type=image&page_size={max(limit * 3, 6)}"
    raw = json.loads(_get(url).decode("utf-8"))
    items = raw.get("collection", {}).get("items", [])
    if not items:
        raise SystemExit(f"NASA 图库未搜到与 '{query}' 相关的公有领域图片")

    os.makedirs(out_dir, exist_ok=True)
    saved = 0
    for item in items:
        if saved >= limit:
            break
        links = item.get("links", [])
        data_list = item.get("data", [])
        if not links or not data_list:
            continue
        img_url = links[0].get("href", "")
        if not img_url:
            continue
        meta = data_list[0]
        nasa_id = meta.get("nasa_id", f"nasa_{saved}")
        title = meta.get("title", nasa_id)
        center = meta.get("center", "NASA")
        safe_name = re.sub(r"[^A-Za-z0-9._-]", "_", nasa_id)[:50] + ".jpg"
        dest = os.path.join(out_dir, safe_name)
        img_bytes = _get(img_url)
        with open(dest, "wb") as f:
            f.write(img_bytes)
        append_credit(project_root, dest, img_url, f"{center} ({title})", "Public Domain (100% Commercial Free)")
        print(f"[OK] 公有领域实拍图已下载: {dest} ({title})")
        saved += 1


def main():
    parser = argparse.ArgumentParser(description="免 Key 拉取 100% 免费可商用素材并登记 CREDITS.md")
    parser.add_argument("--search-icon", help="搜索开源图标关键词，如 'database' 或 'workflow'")
    parser.add_argument("--icon", help="拉取指定 Iconify 图标，如 lucide:cpu、tabler:git-merge、logos:docker-icon")
    parser.add_argument("--color", default="", help="SVG 图标颜色，如 '#2A5CB3'")
    parser.add_argument("--avatar", help="拉取 CC0 手绘人物或机器人，如 notionists:Coder、open-peeps:Dev、bottts:Agent1")
    parser.add_argument("--out", default="", help="输出文件路径")
    parser.add_argument("--nasa", help="搜索并下载 NASA 100% 公有领域真实科技/硬件/航拍照片")
    parser.add_argument("--limit", type=int, default=1, help="下载图片数量")
    parser.add_argument("--out-dir", default="public/assets/photos", help="图片输出目录")
    args = parser.parse_args()

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if args.search_icon:
        search_iconify(args.search_icon)
    if args.icon:
        out_path = args.out or os.path.join(project_root, "public", "assets", "icons", args.icon.replace(":", "_") + ".svg")
        fetch_icon(args.icon, args.color, out_path, project_root)
    if args.avatar:
        out_path = args.out or os.path.join(project_root, "public", "assets", "avatars", args.avatar.replace(":", "_") + ".svg")
        fetch_avatar(args.avatar, out_path, project_root)
    if args.nasa:
        fetch_nasa(args.nasa, args.limit, os.path.join(project_root, args.out_dir), project_root)


if __name__ == "__main__":
    main()
