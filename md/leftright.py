import re
from pathlib import Path
from tkinter import Tk,filedialog,messagebox
MD_LINK=r"!?\[[^\]]*\]\([^)]*\)"
DELIM=r"(?:\(|\)|\[|\]|\\\{|\\\}|\\langle|\\rangle|\||\.)"
WRAPPED=MD_LINK+r"|\\left\s*"+DELIM+r"|\\right\s*"+DELIM+r"|\\[bB]ig(?:g|l|r)?\s*"+DELIM
BARE=r"(?<!\\)(\(|\)|\[|\])|(\\\{|\\\})|(\\langle|\\rangle)"
PAT=re.compile(WRAPPED+"|"+BARE)
BAR=re.compile(r"(?<!\\)((?:\\\\)*\\?)\|")
WRAPPED_PRE=re.compile(r"(?:\\left|\\right|\\[bB]ig(?:g|l|r)?|\\middle)\s*$")
FENCE=re.compile(r"[ \t]{0,3}(`{3,}|~{3,})")
FM_OPEN=re.compile(r"---[ \t]*\r?\n")
FM_CLOSE=re.compile(r"\r?\n(?:---|\.\.\.)[ \t\r]*(?=\r?\n|$)")
HTML_BLOCK=re.compile(r"<(pre|code|script|style)\b[^>]*>.*?</\1\s*>",re.S|re.I)
HTML_COMMENT=re.compile(r"<!--.*?-->",re.S)
VERB_ENV=re.compile(r"\\begin\{(verbatim\*?|Verbatim|lstlisting|minted|alltt|comment)\}.*?\\end\{\1\}",re.S)
VERB=re.compile(r"\\(?:verb|lstinline)\*?(.)")
TEXT_ARG=re.compile(r"\\(?:text|mbox|textrm|textnormal|operatorname|intertext|textsf|texttt)\s*{")
OPT_ARG=re.compile(r"\\([A-Za-z]+)\*?\[")
BRK_OPT=re.compile(r"\\\\[ \t]*\[[^\]\n]*\]")   # \\[4pt] 这类换行间距参数, 里面的方括号不是配对括号
OPT_SKIP=frozenset("""
left right big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr middle
""".split())
TEX_COMMENT=re.compile(r"(?<!\\)%[^\n]*")
ENVS=("equation","equation*","align","align*","alignat","alignat*","gather","gather*",
      "multline","multline*","eqnarray","eqnarray*","flalign","flalign*","displaymath",
      "math","split","split*")
BEGIN_ENV=re.compile(r"\\begin\{("+"|".join(re.escape(e) for e in ENVS)+r")\}")
DL_IN=re.compile(r"(?<!\\)\\\(")
DL_IN_CLOSE=re.compile(r"(?<!\\)\\\)")
DL_OUT=re.compile(r"(?<!\\)\\\[")
DL_OUT_CLOSE=re.compile(r"(?<!\\)\\\]")
def mask_of(text:str,spans)->bytearray:
  m=bytearray(len(text))
  for a,b in spans:
    m[a:b]=b"\x01"*(b-a)
  return m
def env_spans(text:str)->"list[tuple[int,int]]":
  spans=[]
  for m in BEGIN_ENV.finditer(text):
    tag="\\end{"+m.group(1)+"}"
    k=text.find(tag,m.end())
    if k<0:
      continue
    spans.append((m.start(),k+len(tag)))
  return spans
