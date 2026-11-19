# -*- coding: utf-8 -*-
"""Rebuild forced/fa-month2.md from the functional-analysis homework citation
libraries, then sort entries by section number and type per STYLE.md §32.

Order (lib_sort.py RANK): 定义 > 公理 > 引理 > 命题 > 定理 > 推论 > 注记;
其余类型(例/性质/公式/结论/习题/推导/...)排在已列类型之后.

2026-11-19: 首版按周次顺序拼接, 漏收 week9 末尾 定义/定理/注 3.1.1 三条;
重排脚本固化在此, 重建时一并补齐, 排序口径与 lib_sort.py 一致.
"""
import os
import re

SRC_DIR = r"D:\wenje-ma\functional-analysis\homework"
OUT = r"D:\wenje-ma\wenjemaths\forced\fa-month2.md"
WEEKS = ["week1.md", "week2.md", "week4.md", "week5.md",
         "week7.md", "week8.md", "week9.md"]

RANK = {}
for words, rank in (
    (("定义", "Definition"), 0),
    (("公理", "公设", "Axiom", "基本事实", "Basic Fact"), 1),
    (("引理", "Lemma"), 2),
    (("命题", "Proposition"), 3),
    (("定理", "Theorem"), 4),
    (("推论", "Corollary"), 5),
    (("注记", "注", "Remark", "Note", "说明", "Comment"), 6),
    (("例", "例题", "Example", "性质", "Property", "公式", "Formula",
      "结论", "Conclusion", "事实", "Fact", "习题", "Exercise",
      "方法", "Method", "法则", "Rule", "判定", "Criterion",
      "判定定理", "Criterion Theorem", "基本结论", "Basic Conclusion",
      "推导"), 7),
):
    for w in words:
        RANK[w] = rank

TYPE_WORDS = sorted(RANK, key=len, reverse=True)
HEADER_RE = re.compile(r"^\s*##\s+\*\*?")  # unused, kept for reference
LEAD_RE = re.compile(r"^\s*>?\s*\*\*\s*")
NUM_RE = re.compile(r"^\s*(?:of\s+)?([0-9]+(?:\.[0-9]+)*)")
PAREN_NUM_RE = re.compile(r"^\s*\(([0-9]+(?:\.[0-9]+)*)\)")


def split_blocks(lines):
    """Split the library region into entry blocks."""
    starts = [0]
    for i in range(1, len(lines)):
        if re.match(r"^\s*>?\s*\*\*", lines[i]):
            starts.append(i)
    starts.append(len(lines))
    return [lines[starts[i]:starts[i + 1]] for i in range(len(starts) - 1)]


def label(block):
    text = LEAD_RE.sub("", block[0]).strip()
    for tok in TYPE_WORDS:
        if text.startswith(tok):
            rest = text[len(tok):]
            m = NUM_RE.match(rest) or PAREN_NUM_RE.match(rest)
            return tok, (m.group(1) if m else None)
    return None, None


def sort_key(block):
    kind, num = label(block)
    if num is None:
        return (1, (), RANK.get(kind, 7))
    return (0, tuple(int(x) for x in num.split(".")), RANK.get(kind, 7))


def strip_block(block):
    out = []
    for ln in block:
        ln = re.sub(r"^>\s?", "", ln)
        if re.match(r"^\*\*(.*)\*\*\s*$", ln):
            ln = "## " + re.match(r"^\*\*(.*)\*\*\s*$", ln).group(1)
        out.append(ln)
    while out and out[-1].strip() == "":
        out.pop()
    return out


blocks = []
for week in WEEKS:
    path = os.path.join(SRC_DIR, week)
    with open(path, "rb") as f:
        raw = f.read().decode("utf-8")
    lines = raw.split("\r\n" if "\r\n" in raw else "\n")
    # library = from first '>' line to first '## ' problem heading
    qs = [i for i, s in enumerate(lines) if s.startswith(">")]
    hs = [i for i, s in enumerate(lines) if s.startswith("## ")]
    if not qs or not hs:
        continue
    region = lines[qs[0]:hs[0]]
    for b in split_blocks(region):
        if any(x.strip() for x in b):
            blocks.append(b)

ordered = sorted(blocks, key=sort_key)
parts = ["\n\n".join("\n".join(strip_block(b)) for b in ordered)]
content = parts[0].rstrip() + "\n"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "wb") as f:
    f.write(content.encode("utf-8"))

print("entries: %d" % len(ordered))
for b in ordered:
    kind, num = label(b)
    print("%-10s %-8s %s" % (kind, num, LEAD_RE.sub("", b[0]).strip()))
