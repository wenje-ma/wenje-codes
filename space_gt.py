# -*- coding: utf-8 -*-
"""自动为 > 和 < 后补一个空格，并保护 <br> 标签不被破坏。

处理逻辑（等价于“保护 <br> → 补空格 → 还原 <br>”）：
  1. 先把 <br> 临时替换为不可见占位符，避免后续对 < > 的处理破坏标签；
  2. 在 > 和 < 后面补一个空格——但仅当紧跟在后面的不是空格时才补，
     因此不会产生连续空格，也无需再做“双空格→单空格”的全局替换，
     从而保留正文中本来的连续空格（这是对“无条件补空格再压双空格”
     思路的安全改进，净效果一致）；
  3. 把占位符还原为 <br>。

运行方式：
  - 直接运行：弹出文件夹选择框，递归处理其中所有 .md / .qmd / .tex 文件；
  - 或带参数：python add_space_after_gt_lt.py <文件夹路径>（用于脚本化/无界面测试）。
"""
import re
import sys
from pathlib import Path
from tkinter import Tk, filedialog

# 占位符：几乎不可能出现在正文中的不可见串，避免与文档里已有的文本（如 ~~~~）冲突。
BR_PLACEHOLDER = "\x00__BR__\x00"

# 在 > 或 < 后补空格，但仅在后面不是空格时才补（(?! ) 为空格否定断言）。
ANGLE_AFTER = re.compile(r"(>|<)(?! )")


def convert(text: str) -> "tuple[str, int]":
    """返回 (新文本, 补了多少个空格)。"""
    text = text.replace("<br>", BR_PLACEHOLDER)          # 1. 保护 <br>
    text, n = ANGLE_AFTER.subn(r"\1 ", text)             # 2. > 和 < 后补空格
    text = text.replace(BR_PLACEHOLDER, "<br>")          # 3. 还原 <br>
    return text, n


def process_file(path: Path) -> None:
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")                # 识别 UTF-8 BOM
    data = raw[3:] if bom else raw
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        print(f"跳过（非 UTF-8）: {path}")
        return
    new, n = convert(text)
    if new == text:
        print(f"无需修改: {path}")
        return
    path.write_bytes((("\ufeff" if bom else "") + new).encode("utf-8"))  # 保留 BOM
    print(f"已转换: {path}  (+空格 ×{n})")


def process_folder(folder: str) -> None:
    folder_path = Path(folder)
    if not folder_path.is_dir():
        print(f"路径不是有效文件夹: {folder_path}")
        return
    exts = (".md", ".qmd", ".tex")
    targets = [p for p in folder_path.rglob("*")
               if p.is_file() and p.suffix.lower() in exts]
    targets.sort(key=lambda p: str(p).lower())
    if not targets:
        print(f"所选文件夹中没有 .md/.qmd/.tex 文件: {folder_path}")
        return
    print(f"共找到 {len(targets)} 个目标文件，开始转换…")
    for md_path in targets:
        process_file(md_path)
    print(f"转换完成，共处理 {len(targets)} 个文件。")


def select_folder_and_convert() -> None:
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="请选择要处理的文件夹（将递归处理其中所有 .md/.qmd/.tex 文件）")
    if not folder:
        print("未选择文件夹，退出。")
        return
    process_folder(folder)


if __name__ == "__main__":
    # 传入文件夹路径参数时无界面运行（便于测试）；否则弹出文件夹选择框。
    if len(sys.argv) > 1:
        process_folder(sys.argv[1])
    else:
        select_folder_and_convert()
