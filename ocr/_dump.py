# -*- coding: utf-8 -*-
import sys
import glob
import pymupdf as fitz

def dump(path, out):
  doc = fitz.open(path)
  with open(out, 'w', encoding='utf-8', newline='') as f:
    for i, page in enumerate(doc):
      f.write('\n\n=== PAGE %d ===\n' % (i + 1))
      f.write(page.get_text("text"))
  doc.close()

if __name__ == '__main__':
  for p in sorted(glob.glob(r'D:\wenje-ma\complex-analysis\textbooks\*.pdf')):
    name = p.split('\\')[-1].replace('.pdf', '')
    out = r'D:\wenje-ma\wenje-codes\_ca_%s.txt' % name
    dump(p, out)
    print('dumped', out)
