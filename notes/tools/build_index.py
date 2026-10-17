#!/usr/bin/env python3
"""扫描 notes/ 下的主题笔记与每日笔记，自动生成 INDEX.md（知识点索引）和 TIMELINE.md（日期时间线）。

用法（在仓库根目录运行）：
    python notes/tools/build_index.py

规则：
- 只读取 notes/topics/*.md 和 notes/daily/*.md 的 YAML frontmatter（--- 之间的部分）
- 只写 notes/INDEX.md 和 notes/TIMELINE.md
- 不改动任何笔记正文，可反复运行
"""
from __future__ import annotations

import sys
from pathlib import Path

NOTES = Path(__file__).resolve().parent.parent
TOPICS_DIR = NOTES / "topics"
DAILY_DIR = NOTES / "daily"

CATEGORY_ORDER = ["基础结构", "文本处理", "容器", "数据处理", "进阶", "工程", "项目"]
GENERATED_MARK = "<!-- 本文件由 notes/tools/build_index.py 自动生成，请勿手改；修改笔记 frontmatter 后重新运行脚本 -->"


def parse_frontmatter(path: Path) -> dict:
    """解析简单的 YAML frontmatter（key: value / key: [a, b]）。"""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"[警告] 读取失败：{path}（{exc}）", file=sys.stderr)
        return {}
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    meta: dict[str, object] = {}
    for line in text[3:end].splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
            meta[key] = items
        elif value:
            meta[key] = value.strip("'\"")
    return meta


def collect_topics() -> list[dict]:
    topics = []
    for path in sorted(TOPICS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        meta = parse_frontmatter(path)
        title = str(meta.get("title") or path.stem)
        category = str(meta.get("category") or "未分类")
        keywords = meta.get("keywords") or []
        dates = meta.get("dates") or []
        if isinstance(keywords, str):
            keywords = [keywords]
        if isinstance(dates, str):
            dates = [dates]
        if not str(meta.get("title") or "").strip():
            print(f"[警告] {path.name} 缺少 title，已用文件名代替", file=sys.stderr)
        topics.append(
            {
                "path": path,
                "title": title,
                "category": category,
                "keywords": keywords,
                "dates": sorted(dates),
            }
        )
    return topics


def collect_daily() -> list[dict]:
    notes = []
    for path in sorted(DAILY_DIR.glob("*.md"), reverse=True):
        if path.name.startswith("_"):
            continue
        meta = parse_frontmatter(path)
        date = str(meta.get("date") or path.stem)
        topics = meta.get("topics") or []
        if isinstance(topics, str):
            topics = [topics]
        notes.append(
            {
                "path": path,
                "date": date,
                "title": str(meta.get("title") or f"{date} 学习记录"),
                "topics": topics,
                "summary": str(meta.get("summary") or ""),
            }
        )
    notes.sort(key=lambda n: n["date"], reverse=True)
    return notes


def render_index(topics: list[dict]) -> str:
    categories: dict[str, list[dict]] = {}
    for t in topics:
        categories.setdefault(t["category"], []).append(t)

    order = [c for c in CATEGORY_ORDER if c in categories]
    order += [c for c in categories if c not in CATEGORY_ORDER]

    lines = [GENERATED_MARK, "", "# 📑 知识点总索引", ""]
    lines.append(
        f"> 共 **{len(topics)}** 个主题，**{len(order)}** 个分类。"
        "按知识点找笔记从这里进；按日期找去 [TIMELINE.md](TIMELINE.md)；"
        "原始目录见 [topics/](topics/)。"
    )
    lines.append("")
    for category in order:
        items = categories[category]
        lines.append(f"## {category}（{len(items)}）")
        lines.append("")
        lines.append("| 主题 | 关键词 | 笔记 | 记录日期 |")
        lines.append("| --- | --- | --- | --- |")
        for t in items:
            rel = t["path"].relative_to(NOTES).as_posix()
            keywords = "、".join(f"`{k}`" for k in t["keywords"]) or "—"
            dates = "、".join(t["dates"]) or "—"
            lines.append(f"| {t['title']} | {keywords} | [{t['path'].stem}]({rel}) | {dates} |")
        lines.append("")
    return "\n".join(lines)


def render_timeline(daily: list[dict]) -> str:
    lines = [GENERATED_MARK, "", "# 🗓️ 学习时间线（按日期）", ""]
    lines.append("| 日期 | 记录 | 涉及主题 |")
    lines.append("| --- | --- | --- |")
    for n in daily:
        rel = n["path"].relative_to(NOTES).as_posix()
        topics = "、".join(n["topics"]) or "—"
        lines.append(f"| {n['date']} | [{n['title']}]({rel}) | {topics} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    # Windows 控制台默认 GBK，避免 emoji 打印报错
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    topics = collect_topics()
    daily = collect_daily()
    (NOTES / "INDEX.md").write_text(render_index(topics), encoding="utf-8")
    (NOTES / "TIMELINE.md").write_text(render_timeline(daily), encoding="utf-8")
    print(f"[OK] 已生成 INDEX.md（{len(topics)} 个主题）与 TIMELINE.md（{len(daily)} 天记录）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
