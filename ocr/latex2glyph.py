"""Flatten LaTeX math into the character stream a TeX-compiled PDF exposes.

A TeX PDF keeps every glyph's identity but loses the structure: a subscript
becomes a shifted glyph, a fraction becomes three lines, a brace becomes
nothing. Copying a formula out of such a PDF therefore yields correct
characters in reading order. That is the target this module reproduces for
OCR output: drop the markup, keep the characters.
"""
import re
import unicodedata

GREEK = {
  "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "varepsilon": "ε",
  "zeta": "ζ", "eta": "η", "theta": "θ", "vartheta": "θ", "iota": "ι", "kappa": "κ",
  "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π", "varpi": "π", "rho": "ρ",
  "varrho": "ρ", "sigma": "σ", "varsigma": "ς", "tau": "τ", "upsilon": "υ", "phi": "φ",
  "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω",
  "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ", "Pi": "Π",
  "Sigma": "Σ", "Upsilon": "Υ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω",
}

SYMBOLS = {
  "in": "∈", "notin": "∉", "ni": "∋", "leq": "≤", "le": "≤", "geq": "≥", "ge": "≥",
  "neq": "≠", "ne": "≠", "approx": "≈", "equiv": "≡", "cong": "≅", "sim": "∼",
  "simeq": "≃", "ll": "≪", "gg": "≫", "subset": "⊂", "subseteq": "⊆", "subsetneq": "⊊",
  "supset": "⊃", "supseteq": "⊇", "cup": "∪", "cap": "∩", "setminus": "\\",
  "emptyset": "∅", "varnothing": "∅", "complement": "∁",
  "forall": "∀", "exists": "∃", "nexists": "∄", "neg": "¬", "land": "∧", "lor": "∨",
  "wedge": "∧", "vee": "∨", "Rightarrow": "⇒", "Leftarrow": "⇐", "Leftrightarrow": "⇔",
  "leftrightarrow": "↔", "rightarrow": "→", "to": "→", "leftarrow": "←", "gets": "←",
  "mapsto": "↦", "uparrow": "↑", "downarrow": "↓", "nearrow": "↗", "searrow": "↘",
  "times": "×", "div": "÷", "cdot": "·", "pm": "±", "mp": "∓", "ast": "*",
  "infty": "∞", "partial": "∂", "nabla": "∇", "sum": "Σ", "prod": "Π", "coprod": "∐",
  "int": "∫", "iint": "∬", "iiint": "∭", "oint": "∮", "sqrt": "√",
  "prime": "′", "degree": "°", "ell": "ℓ", "hbar": "ℏ", "Re": "ℜ", "Im": "ℑ",
  "langle": "⟨", "rangle": "⟩", "lvert": "|", "rvert": "|", "lVert": "‖", "rVert": "‖",
  "vert": "|", "Vert": "‖", "lfloor": "⌊", "rfloor": "⌋", "lceil": "⌈", "rceil": "⌉",
  "quad": " ", "qquad": " ", "enspace": " ", "thinspace": " ", "left": "", "right": "",
  "{": "{", "}": "}", "_": "", "^": "", "%": "%", "&": "", "$": "",
  "displaystyle": "", "textstyle": "", "scriptstyle": "", "limits": "", "nolimits": "",
  "colon": ":", "cdotp": "·", "ldots": "...", "cdots": "...", "dots": "...", "vdots": "⋮",
  "circ": "∘", "bullet": "•", "star": "⋆", "triangle": "△", "angle": "∠", "perp": "⊥",
  "parallel": "∥", "models": "⊨", "vdash": "⊢", "dashv": "⊣", "aleph": "ℵ",
  "geqslant": "≥", "leqslant": "≤", "nleqslant": "≰", "ngeqslant": "≱",
  "nleq": "≰", "ngeq": "≱", "lesssim": "≲", "gtrsim": "≳", "prec": "≺", "succ": "≻",
  "preceq": "≼", "succeq": "≽", "triangleq": "≜", "coloneqq": "≔", "eqqcolon": "≕",
  "subsetneqq": "⊊", "supsetneqq": "⊋", "nsubseteq": "⊈", "nsupseteq": "⊉",
  "hookrightarrow": "↪", "implies": "⇒", "iff": "⇔", "longrightarrow": "⟶",
  "longleftarrow": "⟵", "longleftrightarrow": "⟷", "Longleftrightarrow": "⟺",
  "rightleftharpoons": "⇌", "leftrightarrows": "⇆", "ddots": "⋱", "ldots": "...",
  "lbrack": "[", "rbrack": "]", "lbrace": "{", "rbrace": "}", "backslash": "\\",
  "mid": "|", "smile": "⌣", "frown": "⌢", "sharp": "♯", "flat": "♭", "natural": "♮",
  "surd": "√", "wp": "℘", "imath": "ı", "jmath": "ȷ", "checkmark": "✓",
  "therefore": "∴", "because": "∵", "minus": "−", "plus": "+", "eq": "=",
  "nsim": "≁", "ncong": "≇", "nmid": "∤", "nparallel": "∦", "lt": "<", "gt": ">",
  "leqslant_": "≤", "overset": "", "underset": "", "stackrel": "", "substack": "",
}

