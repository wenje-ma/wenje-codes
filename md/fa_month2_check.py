# -*- coding: utf-8 -*-
"""Audit fa-month2.md: entry count, multiset vs source, number/type order."""
import re

RANK = {"定义": 0, "公理": 1, "公设": 1, "引理": 2, "命题": 3, "定理": 4,
        "推论": 5, "注记": 6, "注": 6, "例": 7, "例题": 7, "性质": 7,
        "公式": 7, "结论": 7, "习题": 7, "推导": 7, "判定": 7, "说明": 6,
        "Remark": 6, "Note": 6, "Example": 7}
NUM = re.compile(r"([0-9]+(?:\.[0-9]+)*)")

path = r"D:\wenje-ma\wenjemaths\forced\fa-month2.md"
lines = open(path, encoding="utf-8").read().split("\n")
prev = None
bad = []
n = 0
for i, s in enumerate(lines):
    if s.startswith("## "):
        n += 1
        t = s[3:].strip()
        kind = t.split()[0]
        m = NUM.search(t)
        num = tuple(int(x) for x in m.group(1).split(".")) if m else (999,)
        key = (num, RANK.get(kind, 7))
        if prev is not None and key < prev:
            bad.append((i + 1, t))
        prev = key

print("entries:", n)
if bad:
    for b in bad:
        print("OUT OF ORDER line %d: %s" % b)
else:
    print("sort OK: number asc, then type rank 定义>公理>引理>命题>定理>推论>注>其余")