def normalize_delims(text:str,ext:str)->"tuple[str,int,int]":
  # \( \) \x5c[ \x5c] 一律并成 $ 与 $$; .tex 里这两种是原生写法, 只认不改
  if ext not in(".md",".qmd"):
    return text,0,0
  prot=protected_spans(text,ext)
  out=[]
  pos=0
  n_in=n_out=0
  for a,b in prot:
    if a<pos:
      continue
    seg=text[pos:a]
    for pat,rep in((DL_IN,"$"),(DL_IN_CLOSE,"$"),(DL_OUT,"$$"),(DL_OUT_CLOSE,"$$")):
      seg,c=pat.subn(rep,seg)
      if pat is DL_IN or pat is DL_IN_CLOSE:
        n_in+=c
      else:
        n_out+=c
    out.append(seg)
    out.append(text[a:b])
    pos=b
  tail=text[pos:]
  for pat,rep in((DL_IN,"$"),(DL_IN_CLOSE,"$"),(DL_OUT,"$$"),(DL_OUT_CLOSE,"$$")):
    tail,c=pat.subn(rep,tail)
    if pat is DL_IN or pat is DL_IN_CLOSE:
      n_in+=c
    else:
      n_out+=c
  out.append(tail)
  return "".join(out),n_in,n_out
def fenced_ranges(text:str)->"list[tuple[int,int]]":
  ranges=[]
  i,n=0,len(text)
  opened=None
  marker=""
  while i<n:
    eol=text.find("\n",i)
    eol=n if eol<0 else eol+1
    m=FENCE.match(text,i)
    if opened is None:
      if m:
        opened=i
        marker=m.group(1)
    elif m and m.group(1)[0]==marker[0] and len(m.group(1))>=len(marker):
      ranges.append((opened,eol))
      opened=None
      marker=""
    i=eol
  if opened is not None:
    ranges.append((opened,n))
  return ranges
def front_matter_end(text:str)->int:
  m=FM_OPEN.match(text)
  if m is None:
    return 0
  k=FM_CLOSE.search(text,m.end()-1)
  return 0 if k is None else k.end()
def brace_end(text:str,i:int)->"int|None":
  d=0
  n=len(text)
  while i<n:
    c=text[i]
    if c=="\\":
      i+=2
      continue
    if c=="{":
      d+=1
    elif c=="}":
      d-=1
      if d==0:
        return i+1
    i+=1
  return None
def bracket_end(text:str,i:int)->"int|None":
  d=0
  n=len(text)
  while i<n:
    c=text[i]
    if c=="\\":
      i+=2
      continue
    if c=="[":
      d+=1
    elif c=="]":
      d-=1
      if d==0:
        return i+1
    i+=1
  return None
def inline_code_ranges(text:str,mask:bytearray)->"list[tuple[int,int]]":
  ranges=[]
  i,n=0,len(text)
  while i<n:
    if text[i]!="`" or mask[i]:
      i+=1
      continue
    k=1
    while i+k<n and text[i+k]=="`":
      k+=1
    j=i+k
    while j<n and text[j]!="\n":
      if text[j]!="`":
        j+=1
        continue
      m=1
      while j+m<n and text[j+m]=="`":
        m+=1
      if m==k:
        ranges.append((i,j+m))
        i=j+m
        break
      j+=m
    else:
      i=i+k
  return ranges
def html_ranges(text:str)->"list[tuple[int,int]]":
  ranges=[]
  for pat in(HTML_BLOCK,HTML_COMMENT,VERB_ENV):
    for m in pat.finditer(text):
      ranges.append((m.start(),m.end()))
  return ranges
def verb_ranges(text:str,mask:bytearray)->"list[tuple[int,int]]":
  # 行内反引号里的 \verb 字样不算命令; 定界符也不能是反引号/反斜杠/空白, 否则会把行内代码吃掉
  ranges=[]
  for m in VERB.finditer(text):
    if mask[m.start()]:
      continue
    delim=m.group(1)
    if delim.isalnum() or delim in "`\\" or delim.isspace():
      continue
    k=text.find(delim,m.end())
    if k>=0:
      ranges.append((m.start(),k+1))
  return ranges
def text_arg_ranges(text:str)->"list[tuple[int,int]]":
  ranges=[]
  for m in TEXT_ARG.finditer(text):
    b=brace_end(text,m.end()-1)
    if b is not None:
      ranges.append((m.end()-1,b))
  return ranges
def opt_arg_ranges(text:str)->"list[tuple[int,int]]":
  # \\sqrt[n]{x} 的 [n] 是可选参数, 包上 \\left 会编译不过
  ranges=[]
  for m in OPT_ARG.finditer(text):
    if m.group(1) in OPT_SKIP:
      continue
    b=bracket_end(text,m.end()-1)
    if b is not None:
      ranges.append((m.end()-1,b))
  return ranges
