# -*- coding: utf-8 -*-
"""Sort the citation library at the top of every homework file.

The library runs from the first quote line to the first '## ' heading; an entry
starts at a line of the form '> **<type> <number> (...)'.  Its body may contain
unquoted $$ blocks, which travel with it.

Key: sequence number first (numeric, dot separated), then item type in the order
definition > axiom > lemma > proposition > theorem > corollary > remark.
Entries without a sequence number keep their relative order and go last.

Usage: python lib_sort.py [--dry-run] [path ...]
"""
import glob
import os
import re
import sys

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
HEADER = re.compile(r"^> *\*\*")
LEAD = re.compile(r"^>+ *\*\* *")
NUM = re.compile(r"^\s*(?:of\s+)?([0-9]+(?:\.[0-9]+)*)")
PAREN_NUM = re.compile(r"^\s*\(([0-9]+(?:\.[0-9]+)*)\)")


def find_library(lines):
    """Return (start, end) of the library region, or (None, None)."""
    qs = [i for i, s in enumerate(lines) if s.startswith(">")]
    hs = [i for i, s in enumerate(lines) if s.startswith("## ")]
    if not qs or not hs or hs[0] < qs[0]:
        return None, None
    return qs[0], hs[0]


def split_blocks(lines):
    """Split a region into entries; the first entry may start at any quote line."""
    starts = [0]
    for i in range(1, len(lines)):
        if HEADER.match(lines[i]):
            starts.append(i)
    starts.append(len(lines))
    return [lines[starts[i]:starts[i + 1]] for i in range(len(starts) - 1)]


def label(block):
    """Return (kind, number-or-None) for an entry."""
    text = LEAD.sub("", block[0]).strip()
    for tok in TYPE_WORDS:
        if text.startswith(tok):
            rest = text[len(tok):]
            m = NUM.match(rest) or PAREN_NUM.match(rest)
            return tok, (m.group(1) if m else None)
    return None, None


def key(block):
    kind, num = label(block)
    if num is None:
        return (1, (), RANK.get(kind, 7))
    return (0, tuple(int(x) for x in num.split(".")), RANK.get(kind, 7))


def process(path, dry):
    with open(path, "rb") as f:
        raw = f.read().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(nl)
    start, end = find_library(lines)
    if start is None:
        return "no-library", 0
    region = lines[start:end]
    blocks = split_blocks(region)
    ordered = sorted(blocks, key=key)
    if ordered == blocks:
        return "sorted", len(blocks)

    # trailing blank lines of the last block stay in place, right before the heading
    tail = []
    while ordered[-1] and ordered[-1][-1] == "":
        tail.insert(0, ordered[-1].pop())
    if not ordered[-1]:
        raise SystemExit("empty entry in %s" % path)

    head = [ln for b in ordered for ln in b]
    new = nl.join(lines[:start] + head + tail + lines[end:])
    if len(new.split(nl)) != len(lines):
        raise SystemExit("line count changed in %s" % path)
    if sorted(head + tail) != sorted(region):
        raise SystemExit("content changed in %s" % path)
    if not dry:
        with open(path, "wb") as f:
            f.write(new.encode("utf-8"))
    return "changed", len(blocks)


def main(argv):
    dry = "--dry-run" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        paths = sorted(set(glob.glob(r"D:\wenje-ma\*\homework-*\**\*.md", recursive=True)))
    counts = {}
    for p in paths:
        r, n = process(p, dry)
        counts[r] = counts.get(r, 0) + 1
        if r == "changed" and dry:
            print("would change %-3d %s" % (n, os.path.relpath(p, r"D:\wenje-ma")))
    print(counts)


if __name__ == "__main__":
    main(sys.argv[1:])
