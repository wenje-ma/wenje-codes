# -*- coding: utf-8 -*-
"""apply_config: write the mdmath add-on's config.json into the Anki media
stylesheet (_mdmath_style.css). Run after editing config.json, with Anki closed:
    python apply_config.py
"""
import json
import os

ADDON = r"C:\Users\18904\AppData\Roaming\Anki2\addons21\mdmath"
MEDIA = r"C:\Users\18904\AppData\Roaming\Anki2\wenje\collection.media"


def user_css(c):
    def g(k, d):
        return c.get(k, d)

    fs = g("fontSize", 16)
    lh = g("lineHeight", 1.6)
    ff = g("fontFamily", '"LMRoman10","SimHei",serif')
    mf = g("monoFont", "Consolas,monospace")
    tc = g("textColor", "#111")
    bc = g("bgColor", "#fff")
    pm = g("pageMargin", "1in")
    pmm = g("pageMarginMobile", "0.5in")
    return (
        "body{background-color:%s;}\n"
        ".mdmath{font-family:%s;font-size:%dpx;line-height:%.2f;color:%s;padding:0 %s;}\n"
        "@media (max-width:768px){.mdmath{padding:0 %s;}}\n"
        ".mdmath pre,.mdmath code{font-family:%s;}\n"
        % (bc, ff, fs, lh, tc, pm, pmm, mf)
    )


def main():
    if not os.path.isfile(os.path.join(ADDON, "config.json")):
        print("config.json not found:", ADDON)
        return
    cfg = json.loads(open(os.path.join(ADDON, "config.json"), encoding="utf-8").read())
    base = open(os.path.join(ADDON, "assets", "style.css"), encoding="utf-8").read()
    out = (base + "\n" + user_css(cfg)).encode("utf-8")
    path = os.path.join(MEDIA, "_mdmath_style.css")
    open(path, "wb").write(out)
    print("applied config ->", path)
    print("fontSize=%spx margin=%s mobile=%s" % (cfg.get("fontSize"), cfg.get("pageMargin"), cfg.get("pageMarginMobile")))


if __name__ == "__main__":
    main()