def indented_code_ranges(text:str)->"list[tuple[int,int]]":
  # 4 格缩进代码块; 含 \\命令 或 $$ 的块按公式处理, 免得漏改真公式
  ranges=[]
  offs=[]
  pos=0
  for line in text.splitlines(keepends=True):
    offs.append((pos,line))
    pos+=len(line)
  n=len(offs)
  i=0
  while i<n:
    line=offs[i][1]
    ind=line.startswith("    ") or line.startswith("\t")
    prev_blank=i==0 or offs[i-1][1].strip()==""
    if ind and prev_blank:
      j=i
      block=[]
      while j<n:
        l=offs[j][1]
        if l.strip()=="" or l.startswith("    ") or l.startswith("\t"):
          block.append(offs[j])
          j+=1
        else:
          break
      seg="".join(x[1] for x in block)
      if "$$" not in seg and not re.search(r"\\[A-Za-z]",seg):
        ranges.append((block[0][0],block[-1][0]+len(block[-1][1])))
      i=j
      continue
    i+=1
  return ranges
def protected_spans(text:str,ext:str="")->"list[tuple[int,int]]":
  spans=[]
  fm=front_matter_end(text)
  if fm:
    spans.append((0,fm))
  spans.extend(fenced_ranges(text))
  spans.extend(html_ranges(text))
  if ext in(".md",".qmd"):
    spans.extend(indented_code_ranges(text))
  if ext==".tex":
    spans.extend((m.start(),m.end()) for m in TEX_COMMENT.finditer(text))
  spans.sort()
  # 先认行内代码, 再在代码之外认 \verb, 最后带着 \verb 重算一次行内代码(verbatim 内容可能含反引号)
  mask=mask_of(text,spans)
  code=inline_code_ranges(text,mask)
  spans2=spans+code
  mask2=mask_of(text,spans2)
  verb=verb_ranges(text,mask2)
  mask3=mask_of(text,spans2+verb)
  spans2.extend(inline_code_ranges(text,mask3))
  spans2.extend(verb)
  spans2.extend(text_arg_ranges(text))
  spans2.extend(opt_arg_ranges(text))
  spans2.extend((m.start(),m.end()) for m in BRK_OPT.finditer(text))
  spans2.sort()
  return spans2
def math_spans(text:str,ext:str=""):
  spans=[]
  prot=protected_spans(text,ext)
  pmask=mask_of(text,prot)
  envs=[(a,b) for a,b in env_spans(text) if not pmask[a]]
  pk=0
  ek=0
  i,n=0,len(text)
  while i<n:
    while pk<len(prot) and prot[pk][1]<=i:
      pk+=1
    if pk<len(prot) and prot[pk][0]<=i<prot[pk][1]:
      i=prot[pk][1]
      continue
    while ek<len(envs) and envs[ek][1]<=i:
      ek+=1
    if ek<len(envs) and envs[ek][0]==i:
      spans.append(envs[ek])
      i=envs[ek][1]
      continue
    c=text[i]
    if text.startswith("\\(",i) or text.startswith("\\[",i):
      closer="\\)" if c=="\\" and text[i+1]=="(" else "\\]"
      k=text.find(closer,i+2)
      if k<0:
        print(f"Warning: unclosed {text[i:i+2]} at line {text.count(chr(10),0,i)+1} (rest of file left alone)")
        break
      spans.append((i,k+2))
      i=k+2
      continue
    if c=="\\":
      i+=2
      continue
    if c=="$":
      if i+1<n and text[i+1]=="$":
        j=text.find("$$",i+2)
        if j<0:
          print(f"Warning: unclosed $$ at line {text.count(chr(10),0,i)+1} (rest of file left alone)")
          break
        spans.append((i,j+2))
        i=j+2
      else:
        j=i+1
        while True:
          k=text.find("$",j)
          if k<0:
            break
          if k>0 and text[k-1] not in " \t\r\n":
            j=k
            break
          j=k+1
        if k<0:
          print(f"Warning: unclosed $ at line {text.count(chr(10),0,i)+1} (rest of file left alone)")
          break
        spans.append((i,k+1))
        i=k+1
    else:
      i+=1
  return spans