SMALL_CAPS = {"text": "", "mathrm": "", "mathbf": "", "mathit": "", "mathsf": "",
              "mathtt": "", "mathcal": "", "mathfrak": "", "operatorname": "",
              "mathbb": "", "boldsymbol": "", "bm": "", "overline": "", "underline": "",
              "hat": "", "bar": "", "tilde": "", "widehat": "", "widetilde": "",
              "textnormal": "", "mbox": "", "hbox": "", "mathop": "", "mathrel": ""}

BLACKBOARD = {"R": "R", "N": "N", "Z": "Z", "Q": "Q", "C": "C", "P": "P", "F": "F", "E": "E"}

SWASH = {"varOmega": "Ω", "varGamma": "Γ", "varDelta": "Δ", "varTheta": "Θ", "varLambda": "Λ",
         "varXi": "Ξ", "varPi": "Π", "varSigma": "Σ", "varPhi": "Φ", "varPsi": "Ψ"}

PRINTED = {"sup", "inf", "limsup", "liminf", "lim", "max", "min", "log", "ln", "lg", "exp",
           "sin", "cos", "tan", "cot", "sec", "csc", "arcsin", "arccos", "arctan", "sinh",
           "cosh", "tanh", "det", "dim", "ker", "deg", "gcd", "mod", "bmod", "arg", "hom",
           "rank", "span", "diam", "esssup", "essinf", "tr", "Tr", "O", "o"}

TOKEN = re.compile(r"\\([A-Za-z]+)(?:\s*\*?)|\\([^A-Za-z])|\\([A-Za-z])|(\\.)|([{}])|(\^|_)|(\s+)|(.)")


def flatten(latex: str) -> str:
  """Return the character stream a TeX PDF would expose for this formula."""
  latex = latex.replace("\\\\", " ").replace("\\,", " ").replace("\\;", " ")
  latex = latex.replace("\\!", "").replace("\\ ", " ")
  latex = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\{[^}]*\})*", " ", latex)
  latex = re.sub(r"\\tag\{[^}]*\}", " ", latex)
  out = []
  for m in TOKEN.finditer(latex):
    cmd1, csym, cmd2, escaped, brace, script, space, literal = m.groups()
    if cmd1 is not None:
      name = cmd1
      if name.startswith("text") or name in SMALL_CAPS:
        continue
      if name in GREEK:
        out.append(GREEK[name]); continue
      if name in SYMBOLS:
        out.append(SYMBOLS[name]); continue
      if name in ("frac", "dfrac", "tfrac", "binom"):
        continue
      if name in BLACKBOARD:
        out.append(BLACKBOARD[name]); continue
      if name in SWASH:
        out.append(SWASH[name]); continue
      if name in PRINTED:
        out.append(name)
      continue
    if cmd2 is not None:
      name = cmd2
      out.append(SYMBOLS.get(name, name))
      continue
    if csym is not None:
      out.append(csym); continue
    if escaped is not None:
      continue
    if brace is not None:
      continue
    if script is not None:
      continue
    if space is not None:
      continue
    if literal is not None:
      if literal in "&$^":
        continue
      out.append(literal)
  text = "".join(out)
  return unicodedata.normalize("NFKC", text)


if __name__ == "__main__":
  samples = [
    r"F_{n,\epsilon}=\{x\in E:\forall p\geq n,\delta(f_{p}(x),f_{n}(x))\leq\epsilon\}.",
    r"d(y,E)=d(y,x)",
    r"\{x_{i}\}_{1\leq i\leq n}",
    r"\sup_{x\in E}g(x)=\sup_{x\in A}f(x)",
    r"g(x)=\frac{1}{d(x,A)}\inf_{y\in A}\left(f(y)d(x,y)\right)",
  ]
  for s in samples:
    print(flatten(s))
