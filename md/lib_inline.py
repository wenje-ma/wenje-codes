# -*- coding: utf-8 -*-
"""Collapse display math inside the citation library at the head of homework files into inline math.

Usage:
  python lib_inline.py --dry-run --list files.txt [--log out.log]
  python lib_inline.py --list files.txt [--log out.log]
"""
import re
import sys
from pathlib import Path

DELIM = re.compile(r'^(?:>\s*)?\$\$$')
BLANK_Q = re.compile(r'^>\s*$')
HEADER = re.compile(r'^>\s*\*\*')
SEP = re.compile(r'^(.*?)([;,])\\quad$')
TAIL = re.compile(r'^(.*?)([;,.])\s*$')
STOP = ('.', '。', '?', '!')


def load(path):
  text = Path(path).read_text(encoding='utf-8')
  eol = '\r\n' if '\r\n' in text else '\n'
  return text.split(eol), eol


def save(path, lines, eol):
  Path(path).write_text(eol.join(lines), encoding='utf-8', newline='')


def strip_gt(line):
  if line.startswith('>'):
    line = line[1:]
    if line.startswith(' '):
      line = line[1:]
  return line.strip()


def region_bounds(lines):
  start = None
  for i, l in enumerate(lines):
    if l.startswith('>'):
      start = i
      break
  if start is None:
    return None, None
  end = len(lines)
  for i in range(start, len(lines)):
    if lines[i].startswith('## '):
      end = i
      break
  return start, end


def skip_delim(lines, i, end):
  j = i + 1
  while j < end:
    if DELIM.match(lines[j]):
      return j + 1
    j += 1
  return end


def inline_math(content_lines, warn):
  segs = []
  cur = ''
  for raw in content_lines:
    t = strip_gt(raw)
    if not t:
      continue
    m = SEP.match(t)
    if m:
      segs.append((m.group(1), m.group(2)))
      cur = ''
      continue
    if t.endswith('\\quad'):
      warn.append('trailing \\quad without punctuation: ' + t)
      segs.append((t[:-5], ','))
      cur = ''
      continue
    cur += t
  frag = cur
  tail = ''
  m = TAIL.match(frag)
  if m:
    frag, tail = m.group(1), m.group(2)
  if not segs and not frag.strip():
    return '', '', True
  out = ''
  for seg, p in segs:
    seg = seg.strip()
    if seg:
      out += '$' + seg + '$' + p + ' '
  out += '$' + frag.strip() + '$' + tail
  return out, tail, False


def tokenize(body, warn):
  toks = []
  i = 0
  n = len(body)
  while i < n:
    l = body[i]
    if l.strip() == '' or BLANK_Q.match(l):
      toks.append(('blank', None, None, i, i + 1))
      i += 1
      continue
    if DELIM.match(l):
      close = skip_delim(body, i, n)
      s, tail, empty = inline_math(body[i + 1:close - 1], warn)
      if empty:
        warn.append('empty formula block')
        toks.append(('blank', None, None, i, close))
      else:
        toks.append(('disp', s, tail, i, close))
      i = close
      continue
    j = i
    heads = []
    while j < n and body[j].strip() != '' and not BLANK_Q.match(body[j]) and not DELIM.match(body[j]):
      t = strip_gt(body[j])
      if t:
        heads.append(t)
      j += 1
    toks.append(('prose', heads, None, i, j))
    i = j
  return toks


def glue(toks):
  """Drop blank tokens inside one sentence; every other token is kept as is."""
  keep = []
  i = 0
  n = len(toks)
  while i < n:
    t = toks[i]
    if t[0] != 'blank':
      keep.append(t)
      i += 1
      continue
    prev = keep[-1] if keep else None
    j = i
    while j < n and toks[j][0] == 'blank':
      j += 1
    nxt = toks[j] if j < n else None
    drop = False
    if prev and nxt:
      if prev[0] == 'disp' and nxt[0] == 'disp':
        drop = True
      elif prev[0] == 'prose' and nxt[0] == 'disp':
        drop = not prev[1][-1].endswith(STOP)
      elif prev[0] == 'disp' and nxt[0] == 'prose':
        drop = prev[2] != '.'
    if drop:
      i = j
      continue
    keep.extend(toks[i:j])
    i = j
  return keep


def render(para):
  text = ''
  for t in para:
    txt = t[1] if t[0] == 'disp' else ' '.join(t[1])
    text = text.rstrip() + ' ' + txt if text.strip() else txt
  return '> ' + text


def convert(path, dry):
  lines, eol = load(path)
  start, end = region_bounds(lines)
  if start is None:
    return 0, ['no citation library'], []
  heads = [i for i in range(start, end) if HEADER.match(lines[i])]
  out = []
  warn = []
  previews = []
  hit = 0
  i = 0
  while i < len(lines):
    if i < start or i >= end:
      out.append(lines[i])
      i += 1
      continue
    if not HEADER.match(lines[i]):
      if DELIM.match(lines[i]):
        close = skip_delim(lines, i, end)
        warn.append('display block outside any entry at line %d' % (i + 1))
        out.extend(lines[i:close])
        i = close
        continue
      out.append(lines[i])
      i += 1
      continue
    nxt = end
    for h in heads:
      if h > i:
        nxt = h
        break
    body = lines[i + 1:nxt]
    toks = tokenize(body, warn)
    out.append(lines[i])
    para = []

    def flush():
      nonlocal para
      if not para:
        return False
      cur, para = para, []
      s0 = min(t[3] for t in cur)
      s1 = max(t[4] for t in cur)
      kinds = set(t[0] for t in cur)
      if 'disp' in kinds and 'prose' in kinds:
        line = render(cur)
        previews.append((i + 1 + s0, line))
        out.append(line)
        return True
      if 'disp' in kinds:
        warn.append('formula-only paragraph at line %d' % (i + 1 + s0))
        line = render(cur)
        previews.append((i + 1 + s0, line))
        out.append(line)
        return True
      out.extend(body[s0:s1])
      return False

    for t in glue(toks):
      if t[0] == 'blank':
        if flush():
          hit += 1
        out.extend(body[t[3]:t[4]])
        continue
      para.append(t)
    if flush():
      hit += 1
    i = nxt
  if not dry and hit:
    save(path, out, eol)
  return hit, warn, previews


def main(argv):
  dry = False
  log = None
  args = []
  i = 0
  while i < len(argv):
    a = argv[i]
    if a == '--dry-run':
      dry = True
    elif a == '--log':
      i += 1
      log = argv[i]
    elif a == '--list':
      i += 1
      with open(argv[i], encoding='utf-8') as f:
        args.extend(x.strip() for x in f if x.strip())
    else:
      args.append(a)
    i += 1
  sink = open(log, 'w', encoding='utf-8', newline='') if log else None

  def say(s):
    if sink:
      sink.write(s + '\n')
    else:
      print(s)

  total = 0
  for p in args:
    hit, warn, previews = convert(p, dry)
    total += hit
    if hit or warn:
      say('%s: paras=%d' % (p, hit))
    for w in warn:
      say('  WARN ' + w)
    if dry and previews:
      for ln, text in previews:
        say('  L%d -> %s' % (ln, text))
  say('total rewritten paragraphs: %d' % total)
  if sink:
    sink.close()


if __name__ == '__main__':
  main(sys.argv[1:])