def _is_wrapped_before(seg:str,i:int)->bool:
  return bool(re.search(r"(?:\\left|\\right|\\[bB]ig(?:g|l|r)?|\\middle)\s*$",seg[:i]))
def convert_span(span:str,prot_local=None)->str:
  # 整段先配对, 只包"两端都落在可改区"的括号; 半开区间 \\left(...\\right] 允许左右定界符不同
  n=len(span)
  prot_local=prot_local or bytearray(n)
  opens={"(":")","[":"]","{":"}","\\{":"\\}","\\langle":"\\rangle"}
  events=[]     # (pos, is_open, tok_pos_len)
  i=0
  while i<n:
    ch=span[i]
    if ch=="\\" and i+1<n and span[i+1] in "{l":
      if span[i+1]=="{":
        tok="\\{"
        if not prot_local[i] and not _is_wrapped_before(span,i):
          events.append((i,True,2))
        i+=2
        continue
      m=re.match(r"\\langle",span[i:])
      if m:
        if not prot_local[i] and not _is_wrapped_before(span,i):
          events.append((i,True,len(m.group(0))))
        i+=len(m.group(0))
        continue
      i+=1
      continue
    if ch=="\\" and i+1<n and span[i+1]=="}":
      if not prot_local[i] and not _is_wrapped_before(span,i):
        events.append((i,False,2))
      i+=2
      continue
    if span.startswith("\\rangle",i):
      if not prot_local[i] and not _is_wrapped_before(span,i):
        events.append((i,False,len("\\rangle")))
      i+=len("\\rangle")
      continue
    if ch in "([":
      if not prot_local[i] and not _is_wrapped_before(span,i):
        events.append((i,True,1))
      i+=1
      continue
    if ch in ")]":
      if not prot_local[i] and not _is_wrapped_before(span,i):
        events.append((i,False,1))
      i+=1
      continue
    i+=1
  # 按嵌套顺序配对(不限类型, 与 LaTeX 的 \left/\right 规则一致)
  stack=[]; pairs=[]
  for pos,is_open,ln in events:
    if is_open:
      stack.append(pos)
    else:
      if stack:
        pairs.append((stack.pop(),pos))
      # 没有对应的开括号: 保持裸写, 不硬塞 \right
  edits=[]
  for o,c in pairs:
    edits.append((o,"\\left"))
    edits.append((c,"\\right"))
  # 竖线另行成对(不受括号嵌套影响)
  bars=[]
  for m in BAR.finditer(span):
    if prot_local[m.start()] or _is_wrapped_before(span,m.start()):
      continue
    bars.append((m.start(),m.end()))
  if len(bars)%2:
    print(f"Warning: odd | count in math span (skipped): {span[:60]!r}")
  else:
    for k,(a,b) in enumerate(bars):
      edits.append((a,"\\left" if k%2==0 else "\\right"))
  edits.sort(key=lambda x:-x[0])
  out=span
  for pos,txt in edits:
    out=out[:pos]+txt+out[pos:]
  return out
BIGCMD=re.compile(r"\\(?:biggl|biggr|biggm|bigg|Biggl|Biggr|Biggm|Bigg|bigl|bigr|bigm|big|Bigl|Bigr|Bigm|Big)(?![A-Za-z])")
BIG_DELIM=(("\\{","o"),("\\}","c"),("\\|","b"),("\\Vert","b"),("\\vert","b"),
  ("\\lvert","o"),("\\rvert","c"),("\\lVert","o"),("\\rVert","c"),
  ("\\langle","o"),("\\rangle","c"),("\\lbrack","o"),("\\rbrack","c"),
  ("\\lfloor","o"),("\\rfloor","c"),("\\lceil","o"),("\\rceil","c"),
  ("\\backslash","o"),("\\uparrow","o"),("\\downarrow","c"),
  ("(","o"),(")","c"),("[","o"),("]","c"),("|","b"),("/","s"),(".","n"))
CMD_TOKEN=re.compile(r"\\(?:[A-Za-z]+|.)")
ARG_CMD=frozenset("""
frac dfrac tfrac cfrac binom tbinom dbinom mathrm mathbf boldsymbol mathbb mathcal
mathfrak mathsf mathtt mathit mathnormal operatorname text mbox hbox dot ddot hat
check bar tilde vec acute grave breve widehat widetilde overline underline sqrt
underbrace overbrace overset underset substack mathop mathrel mathbin mathord
mathopen mathclose mathpunct
""".split())
TALL=re.compile(r"\\(?:frac|dfrac|tfrac|sqrt|sum|prod|int|iint|iiint|oint|left|right|begin|end|middle|binom|overbrace|underbrace)")
def skip_scripts(s:str,j:int)->int:
  n=len(s)
  while j<n and s[j] in "_^":
    j+=1
    if j<n and s[j]=="{":
      e=brace_end(s,j)
      if e is None:
        return j
      j=e
    else:
      j+=1
  while j<n and s[j]=="'":
    j+=1
  return j
def delims_end(s:str,i:int)->int:
  # \\right 后面跟着的定界符可以是 \\} 这种双字符, 也可以是一个字符
  if i>=len(s):
    return i
  if s[i]!="\\":
    return i+1
  for d,_ in BIG_DELIM:
    if s.startswith(d,i):
      return i+len(d)
  return i+2
def tokenize(s:str,mask:bytearray)->"tuple[list,list]":
  # 把公式区分成原子与分隔符, 只为找"取值竖线"前面的那个原子
  atoms=[]
  seps=[]
  i,n=0,len(s)
  while i<n:
    c=s[i]
    if c in " \t\r\n" or mask[i]:
      i+=1
      continue
    if s.startswith("\\\\",i):
      j=i+2
      if j<n and s[j]=="[":
        e=bracket_end(s,j)
        j=e if e else j
      seps.append((i,j))
      i=j
      continue
    if c in "&=+-<>|,;:$":
      seps.append((i,i+1))
      i+=1
      continue
    if c=="\\" and s.startswith("\\left",i) and not (i+5<n and s[i+5].isalpha()):
      j=delims_end(s,i+5)
      d=1
      while j<n and d:
        if s.startswith("\\left",j) and not (j+5<n and s[j+5].isalpha()):
          d+=1
          j=delims_end(s,j+5)
          continue
        if s.startswith("\\right",j) and not (j+6<n and s[j+6].isalpha()):
          d-=1
          j=delims_end(s,j+6)
          continue
        j+=1
      j=skip_scripts(s,j)
      atoms.append((i,j))
      i=j
      continue
    if c=="{":
      e=brace_end(s,i)
      if e is None:
        atoms.append((i,i+1))
        i+=1
        continue
      e=skip_scripts(s,e)
      atoms.append((i,e))
      i=e
      continue
    if c=="\\":
      m=CMD_TOKEN.match(s,i)
      j=m.end()
      word=m.group(0)[1:]
      if word=="begin" or word=="end":
        while j<n and s[j] in " \t":
          j+=1
        if j<n and s[j]=="{":
          e=brace_end(s,j)
          j=e if e else j
        seps.append((i,j))
        i=j
        continue
      if word in ARG_CMD:
        while True:
          k=j
          while k<n and s[k]==" ":
            k+=1
          if k<n and s[k]=="{" and not mask[k]:
            e=brace_end(s,k)
            if e is None:
              break
            j=e
            continue
          if k<n and s[k]=="[":
            e=bracket_end(s,k)
            if e is None:
              break
            j=e
            continue
          break
      j=skip_scripts(s,j)
      atoms.append((i,j))
      i=j
      continue
    j=skip_scripts(s,i+1)
    atoms.append((i,j))
    i=j
  return atoms,seps
def is_simple(s:str,a:int,b:int)->bool:
  t=s[a:b]
  if len(t)>16 or TALL.search(t):
    return False
  if any(c in t for c in "{}\\"):
    return bool(re.fullmatch(r"\\(?:boldsymbol|mathrm|mathbf|mathcal|mathbb|operatorname|dot|ddot|hat|bar|tilde)\{[^{}]*\}",t))
  return bool(re.fullmatch(r"[A-Za-z0-9']+",t))
def operand_start(s:str,mask:bytearray,atoms,pos:int)->"int|None":
  # 取值竖线 \\big|_x 的左侧就是紧邻的那一个原子; 前面若还是简单因子 S 或 a, 一并收进来
  k=pos
  while k>0 and s[k-1] in " \t":
    k-=1
  idx=None
  for t,at in enumerate(atoms):
    if at[1]<=k:
      idx=t
    else:
      break
  if idx is None or atoms[idx][1]!=k:
    return None
  a=atoms[idx][0]
  p=idx-1
  while p>=0 and is_simple(s,atoms[p][0],atoms[p][1]) and atoms[p][1]==a:
    a=atoms[p][0]
    p-=1
  return a if not mask[a] else None
def operand_after(s:str,atoms,pos:int)->"tuple|None":
  # 斜杠右侧的分母: 从紧跟的那个原子起, 把相邻的因子一并收进来, 遇到运算符就停
  idx=None
  for t,at in enumerate(atoms):
    if at[0]>=pos:
      idx=t
      break
  if idx is None:
    return None
  a,b=atoms[idx]
  p=idx+1
  while p<len(atoms) and s[atoms[p-1][1]:atoms[p][0]].strip()=="":
    b=atoms[p][1]
    p+=1
  return a,b
def convert_big_span(s:str,mask:bytearray)->"tuple[str,list,list]":
  # \\big 族一律改写成 \\left/\\right: 成对的括号/竖线直接配, 取值竖线补 \\left., 斜杠后面补 \\right.
  toks=[]
  for m in BIGCMD.finditer(s):
    if mask[m.start()]:
      continue
    j=m.end()
    while j<len(s) and s[j] in " \t":
      j+=1
    dl,cl="", "n"
    for d,k in BIG_DELIM:
      if s.startswith(d,j):
        dl,cl=d,k
        break
    toks.append((m.start(),j+len(dl),dl,cl))
  if not toks:
    return s,[],[]
  atoms,_=tokenize(s,mask)
  edits=[]
  warns=[]
  stack=[]
  bars=[]
  for st,en,dl,cl in toks:
    if cl=="o":
      stack.append((st,en,dl))
    elif cl=="c":
      if stack:
        o=stack.pop()
        edits.append((o[0],o[1],"\\left"+o[2]))
        edits.append((st,en,"\\right"+dl))
      else:
        warns.append(("orphan-close",st,dl))
    elif cl=="b":
      if s[en:en+1]=="_":
        a=operand_start(s,mask,atoms,st)
        if a is None:
          warns.append(("no-operand",st,dl))
          continue
        edits.append((a,a,"\\left."))
        edits.append((st,en,"\\right"+dl))
      else:
        bars.append((st,en,dl))
    elif cl=="s":
      nx=operand_after(s,atoms,en)
      if nx is None:
        warns.append(("no-operand",st,dl))
        continue
      edits.append((st,en,"\\left/"))
      edits.append((nx[1],nx[1],"\\right."))
    else:
      warns.append(("no-delim",st,dl))
  for o in stack:
    warns.append(("orphan-open",o[0],o[2]))
  if len(bars)%2:
    warns.append(("odd-bars",bars[-1][0],bars[-1][2]))
  for k in range(0,len(bars)-len(bars)%2,2):
    edits.append((bars[k][0],bars[k][1],"\\left"+bars[k][2]))
    edits.append((bars[k+1][0],bars[k+1][1],"\\right"+bars[k+1][2]))
  edits.sort(key=lambda e:(-e[0],-e[1]))
  out=s
  for p,e,r in edits:
    out=out[:p]+r+out[e:]
  return out,edits,warns
def normalize_big(text:str,ext:str="")->"tuple[str,int]":
  prot=protected_spans(text,ext)
  out=[]
  pos=0
  n=0
  for a,b in math_spans(text,ext):
    out.append(text[pos:a])
    mask=bytearray(b-a)
    for p,q in prot:
      if q<=a or p>=b:
        continue
      mask[max(p,a)-a:min(q,b)-a]=b"\x01"*(min(q,b)-max(p,a))
    new,edits,warns=convert_big_span(text[a:b],mask)
    for w in warns:
      print(f"Warning: \\big {w[0]} at {w[2]!r} near {text[a:b][max(0,w[1]-40):w[1]+40]!r}")
    n+=len(edits)
    out.append(new)
    pos=b
  out.append(text[pos:])
  return "".join(out),n
def convert_segment(chunk:str,base:int,prot)->str:
  # 公式区内部也可能有受保护区(\\text{} 的参数, \\sqrt 的可选参数, \\verb 等), 只标出不改, 配对照整段算
  n=len(chunk)
  mask=bytearray(n)
  end=base+n
  for a,b in prot:
    if b<=base or a>=end:
      continue
    a2=max(a,base)-base
    b2=min(b,end)-base
    mask[a2:b2]=b"\x01"*(b2-a2)
  return convert_span(chunk,mask)
def convert(text:str,ext:str="")->str:
  prot=protected_spans(text,ext)
  out=[]
  pos=0
  for a,b in math_spans(text,ext):
    out.append(text[pos:a])
    out.append(convert_segment(text[a:b],a,prot))
    pos=b
  out.append(text[pos:])
  return "".join(out)
def process_file(path:Path):
  raw=path.read_bytes()
  bom=raw.startswith(b"\xef\xbb\xbf")
  data=raw[3:] if bom else raw
  try:
    text=data.decode("utf-8")
  except UnicodeDecodeError:
    print(f"Skipped (non-UTF-8): {path}")
    return
  ext=path.suffix.lower()
  norm,n_in,n_out=normalize_delims(text,ext)
  norm,n_big=normalize_big(norm,ext)
  new=convert(norm,ext)
  if new==text:
    print(f"No change: {path}")
    return
  path.write_bytes((("\ufeff" if bom else "")+new).encode("utf-8"))
  n1=new.count("\\left(")-text.count("\\left(")
  n2=new.count("\\left[")-text.count("\\left[")
  n3=new.count("\\left\\{")-text.count("\\left\\{")
  n4=new.count("\\left|")-text.count("\\left|")
  n5=new.count("\\left\\|")-text.count("\\left\\|")
  n6=new.count("\\left\\langle")-text.count("\\left\\langle")
  n7=new.count("\\right\\rangle")-text.count("\\right\\rangle")
  print(f"Converted: {path}  (+\\big->\\left/\\right x{n_big}, +\\left( x{n1}, +\\left[ x{n2}, +\\left\\{{ x{n3}, +\\left| x{n4}, +\\left\\| x{n5}, +\\left\\langle x{n6}, +\\right\\rangle x{n7}, \\(\\)->$ x{n_in}, \\[\\]->$$ x{n_out})")
def select_folder_and_convert_mds():
  root=Tk()
  root.withdraw()
  folder=filedialog.askdirectory(title="Select folder (recursively processes .md/.qmd/.tex)")
  if not folder:
    print("No folder selected, exit.")
    return[]
  folder_path=Path(folder)
  exts=(".md",".qmd",".tex")
  targets=[p for p in folder_path.rglob("*") if p.is_file() and p.suffix.lower() in exts]
  targets.sort(key=lambda p: str(p).lower())
  if not targets:
    print(f"No .md/.qmd/.tex files in folder: {folder_path}")
    return[]
  print(f"Found {len(targets)} target files, converting...")
  for md_path in targets:
    process_file(md_path)
  print(f"Done, processed {len(targets)} files.")
if __name__=="__main__":
  select_folder_and_convert_mds()
