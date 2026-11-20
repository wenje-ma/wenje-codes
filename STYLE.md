# wenje-ma 文稿规范

本仓库所有 `.md`/`.qmd`/`.tex` 的排版与写作口径. 改文稿, 改脚本前先按这里对齐.

**本文件是唯一的长期记忆**: 每次对话开始先读它; 之后产生的新规矩, 新偏好, 新路径, 一律追加到这里, 不再写进豆包自己的记忆库 (记忆库只留一条 "先读本文件" 的指针).

## 公式源码

- 公式内部不出现任何空白字符; 需要间距时一律用命令表达.
- 等价用 `\Leftrightarrow`, 不用 `\iff`; 蕴含用 `\Rightarrow`, 不用 `\implies`.
- 同一行并排的间距只用 `\quad`, 不用 `\qquad`.
- `\text{}` 与前后公式之间留 `\;`;`\text{}` 内部的词距用 `~`.
- `\,` 只留在微分号/单位之前, 两个因子之间; 逗号后紧跟的 `\,` 一律删除.
- 上下标要错开时写 `^{A}{}_{B}`, 不用 `^{A}_{\,B}`(`\,` 只把字形右推, 下标仍压在上标正下方).
- `\!` 保持原样——`R[\![t]\!]` 的双括号靠它收紧.
- 控制词后接字母一律加大括号:`\partial{u}`,`\sqrt{g}`,`\mathrm{d}`; 不写空参数 `\partial{}u`.
- 矩阵与向量一律加粗, 记号统一 `\boldsymbol{}`(斜粗, 不用 `\mathbf`,`\bm`). 矩阵指 `M_n`,`GL(n,\cdot)`,`SO(n)`,`diag` 之下的元素; 向量指 `\mathbb{R}^n`,`\mathbb{R}^2`,`C^n`,`K^n` 这类坐标空间中的点与向量, 包括 `\left\|x\right\|`,`x+y`,`\left(1-t\right)x+ty`,`\left[x,y\right]` 这种按分量或线性运算使用的场合. 下标照常:`\boldsymbol{M}_p`,`\boldsymbol{v}_\lambda`,`\boldsymbol{x}_n`,`\boldsymbol{D}_t`.
- 行内公式必须写在一行里. 正文按列宽硬换行时, 不许把 `$...$` 从中间劈开, 更不许在中间夹一个空的 `>`; 宁可让这一行超宽, 也不让价牌跨行. 标题里的公式同理.
- 行间公式一律与上下各空一行: `$$` 的开定界符上一行, 闭定界符下一行都必须是空行, 不允许 `$$` 紧贴正文; 相邻两个 `$$...$$` 块之间也空一行. 只空一行, 不空两行. 公式块内部各行照旧紧贴, 不插空行. 文首 `> ` 引用块随块走, 不受此条约束.
- 以下一律不加粗: 标量; 集合与空间名(`K`,`A`,`E`,`\mathbb{R}^n`,`GL(n,\mathbb{R})`); 映射, 函数, 算子(即使在 `L(E,F)` 里, 也含路径与曲线 `\gamma`); 抽象赋范/拓扑向量空间与序列空间 `E`,`F`,`l^p`,`l^\infty`,`C([0,1])` 里的元素(按抽象点处理, 不逐个加粗); 元素分量 `v_i` 与矩阵元 `T_{ij}`; 点对与元组 `\left(x,y\right)`,`\left(u,v\right)`.`
- 巨型定界符一个都不许出现: `\big`, `\Big`, `\bigg`, `\Bigg` 连同 `l`/`r`/`m` 变体, 一律换成 `\left`/`\right`, 后者按内容自动取高, 更灵活. 三种写法: 成对的括号与竖线 `\big( ... \big)` → `\left( ... \right)`; 带下标的取值竖线 `f\big|_{x=0}` → `\left.f\right|_{x=0}`; 二元斜杠 `\frac{a}{b}\Big/\frac{c}{d}` → `\frac{a}{b}\left/\frac{c}{d}\right.`. 配对按整段一条栈算, 配不上只报 Warning 不改.
- 尖括号只在 `<` 紧接字母时才危险: `<x` 会被渲染器当成标签开头, 把后文吞掉, 由 `math_space_strip.py` 统一改写成 `<{}x`; `<\命令`(`<\alpha`, `<\left`)与 `>` 后接字母都安全, 不必处理. 因此不再给 `<>` 补空格: 补空格会把真正的 `<div>`/`<br>`, 自动链接 `<https://...>` 劈成非标签, 还会把 `<=`/`>=`/`<<`/`>>` 劈成两个半角符号分开的两截, 干这事的 `space_gt.py` 已删除. 正文(公式外)出现 `<字母` 时写进行内代码, 不写裸的 `<script>`.
- 公式里的 `>{}`(`$x>{}y$`)是旧 `space_gt.py` 留下的等值余噪, 已全库清除(868 处 / 213 个文件); 只有 `<{}x` 是该留的, 别再产出 `>{}`.
- 抄协变微分的定义时不要把定义域写成 `\mathscr{X}(S)`: 渲染器不保证有 `\mathscr`, 改写成"对任意切向量场 $\boldsymbol{W},\ldots$ 满足 ..."的文字表述 (2026-11-18, week9).
- 实数的集合名写"取遍实数", 不写 `$u\in\mathbf{R}$`: `\mathbf` 已禁用, 集合与空间名不加粗 (2026-11-18, week9).

## 文档写作

- 抄写原题; 解答中任意相邻两句都能由上一句推出, 不跳步.
- 数学作业集文首引用库只收书内带编号条目, 正文引用须加粗条目名. 先写解答, 解答里用到哪条就把哪条抄到文首: 解答没加粗引用的条目一律不写, 不论与本周末章多相关.
- 数学 homework 的文首引用库(中英两版都算)里的公式一律写成行内 `$...$`, 不许出现 `$$...$$` 行间公式块: 一条条目压成一行, 公式按句法嵌回句子里; 原本行末的 `,`/`;` 提到 `$...$` 之后, `,\quad` 这类分段符把公式拆成多组 `$...$, $...$`, 块尾的 `,`/`.`/中文句号一律移到 `$...$` 之外; 条目之间的空行与标题后的空行照旧保留. 工具:`D:\wenje-ma\wenje-codes\lib_inline.py`, 幂等, 先 `--dry-run` 看改动数再实跑.
- 文首引用库的排列一律按序号升序; 序号相同的, 按 定义 > 公理 > 引理 > 命题 > 定理 > 推论 > 注记 排(其余类型如 例, 性质, 公式, 结论, 习题 与中英对照的 判定定理, 基本结论 一并排在列出类型之后); 没有序号可排的条目(数学活动, 综合与实践, 只以名字出现的条目)排在库末, 内部保持原相对次序. 全部 homework 文稿的中英两版都适用. 工具:`D:\wenje-ma\wenje-codes\lib_sort.py`, 幂等, 先 `--dry-run` 看改动数再实跑.
- 教材里的任何文字——定义, 定理, 公式, 例题, 习题结论——都可作为现成结论直接引用使用, 不在解答中重新推导; 只交代它为何用得上, 不重算一遍.
- 证明按子结论收尾: 一题里有几个独立结论(必要性/充分性, 上界/下界, 各小问), 就各标一次 `$\blacksquare$`, 不等到全题结束才标一次, 末尾也不补第三次. 此条适用于全部泛函作业, 老周次一并回改.
- `$\blacksquare$` 单独占位, 不与别的记号挤在同一行: 证明以句子收尾时接在句末, 以行间公式收尾时单独成一段, 公式那一行不留 `\qquad\blacksquare` 这类填充.
- 一切学科的整理文档里, 加粗只用于引用编号条目, 步骤标签等不加粗.
- 解答不写 "第X步" 这类步骤标签 (2026-11-19, 用户原话 "我不喜欢这样表示", 参照 functional-analysis 的 `homework\week9.md`): 段落直接承接推导, 转折只用 "先证/再证/最后验证" 这类词, 跨步指代换成 "上面的 `\mathrm{I}`" / "上两段" 这种说法, 全文不留步骤编号. 已按全库口径改毕 (2026-11-19, 用户指令 "改 `D:\wenje-ma` 中所有这种问题"): `homework` 下 62 个 md 与 `reset-20261119` 镜像里的步骤标签与跨步指代全部清掉, 只留 `junior-mathematics\homework\week48.md` 与 `primary-mathematics\homework\week49.md` 题干本身的折纸步骤与运算顺序 (题目原文, 不能动). `differential-geometry\textbooks\handout` 是讲义原文, `states-python` 是建模流程与教程, 未动.
- 正文只写题目与推导, 不写依据说明, 心得, 旁注; 正文里不出现 `>` 引用块(引用块只用于文首条目库).
- 英文人名一律改中文译名, 不保留英文原名; 微分几何里固定写作 Gauss→高斯, Gauss-Bonnet→高斯-博内, Stokes→斯托克斯, Frenet→弗雷内, Fenchel→芬切尔, Poincaré→庞加莱, Hopf-Rinow→霍普夫-里诺, Weingarten→魏因加滕, Minkowski→闵可夫斯基; Hessian 不写人名, 直接称 二阶偏导数矩阵.
- 笔记与教材不符处, 悄悄按教材改掉, 不写差异说明.
- 微分几何: 文首条目库只抄条目本身(陈述, 条件, 结论), 不写 `来历` 这类推导来源; 正文不重复推导, 也不另加骨架小节.
- 微分几何作业集的依据一律取讲义 `D:\wenje-ma\differential-geometry\textbooks\handout\*.md`(14 讲); 讲义条目编号讲义自编, 三级 `章.节.条`: 章按知识点所属板块定(共 11 章, 从 1 起), 节沿用讲义原有的每个 §(95 节, 在章内从 1 重排), 条为节内全部条目按出现顺序从 1 编到底, 不分类型, 不用字母后缀; 教材只用于对齐记号, 不得把教材的章节号, 类型号, 式号, 图号搬进 md: 全库不出现"教材"二字, 也不出现 `§x.y` 与教材式号——一旦标注 `(教材 §5.3 定理 3.4)` 就等于承认该条目抄自教材, 与"教材只对齐记号"自相矛盾; 条目标头只写 `**类型 编号 (名称)**`, 无名则只写 `**类型 编号**`; 文首条目库只用讲义编号(如 `定义 1.2.5`), 不加授课日期, 不写"讲义第几讲"之类的来历; 题目照抄, 解答按讲义记号, 顺序与已有结论重写, 讲义已有的结论直接加粗引用, 不重算.
- 微分几何讲义开写一节前, 先在 `handout\*.md` 里搜这节要讲的结论是否已有条目(定理 2.4.1 芬切尔, 定理 7.5.5 高斯-博内, 定理 11.5.1 椭圆点都是早有的), 已有一律写成"另证"或"说明", 不另立定理号, 不重抄陈述.
- 教材 `differential-geometry.pdf` 无文本层, 只能按页读图; PDF 页 = 书页 + 11 (`§7.3` 在 PDF 173-178, `§7.2` 在 PDF 181-182, `§7.5` 是曲面的完备性, 常被误当成高斯-博内或指数). 读它只为核对同一个量的记号写法(如 $k_g$, $b_{\alpha\beta}$, $\Gamma^\alpha{}_{\beta\gamma}$), 读到的定理, 证明, 例题, 习题一律不进 md, 也不许据此在 md 里写"由教材 §x.y 得".
- 每个任务交付前固定复盘一次: 把这次新踩的坑, 新口径, 新路径追加到本文件对应小节, 一句话一条, 不重抄已有条目; 用户在对话里当下指出的错误(人名未中文化, 引用了不存在的编号等)必须落成条目, 不许只留在对话里.
- `functional-analysis.pdf`(王凯, 姚一隽, 黄昭波, "101 计划"核心教材, 高等教育出版社 2024)无文本层, 只能渲染成 PNG 再读图; PDF 页 = 书页 + 11 (§2.3 在书 p82-85, 习题 2.4 在书 p95-96, 习题 2.5 在书 p107-108, 习题 3.1 在书 p116-117).
- 证"某空间上不存在非零连续线性泛函"时, 不许先断言该泛函在"某度量下的有界集上有界"再取矛盾: `d(f,g)=\int|f-g|/(1+|f-g|)` 这种度量恒不超过全测度, 所有集合都"有界", 那条路必然走空. 改用齐次性: 取 δ 使 `d(g,0)<δ` 蕴涵 `|Λg|≤1`, 则测度小于 δ 的集上任意常数倍的 `|Λ(cχ_A)|≤1`; 再对 `tΛ(s)` 令 `t→∞` 逼出 `Λ(s)=0`, 有界函数靠"乘以 t 后仍被同一常数界住"归零, 一般函数靠截断加连续性 (2026-11-17, week9 习题 2.5-2 返工).
- 自反性一题(习题 2.5-9)的充分性: 在 `X^{**}` 内用 推论 2.3.4 分离 `J_X(X)` 与 `x^{**}`, 再用 `J_{X*}` 的满射性把分离泛函拉回 `X^*`; 不要绕 `X^{****}`, 那里元素的施加对象类型对不上.
- 复空间的分离题(习题 2.4-9)先用 注 2.4.1 以 `Re f` 分离, 再用均衡性把 `|f(x)|` 写成 `\sup_{|\lambda|=1}Re f(\lambda x)` 归到同一个上确界; `c>0` 与严格不等式都靠"若取到等号, 则 `Re f` 在开集的内点取到上确界, 从而 `f=0`"来排除.
- 习题 2.4-5 的题面按 2026-11-18 用户改定的口径: 上边界 `f_1=\max A_x` 是凹函数, 下边界 `f_2=\min A_x` 是凸函数, 恒等式写成 `f_2(x)\le y\le f_1(x)`; 旧版"`-f_2` 加两个都叫凸"的写法作废, 见到即改.
- 习题 2.4-6 必须真落在**定理 2.4.1 (凸集分离定理)** 上: 只引**引理 2.4.1 (一点与凸集的分离)** 等于没按题目要求, 用户 2026-11-18 原话"这也没用凸集分离定理证明啊"返工. 定稿写法是取两个凸集——上方图 `M` 与单点集 `N=\{(x,\varphi(x))\}`——先算 `M^\circ=\{v>\varphi(u)\}\ne\emptyset` 与 `M^\circ\cap N=\emptyset`, 由定理得 `\sup_{M}f\le\inf_{N}f=f(x,\varphi(x))`, 再定 `b\le0`, 排除 `b=0` 得 `b<0`, 除以 `b` 反号取 `m=-a/b`; 同时补上三处跳步(实值凸函数在 `\mathbb{R}` 上连续给出内部的球估计, `b=0` 时由 `u\to\pm\infty` 逼出 `a=0`, 结论后点明该等值线是过 `(x,\varphi(x))` 的支撑直线, 斜率即 `m`).
- 求测地曲率前先算 `n=e_1\times e_2` 的指向(球面按 `u,v` 排序时是内法向), 在解答里写明引用**推导 7.3.1 (正交参数网下的测地曲率)** 用的就是这个定向, 答案后再补一句换向时的符号(球面纬圆: 内法向 `-\tan u_0/a`, 外法向取正) (2026-11-18, week9 习题五 10, 11).
- 求旋转面 `\boldsymbol{r}=(u\cos v,u\sin v,f(u))` 的测地线走正交网路线, 不写克里斯托费尔, 也不写测地线方程组: 由 **推论 7.3.2 (正交参数网下的测地线方程)** 得 `\theta'=-\sin\theta/(u\sqrt{A})`, 配上 `\cos\theta=\dot{u}\sqrt{A}` 与 `\sin\theta=u\dot{v}` 即 `(u\sin\theta)'=0`, 记 `h=u\sin\theta=u^2\dot{v}`; 弧长给 `A\dot{u}^2=1-h^2/u^2`(`A=1+f'^2`), 故 `h=0` 是经线, `h>0` 给 `\frac{\mathrm{d}v}{\mathrm{d}u}=\pm\frac{h\sqrt{A}}{u\sqrt{u^2-h^2}}` 的积分, 转向点 `u=h` 处 `\sin\theta=1`; 充分性不必用能量, 对 `u\sin\theta=h` 求导就回到同一方程, `\cos\theta=0` 只在转向点出现, 由 `\theta` 光滑取极限 (2026-11-19, 用户指定 week9 习题五 15 改走这条 B 路线).
- 改用 B 路线后 week9 正文不再引用 **命题 7.2.2 (测地线方程)**, 该条已从 week9 库区删掉; 以后回改这题别再把它抄回去, 除非解答里真的用到 `\ddot{u}^\alpha+\Gamma^\alpha{}_{\varepsilon\tau}\dot{u}^\varepsilon\dot{u}^\tau=0`.
- 圆柱面的和乐群: `I=\mathrm{d}\theta^2+\mathrm{d}u^2` 系数全常数 ⇒ `\Gamma\equiv0` ⇒ 平行场分量常数 ⇒ 每个和乐变换都是恒等映射, `\mathrm{Hol}(P)=\{\mathrm{id}\}`, 是平凡群; 别停在"是 O(2) 的子群" (2026-11-18, week9).

- 习题 2.5-1 的定稿口径: 直接引**注 2.5.1**, 不构造极值函数 $f_0$, 也不分 $p=1$ 与 $1<p<\infty$ 两段重算; 只留一句赫尔德不等式说明每个 $\beta\in{L}^q$ 给出 $L^p$ 上的连续线性泛函, 满射, 保范与范数相等一律由注中的唯一性与 $\left\|\psi\right\|=\left\|g\right\|_q$ 直接读出 (2026-11-19, week9).

## 代码

- 2 格缩进; 注释用英文且尽量少写; 等号, 逗号, 运算符两侧不加多余空格.
- 既有代码不合上述风格时, 顺手改正.
- 保留功能性注解 (`// [[Rcpp::...]]`), 生成文件与压缩库不动.

## 标点

- 全文不出现中文标点, 一律换成对应的半角符号, 并按英文习惯补空格: `，`/`、`→`, `, `。`→`. `, `：`→`: `, `；`→`; `, `？`→`? `, `！`→`! `.
- 括号一律半角: `（）`→`()`,`【】`→`[]`,`〔〕`→`()`. 左括号前补一个空格, 右括号后紧跟中文时补一个空格; 不许出现 `(` 开,`）` 收的半全角混用.
- 引号书名号一律 `"`: `“”`/`「」`/`『』`/`《》` 都换成 `"`; `‘’`→`'`. 唯一例外是 YAML 头里已经在双引号内的, 降为 `'`, 否则破坏 front matter.
- 省略号 `…`(含 `……`)→`...`; 全角空格 `　`(U+3000)→普通空格.
- `—`(U+2014) 与 `·`(U+00B7) 保留: 本身就是英文破折号与间隔点, 不要换成 `-` 或 `·` 的别名.
- 全角字母, 数字与运算符 (`１`/`Ａ`/`＝`/`＋`/`－`/`＜`/`＞`/`～`) 一并降半角, 否则会出现半角运算符夹全角数字. 只保留 `.tex` 里的 `％`, 免得把正文变成注释.
- 空格只在正文补: 终止符后, 开括号前, 闭括号或闭引号后接中文时各补一个; 汉字与汉字之间一律不加空格, 同一个词里的字不许拆开; 汉字与西文或数字相接处照英文习惯留一个空格; 标点前不留空格. 公式内部一律不补.
- 代码块, 行内代码与 `.tex` 的 `%` 注释不动; 那里出现中文标点不算违规.
- 工具:`D:\wenje-ma\wenje-codes\cn_punct.py`, 幂等, 先 `--dry-run` 看改动数再实跑.

## 编辑器

- LaTeX 的 PDF 不留在 VSCode 标签里看, 一律外置 `D:\SumatraPDF\SumatraPDF.exe`. `settings.json`: `latex-workshop.view.pdf.viewer` 为 `external`, `...external.viewer.command` 指 SumatraPDF, `...external.viewer.args` 为 `-reuse-instance`,`-inverse-search`,`"D:/Microsoft VS Code/bin/code.cmd" -g "%f:%l"`,`%PDF%`; `...external.synctex.command` 同上, `...external.synctex.args` 为 `-reuse-instance`,`-forward-search`,`%TEX%`,`%LINE%`,`%PDF%`. 正向: VSCode 里 "SyncTeX from cursor"; 反向: SumatraPDF 里双击(走的是 `code.cmd`, 会闪一下控制台). 前提是编译带 `-synctex=1`, 且 `autoBuild.run` 是 `never`, 要先手动编译.
- VSCode 分词:`_` 与 `^` 连着的左右两段算一个整体, 双击, 按词移动, 基于文档的词补全都按整体走. 词补全只认语言配置的 `wordPattern`, `editor.wordSeparators` 管不到它, 所以 `~\.vscode\extensions\wenje.caret-txt-0.0.1` 注册语言 `wenje-plaintext`(`wordPattern` 里删掉 `^`), 再由 settings 的 `files.associations` 把 `*.txt` 指过去; `editor.wordSeparators` 里的 `^` 一并删掉, 双击与按词移动才跟补全一致.

## 工作方式

- 有疑问先提问, 允许质疑和否定, 尽量减少返工.
- 每完成一项工作模式任务之后随时更新本文件: 新定的规矩, 新踩的坑, 新路径, 新工具当场追加, 不等下轮再补.
- 用户说的一切都可以质疑: 有实测依据就当场指出并反驳, 不因是用户所说而默认接受.
- 涉及附件, 路径, 版本时先核对再动手; 不确定就停下来问, 不擅自猜.

## 常用位置

- 微分几何作业集:`D:\wenje-ma\differential-geometry\homework\week6.md`,`week7.md`.
- 泛函作业集:`D:\wenje-ma\functional-analysis\homework\week1.md` 到 `week9.md`(`week3`,`week6` 不存在), 教材 `D:\wenje-ma\functional-analysis\textbooks\functional-analysis.pdf`; 排版脚本 `cn_punct.py`/`lib_sort.py`/`lib_inline.py`/`leftright.py`/`math_space_strip.py` 实际在 `D:\wenje-ma\wenje-codes\md\` 子目录, 只有入口 `auto_typesetting.py` 在 `wenje-codes\` 根下.
- 书稿(英文, Quarto book, 只出 PDF):`D:\wenje-ma\ed4dse\tex`;骨架 `_quarto.yml`,`preamble.tex`,`index.qmd`,`chapters/`;编译在 `tex` 下跑 `quarto render`,产物 `_book\Experimental-Design-for-Data-Science-and-Engineering.pdf`;图从章内引 `../../figures\N.M.pdf`;结构与引用写法见 `tex\README.md`.
- 交接文档(给同学及其 AI, 讲装 Git/VSCode/MPE 并克隆全部仓库):`D:\wenje-ma\wenjemaths\tutorial\tutorial.md`.
- 微分几何条目库:`D:\wenje-ma\wenjemaths\forced\dg-mid.md`(按章编号, 引用前先核对条目原文与编号); 它用教材式 `章.节.条`, 与讲义自编的三级号是两套, 改讲义编号时不动它.
- 公式改写工具链:`D:\wenje-ma\wenje-codes\auto_typesetting.py`(`leftright.py` → `math_space_strip.py`); 标点另跑 `cn_punct.py`; 文首引用库排序另跑 `lib_sort.py`.
- `math_space_strip.py` 认公式区之前先屏蔽围栏代码, 行内代码与 `.tex` 注释; 公式区里若混进反引号, 或出现"词 空格 词", 判为散文误判, 整文件跳过并报 Warning(`wenje-codes` 自己的 `.md` 是讲代码的散文, 每次都被跳过, 属正常), 因为压缩空白正是把散文空格抹平的那一步.
- `lib_sort.py` 认的库区: 首个 `>` 行到首个 `## ` 小标题之间的全部内容; 块首行是 `> **类型 编号 (名称)**`, 块内可含未加引用的 `$$...$$` 行间公式, 随块一起搬. 编号取类型词之后的第一串阿拉伯数字(`4.2.M` 按 `4.2` 排), 括号里只写编号的(`公式 (4.2.17)`)按括号内的编号排.
- `lib_inline.py` 认的库区与 `lib_sort.py` 一致, 但按"上一条 `> **` 到本条 `> **`"切块写在引用块里; 只丢句内空行, 条目之间与标题后的空行原样回吐. 只剩公式没有正文的段落(条目正文被截断在"则/且/为", 公式失了主)也折成一行, 并报 `formula-only paragraph` Warning, 这类要回教材补条目正文, 工具改不了. 全库清单用 `Get-ChildItem D:\wenje-ma -Recurse -Depth 3 -Directory | Where-Object { $_.Name -match 'homework$' }` 下的 `.md` 全路径过 `--list`, 901 条超出命令行长度上限, 只能走清单文件.
- `leftright.py` 认的公式区: `$...$`, `$$...$$`, `\(...\)`, `\[...\]`, 以及 `\begin{equation}`/`align`/`gather`/`multline`/`eqnarray`/`flalign`/`displaymath`/`math`/`split` 及其带星变体这类环境.
- `\(...\)` 与 `\[...\]` 是糟粕: `.md`/`.qmd` 里一律并成 `$...$` 与 `$$...$$`; `.tex` 里 `\[ \]` 是原生写法, 只当公式区处理, 不改定界符.
- `leftright.py` 的受保护区(区内一律不改): front matter, ```/~~~ 围栏代码块, 行内反引号, 4 格缩进代码块(块内含 `\命令` 或 `$$` 时按公式处理以免漏改), `<pre>/<code>/<script>/<style>` 与 `<!-- -->`, `\verb`/`\lstinline`, verbatim 类环境, `.tex` 的 `%` 注释, `\text{}` 一类文本命令的参数, `\sqrt[n]` 这类可选参数, `\\[4pt]` 这类换行间距参数. 公式区内部也按同样规则标出不改的位置, 配对仍按整段算. 未闭合的 `$`/`$$`/`\(`/`\[` 报 Warning 并放弃该文件后续内容.
- 括号配对按"整段一条栈"算, 只包两端都落在可改区的 `()`/`[]`/`\{`/`\langle`; 允许 `\left(0,1\right]` 这种左右定界符不同的半开区间; 不配对不硬塞 `\right`; 裸 `{}` 是分组不是定界符, 不许包. `\|` 是范数双竖线, 前一个字符必须是 `\` 且插入点在 `\|` 之前, 否则会写出 `\left\\left|`; 竖线只数未被 `\left`/`\right`/`\middle` 包住的裸 `|`(`\big` 族在更早一步就已被改写, 不再参与判断).
- `leftright.py` 在正式配对之前先做一步 `\big` 族归一(函数 `normalize_big`): 成对括号与竖线 → `\left`/`\right`; 带下标的取值竖线在左侧那个原子前补 `\left.`, 记号本身换成 `\right|_{...}`; 二元斜杠把右边整串因子包成 `\left/ ... \right.`. 左侧原子由 `tokenize` 认, 只吃 `ARG_CMD` 名单里的命令参数(`\qquad` 这类不吃参数的命令不许把后面的 `{}` 吞掉).
- 孤儿记号(没配上对的 `\left`/`\right`)由配对结果决定: 只删记号本身, **定界符必须留下**; `\right` 后面若连定界符都没了, 按左定界符补回对应闭合符(`\left(` → `\right)`). 整词删 `\right]` 会连 `]` 一起吃掉, 已证伪.
- 改完全库后必须做四件事验收: 全库预演 `would change 0`, 16 条边界用例只许 `cases`/`odd bar`/`aligned` 三条变, 结构审计与 HEAD 对比无新增不平, 把结构可疑的公式区逐条喂给 `latex.exe` 编到 0 失败.
- Minecraft 实例(anything form nothing,1.20.1 + Embeddium 0.3.31 + Oculus 1.8.0):`D:\Minecraft\.minecraft\versions\anything form nothing`;光影放其下 `shaderpacks`.
- Minecraft 备份目录:`D:\Minecraft\_backup\anything-form-nothing-<时间戳>`(含 `saves`,`config`,`kubejs`,`options.txt`);`latest.txt` 记最新一份.
- 堆叠模组已由 Overstack 换成 All Stacks Infinite 14.3.0.11,配置 `config\All-Stacks-Infinite.toml`(`global_stack_size=99000000`,`experimental=false`,附魔类物品走 `[items_custom_stack_size]` 压回 1).
- Minecraft 实例(magic,1.21.1 + NeoForge 21.1.265):`D:\Minecraft\.minecraft\versions\magic`;堆叠模组 All Stacks Infinite 14.1.0.11,配置 `config\All-Stacks-Infinite.toml`(`global_stack_size=99000000`,`experimental=false`),68 个可附魔物品走 `[items_custom_stack_size]` 压回 1,名单取 `minecraft:enchantable/*` 物品标签并集加 `enchanted_book`.
- HMCL 版本图标:在版本根目录放 `icon.png`(png/jpg/jpeg/bmp/gif/webp 皆可, 按 64 像素加载, 图最好 64 或 64 的整数倍);`versions\<实例>\.hmcl\config\instance-game-settings.json` 里的 `icon` 字段只管内置图标, 存在图标文件时优先用文件.
- 物品图标素材:游戏本体与模组 jar 内 `assets\<命名空间>\textures\item\*.png` 即 16x16 原图, 直接解压加最近邻放大即可, 不必进游戏截图.
- Minecraft 实例(1.20.1-Fabric, 纯 Fabric + Sodium/Iris/Jade/JourneyMap/Sodium):`D:\Minecraft\.minecraft\versions\1.20.1-Fabric`;模组改键一律是原版键位, 记在 `options.txt` 的 `key_key.<命名空间>.<按键名>:key.keyboard.<键名>` 行(如 `key_key.dupetrigger.dupe_trigger_keybinding:key.keyboard.equal`), 要么游戏内 选项 → 控制 → 按键绑定(无中文译名的模组条目落在"杂项"分类里, 显示英文原名), 要么退出游戏后改这一行;右 Alt 写 `key.keyboard.right.alt`. 游戏运行时改 `options.txt` 会被退出时写回的值覆盖, 必须先退游戏 (2026-11-20).
- Java 工具链:`D:\MicrosoftJDK` 是 Microsoft OpenJDK 25.0.4 完整 JDK, `javac` 与 `java` 都在其 `bin` 下, `PATH` 已含该目录, 用户级 `JAVA_HOME` 也指它. `D:\Downloads\jre-8u511-windows-x64.exe` 只是 JRE 不含 `javac`, 未安装, 写代码用不上; 要 Java 8 语义时用 `javac --release 8` 而不是换 JDK.
- VSCode Java:扩展 `vscjava.vscode-java-pack`(`redhat.java` 1.58.0, JDT LS 3.48, 支持 Java 25);`settings.json` 里 `java.jdt.ls.java.home` 与 `java.configuration.runtimes`(`JavaSE-25`, `default`)都指 `D:\MicrosoftJDK`;格式化 profile 取 `GoogleStyle`,`[java]` 缩进 2 格并关掉 `detectIndentation`;保存只整理 import, 不自动格式化和不自动组织代码.
- VSCode Java 卡在 "Loading Java progress" 的根因:JDT LS 导入 `D:\wenje-ma` 下 `SpellEngine` 与 `wizards` 时, Gradle wrapper 要先下载发行包, 而 `services.gradle.org` 307 跳到 GitHub release assets, 国内实测 30 KB/s, 每次 4 分钟超时后无限重试. 已把 Gradle 8.14 预置进 `C:\Users\wenje\.gradle\wrapper\dists\gradle-8.14-bin\38aieal9i53h9rfe7vjup95b9`(解压目录 `gradle-8.14` 加空标记文件 `gradle-8.14-bin.zip.ok`, wrapper 见到标记即跳过下载), `D:\wenje-ma\SpellEngine\gradlew.bat --version` 528 ms 通过. 之后换 gradle 版本用 `https://mirrors.huaweicloud.com/gradle/gradle-<版本>-bin.zip`(1-4 MB/s) 或 `mirrors.cloud.tencent.com/gradle`, 不要用官方链接.
- Gradle 当前版本状态:`SpellEngine` 的 wrapper 于 2026-11-11 11:15 自行升到 9.7.1(dist 已完整装在 `dists\gradle-9.7.1-bin`, 带 `.ok`), `wizards` 仍用 8.14; `gradlew help` 在 9.7.1 上 16 秒通过, Architectury Loom 1.11.458 正常加载, 只报 "incompatible with Gradle 10" 的弃用警告. 回退只需把 `gradle\wrapper\gradle-wrapper.properties` 的 `distributionUrl` 改回 8.14(8.14 的预置仍在, 不会再下载). 两个工程版本分叉会同时跑两套 daemon, 尽量对齐.
- 2026-11-11 已彻底移除 VSCode 的 Java 支持:`vscjava.vscode-java-pack` 连同 `redhat.java`,`vscjava.vscode-gradle`,`java-debug`,`java-test`,`java-dependency`,`vscjava.vscode-maven` 一并卸载并删掉扩展目录, `settings.json` 里整段 `java.*` 与 `[java]` 也删了, 同时删掉 `C:\Users\wenje\.gradle`(1012 MB) 与 `globalStorage\redhat.java`(18 MB). 以后不要在 VSCode 里开 Java/Gradle 工程; 若要用命令行构建 `wizards` 或 `SpellEngine`, Gradle 依赖需重新下载(约 1 GB). `SpellEngine` 源码与改 `wizards` 无关: `wizards` 走的是 `maven.modrinth:spell-engine:1.10.0+1.21.1` 成品 jar, 只有要同步改 SpellEngine 本身时才需要它.
- 显卡与独显设置(i7-13620H + Intel UHD + RTX 4060 Laptop, 驱动 610.60, 屏 2560x1600@120Hz 挂在核显上): 全局首选图形处理器在 NVIDIA App 11.0.9.585 的 `图形 → 全局设置 → "GPU 应用程序分配"` 里设为 RTX 4060, 该项就是旧版 NVIDIA 控制面板 "首选图形处理器" 的改名, 旧 `nvcplui.exe` 已不再随驱动安装. Windows 侧另有 HKCU `Software\Microsoft\DirectX\UserGpuPreferences` 逐 exe 写 `GpuPreference=2;`(Windows 的逐程序设置优先于驱动全局项, NVIDIA 官方文档明说), 现 21 条, 覆盖全部 Java 运行时与 Steam 各游戏. 批量登记脚本 `C:\Users\wenje\Doubao\chats\2026-11-12\new-chat-5\force-dgpu.ps1`(可传 `-Paths`, 只写 HKCU, 不需要管理员).
- Minecraft 实例(miniature-shader-2.19, 26.3 Fabric + Iris 1.11.7 + Sodium 0.9.2): `D:\Minecraft\.minecraft\versions\26.3`. 此前画面闪烁的根因是 GL 上下文落在 Intel 核显(日志里 `Preferring discrete GPU` 之后仍 `Using graphics device: Intel`), 2026-11-12 改走 4060 后消失; `config\iris.properties` 的 `maxShadowRenderDistance=32` 与包 NORMAL 档 `shadowDistance=128` 仍不一致, 未改动.
- Clash Verge(`D:\Clash Verge\clash-verge.exe`, 2.5.10, 数据目录 `%APPDATA%\io.github.clash-verge-rev.clash-verge-rev`): 全局 GPU 分配改成 4060 之后, 它的 WebView2 前端不渲染, 日志停在 `新窗口创建成功, 等待前端渲染后显示` 就再无下文, 表现为"打不开". 已给 clash-verge.exe 单独写 `GpuPreference=1;` 钉回核显, 恢复 `Clash Verge` 窗口正常渲染. 它开着 `enable_silent_start: true`, 启动只进托盘不出窗口, 且 2026-11-12 16:25 那次托盘图标创建失败(`os error -2147467259`), 两者叠加才像彻底打不开; 唤醒方式就是再运行一次 exe 走 secondary instance 或点托盘图标. 排查看 `logs\latest.log`.
- PDF 文字层工具:`D:\wenje-ma\wenje-codes\pdf_tex_layer.py`, 用法 `python pdf_tex_layer.py 源.pdf --tex 手抄.tex [--dpi 600] [--vector] [--out 输出.pdf]`, 默认输出同目录 `<名>_ocr.pdf`. `\newpage` 分页, `%` 开头的行与空行跳过, 其余每行注入一条. 每条按源页自己的文本行框逐行落位(纯扫描页没有行框时退回固定行距的阶梯), 字号取"行高 0.78 倍"与"框宽/该行字宽"的较小者, 下限 0.8 pt, 因而长行自动缩到框内而不出页. 背景默认 600 dpi 栅格化, 为的是彻底丢掉原页那层坏文本(`--vector` 会把它一起带过来, 只在源页文本层本来就干净时才用). 写完必须回读 `get_text` 逐行比对, 缺一行就报错退出.
- 作业与讲义类 PDF 复制出来是乱码, 根因是字体子集没有 `ToUnicode`(只有字形, 缺"字符码→Unicode"那张表), 不是 OCR 参数问题:`week8.pdf` 页面 0 张图片, 30 多个 `KaiTi` 子集加 TeX 字体(`txsy`/`rtxmi`)的 `ToUnicode` 全是 `null`. 这类只能手抄 `.tex` 再注入; 用 OCR 模型抽数学内容必然丢上下标与希腊字母(实测 `du^{2}+u^{2}dv^{2}` 抽成 `dudu+u?dvdv`, `\lambda\tilde{I}` 抽成 `入I`).
- `pdf_OCR.py` 已删(2026-11-12): 本机 `rapidocr_onnxruntime` 未安装, 直接 `ModuleNotFoundError`, 且输出只到"整行纯文本"一级, 数学公式不可用. 要恢复从 `wenje-codes` 的 git 历史取(`git checkout d57848d -- pdf_OCR.py`), 纯文字扫描件(小说, 史书)仍可一用.
- `page.insert_text(fontname="china-s", render_mode=3)` 看着是标准 Tr 3 隐形层, 实测留下一个未嵌入的 `Heiti` 引用, 并在长行上丢字(13 行里缺 2 行); 别用它, 用 `pymupdf.TextWriter(...).write_text(page, opacity=0)`, 字体以内嵌 ttf 写入, 13/13 全部回读成功.
- PDF 处理范围(2026-11-12 定): 整份排除 `applied-multivariate-statistics`, `appreciation`, `differential-geometry`, `states-python`, `topology`; `mathematical-analysis` 只排除 `Zad-01…10`. 全库 314 份 24595 页里剔除 140 份 14815 页, 剩 174 份 9780 页; 其中"手搓 LaTeX 注入"只剩 `junior-mathematics\textbooks\9.1_part2.pdf` 11 页, 其余是 99 份插图、49 份文本层已可用、16 本扫描教材 4113 页(OCR 可搜索层, 按需)、9 份有源。清单在 `wenje-codes\PDF-INVENTORY.md`。
- 判断"PDF 是否自产"不能只看目录里有没有 `.qmd`: `reference\` 下放扫描书时旁边也躺着自己的笔记 `.qmd`, 资治通鉴与张的多元统计两本都被误判成有源。判据应是"同目录有**同名** `.qmd`/`.tex`", 或该目录本身是书的编译目录(`index.qmd`/`_quarto.yml`/`main.tex`)。
- "有源"只是"能查源文件", 不等于"公式能复制": TeX 编出的 PDF 文本层天生把公式压平(`x_p` 抽成 `x1`, 上下标只是字号更小基线更高, 没有语义), 换编译器重编也一样; 要 LaTeX 只有两条路——从源文件拿, 或在 PDF 里塞手抄的隐形 LaTeX 层。注入不是提取而是重新录入, 所以它的成本等于打字成本, 与 OCR 技术无关, 也就无法全库规模化。

- Minecraft 实例(Witchcraft and Wizardry, 1.16.3 + Forge 34.1.42, 零模组): `D:\Minecraft\.minecraft\versions\Witchcraft and Wizardry`. 存档 `saves\Witchcraft and Wizardry` 已还原为原版世界 (region 与 level.dat 取原始 zip), 数据包 `hp` 保留汉化版, 资源包 `WnW-zh_CN` 负责界面与物品名. 备份: 原始解包 `D:\Minecraft\backups\原始地图-解包-20261114`, 汉化前存档 `D:\Minecraft\backups\主存档-修复前-20261114`, 原始数据包 `D:\Minecraft\backups\hp-数据包-原文-20261114.zip`.
- 地图逻辑: 命令方块时钟在 x 10002..10012, y 65, z 0..12; 出生点 10009/59/9; 输入靠计分板 `sneak`/`pressQ`/`pressF`/`rightClick`, 再转实体标签. 界面退出普遍是 `shiftTest==1` 加 `selectSecondary==0`, 长按 Shift 反而失效, 要松开再点.
- 翻译铁律: 只动显示字段 (告示牌 `Text1..4`, `CustomName`, 物品 `display.Name`/`Lore`, 书 `pages`); `Command` 字段, 方块 `Properties`, 区块 `Status`, 实体 `id` 一律不许翻. 之前整片翻译把 `postprocessed` 翻成"后处理的", 方块 ID 翻成"我的世界:石头", 命令方块全部失灵, 表现就是"进世界没剧情".
- 仓库 `D:\wenje-ma\witchcraft-wizardry` (2026-11-14 建): 只放自写脚本, 机制文档, 英中对照表, 示例数据包; 原作者素材 (zip, mca, saves, 原数据包) 由 `.gitignore` 挡住. 首个提交 `d4f238e`, 25 个文件.
- git 本体在 `D:\Git\cmd\git.exe`, 不在 PATH 里, 命令行调用要写全路径.
- 本文件实际位置 `D:\wenje-ma\wenje-codes\STYLE.md`:记忆库里的指针只写 `wenje-codes\STYLE.md`, 不带盘符, 也不在 `C:\Users\wenje` 下, 找它直接去 D 盘 `wenje-ma`.
- 高级代数教材是丘维声《高等代数》第三版: 上册 `advenced-algebra\textbooks\advenced-algebra1.pdf`(270 页), 下册 `advenced-algebra2.pdf`(268 页), 都是扫描图没有文本层, `page.get_text()` 返回空, 只能按页读图像; PDF 页 = 书页 + 21(上册), + 22(下册).
- 丘维声条目实号(2026-11-15 核对): §2.4 范德蒙行列式在书 p40-41 公式 (10) `∏_{1≤j<i≤n}(a_i−a_j)`, 书里**不带例号**; §3.5 例 2(书 p85) 是 `s×n` 范德蒙型矩阵求秩, 正文只说"前 `s` 列组成的 `s` 阶子式为范德蒙行列式", 不给 `∏` 公式; §7.8 依次为 定义 1 本原多项式, 引理 1 相伴, 引理 2 高斯引理, 定理 1 唯一分解, 推论 2, 定理 3 实系数分解, 定理 4 有理根, **定理 5 艾森斯坦判别法(书 p47)**, 推论 6, 命题 7; §7.9 定义 1 `n` 元多项式, 定义 2 齐次, 定理 1 首项定理, 推论 2, 定理 3, 定理 4; §7.10 定义 1 对称多项式, 命题 1 W 是子环, 命题 2, 定理 3 对称多项式基本定理, 例 1, 例 2, 幂和 `s_k` 与 **牛顿公式(书 p65)** 都不编号.
- 作业库原写作"引理 7.8.1 (高斯引理)"与"定理 7.8.1 (艾森斯坦判别法)", 与书不符(书是引理 2、定理 5); 2026-11-15 用户决定按书重编号, 已全域改为 **引理 7.8.2 (高斯引理)** 与 **定理 7.8.5 (艾森斯坦判别法)**, week23/week24 的 cn/en 库区标题与 week23 正文引用同步.
- 复变讲义条目实况: 定理 8.3.1 柯西积分公式, 定理 8.3.2 均值性质, **定理 8.3.3 才是高阶导数公式**(作业原写作"定理 8.3.2 (高阶导数公式)", 与讲义号错位; 2026-11-15 已全域改为 **定理 8.3.3**, complex week4/5/7/8 的 cn/en 库区与 week4 正文引用同步); 定理 13.2.5 讲义本身不带给括号名; 定义 14.1.4 无穷远处的留数给出 `Res_∞f=−c_{-1}`, 其"练习(ii)"就是 `Res_∞f=−Res_0(1/z² f(1/z))`, "练习(i)"是 `Res_∞f=1/(2πi)∮_{C_R^-}f dz`, 定理 14.1.5 是 `∑Res_{a_j}f+Res_∞f=0`.
- 书里没有编号的条目(范德蒙行列式, 牛顿公式)入库时只写名字, 按第 30 条排到库末, 正文引用写成"由**范德蒙行列式**"/"由**牛顿公式**".
- 删库区残块的坑: `Edit` 的 `old_string` 若只截到"下一行标题"、`new_string` 又把目标行原样写了回去, 等于把残块复制一遍; 删行时 `old_string` 必须包含被删内容本身, 改完立刻回读该区块.
- 复变讲义有文本层, 抽文本用 `D:\Python314\python.exe D:\wenje-ma\wenje-codes\_dump.py`(产物 `_ca_<分册>.txt`, 每页 `=== PAGE n ===` 分隔); 抽完即删, 别留在库里. 高级代数那两本无文本层, 只能 Read 图像页.
- 钢琴自学计划:`D:\wenje-ma\wenje-piano` (2026-11-15 由 `D:\wenje-ma\piano` 改名). 2026-11-16 用户把 `schedule.md` 改名成 `README.md`, 又删掉 `plan.md` 与 `books.md`, 原话"我只需要看日程就好了, 所以改名为README": 仓库现在只有一个 README.md, 索引, 阶段门, 教材说明都并进它, 别自作主张再建 plan.md 或 books.md. 教材放 `books\`, 用户已把文件名改成短名, 共七个: Adult Piano 1, Adult Piano 2, Jazz Piano, John Thompsons 1, Piano Grade 1, 钢琴即兴伴奏普修教程, 基本乐理通用教材; 哈农, 拜厄, 音乐理论基础已删, 别再让他下书.
- 零基础的写法 (2026-11-16, 用户原话"我看第一天就要弹曲子, 我真的能会吗"): 排表不能只写页号和曲名, 必须写清这一页在教什么, 以及"不是弹完而是看懂"的口径; 一天列两页也要注明只精做一页. 用户是钢琴零基础, 任何缩写, 指法编号, 谱表概念都要当场解释一句.
- 钢琴计划的终点与强度 (2026-11-16, 用户原话: "它就已经是我学习的终点了, 而不是我学钢琴的过度", "养老级别"): 终点是在 `D:\OpenPiano\OpenPiano.exe` 这台虚拟钢琴上弹唱, 不是过渡到真琴; 所以力度 触键 踏板 手型 与手指音程距离感练不到也无所谓, 教材里讲这些的段落一律跳过, 不要再劝他补真琴. 强度是养老级, 一天 15 到 20 分钟. 风格是欧美流行, 素材从自己的网易云喜欢列表里挑 (他给看列表只是让我知道终点, 别在文档里写缓存路径与统计数). 教材以英文为主: 主线只有 Faber 成人 1, Levine 只取前三章, 辛笛 与 李重光 只备查.
- 钢琴计划的模型 (2026-11-16 定稿): 按训练日 `Day 1` 顺延, 不排周, 累了就歇一天, 漏一天不跳编号; 一天 18 分钟 = 热身 3 (音阶与 `I-IV-V-I` 隔天交替) 加主任务 10 加听辨 3 (`Functional Ear Trainer`) 加记录 2; 一天只有一项主任务; 只有热身与听辨不许块化; 阶段切换看 gate 不看天数. 阶段 0 = 读谱与和弦, `Adult Piano 1` 页 9 到 81, 一天列两页但只精做一页, 排到 `Day 37`; 阶段 1 = 一首歌六天; 阶段 2 = 扒谱六步一首六到八天; 阶段 3 = 整首加移调, 不排天数. 排表铁律: 只排到当前阶段结束, 不假造远期逐日, 也不写"一周"口径.
- 书目纠错: `Four Star Sight Reading and Ear Tests` 是 Boris Berlin 与 Andrew Markow 编, Frederick Harris / 加拿大皇家音乐学院 (RCM) 出版, 不是 Faber 出品 (2026-11-15 已改 `plan.md` 原文).
- 解答为王, 引用为臣(2026-11-15, 用户原话: "哪有解答服从引用的道理, 别弄乱了大王小王"): 解答先写, 引用后补; 条目该不该留、编号怎么写, 全由解答说了算. 正文用到某条就给它补加粗引用, 绝不为迁就库区去删或改解答要用的内容. 缺引用的标准处理是"正文补加粗", 不是"删条目".
- 重编号铁律: 号 = 类型 + 章.节.书内同类型条号(书 §7.8 定理 5 写成 `定理 7.8.5`); 改号先 `git grep` 扫全库, cn/en 双版的库区标题与所有正文加粗引用一起改; 批量替换要用脚本按"每个 old 串的出现次数"断言, 实际数目不符就别写盘.
- 2026-11-15 复核: complex 已无 `8.3.2`, algebra 已无 `引理 7.8.1`/`定理 7.8.1`; week8 的 定理 8.3.1 / 定义 13.2.2 / 定义 13.1.3 / 定理 13.2.5 / 定义 14.1.1 与 week24 的 定义 7.9.1 / 定义 7.10.1 都已在正文补齐加粗引用. 本文件正文用不到的条目已从该文件库区删掉: week8 的 定理 8.3.3 (高阶导数公式, 这几道题不碰, week4 才用), week23 的 定义 7.8.1 / 引理 7.8.2, week24 的 定义 7.8.1 / 引理 7.8.2 / 定理 7.8.5 (艾森斯坦, week23 用了并保留). 删条目只删本文件副本, 别把别处还在用的条目一起清掉.
- 库条目"是否被引用"的判定标准(2026-11-15 定): 正文出现 `**<类型> <编号>`(如前缀 `**定理 4.4.2`)就算引用, 不要求括号里的名字也完全匹配; 早先用"整条 token 完全匹配"判, 把 `**定理 4.4.2**` 这种只写号的引用全判成没引用, 是错的. 英文条目比对名字要大小写不敏感(`Cycle`/`Subgroup` 与正文小写不匹配, 否则 en 全被误删).
- 根除"库条目正文无引用"的四步(2026-11-15 全库执行): ①正文有裸编号 → 就地加粗; ②名字紧跟"由/根据/按/By" → 换成加粗全称; ③名字出现在正文但没引用 → 在其所属 `### 解答`/`### Solution` 第一句前补"由/按**全称**, "(英文 `By **...**, `); ④编号与名字在正文都不出现 → 整条删, 原文全存 `wenje-codes\docs\library-pruned.md`(按 `## 相对路径` 分组, 可直接回滚).
- 删完必做两条自检: ①对称性(每周 cn/en 编号集合相同); ②同号去重(同类型同编号在一份文件里只能一条). 从备份回填缺条时, 引用位置照兄弟文件同一个 `### 解答` 的落点补, 不要另找地方.
- 同号两条是缺陷, 按书定号(2026-11-15 实例): complex week4 的"定理 7.2.3 (原函数存在性)"实为讲义 **定理 8.2.3**(5-8.pdf p35), 已改; 讲义 p26 的 7.2.3 是古尔萨引理, "$1/z$ 有原函数当且仅当存在单值分支"在 p36 只是无号练习, 按第 28 条删; real week11 两条"定义 11.4.1"内容相同, 删重复那条.
- 无头残块同样要清: real-analysis week11 cn/en 库区里那条只有 `> $\dot{M}f(x)=\sup...$` 没有 `> **标题**` 的极大函数残块, 与符号测度那周正文无关, 已删(2026-11-15). 判据: 库区里"只有 `> ` 正文、没有 `> **标题**`"的行就是残块.
- 2026-11-15 根除结果: 128 份文件里 985 条本来合规; 2 条裸编号改加粗, 6 条"由+名字"改加粗全称, 71 条在解答开头补引用, 437 条整条删(备份 `docs\library-pruned.md`), 34 条因英文大小写漏判从备份回填并补引用, 2 条同号重复删除, 1 条无头残块删除, 44 份文件库区空行压平. 终检: 未引用 0 条, 空库 0, cn/en 条数差 0, 库区无连续空行, 编号逆序 0 处.
- 重申(2026-11-15 用户要求): 一切 homework 文首引用环境(库区)里的数学公式一律用行内 `$...$`, 不写 `$$` 行间块(第 29 条); 并且每完成一次工作模式任务都要随即更新本文件(第 67 条).
- 第 19 条不是摆设(2026-11-15 全库补): `$$` 块上下各空一行, 只空一行; 块内不插空行; 文首 `> ` 引用块不受此条约束. 本轮漏检, 全库补 115 处(differential-geometry homework week8 单文件 113 处, functional-analysis homework week7 2 处).
- 第 28 条写法(2026-11-15 明确定调): 正文引用一律写加粗的完整条目名 `**类型 编号 (名称)**`, 只写 `**类型 编号**` 是违规. 第 127 条那句"前缀 `**<类型> <编号>` 出现即算引用"只是**判定条目有没有被引用**的口径, 不是**写引用**的标准, 两者不可混用. 本轮给 differential-geometry homework week1/2/4/5/6/7/8 补名 203 处, 另 functional/real 20 处, 合计 223 处; 用户点名的 week8 解答 1 现为"按**推导 8.1.2 (切映射及其系数矩阵)** 的定义".
- 补名会留下重复括注: 原文常写成 `由**定理 4.5.7** (曲率线网参数)`, 补名后变成 `**定理 4.5.7 (曲率线网参数)** (曲率线网参数)`, 必须按"括注与加粗内括注同文"删掉后一个(本轮 18 处). 引用名与库区名不一致时对齐库区(本轮: functional week4 库区裁成 `(毕达哥拉斯定理)`, real week11 cn/en 正文改成 `(相互奇异的符号测度)`/`(Mutually Singular Signed Measures)`).
- 事故教训(2026-11-15): 用正则压空格**禁止** `\s{2,}`, 因为 `\s` 含 `\n`, 会把"句末 `.`/`,` + 空行"整段并成一行(157 份文件、约 4900 处段落被并, 库区条目串成 `… 则称 $R$ 为一个环. > **定义 2.1.8**`). 要写 ` {2,}` 或 `\*\* +` 这类只认空格的形式. 已按此改写收尾脚本.
- 段落被并后的恢复法(2026-11-15 实战): git 无 09:00 后的提交, 只能以 `HEAD` 版做断行参照 — 取 HEAD 里"非空行 + 其后第一个非空行"(可跨过被删条目)的 `tail(24) + " " + head(30)`, 命中就换成 `tail + "\n\n" + head`; 循环至稳定. 库区另按结构拆: 行内 ` > ` 就是两个 `> ` 块被串起来; 行内 `$$` 一律拆成独占行; 最后按"头 / `> ` / 正文, 条目间一个空行"规范化库区. 校验: 四项(公式空行、引用缺名、名与库区不一致、连续空行)全 0, 并拿行数与非空白字符数对 HEAD 做量差核对.
- 本轮终检(2026-11-15): 全库 `$$` 空行缺 0, 正文引用缺名 0, 引用名与库区不一致 0, 连续空行 0; 另查出 68 条库区条目正文一次都没引用(其中 23 条正文只提到名字), 9 处引用指向"习题/解答"这类非库区编号(不算错), complex week4 正文的 `定理 7.2.3` 已按重编号改成 `定理 8.2.3`, functional week7 漏掉的 `定理 2.2.6 (埃尔米特泛函的有界性)` 已从 HEAD 回填.
- 以撒四魂卡牌复刻工程 (2026-11-15 起): `D:\wenje-ma\isaac-four-souls`. 抓取走用户自己 Chrome 的控制台脚本 `scrape-console.js`, 因为 foursouls.com 有 Cloudflare, 本机直连硬封 403, 云主机 curl 与无头/headful chromium 都停在 `Just a moment...`, 只有用户手工过 Turnstile 的那个会话能用. 产物 `raw\` 放原始 json/csv, `normalize.py` 出 `cards.csv` 供 nanDECK 排版; 卡面保持英文原文, 不翻译.
- foursouls.com 检索页的坑 (2026-11-15 实测): `/card-search/?card_type=x` 与 `?origin=x` 可用, 但追加 `&page=N` 一律 404, 分页参数名未知; 单页最多回 128 条 (`card_type=loot` 正好卡在 128); 结果里的卡页链接是绝对 URL 而非 `/cards/` 相对路径, 按 `pathname.startsWith('/cards/')` 判才对; 单卡偶发 520 (Cloudflare 源站错误, 退避重试能过). 绕开分页的唯一办法是拿 `origin` × `card_type` 全组合 (26 × 7 = 182 格) 各取首屏, 并上 33 条原始筛选, 去重后 1258 个卡页.
- 以撒工程的卡图抓取 (2026-11-15): 同一批 113 张 `wp-content/uploads/*-308x420.png` 用 `fetch(u,{credentials:'include'})` 连发会全部 403, 而同一会话里 `<img>` 加载同一 URL 是 200 (308x420). 结论: 被拦的是请求类型不是会话, 批量取图一律走 `new Image()` 加间隔与退避重试, 再 `ctx.drawImage` 到 canvas, 同源不脏. 卡面文字 OCR 也靠同一招: 浏览器里裁下半卡面拼成对照表 PNG 存本地, 再用读图的方式逐张抄, 不引入任何第三方 OCR 包.
- 以撒工程的 OCR 对照表排版 (2026-11-15): 卡图尺寸 308x420, 一次性把整张卡面拼进对照表会带上大量怪诞插画, 读图环节会命中内容审核直接中断. 稳妥做法是只裁底部 `STARTING ITEM` 那一小条 (卡面 y 从 0.82 到 1.0), 再把 slug 标签条单独裁出来贴在文字条上方, 得到纯文字的核对表; 裁切用 PowerShell 加 `System.Drawing` 做, 不装 Pillow.
- foursouls 卡页结构 (2026-11-15 实测): 属性 `table#StatTable` 的 `td.value` 文本自带一个 `: ` 前缀必须剥掉, 图标 `img[alt]` 为 `HP`/`DC`/`ATK` (`DC` 即骰面); 技能 `#CardInfo div.effectOutcome`, 可以多个, 按序拼接 (角色牌第一条是所有角色共用的 "Play an additional loot card this turn."); 掉落标题 `h2.rewardTitle`, 数值在 `table#RewardTable` 的 `td.value` (`3x`) 加 `td.icon img[alt]` (`Coin`); 整块卡面文本 `#CardDisplay` 里还夹着 `Front character artist:`/`Card back artist:` 署名. 角色的起始道具只印在卡图上, 网页文字里没有, 属唯一无法抓取的字段.

- nanDECK 是排版 DSL 加渲染器, 不是编译器: 一行一条指令, 逗号分隔, `;` 注释, 双引号字符串, 脚本是纯文本可用 VSCode 编辑, 官方无扩展. 以撒工程脚本 `D:\wenje-ma\isaac-four-souls\cards_print.ndeck.txt` 由 `build_deck.py` 生成, 命令行 `nanDECK.exe /EXEC <脚本> [/CREATEPNG <前缀>] [/HIDE]`, PDF 名由脚本名派生 (`cards_print.ndeck.txt` -> `cards_print.pdf`), 1258 张全量约 6 分钟 21 MB.
- nanDECK 七条实测坑 (2026-11-15, 全部在本工程验证): ①`FONT` 样式位必须带 `T` (透明底), 否则每条 `TEXT` 先铺一块白底压住下面的元素; ②`FONTRANGE` 只对它后面紧挨的 `TEXT` 生效, 中间插 `FONT` 会把字号冲掉, 所以"分字号 + TEXT"要成组连写; ③单元格里出现 `|` 会把后面内容整段吃掉, 竖线一律换 `/`; ④`TEXT` 的换行靠第 8 参 `wordwrap`(顶对齐)/`wwcenter`(垂直居中), 写 `justify` 或把 `wwcenter` 放第 7 位会让整条指令静默失效一个字都不画; ⑤`RECTANGLE` 只画实心块, 颜色写 `empty` 等于不画, 线条用 `LINE`, 卡边用 `BORDER = RECTANGLE, #A8A8A8, 0.05`; ⑥`FONT` 的 `X`/`F` 自动缩字只微调, 1000 字符正文照样溢出, 字号必须在外部按字符宽与行高预算好; ⑦nanDECK 按"用到的最大卡号"建卡, 测试子集沿用原始编号会凭空多出几百张空卡, 子集 CSV 必须从 1 连续重编号.
- 以撒版面尺寸取舍 (2026-11-15): 63x88mm 成品加 3mm 出血是 69x94, 3x3 排布 207x282mm 超出 A4 可打印区 (约 200x287), 会被打印机吃掉边. 主稿改为 63x88 无出血 (189x264 正好装下), `build_deck.py` 顶部 `BLEED = 0.0` 是开关, 改 0.3 即切成 69x94 加四边裁切线.
- nanDECK 的静默启动 (2026-11-15 实测): 只有 `/HIDE` 能藏住它自己的窗口, `Start-Process -WindowStyle Hidden` 只管控制台, GUI 照样弹. 正确写法 `nanDECK.exe /HIDE /EXEC <脚本>`; 校验: 启动 1.2 秒时 `MainWindowHandle` 为 0 且 `IsWindowVisible` 为 False, PDF 正常产出. 副作用是脚本报错时对话框也是隐藏的, 进程会一直挂着, 所以必须配 `Wait-Process -Timeout` 并在超时后确认 PDF 是否真的生成了.
- nanDECK 是 32 位 Delphi 程序 (PE machine 0x014C), 地址空间 2 GB 封顶, 一次排 286 页会报"显示内存资源不足"并退出 (但 `ExitCode` 仍是 0, 不能拿退出码判成败, 要查产物文件). 超过约 150 页就按牌堆拆成独立脚本分别建, 再用 pypdf 合并; 本机 `D:\Python314\python.exe` 已 `pip install pypdf` (6.21.4).
- nanDECK 的 `1-{(字段)}` 不是筛选 (2026-11-15 最小实验 t7 证实): 它解析成"该字段有值的最大卡号", 所以 `TEXT = 1-{(back)}, "字面串", ...` 和 `LINE = 1-{(back)}, ...` 会画到 1..最大卡号范围内的每一张卡, 正面也躲不掉; 只有 `[字段]` 取值为空时那一张才不画. 需要"字面串/线框只出现在某类卡上"时, 把那类卡做成独立牌堆单独建, 别指望字段范围能过滤.
- 以撒四魂工程按功能分目录 (2026-11-15, 用户要求, 全英文): `data\` 抓取与清洗数据 (含 `raw\`), `deck\` 排版 (CSV + `.ndeck.txt` + 四个 py), `scrape\` 三个控制台 js, `tools\` 三个清洗 py, `print\` 两份成品 PDF. 脚本里不再写死 `D:\...` 绝对路径, 一律 `Path(__file__).resolve().parent.parent` 推仓库根, 整个文件夹搬位置不会坏. 中间产物落 `deck\build\`, 已进 `.gitignore`, 合并完即可删.
- nanDECK 的 `SAVEPDF` 认相对路径 (2026-11-15 实测): 脚本在 `deck\` 里写 `SAVEPDF = "..\print\x.pdf"` 会真的把 PDF 输出到上一级 `print\`, 写 `build\x.pdf` 则输出到 `deck\build\`; 目录不存在要先自己建. 因此不再需要"生成完再搬文件"那一步.
- 卡面不印无作用的字 (2026-11-15, 用户口径): 正面底部的系列名 (如 `Warp Zone`) 与右下角 slug (`rwz-abe`) 这类灰字一律去掉, 卡背底部的 `TEXT-ONLY REPRINT` 同样去掉, 判据就是"对游玩没有任何作用". `build_deck.py` 已删 `[set]` / `[slug]` 两条 `TEXT` 与 `Y_META`/`H_META` 常量.
- 双面稿的卡背不画卡边 (2026-11-15, 用户提出): 打印机翻面有 1-3mm 偏移, 卡边那条 `BORDER` 会跑到裁切线以内, 在成品卡上留一道灰边; 所以 `BORDER` 只给正面牌堆 (`if not back:`), 卡背只留距边 5.5mm 的内框, 偏移也裁不到.
- `TEXT` 落到内框线上会被切断 (2026-11-15 实测): 卡背内框底边在 8.25, 标签放在 y=8.05 时字形正好压线, 渲染出来像被划掉; 文字块底边要留在框内 (现坐标 7.45, 高 0.45).
- 配件卡规格 (2026-11-15 定, 后按用户意见改两次): 硬币与血量都做 63x88, 与卡同尺寸, 一把刀切完. 硬币 1¢ 100 张加 5¢ 10 张 (对标 Ultimate Collection 的 100 便士加 10 镍币); 5¢ 不是规则必需 — 规则里没有 5¢ 硬币, `A Nickel!` 是掉落牌, 效果就是 `Gain 5¢`, 基础盒也只给 100 枚 1¢, 留着只为手上钱多时少拿卡. 血量不做 0-8 数字卡, 改成"一血一张 ♥ 卡": 掉血直接抽走卡, 不换牌, 与三国杀的体力牌同理; 数量 48 (4 人各 3 血 = 12, 两个 8 血怪槽 = 16, 余量). 计数器不做纸片, 用 12mm 骰子: 99 张卡用 counter 且单卡最多 32 个, 纸片在一张卡上摆不下. 充能不另做卡, 官方就是横置/竖置. 脚本 `deck\build_tokens.py`, 产物 `print\tokens.pdf` 158 张 18 页; 硬币与 ♥ 各占一列 (`big` 50pt / `heart` 72pt), 哪列为空就哪条 `TEXT` 不画, 一副稿子里两种卡用水不同字号.
- nanDECK 不写 `BORDER` 就会自己画黑边 (2026-11-15 踩坑, 卡背先受害): 卡背曾只在 `if not back:` 里给正面写 `BORDER`, 结果每一张背面卡图最外一圈像素是纯黑 (0,0,0), 正面那圈是 `#A8A8A8` (168,168,168) — 说明 nanDECK 有默认边框且是黑的, 与"卡背不画卡边"的初衷正好相反. `BORDER = EMPTY` 不生效, 还会让 `/HIDE` 下的报错对话框挂住进程 (白等一场); 可行解是给背面写白边框 `BORDER = RECTANGLE, #FFFFFF, 0.05`, 白线不印墨, 等于没有. 校验法: 取卡图位图 (`page.get_images` 后 `Pixmap(doc, xref)`) 读 `pixel(w//2, 0)` 与 `pixel(0, h//2)`, 全 255 才算干净.
- 配件卡也做双面 (2026-11-15, 用户要求): 面与背各一份脚本 (画 1¢ 与 ♥ / 只画卡背), 背面的字由 `tokens.csv` 的 `back` 列给, 硬币印 `COIN`、心印 `HEART` — 混在一起后看背面就能分开; 一开始整份背都是 `TOKEN`, 是用户指出不够用才改成两值. 再按页交替合成 `print\cards_duplex_token.pdf` 18 张纸 36 页. `build_tokens.py merge` 子命令负责合成, 与 `merge_duplex.py` 同一台 pypdf. 单面 `print\tokens.pdf` 已删.
- nanDECK 产的 PDF 没有可提取文字 (2026-11-15 实测): pypdf 与 PyMuPDF 的 `get_text()` 都返回空串, 校验版式不能抽文本, 要用 `pymupdf` 栅格化成 PNG 再读图 (已装), 抽查时用 `clip` 只渲染一张卡省时间.
- foursouls.com 只是本机 curl 被挡 (2026-11-15): `web_fetch` 能正常取 `https://foursouls.com/rules/quickstart_guide/` (4031 tokens) 与 `.../extended-rulebook/` (25999 tokens, 输出过大会自动落盘), 抓正文不必再借浏览器会话. 规则全套已抄成 `rules\rulebook.md` (18847 词, 1378 行); 唯一缺损是 Special Counters 里两个"图标即名称"的计数器, 已按各自提升的属性标成 +1 attack / +1 HP counter.
- 规则要点 (2026-11-15 核对): ¢ 池至少 100¢, 开局每人 3 loot 加 3¢; 所有判定用 D6, 攻击掷 >= 闪避即命中, 失手自己吃伤害; 购买 10¢; 手牌上限默认 10; 死亡罚是毁一件非 eternal 物品, 弃一张 loot, 失 1¢, 横置全部 ↷ 与角色; 先控 4 souls 胜; D8 只在单刷/合作模式当回合倒计时. 官方基础盒只给 340 卡, 100 枚塑料 1¢, 1 D6, 1 D8 与规则书.- ScrAPING: 抓卡面正文必须存 innerHTML，不能存 textContent/innerText。图标是 <img>，textContent 只回文本节点，图标连位置一起消失（"they gain 1$"、"equal to its ."）。v4 就是这么错的，git 里只有那一版，没有"修好过"的版本。
- 站点正文的图标带 alt："HP"/"ATK"/"DC"/"Tap Effect"/"Paid Effect"/"Curse Effect"/"LVn Effect"，靠 alt 回填文字即可；lazyload 的 <img> 后面还有一份 <noscript> 同图标副本，不去掉会变成两遍。
- Arial 没有 ❶ ↷ ☠ ⚔ 的字形（fontTools 查 cmap 确认），nanDECK 会渲染成 ?；卡面文字一律用 Arial 能画的字符：骰点写数字、Tap 写 Tap、Curse 写 Curse。¢ ♥ • · 是 Arial 有的。
- 站点自身符号不一致：有的页写 $ 有的写 ¢，印面永远是分币符号，所以 $ 一律归一到 ¢。站点原文的拼写错误（如 "x is squal to"）照抄，网站是基准。
- nanDECK 的 LINK 与 SAVEPDF 相对脚本所在目录解析；脚本放在 deck\ 时要用 -WorkingDirectory deck 启动，否则静默不出 PDF 且 ExitCode 仍 0。
- 内容一致性要能自动化：tools/check_text.py 守四条不变量（无 $、无标点前空格、无残留标签、无未映射 [icon]），tools/diff_cards.py 出逐字段对比，别靠人眼。
- 魂是一个物件，不是数量 (2026-11-16): 怪物带魂徽标时，死掉的是那张怪卡本身翻面变成魂，徽标上的 +2 是"值 2"，不是"两张"。所以奖励框里 Soul 一律写 `Soul +N`（N=价值），`2x Loot` / `2x Treasure` 才是数量。抓取的 `reward_rows` 把 +2 记成 `2x`，是脚本把正号当成了乘号，`deck\make_duplex_csv.py` 的 `reward_text()` 已改。全表 13 张值 2。
- 魂值徽标只存在于卡图 (2026-11-16): 站点文本完全没有 Soul 图标，能进文字的只有奖励框里的那一个；没有奖励框的卡（部分道具、角色）的魂值只能读图，全量要读约 900 张卡图，已按"技能文字覆盖玩法，暂时不读"处理。
- bindingofisaacrebirth.wiki.gg 禁止自动访问 (2026-11-16): `api.php` 与 `/wiki/` 都返回 403 / robots.txt disallowed，`web_fetch` 也被明确拒绝；Fandom 镜像 (`bindingofisaacrebirth.fandom.com`) 的普通页面 `web_fetch` 能读，但 Items 页单页 185 万字符，不适合逐条取名单。按游戏名单筛选只能靠集合归属 + 人工判断，别指望抓 wiki。
- nanDECK 调用的正确写法 (2026-11-16): 
anDECK.exe /HIDE /EXEC <脚本>。只给脚本路径会把 nanDECK 当 GUI 打开并停在主窗口，Start-Process -Wait 永远不返回；-WindowStyle Hidden 只隐藏控制台，压不住它自己的窗口。/EXEC 可给绝对路径。
- nanDECK 画不了中文 (2026-11-16 实测): 一行 TEXT 里 4 个及以上的汉字就死循环（3 个正常，12 个 ASCII 正常），与字号、框高、wordwrap、字体名无关；换 YaHei / 微软雅黑 / SimHei / SimSun 都一样。中文卡面因此改走 reportlab（cn\deck\render_cards.py），几何与英文版一致，字号用 stringWidth 实测而不是估算。
- CSV 里写中文卡面文字必须带引号: 手写的 CSV 正文里只要出现一个半角逗号，字段就被截断，后半句会溢到 footer 列上印出来。用 csv.writer + QUOTE_ALL 生成，别手打。
- isaac.huijiwiki.com 禁止自动访问 (2026-11-16): web_fetch 被 robots.txt 直接拒绝，只能借浏览器会话跑 cn\scrape\huiji-dump.js（同源 pi.php）导 huiji_index.json，再在本地解析中英对照。
- 中文卡面改走 XeLaTeX (2026-11-16, 用户拍板): MiKTeX 26.5 的 XeTeX + ctexart(fontset=none) + xeCJK, 中文 SimHei (AutoFakeBold=2 合成加粗), 西文/数字/¢ 用 MiKTeX 自带 lmroman10-*.otf (XeTeX 直接读 CFF, 不需要转 TTF). 两端对齐、避头尾、标点挤压都由 xeCJK 给, PDF 里是可选文字, 版面能靠量文字坐标验证, 不用读图. 586 张 68 页约 70 秒.
- TeX 里三个踩过的坑 (2026-11-16): (1) TikZ 的 lign=center 会把单行标题拉成两端对齐, 中文被抻成一字一空格, 要用 lign=flush center; (2) 
emember picture, overlay 的版面以 current page.north west 为原点时必须编译两遍, 只编一遍是白页; (3) \newcommand 里不能出现 %（TeX 注释符), 基线间距用 \dimexpr#1pt*#2\relax 算.
- fontspec 在这台机器上只能按文件名找字体 (2026-11-16): \setmainfont{lmroman10-regular.otf} 走 kpathsea 能找到 MiKTeX 自带的 LM; 给绝对路径 (带或不带 Path=) 一律报 cannot be found. Windows 系统字体反过来要 Path=C:/Windows/Fonts/, + 文件名 (simhei.ttf).
- 卡面量溢出必须用 mm→pt 换算 (2026-11-16): pymupdf 的 Rect 是 pt, 图纸常量是 mm, 直接比较会把所有卡判成溢出; 另外页脚也在正文 x 范围内, 判定正文溢出要把脚注区排除, 否则每张卡都会被判超框.
- xelatex 不总在 PATH 上 (2026-11-16 实测): 前台 PowerShell 里 Get-Command xelatex 查不到, subprocess.run(["xelatex", ...]) 直接 WinError 2; 而脚本在外面包了一层 try, 失败时留着上一轮的旧 PDF, os.replace 照旧把旧 PDF 搬到成品目录, 于是"重出成功"其实一个字没变. 解法: render/build 脚本启动时 shutil.which("xelatex") 加 D:\MiKTeX\miktex\bin\x64\xelatex.exe 兜底, 常量 XELATEX 传进 subprocess. 校验版式变化不能看退出码或 done 字样, 要比对 build\tex\*.tex 的 mtime 或直接抽 PDF 文字.

- 标题字号算宽要用 72/25.4 (2026-11-16): fit_title 里把 mm→pt 写成 0.3528 (那是 pt→mm 的倒数), 可用宽度只剩 18pt, 所有三词以上的卡名都被判超两行一路缩到 6pt 地板 (Jacob and Esau / Book Of Belial / Daddy Long Legs 全是小字). 卡面常量是 mm, PDF 坐标是 pt, 换算只有 2.835 一个方向.
- 报版心错误再缩字号, 必须先验测量本身 (2026-11-16): 加了"量标题越界就缩 0.5pt"的反馈环后, 测量忘了按卡分栏, 同页其余 8 张卡的标题全被算到本卡, 于是每张卡都"紧", 12 轮把 1052 个标题全压成 6pt. 而且缩字号那轮不看 over 是否为空, 循环打印 "0 cards overfull" 12 次, 日志看着像正常收敛.
- 站点把 Choose one 的 bullet 压平成句子 (2026-11-16): 抓下来的文字里选项之间没有分隔符, 按句号硬切会把 "Gain 6¢. Take 1 damage." 拆成两选项 — Devil Deal 印面其实只有 3 个选项, 第 2 个是"拿 6¢ 并受 1 点伤害". 这类卡要靠卡图确认边界, 写死的分组放在数据里, 渲染器只负责排; 目前 Devil Deal (77) 与 Dagaz (385) 是手工分组, 其余 choose-one 卡恰好一句一选项.
- 选项/骰点列表统一用 / 分隔 (2026-11-16, 用户拍板): 逐条换行在卡面里读起来太空, 改成一行的 "a / b / c", 和奖励框 REWARD 的写法一致; 只有源文本自带 bullet (·/•) 的卡仍走独立行.
- ¢ 单独出现是能力标签不是钱 (2026-11-16): 规则书里 dollar 记号表示"成本不含横置的启动式能力", 抓取把标签图标记成了 ¢ (如 "¢ Destroy this: ...", "¢ Pay 3¢: ..."). 印面写 \$ , TeX 里必须转义成 \$, 否则美元符把整页带进数学模式, xelatex 在那一页直接停, 后面 200 多张卡全丢.
- 编译中途失败会留半份 PDF (2026-11-16): 那个 $ 的错让 treasure 的 205 张只编出 1 页, os.replace 照样把半份搬进成品, merge 还打印 done 26 sheets. render 循环里加了页数校验 (期望 ceil(n/9)), 不够就报停在第几页, 不再替换成品.
- 奖励框数量写法统一 Nx (2026-11-16): 站点把一毛钱写成 "x10 Coin", 印面统一成 "10x Coin", 与其他 "3x Loot" 一致; A Dime!! 的奖励就是 10 枚 1¢.

- 卡名只允许一个字号 (2026-11-16): 名字过长不缩字, 走三行并把它下面的副标题和正文整体下推 5mm (title_shift). 缩字是上一轮 1052 个名字全掉到 6pt 的直接原因, 用户明确要"所有卡名一样大".
- 量标题宽度要用字体真宽度 (2026-11-16): 按 0.5em/字符估算会把 "CURSE / INDOMITABLE / FAMILIAR" 算成两行 (真宽 162pt > 150pt 可用宽), 于是不触发三行分支, 第三行压到副标题上. 改成读 lmroman10-bold.otf 的 hmtx 累加 advance.
- 奖励写 "+N 单位", 不写 "Nx 单位" (2026-11-16): "REWARD: x10 Coin" 被读成"硬币翻十倍", 印面统一成 "+10 Coin", 和魂的 "Soul +1" 同一形状. 只有整条奖励都是纯数量列表时才改写, "1x Coin; 2x Loot; ..." 这种骰点表原样保留.
- 能力标签用 ◆, 不用 \$ (2026-11-16): 用户把 $ 读成"扣我钱". 但 ◆ 属 Geometric Shapes, xeCJK 默认不算 CJK 字符, 会落到 lmroman 里静默丢字 — 日志报 "Missing character", PDF 里是空白, pymupdf 抽出 U+FFFD. 修法是前导加 \xeCJKDeclareCharClass{CJK}{"25C6}, 并且符号后面接 \hspace{0.25em}, 否则 xeCJK 把紧跟的空格吃掉, 印成 "◆Destroy".
- 卡面字号必须均匀 (2026-11-16): 带副标题的卡若把正文起点下移到副标题之下, rule 堆被迫降到 7pt 且 Ansuz 溢出; 正文起点只按 stats/footer 判断, 副标题不参与.
- 卡面文字是节点长出来的, 溢出要看"最低一行" (2026-11-16): TikZ 的 node 去掉 minimum height 后文字顶部起排, 不再垂直居中(否则 "+1 HP" 浮在卡面中部). 代价是超框的文字会一直往下印到下一张卡上, 而 measure() 原来只统计落在卡框内的 span, 越界那几行全被 `card_box.contains` 过滤掉, 于是 8 张 rule 卡溢出 13mm 仍然报 "10.00pt 全卡通过". 判定改成: 取本卡 x 栏内, 起点在本卡内的所有 span 的最高 y1, 与正文框下沿比较; 有 footer 的卡要排除起点 ≥ Y_FOOT-1.2 的奖励行.
- 没有 footer 的卡正文可以用到 78.0mm (2026-11-16): 卡面 5..83, 奖励行只占 70.4..80, 空着就浪费. rule 的 8 张速查卡因此从 8pt 回到 10pt 再回落到 8pt 的真实值, 全堆一个字号.
- 仓库只留五类 (2026-11-16, 用户口径): 爬虫代码, 抓来的原始数据, 处理后的数据, tex, 编译成品. 已删: build\tex 的 22 组 .aux/.log 与 probe_mark*, 根目录 8 张 en_pv_*.png 预览, data\raw\start_items 的 10 张对照 PNG (13.4MB). 全库从 16MB 降到 1MB 级, 只剩 en\{scrape,data,deck,print,rules,tools}.
- 不用把 tex 换成 qmd (2026-11-16): 这份 .tex 是 render_cards_tex.py 按 CSV 程序化生成的, 不是手写源; 换 qmd 等于再套一层 Quarto, 既不会减少 xelatex 的 .aux/.log (那是编译产物, 只能清理), 也表达不了每张卡的 TikZ 定位.


- 起始道具是独立一叠, 与角色配对发放 (2026-11-16): 官方把每个角色的起始道具印成 Eternal Treasure Card, 单独一叠随角色发给玩家, 不进宝物堆. 旧筛选按"名字要在游戏里存在"把这 16 张全删了, Cain 的 Sleight Of Hand, Samson 的 Blood Lust, Jacob and Esau 的 Sibling Rivalry 连同名宝物卡都没有, 玩家拿到角色就没有道具. 现在 cards_final.csv 用 kind=start 补回 16 张 (Eden 没有起始道具, 开局自己挑), 牌背印 STARTING ITEM; 角色卡 footer 只印名字, 实体卡在这叠里.
- 牌背堆名只压宽度, 不降字高 (2026-11-16, 用户口径 = Word 字符缩放): 20pt 粗体大写只够 9 个字符, CHARACTER(151.6pt) 会被 TeX 断词成 CHARAC-/TER, STARTING ITEM(193.6pt) 会折行. 用 lmroman10-bold 的真实 advance 量宽, 超过 144pt 就把外层 node 撑到 IN_W/scale 宽, 内容 \scalebox{s}[1] 压回 53mm, 字高仍是 20pt. \scalebox 里不能有 \par, 否则压不到段落盒, 字会溢出边框.
- 卡背不印任何边框 (2026-11-16): 背面对不齐时边框会露成灰边, 裁切以正面为准. 卡背只剩品牌两行, 堆名, 一条细线.
- 牌背文字不居中时先查模板里的空格 (2026-11-16): "{\cardfont{20.0}{1.1} %s\par}" 里那个分隔用的空格在 } 之后不会被 TeX 吞掉, 变成行首的 1.35mm 空白, 于是所有堆名整体右偏 3.9pt, 肉眼上就是和下方那条短线不对称. 去掉空格 (}%s) 后 ink 中心正好落在 119.1pt = 卡心.
- 卡背恢复细边框 (2026-11-16, 用户改口): 之前怕裁偏露灰边把背面边框删了, 结果用户觉得"有边框挺好"; 边框仍内缩 5.5mm, 裁偏 1mm 也还在里面.
- 空白牌不进独立一堆 (2026-11-16): 官方的空白包是每种类型一张, 背面就是那一类的背面, 混进对应牌堆后从背面看不出是空白, 这本身是玩法的一部分. 我们的 Blank Rune/Blank Loot 已并进 loot, Blank Monster 并进 monster, other 堆取消; Blank Canvas 是挑战模式卡, 不在六堆内, 已从牌表移除.
- 过期产物随手清 (2026-11-16, 用户口径): 仓库只留四条线 —— 爬虫代码、原始数据、处理后数据、tex+编译结果. 某个牌堆/某张卡被取消后, 它的 csv / 中间 pdf / tex / aux / log 要当场删掉, 不能堆着等下次. 检查用的栅格化 png 一律写到 agent 的临时目录, 不要落在 en\print 或仓库根.
- 全局能力上移到速查卡 (2026-11-16, 用户口径 = 更看重精简): 17 张角色卡原本都印着同一句 "Tap: Play an additional loot card this turn.", 其中 3 张后面还接各自能力. 现在这句话从所有角色卡删掉, 单独做一张 RULE 卡 "EVERY CHARACTER / GLOBAL RULE" 承担; 那 3 张只留后半句. 代价是 14 张角色卡正面除了名字和 HP/ATK 再无文字, 已由用户确认接受.
- 正文垂直居中 (2026-11-16, 用户口径): 正文块在可用带内垂直居中, 不再顶部对齐, 否则短效果卡下方留一大片空. 用 TikZ node anchor=center, 坐标给 (卡左+5+53/2, 带中线), 注意 anchor=center 是横向也居中, x 必须给卡心, 只改 y 会把整块正文左移 26.5mm 压到邻卡上.
- 角色卡多个版本时的起始道具 (2026-11-16): 同一角色的 Base Game / V2 / Gold Box / Alt Art 各种版本印的起始道具完全一致, 唯一例外是 Isaac 的 Nendoroid 版给 GUPPY'S HEAD, 普通版给 THE D6. 我们要的 17 角色里只有 Isaac 需要选, 已取 b2-isaac (THE D6), 与原版以撒的初始道具一致.
- 卡面分区固定, 不随内容伸缩 (2026-11-16, 用户口径): 奖励带永远存在, 即使卡上没有 REWARD / STARTING ITEM 这类行. 之前把 8.4mm 还给无 footer 的卡, 导致 Eden (没有起始道具) 的正文中心比同页其它卡低一截. 现在所有卡正文区一律 22.0(无 stats)/25.6(有 stats) 到 69.6mm, 正文在这个区里垂直居中, 全堆同一条中线.
- 奖励行压成一行 (2026-11-16): REWARD / STARTING ITEM 过长会折行, 折行后这条带的高度就不统一. 处理同牌背堆名: 超过 140pt 就横向 \scalebox 压回 140pt, 外层 node 撑到 IN_W/scale, 内容不写 \par, 字高不变.
- 模板里的空格既会右移也会缩进 (2026-11-16 补): "{\cardfont{..}{..} %s\par}" 那个空格在居中的标题上看不出来, 但在两端对齐的正文上就成了约 2 个字母的首行缩进. 所有模板一律写成 "}%s", 卡面正文实测首行与次行左边界都在 43.94pt, 无缩进.
- 正面上下边距必须相等 (2026-11-16, 用户口径, 推翻"上窄下宽无妨"): 量得卡名顶端距裁切线 7.57mm、footer 底端 11.25mm, 差 3.7mm, 看着像整张卡往上浮. 渲染器加 CONTENT_DY=1.85, 在 card() 里裁切框\draw 之后把 yt 整体下移, 只动文字不动框; 实测 9.42 / 9.40mm. 改这个常量等于版面调垂直重心, 正文带 22.0/25.6→69.6 与 footer 70.4 的相对距离不变.
- 卡背彻底不印边框 (2026-11-16, 用户第二次改口, 最新): 裁切以正面裁切线为准, 双面打印第二遍常有 1~2mm 定位偏差, 背面的框没有参照就能看出来, 有框就变成"上宽下窄". 卡牌背(back_card)、token 背(back_cell)、track 背(back())三处灰框 \draw 全部删除, 背面只剩品牌行 + 堆名 + 短线. 留 BACK_DX / BACK_DY(mm, 正=右/下) 作为整张背网格的校准钩子, 当前 0.
- 标签行统一成灰标签 + 粗体值 (2026-11-16): footer 里 STARTING ITEM: 和 REWARD: 走同一分支, 前缀渲染成 "starting item" / "reward" 小写喂 lmromancaps10 (FakeBold 3.0, Scale 1.06) + black!50, 值 8pt 粗体, 两者宽度相加后按 140pt 折算 scalebox; 没有这两个前缀的 footer 才落回整段压宽.
- 三层字体终值 (2026-11-16, 用户逐档试定): 标签(HP/ATK/DICE/STARTING ITEM/REWARD) = lmromancaps10 8pt + black!50 + FakeBold 3.0 + Scale 1.06; 正文术语(9 词白名单) = 同字体 FakeBold 3.0 但纯黑, 视觉上是强调; 数值/名字 = lmroman10 bold. lmromancaps10 只有 regular, 无真粗体, FakeBold 是描边加粗. 喂这个 caps 字体前必须 lower(), 它只把"小写"转小型大写, 已大写的字符串会印成全高大写.
- 白名单 9 词不分大小写 (2026-11-16): (?i)(?<![A-Za-z])(HP|ATK|DICE|TAP|COIN|COINS|LOOT|SOUL|SOULS|TREASURE)(?![A-Za-z]). 区分大小写时 character 正文只有小写 treasure, 一个都不命中.

- 正面不印任何边框 (2026-11-16, 用户口径): 只用刀按网格线划, 不需要沿框描. card() 里那条 \draw[line width=0.2pt] 矩形删掉, 卡的位置只由 63x88 的槽位和 X0/Y0 决定. 页边距 10.5/16.5mm, 卡内文字再内缩 5mm, 所以离纸边最近的墨迹有 15.5mm, 打印机 10mm 白边也切不到内容; 真正的风险是打印对话框里的"缩放/适应页面", 它会改几何, 裁切线就对不上.
- 卡背只有品牌两行 + 堆名 (2026-11-16, 用户口径): 灰色方框和堆名下面那条短线都删了, 没有框陪衬时短线显得突兀. 堆名那块的 y 从 30.0 改成 34.0, 20mm 高的盒子中心正好落在 44mm = 卡心, 横竖都居中.
- loot 不印 REWARD (2026-11-16, 用户口径): 战利品卡的正文已经写清"Gain 1c.""Loot 3.", 奖励行只是重复. make_duplex_csv.py 的 footer() 里对 kind=loot 且 hp 为空的行直接返回空; 带 HP 的那些其实是错分到 loot 的怪物卡, 奖励是死亡奖励、正文没写, 仍然保留.
- 正文术语先 lower() 再进 caps 字体 (2026-11-16): 数据里写的是大写的 HP/DICE/SOUL, 直接喂 lmromancaps10 会印成全高大写, 比周围小写高出一截. style_keywords 改成 lambda 里 m.group(1).lower(), 印出来是真小型大写. 注意 lambda 替换不会被 re.sub 处理转义, 反斜杠只能写一个.

- 卡牌尺寸定为 70 x 99 mm (2026-11-16, 用户拍板, 最新): 用户买了内径 70x99 / 外径 76x102 的卡套, 且要 A4 对折即裁. 210=70x3, 297=99x3, 只有 70x99 能让 A4 整除成 3x3 (4x4 的 52.5x74.25 太小, 官方 63x88 除不尽). 代价: 网格满版, X0=Y0=0, 最外一排落在纸边.
- 满版后正面/卡背/千元牌一律不印边框 (2026-11-16, 物理原因而非审美): 纸边是打印机的不可印区(4~6mm), 边框必被吃掉一半. render_cards_tex.py 的 card() parts 直接置空; build_tokens.py 的外层 0.2pt 框删除, 内层硬币圈从 5.5mm 退到 7.0mm 躲开不可印区.
- 裁切线只画内部网格 (2026-11-16, 用户要求): 外面四条边就是纸边, 不用画也画不出; 只在前景页画 0.2pt 直线, 位置 x=70/140mm, y=99/198mm, 全长贯穿. 背页不画(否则第二遍套位会露出双线). token 页同样处理. 用户裁切方式 = 先对折两次(105/148.5 处), 再沿内部细线切.
- 70x99 版面的纵向常量 (2026-11-16): Y_FOOT 81.4 / BODY_BOTTOM 80.6 (footer 距下边 8.6mm), CONTENT_DY 1.85 仍有效, 实测正面墨迹上 9.37mm / 下 9.41mm, 仍是等距. token 各带整体 +5.5 (大字 28.5, 心 25.0, caption 73.0, tag 80.0; 背面 17.5/22.1/39.5/63.0), track TOP 26.5, BOX_X=X0+14.0 让 42mm 的 8 格在 70mm 卡里居中.
- 字号尚未随加宽重算 (2026-11-16, 待办): 正文框从 53mm 加宽到 60mm, 现有 10pt 偏保守, 卡面留白偏多; 要更饱满就把 SIZE_BODY 提到 11pt 再让溢出自动回调, 但这是观感取舍, 等用户点头.
- 卡背小方框恢复 (2026-11-16, 用户第三次改口, 最新): 之前删边框的理由是"双面第二遍偏移会被看出来"; 现在裁切基准从"看着边框找"变成"沿内部裁切线切", 偏移量有了绝对参照, 边框不再是暴露误差的元凶. render_cards_tex.py 的 back_card、build_tokens.py 的 back_cell、build_track.py 的 back 三处都画回 0.2pt black!70 矩形, 内缩 7.0mm (比原来的 5.5 更靠里, 躲开打印机不可印区, 也和 token 正面的硬币圈同一内缩). 卡背堆名盒子 y=39.5 (99mm 卡心 49.5), 品牌两行 17.5/22.1, 短线 63.0.
- 满版卡背也必须内缩 (2026-11-16): 70x99 满版时卡背的"卡边"就是纸边, 边框不能画在卡边(不可印), 只能内缩; 这是背框从 5.5 改 7.0 的直接原因.
- loot 副标题统一成 "Loot Card" (2026-11-16, 用户口径): 站点把 loot 拆成 Bad/Good Event、Curse、Bomb、Wildcard、每月 box 等十几种, 这些分类对玩家没有任何可执行信息. make_duplex_csv.py 的 subtitle() 对 kind=loot 直接返回 "Loot Card", 与 character 的 "Character Card" 同一形式. 注意: loot 里混着带 HP 的怪物卡和 Wildcard, 副标题也一并变成 Loot Card, 这是"牌堆即分类"的取舍.
- ¢ 进白名单 (2026-11-16, 用户口径): KEYWORDS 正则尾部加 \u00a2, 命中走专门宏 \kcent (lmromancaps10 + FakeBold=3.0, 但**不带 Scale=1.06**). 理由: 1.06 是给字母补 x-height 的, ¢ 是全高符号, 放大 6% 会显得比数字高一头. 实测 9.96pt, 与正文同高、笔画加粗, 视觉上就是强调态.
- 数据里的重复词已修 (2026-11-16): "loot deck deck"(Devil Deal 等 2 处) → "loot deck"; "attack this this turn"(Krampus) → "attack this turn". 这类重复是抓取时关键词插入留下的, 用 \b(\w+)\s+\1\b 全表扫一遍只剩这两处.
- loot 里的怪物清理 (2026-11-16, 用户口径"必须是原版游戏里的怪物才能归入, 否则剔除"): 促销盒/订阅盒页面被整页归成 loot, 导致 15 张非战利品卡混在 loot 里. 处理: Big Horn / Loki / Eggy / Evis / Teratoma 这 5 张真·游戏 Boss 改成 kind=monster 并把 type 从 "January Box(...)" 改成 "Boss Card"; 其余 10 张直接删行 —— Delirium / Larry Jr. / The Adversary / Dogma 是 monster 堆已有的重复, Cain / Isaac / The Lost 是 character 堆已有的订阅盒 alt art 重复, Greedling Rush! / "Christian Broadcasts" / Monster Card(Wildcard) 不是原版游戏里的怪物. 结果: loot 178→163, monster 153→158, 总行 600→590, sheets 仍 69 (loot 19 + monster 18).
- 改 kind 后必须同时改 type (2026-11-16): subtitle() 对 monster 直接用数据里的 type 行, 不改就会把 "January Box(Isaac is Doomed!)" 印在卡上.
- 数据备份习惯 (2026-11-16): 批量删行前把 cards_final.csv 复制到 agent workspace (cards_final.before_lootfix.csv), 仓库里不留 .bak.
- 同一张卡的多版本只留最新印刷 (2026-11-17, 用户口径"要最新的"): 站点把每个版本都单列一行, 于是同名牌出现两次 —— b/dagaz [Base Game] 与 b2-dagaz [Base Game V2]、fsp-ansuz [Four Souls+] 与 fsp2-ansuz [Four Souls+ V2]、g-jera [Gold Box] 与 g2-jera [Gold Box V2], 还有 Requiem 重写的 b-soul_heart / r-soul_heart 等. 排序规则: set 里带 V2 的优先(3), 其次 Requiem(2), 其余(1), 同名只保留最高分那一行. loot 因此 163→125 (38 组各减 1), 总行 552, sheets 69→64. monster 里还有 5 组同样的重复待处理, treasure/room/character/start/soul 为 0.
- 去重脚本要按行对象身份删 (2026-11-17): 用 id(r) 收集待删行, 不要按名字再筛一遍, 否则同名的两行会一起留下或一起删掉.

- Roll 标签统一成 em dash + 冒号 (2026-11-17, 用户口径): 站点把 roll 表写成 `Roll- 1: .. 2: ..` 或 `Roll: ..`, 破折号会被读成负数区间, 所以 `_roll_lines()` 把头统一成 `Roll ---`, 与 `Choose one ---` 同一处理. 表内各结果一律印成 `N:` / `N-M:`, 不管站点用 `:`、`;` 还是 `.` 分隔 —— 用户点名 `3. Loot 3. 4. Lose 4¢.` 缺 `/` 就是因为点号分隔没被识别. 实现: `_roll_chunks()` 按 1,2,3.. 递增只认"下一个该出现的数字", 句子里的普通数字因此不会被误切成条目.
- Curse 也是标签 (2026-11-17, 用户口径): `Curse:` 同样换成 `Curse ---` (`_curse_lines()`), 并进白名单, 印成小型大写加粗.
- 白名单扩到 21 项 (2026-11-17, 用户逐条拍板): 追加 DAMAGE/DAMAGES、ROOM/ROOMS、CURSE/CURSES、BOSS/BOSSES、DC、ETERNAL、COUNTER/COUNTERS. 不收敛就没强调, 所以划了入选标准: (1) 规则书里自成词条/一类牌/一种计数物; (2) 扫卡时必须认出它才能决定行动. 明确排除 MONSTER(158 张里几乎都出现, 加粗后整页发黑)、ATTACK(112)、ITEM(74)、PLAYER、CARD、TURN、CHARACTER. 用户当场确认 monster 不加.
- `loots` 只给 loot 变体 (2026-11-17, 用户口径 → 当天推翻, 见下一条): 曾印成 `\mbox{\kw{loot}}s`, s 留在正文字体. 用户看到实物后改口: s 也要变体.
- 术语禁止断词 (2026-11-17): 60mm 宽的正文里 TREASURE 会被断成 `TREA-` / `SURE`. style_keywords 的每个替换都套 `\mbox{}`, 术语整体不折断.
- ¢ 不吃词边界 (2026-11-17, 用户发现 `x¢` 没加粗): ¢ 紧贴金额(`25¢`)或变量(`x¢`), 加 `(?<![A-Za-z])` 就会漏掉. 正则把 ¢ 拆成独立分支 `|¢`, 不设前后界; 其他词仍要词边界.
- `¢` 只在动词前才算付费能力标签 (2026-11-17): 站点用 `$` 表示"花代价发动的能力", 卡面印 ◆ 代替. 但原正则 `¢\s+(?=[A-Za-z])` 把句中表示钱的 ¢ 也换成了 ◆ (VIII. Justice 印成 "gain ◆ until ..."). 现在只认 `¢ (Destroy|Pay|Discard|Remove)`, 句中钱一律是 ¢.
- 牌堆排序暂缓 (2026-11-17, 用户喊停): 想按卡名首词字母序排, 但用户说"重排暂缓, 等我通知". 已做的改动全部回滚 (cards_final.csv 恢复原序, make_duplex_csv/build_filter 的 sort 撤掉), 等通知再动.
- roll 表切分不能要求"标签连续递增" (2026-11-17, 用户抓到 Pills!): 房卡/标记卡常常只有 3-4, 5, 6 (缺 1-2), 递增规则会把这种表整段吞掉. 现在的规则: 标签数字必须在 1..6 内; 且标签前面那个词不能是"接数量的动词"(loot/gain/take/deal/lose/steal/heal/add/pay/discard/put/remove/give/choose/roll), 否则 `Loot 3. Then put...` 里的 3 会被当成下一条结果 —— Pills! 就是这样被切成 `1-2: loot / 3: Then put 3 cards...` 的. 反例: `monster deck 3-4:` 前面是名词, 必须认成标签 (I Am Error).

- Minecraft 实例(Cobblemon Official Modpack [Fabric], 1.21.1 + Fabric 0.20.1): `D:\Minecraft\.minecraft\versions\Cobblemon Official Modpack [Fabric]`; 75 个 jar, Cobblemon 1.8.4, 语言已设 zh_cn; 自带演示存档 `saves\Tutorial World v4 (1.8)`(世界名是 Cobbled Farms, 内容不是任务地图); `config\cobblemon\main.json` 里非默认的数: `experienceMultiplier` 2.0, `healPercent` 0.05 与 `healTimer` 60 (战斗外每 60 秒自愈 5%), `secondsToChargeHealingMachine` 900 且 `maxHealerCharge` 6, `defaultBoxCount` 40, `shinyRate` 8192; 键位 M 看能力 (未选初始伙伴时开选择界面), R 放宠或对野生的开战, 方向键换选中, O 收队伍栏, 骑乘时左 Alt 自由视角.

- 白名单复数一律同变体 (2026-11-17, 用户口径): loots 的 s 也要进小型大写, 和 souls 一致. 现在 14 个名词在代码里只写单数 (TERMS), `_term_forms()` 自动追加 `s` / `es`, 正则按长度倒序拼, 让 `bosses` 压过 `boss`. 印出来的 `loots` / `treasures` / `coins` / `bosses` 整词进 caps 字体, 不再出现「术语 + 普通 s」的断字.
- U+2014 会被 xeCJK 吞掉后面的空格 (2026-11-17, 用户发现 `instead —1-4:`): xeCJK 把 em dash 归成 CJK 标点, 按其挤压规则吃空格, 数据里一个字面的 U+2014 印出来就紧贴后面的数字. 全文破折号改用 TeX 的 `---` (三个连字符, 拉丁标点, 保留空格). 两处归口: render_cards_tex.py 的 format_body()/style_labels(), make_duplex_csv.py 的 clean()/reward_text().
- clean() 可能被调用两次, 替换必须幂等 (2026-11-17, 自己踩的坑): 用 `(?i)\binstead\s*-\s*` 换成 `instead --- ` 时, 第二次调用会把 `---` 的开头再吃一遍, 印成 `instead --- -- 1-4:`. 现在只认紧贴单词的单个连字符 `instead-(\s+)`, 已写成 `---` 的不会再被匹配.
- Dice Room 改用罗马数字 (2026-11-17, 用户口径): 站点把六张同名房卡写成 `Dice Room!` / `Dice Room!!` / ... / `Dice Room!!!!!!`, 卡面标题印 `Dice Room I` .. `Dice Room VI`, 感叹号个数 = 罗马数字, 对应游戏里骰面的六种效果. 改名后卡名顺序变了, 重排 cards_final.csv 并删掉 build\sizes_room.json 再编.

- 引号要印成一眼能看出的双引号 (2026-11-17, 用户口径): 数据里 `with "Bomb" in its name` 这种直引号, 原来 clean() 用 `" -> '` 变成撇号, 用户说`这种引号都替换成 "" 吧, 否则实在是看不出来啊`. 现在 make_duplex_csv.py 的 smart_quotes() 逐字符按出现顺序交替转成 U+201C/U+201D, 已弯的不动; `’ -> '` 的撇号归一保留.
- 弯引号必须回到拉丁字体 (2026-11-17, 用户发现 `感觉"和周围格格不入`): xeCJK 把 U+2018/201C 归入 FullLeft、U+2019/201D/2013/2014 归入 FullRight (xeCJK.sty 的 OP/CL 列表), 于是引号被当全角 CJK 标点用 simhei 排, 夹在 LM 正交正文里极突兀. 在 preamble 顶层 `\xeCJKDeclareCharClass` 无效 —— 包加载时它自己的列表会覆盖. 有效写法: `\AtBeginDocument{\xeCJKDeclareCharClass{Default}{"2013, "2014, "2018, "2019, "201C, "201D}}`. 验证方式: pymupdf 读 span 字体, 应为 LMRoman10-Regular, SimHei 就是没生效.

- 钱一律印 ¢, 站点写出来的 `cents` 也算 (2026-11-17): `lose x cents` / `costs 10 cent` 这类英文写法在卡面上一律转成 `x¢` / `10¢`. 两处归口: make_duplex_csv.py 的 clean() 认 `(x|数字) cents?`, build_rules.py 的速查卡文案手改. 词条标题 `CENT` 保留 (它是术语表的词头, 和 HP/ATK 一样).
- REWARD 行只留 monster (2026-11-17, 用户口径 + 反例证据): 其他六个牌堆正文已覆盖奖励, 删掉; monster 例外, 因为 160 张里 139 张正文根本不提击杀奖励 (Anonymous Mask of Infamy / Avaricious Greed 等), 删了就丢信息.

- 正面只有一行的牌堆类型名, 细分全删 (2026-11-17, 用户口径): 站点把每堆切成 Passive/Active/Eternal/One-Use/Paid treasure、Basic/Boss/Epic monster、Good/Bad Event、Bonus Soul、QUICK REFERENCE n/4、KEYWORD n/4 等一堆细分, 用户说"在正面展示细分毫无意义". 现在 make_duplex_csv.py 用 SUBTITLE 表按牌堆给一个常量 (Character Card / Starting Item / Treasure Card / Monster Card / Loot Card / Room Card / Soul Card), rule 堆在 build_rules.py 里也写死 Rule Card. 细分信息靠正文自证 (有 Tap 就是能激活, 正文写 Roll 表就是 boss 之类).

- ABILITY 进白名单, ROLL 不进 (2026-11-17, 用户问 `abilities` / `rolls` 该不该入): ability 16 张卡 18 处, 和 ETERNAL(16 张)、COUNTER 同级, 是"扫卡必须认出的对象类别" (Tap ability / ¢ ability / triggered ability), 已加, 复数走 y->ies (`abilities`), _term_forms 加了 _plural 特例. roll/rolls 173 张 211 处, 是动作动词不是对象, 而且掷骰表开头已有 `Roll —` 标签, 再加小型大写会把几乎每张卡打花 (和 MONSTER/ATTACK 被排除同理).

- RULE 专用术语组 (2026-11-17): 不要在全体牌堆里放 RULE 的 26 个卡名. 552 张卡正文里, indomitable / familiar / team up / guppy / die face / every character 都是 0 次, trinket 和 ambush 只在 Ball of Tar 一张卡里各出现 1 次, curse 的 23 处有 20 处是卡名 (Curse Of The Tower 之类). 真正在 rule 正文里互相引用的只有 stack 8 / priority 5 / slot 7 / purchase 2 / death 2 / win 1 / phase 5. 因此 render_cards_tex.py 里另立 RULE_TERMS, 只在 stack=="rule" 时并进 KEYWORDS (`_keywords()` 按 _DECK 缓存两套正则), 全局 TERMS 保持 15 个 + ability.
- 孤儿规则卡 (2026-11-17): TEAM UP / GUPPY / INDOMITABLE / FAMILIAR / TRINKET / AMBUSH / DIE FACES / EVERY CHARACTER 描述的是"副类型关键字", 而副类型已按要求从正面类型行删掉 (monster 的 Boss / Bad Event / Curse, treasure 的 Trinket / Paid / One-Use), 所以这些词在整套牌上彻底不可见. 待用户决定: 补回一行副类型关键字, 还是删掉这几张规则卡.

- 关键字行缺失 (2026-11-17, 我先前判断错了): 这些词不是游戏不用, 而是我们的 cards_final.csv 把官方卡面上的关键字行 (-Indomitable- / -Trinket- / -Curse- / -Guppy- / -Ambush- / -Familiar- / -Eternal-) 整行丢掉了. raw 里关键字行计数: Eternal 69 / Trinket 27 / Indomitable 15 / Curse 10 / Guppy 8 / Ambush 2 / Familiar 1. 例: The Impostor! 官方效果是 "Indomitable monsters can't be covered...", 我们的卡只剩投票那句, 不可被覆盖的机制直接消失. 补一行关键字 (类型行下面灰色小字) 才是正解; 在此之前不要删 TRINKET/AMBUSH/INDOMITABLE/FAMILIAR/GUPPY 这几张规则卡.
- DIE FACES 没有对家 (2026-11-17): raw 里 circled 数字 0 处, 我们的卡面也没有圈号触发, 这张规则卡可以删.
- EVERY CHARACTER 必须保留 (2026-11-17): 它的存在理由是把"Tap: Play an additional loot card this turn"从 17 张角色卡上搬进规则堆, 删了这条规则就没有任何地方写着.

- RULE 堆收敛到 18 张 (2026-11-17, 用户拍板"1 2 全删"): 删掉 TRINKET / AMBUSH / CURSE / INDOMITABLE / FAMILIAR / TEAM UP / GUPPY / DIE FACES. 保留 START PHASE / ACTION PHASE / END PHASE / ATTACK / PURCHASE / SLOTS / DEATH / WIN / DICE / STACK / PRIORITY / ETERNAL / ROLL / TAP / CENT / HP / ATK / EVERY CHARACTER. 结果 2 sheets, 全量 65 sheets. 删卡后 sizes_rule.json 的 index 键会错位 (旧 26 个 key), 必须清缓存再编.

- token 大字符垂直居中 (2026-11-17): build_tokens.py 的 big 节点起点从 28.5 改 27.75, 因为 LM 粗体数字在行框里偏低, 墨迹中心比行框中心低 0.75mm; 改后 1¢ / 5¢ 的墨迹中心落在 49.50mm (卡高 99 的中点), ♥ 本来就在 49.40mm, 不用动. 验证法: pymupdf 取 size>20 的 span bbox, 算 (y0+y1)/2 - 该卡行顶.

- TRACK 卡 3×3 九张一版 (2026-11-17, 用户问"做 9 个可以吗"): build_track.py 原来一张 A4 只印 1 张, 改成和主牌堆一样的 3×3 满版 + 中线裁切, 一版 9 张, 正背各 9. 顺带修 bug: 两行脚注 (DOWN 1 PER ROUND / AND 1 FOR EVERY DEATH) 原来在 73.8/77.2, 正好压在 0 行 (行区 26.5..77.3), 已移到 79.4/82.9.
- TRACK 用途: 只服务单人/合作模式, 替代官方 D8 的倒计时 (开局 8, 每轮 -1, 每死一个角色再 -1, 过 1 判负). 多人竞争局用不到, 所以 9 张里 8 张是备件.

- TRACK 行内对齐 (2026-11-17, 用户指出"数字和字母居中但方框没对齐"): 原因是行框 5.2mm 高, 但 15pt 数字/6.5pt 小字的墨迹都偏下 1.59mm (锚点用 north west, 墨迹跟着基线走), 于是字压在行框下线上、上半留白, 看着像框没包住字. 改成 anchor=center 的 cbox() 并整体上移 0.08mm; 数字降到 13.5pt (墨迹 4.75mm, 上下各留 0.2), 并加 26mm 处竖线把行分成 12mm 数字格 + 30mm 字格, 数字居中于 20, 字居中于 41.

- TRACK 卡只留一个标题 TRACK (2026-11-17, 用户要求简洁): 删掉 TURN TRACK 下的 SOLO AND CO-OP 副标题, 删掉行内 26mm 的竖线; 标题上移到 9.4mm 补空.
- token 去掉 tag 行 (2026-11-17, 用户要求): CENT POOL / HEALTH 两行删掉, 只留大字符 + 下方 ONE CENT / FIVE CENTS / 1 HP 说明.

- token / track 正面也不留框 (2026-11-17, 用户要求): 主牌堆正面前面就已经无框, token 的"硬币边"和 track 的 5.5mm 内框是最后两个例外, 现已删. 背面仍保留 7.0mm 灰框 (那是对齐依据). 检查法: pymupdf get_drawings() 里 page0 不应存在 >40x70mm 的矩形.

- 白名单"灭绝即删"规则 (2026-11-17, 用户口径): 某词若在所有牌堆正文/数值/奖励行里都搜不到了, 就当它已灭绝, 从 TERMS / RULE_TERMS 里删掉. 新增 en\deck\terms_audit.py 做这件事 (读 cards_final.csv + cards_fronts_rule.csv, 扫 stats/effect/footer/rule body, 打印命中数与分布, 0 命中的直接标 EXTINCT). 首次跑: 15 个 TERMS 与 9 个 RULE_TERMS 全部有命中, 无一灭绝; 最濒危的是 coin (2 处, 全在 PRIORITY 卡 "Bartering coins and promises"), 其余最少 5 处.

- 圆点选项删除 (2026-11-17, 用户要求): `•` 只是选项符号, 全牌堆只有 4 张在用 (Void 两份, Ball of Tar, Magic Mushroom). clean() 里把圆点换成 ` / `, 并把 `Choose one:` / `Choose one-` 统一成 `Choose one ---`, 于是二选一只剩一种写法.
- 幂等坑: body() 与 front_row() 都调 clean(), 所以 clean() 里每条规则必须在已清洗文本上仍然成立. `Choose one\s*[-:]` 会在第二遍吃掉 `---` 的一条杠变 `--- --`, 已加 `(?![-:])` lookahead.
- coin 灭绝 (2026-11-17, 用户决定): 白名单删掉 coin, 全牌堆的 coin 都改印 `¢` —— 正文 `Gain 10¢`, 奖励 `+4¢`, 规则卡 `Bartering ¢ and promises ...` / `A cost or an amount of ¢.`. 站点遗留的占位奖励也一起规整: `Gain x Coin` -> `Gain x¢`, `Loot x Loot` / `Gain x Loot` -> `Loot x`, `1¢ Coin` -> `1¢`.
- RULE 牌堆扩到 27 张 (2026-11-17, 用户要求"每个白名单名词都列一张": 新增 DAMAGE / ROOM / SOUL / ABILITY / COUNTER / LOOT / TREASURE / BOSS, 并从 DICE 拆出 DC). 全堆正文统一 8.00pt, 3 sheets. 动因: 中文版只翻非白名单部分, 白名单名词的解释由 RULE 统一提供.

- 圆点规则返工 (2026-11-17, 用户要求): 早先"把 `Choose one` 写成 `---`"的做法作废 —— 那会让 renderer 的 CHOOSE 正则只吃掉一条杠, 印出 "— –". 现在 CSV 只把圆点换成 ` / `, 标签一律保留冒号 (`Choose one:`), 破折号交给 renderer 生成; 中圆点 U+00B7 (Isaac's Last Will, `Choose 1`) 与圆点 U+2022 一起处理.
- REWARD 删除做成通用判断 (2026-11-17, 用户口径): monster 的 REWARD 只在正文没说 payout 时印. covered() 要求"动词+数量+单位" (PAYOUT: gain/loot N treasure, gain/draw N loot 或 loot N, gain/take N c, gain/take/control N soul), 因此 `discard 2 loot cards` 不算覆盖. 实际删掉的 5 张: Angel Room, Double Treasure!, I Am Error!, Secret Room!, Spiked Chest; Dank Globin 保留.
- reward 里的 soul 与其余单位同形 (2026-11-17, 用户要求): 一律 `+N Soul` (不再是 `Soul +1`); 混合列表 (`1x Soul; Roll- Gain x Coin`) 里的计数项也要格式化, 非计数项原样保留.
- TRACK 改名 COUNTER (2026-11-17, 用户要求"TRACK 和 D8 统一叫 counter"): build_track.py 正面标题与背面堆名都印 COUNTER, 输出改成 print\cards_duplex_counter.pdf (旧 track 文件自动删), ATTACK 规则卡的 "You may use a D8" 改成 "Use a counter card".
- STARTING ITEM 只留非 treasure 的 4 张 (2026-11-17, 用户选 B): 官方起始道具本身就是 treasure 卡, 开局从 treasure 堆抽出交给角色; 因此 make_duplex_csv 在 start 堆里剔掉同名 treasure 卡 (12 张), 只剩 Blood Lust / Lazarus' Rags / Sibling Rivalry / Sleight of Hand.
- CROWD SLOT 规则卡 (2026-11-17, 用户同意补): Anonymous Mask of Infamy 的 "crowd slot" 在 rulebook 里 0 命中; build_rules 新增 CROWD SLOT 卡 (怪物行之外追加的怪物格, 不属于 shop/monster/room 三种 slot, 不参与补位, 里面的怪物能被打且照常结算奖励), 并把 `crowd slot` 加进 RULE_TERMS (正则按长度排序, 长词优先匹配, 不会被 `slot` 抢先).

- 本机有梯子 (2026-11-17, 用户口径): Clash Verge 常驻, 混合端口 `127.0.0.1:7897` 在监听, 但系统代理 `ProxyEnable=0` (所以浏览器之外的命令行不会自动走它). 要访问 GitHub / HuggingFace / pypi 外网时显式加 `-Proxy http://127.0.0.1:7897` 或设 `HTTPS_PROXY`, 并且**先向用户开口要求开梯子**, 不要绕道第三方镜像或降级模型; 原话"别总绕开, 我怕会降低效果".
- 注入引擎环境 (2026-11-17): `D:\wenje-ma\wenje-codes\.venv-ocr` 是 uv 装的 Python 3.12.16 (D:\Python314 的 3.14 装不上 rapid_latex_ocr, 它要求 <3.13; uv 本体 `pip install uv` 就够, 不必下 exe). 内含 rapid_latex_ocr + pymupdf.
- 公式识别实测 (2026-11-17): rapid_latex_ocr 对**完整的一条行间公式**能到字符级正确 (实例: TeX 层 `𝐹𝑛,𝜖= {𝑥∈𝐸; ∀𝑝≥𝑛, 𝛿(𝑓𝑝(𝑥), 𝑓𝑛(𝑥)) ≤𝜖}` 被认出 `F_{n,\epsilon}=\{x\in E:\forall p\geq n,\delta(f_{p}(x),f_{n}(x))\leq\epsilon\}`, 转成扁平字符逐字一致); 但裁到半句就崩 (TeX 文字层的行框会把公式切开, 半截图进去出来的是 `\stackrel{\leftarrow\leftarrow}{x}` 这类垃圾). 结论: 管线必须先做公式区域检测, 不能照文字行框切图.
- 基准尺子 (2026-11-17): 有 TeX 文字层的 PDF 就是免费 ground truth — 同页渲染成图走 OCR, 再与 `page.get_text()` 逐字符比, 准确率可自动量. `Topology2024_Anon.pdf` (47 页, xdvipdfmx 产物, 无位图) 是最合适的那把尺子.
- 引擎选型与收尾 (2026-11-17, 用户口径"本地比较无所谓, 最终确定好了清除其余的就行"): 横评阶段允许多套引擎/venv/权重同时驻留, 不要为了省盘只装一套; 定稿后把落选的引擎、权重、venv 一并删掉, 不留备胎. 终选判据不是榜单, 是自家页面上的逐字符准确率 + 抽取 50 页扫描教材人眼核.
- `mineru` 的 PyPI 包在 4.x 已换成云端文档中心产品 (命令是 parse/scan/search, 无 torch, 走远程额度); 本地管线版必须装 2.x (末版 2.7.6), 且 4.x 与 2.x 同名不同物, 别装串.
- 术语译法备忘 (2026-11-16, 用户口径): may = 可选择, 可以执行也可以放弃, 译"可"而不是"必须"; steal 译"夺取"(直接从对方手里拿走并归自己), 不用"偷窃"那种隐秘含义.
- TRACK 改回本名, COUNTER 只指骰子标记 (2026-11-17, 用户推翻上一轮": 阶梯卡 (8→0, START/LAST STEP/DEFEAT) 正反面都印 **TRACK**, 输出 `print\cards_duplex_track.pdf` (旧的 counter 文件自动删); 卡面正文里的 `counter` 专指放在卡上的计数标记, 用户实际用 20 颗 12mm D6 当标记 (1~6 一颗, 7~12 按"6 + 余数"两颗, The Dead Cat 的 9、Greed's Gamble 的 20 就靠叠加). RULE 堆的 ATTACK 卡从 "Use a counter card" 改成 "Use the TRACK card"; COUNTER 规则卡改写成"卡上的标记, 本桌用骰子".
- RULE 堆补到 30 张 (2026-11-17, 用户"不打印说明书, RULE 必须完备且够用"): 新增 SETUP (洗四堆/各自弃牌堆/100¢ 池/2 shop + 2 monster + 1 room/事件换底/每人角色卡+起始道具+3 loot+3¢/角色 deactivated、起始道具 charged), TRACK (8→0 阶梯: 单人合作计时器 8 起, 双方回合结束 -1, 死角色再 -1, 到 0 判负; 任何模式都可当怪物血量尺), FLIP (翻面 = 读另一面, 本印张只有 Trick/Treat), EVENT (无数值块的怪物卡, 占怪物格不可攻击, 进场的触发能力全触发后进弃牌); HP 卡改成"怪物在卡上、玩家在角色卡上, 用心形 token 或骰子记, 每回合结束全部回满".
- OCR 文字层带 txt 旁文件 (2026-11-17, 用户口径"下次你读 PDF 也就直接读了, 提升效率"): `ocr_books.py` 除 `xxx_ocr.pdf` 外再写 `xxx_ocr.txt`, 每页以 `# page N` 打头, 内容是注入后回读的真实文本. 读一本扫描书要先读这个 txt (grep 定位页码), 不要再逐页截图或渲染; 这个项目的验收标准就是"助手能直接读、不用截屏".
- 页面上采样默认 2x (2026-11-17): `--scale 2`. 同一 4 页正文实测 1x 318 s, `三形`/`方体`/`平中` 丢字且范数读成 `|T|`; 2x 196 s, 范数 `‖T‖` 与标点恢复, 仍丢个别偏旁; 3x 119 s 能救 `三角形`/`平面中的一个凸集` 但范数退回 `|T|`. 中文教材重的书用 3, 公式书用 2.
- 数学斜体只能落成 ASCII (2026-11-17, 实测): PyMuPDF TextWriter 无法把补充平面码位 (U+1D400 区) 映射回 Unicode, 写进去的 `𝑦` 回读成 `ᵕ`; 本机 seguisym.ttf / cambria.ttc 虽覆盖该区也没用. 于是 NFKC 折成 `y`, 而 `∈ ≤ ‖ √ ∂` 这些 BMP 符号保真. 用户已接受 (2026-11-17: "这个无所谓, 毕竟我的要求确实太高了").
- 断点与打断 (2026-11-17): 缓存 `%TEMP%\ocr_books\<stem>_<路径指纹>\blocks_<a>_<b>_s<scale>.json`, 断点粒度是 chunk; 成品先写 `.part` 再 `os.replace`, 所以 Ctrl+C 不会留半截 PDF, 也不会被"已存在即跳过"误判. 改 `--chunk` 或 `--scale` 会换缓存名, 旧缓存作废. 缓存目录带路径指纹是因为扫整个 `D:\wenje` 时同名书会互相污染.
- 文件夹模式 (2026-11-17, 用户要求"像 auto_typesetting.py"): `python ocr_books.py <文件或文件夹>`, 无参数弹文件夹框; 已有文本层的书、已有 `_ocr.pdf` 的书直接跳过 (`--force` 覆盖). `ocr.bat` 与 `run-ocr.ps1` 已删, 只留这一个入口.- 目录分层 (2026-11-17, 用户要求"其余的放文件夹里, 要不我不好找"): 仓库顶层只留四个要手动跑的脚本 `ocr_books.py` / `auto_typesetting.py` / `md_merge.py` / `pdf_split.py` 加三份文档; Markdown 与数学排版链 (leftright / math_space_strip / cn_punct / lib_inline / lib_sort) 放 `md/`, OCR 支撑件 (ocr_inject / latex2glyph / ocr_bench / ocr_qa / _dump) 放 `ocr/`. `ocr_all.py` 已删, 文件夹模式取代它. import 路径随之改成 `sys.path.insert(0, 本目录/ocr)` 与 `auto_typesetting.py` 的 `HERE/"md"`, 所以脚本仍可从顶层按路径启动.- 新增代码一律进子目录 (2026-11-17, 用户"以后新增代码也别放表面, 除非是我让你放的, 要不然太乱了"): 顶层永远只有四个入口脚本 `ocr_books.py` / `auto_typesetting.py` / `md_merge.py` / `pdf_split.py` 与 README/STYLE. 新写的工具放 `md/` 或 `ocr/`, 备份与数据放 `docs/`; 只有用户明确点名要放顶层才放顶层.
- 任意 PDF 都产出 `_ocr.pdf` + `_ocr.txt` 成对 (2026-11-17, 用户"我希望任意PDF都生成, 要是原本就有文本层的, 也生成一个ocr版本, txt就是直接复制其文本层...我也方便监督文本的效果和谁还没OCR"): 有真文本层的书不再跳过, 原样复制成 `_ocr.pdf` 并由其自身文本层生成 sidecar (实测 47 页逐页 get_text 完全一致); 扫描书仍走 OCR 注入. 想强行对有文本层的书重跑 OCR 用 `--ocr-anyway`; `--force` 只表示"覆盖已存在的成品", 不再兼作"无视文本层". 判据仍是抽样 6 页平均正文 > 40 字符, 落在 `has_real_text_layer(doc)`.
- 中文卡面标点也得半角 (2026-11-17, 用户纠错 "我们的标点符号都应该用英文的, 这个我似乎写在STYLE里了"): 第 48-59 条本就管全库, 中文卡面同样适用 —— 中文标点换半角, 终止符后补一个空格, 汉字与西文/数字相接处补一个空格, 开引号前与闭引号后接汉字各补一个空格, 弯引号换直引号, 汉字之间仍不加空格. cn\data\translations.csv 已按此一次性洗完 (94 行), 以后新译文照这个口径直接写. 兜底在 cn\deck\build_cn.py 的 punct() 里, 构建期再跑一遍, 幂等 (洗完的源再 build, 生成的 fronts CSV 与洗前逐字节一致). 手洗源 CSV 必须 csv.DictWriter + QUOTE_ALL 写回, 否则正文里的半角逗号会把字段截断.- 中文全库完工 (2026-11-17, 用户「直接弄完吧」): 译文按堆落成 `cn\data\zh\{monster,treasure,rule_soul_char,flip}.txt`, 每行 `slug|中文`, 换行写字符 `\n` (渲染器按真实换行切关键字行, 只在汇总时展开); `cn\deck\merge_translations.py` 把它们并进 `cn\data\translations.csv` (QUOTE_ALL, 经 build_cn.punct() 幂等洗标点), 并按 cards_final 里「有正文的卡」反查缺漏 — 只有天生无正文的 19 张怪物 + 14 张角色卡不译. 中文成品 7 堆 + flip + track + token = 85 sheets / 170 页, 与英文同数; 合并件 `cn\print\cards_all_cn.pdf`.
- 中文规则卡的术语桶 (2026-11-17): `_keywords()` 的 bucket 判据是 `_DECK in ("rule", "cnrule")`, 原来只认 `rule`, 于是中文规则卡里的 stack / priority / slot 全是裸词不加粗 (英文同一句是 `kw` 小体大写). cn 堆沿用英文的粗体 + 小型大写, 两版一致.
- 中文堆不断词 (2026-11-17): 汉字排到页边时只剩几个拉丁词可断, `pri-ority` 一拆行在汉字之间读起来像错字. `build_tex()` 里 `stack.startswith("cn")` 时把 preamble 的 `\hyphenpenalty=100` 换成 `10000`, 英文堆不动 (英文断词是版式的一部分).
- flip / track / token 三张辅卡的中文版 (2026-11-17): flip 走 `cn\deck\build_flip_cn.py` (两面正文取自 translations.csv, 按 `Treat:` 切两半, 复用英文 builder 的中心格与缩字号循环); track 走 `cn\deck\build_track_cn.py` (数字不变, 只译 START/LAST STEP/DEFEAT 与两行脚注, 字体换 simsun); token 一枚字都没有 (只有 1¢ / 5¢ / ♥), 中文册直接并进英文 `cards_duplex_token.pdf`. 中文 RULE 全堆统一 9.0pt (36 张里最长的是 ATTACK/ATK), 用 `sizes_cnrule.json` 写满 36 个键固定, 不再逐卡缩.
- 中文卡面直引号 (2026-11-17): xeCJK 把 ASCII `"` 一律印成 U+201D, 开口闭口不分, 于是 `名称含 "bomb" 的牌` 被印成 `名称含”bomb”的牌` —— 这正是用户当时说的"和周围格格不入". cn 堆在 `esc()` 里把 `"` 换成 `\textquotedbl{}` 强制直引号 (`_STRAIGHT_QUOTE` 由 `build_tex()` 按 `stack.startswith("cn")` 置位); 英文正文里一个 ASCII 引号都没有, 不受影响. 卡名里的 `’` (Bob’s Brain / Lazarus’ Rags) 是游戏原名, 照抄不改. `\xeCJKDeclareCharClass{Default}{"0022}` 试过无效, 转换不走在字符类上.
- 进度显示与先易后难 (2026-11-17, 用户"能不能有个进度显示...先处理最简单的, 把最复杂的放在最后"): `ocr_books.py` 每 20 秒打一条 `[#####...] 37.5%  812/2190 pages  elapsed 1h02m  left ~1h48m  book.pdf`, 同时写 `%TEMP%\ocr_books\progress.json` 供外部查; 外加每个 chunk 结束各打一行. 排序 `--order easy|hard|name` (默认 easy): 复杂度 = 页数 × (1 + 5×墨量), 墨量是抽样 4 页按 48 dpi 灰度算暗像素占比, 几十毫秒一本书, 与引擎真正花的时间同向.
- 子目录必须当包用, 不用 sys.path 拼兄弟模块 (2026-11-17, 用户报 Pylance 把 `from latex2glyph import flatten` 标红): `md/` 与 `ocr/` 各加 `__init__.py`, 入口改为绝对导入 `from ocr.latex2glyph import flatten`; 子目录内脚本要跑自己时先 `sys.path.insert(0, parent.parent)` 再绝对导入. 另一类红是 PyMuPDF 2.x 的 `get_text()` 重载返回 `str | list | dict`, `.strip()`/`len()` 会被判成在 list 上调用 — 一律写 `get_text("text")` 锁死 str 重载.- Ctrl+C 的正确行为 (2026-11-17, 用户连按 7 次 Ctrl+C 得到一屏 traceback): 旧版 interrupt 打在 `as_completed` 或 `ThreadPoolExecutor.__exit__` 的 `join` 上, 每按一次抛一层, 还留一串 `Exception ignored on threading shutdown`, 且 `subprocess.run` 的引擎子进程不会被带走, 主进程死后引擎继续烧核. 现在: 引擎走 `run_engine()` + `Popen` 登记到 `LIVE`, interrupt 时 `stop_engines()` 用 `taskkill /PID x /T /F` 杀整棵树, 打印一行提示后 `os._exit(130)` 直接退出 (线程池 `shutdown(wait=False, cancel_futures=True)` 不再 join). 已完成的 chunk 缓存不受影响, 重跑同一命令续上.
- 规划阶段也要能中断且要缓存 (2026-11-17): 对 `D:\wenje-ma` 全库冷启动规划实测 28.3 s (382 个 PDF 各开一次、抽 4 页 48 dpi 渲染), 用户误以为卡死就 Ctrl+C 了. 现在 `complexity()` 按 (路径, size, mtime) 缓存到 `%TEMP%\ocr_books\plan.json`, 第二次规划实测 1.3 s (0 measured / 382 reused); 进度按"实测了几个"打印; 新增 `--plan-only` 只印排期不干活, `--min-pages N` 过滤一页一张的插图切片. 规划也纳入主 try, 任何时刻 Ctrl+C 都是同一句提示.
- 别对 `D:\wenje-ma` 根目录无脑跑 (2026-11-17 实测): 382 个 PDF / 26401 页, 含 5255 页《资治通鉴》与大量 1 页插图切片; `--min-pages 20` 后仍 115 本 / 25704 页. 目标若只是 20 本数学书, 就把参数指到那 20 个 `textbooks` 目录.
- 两个解释器都能跑 driver (2026-11-17 实测): `D:\Python314\python.exe` 带 pymupdf 2.0, `.venv-ocr` 带 2.1, `TextWriter.write_text` 与 `fill_textbox` 签名逐字相同 — 但默认仍用 venv python, 免得分叉. 引擎子进程永远固定走 `VENV_PY`, 与 driver 用哪个无关.- 原地重绘的进度条 (2026-11-17, 用户问"pip 安装包时的进度条是咋做的, 我们能实现吗"): pip 那条是它自带的 `rich.progress` 画的, 本质就是 `\r` 回车不换行 + 覆盖旧内容, 再用"已完成量/已用时间"推 ETA (rich 内部对速率做指数平滑). 我们不用装任何库: `Status` 类持有 stdout 的 tty 判定与非 tty 降级, `draw()` 写 `\r` + 整行 + 用空格补齐旧宽度 (不依赖 ANSI, conhost 也能用), `say()` 打日志前先按旧宽度刷空格擦掉进度条再换行, 所以日志永远在条的上方. 非 tty (重定向到文件或管道) 自动降级成每 30 秒一条普通行 — 同 pip 的做法. 字形 `█░`, 若 stdout 编码吐不出就退回 `#.`. 刷新频率 5 秒 (`watch(every=5)`), 因为 chunk 只有几十份之一会变, 但时间/ETA 要看着在走.
- 骰子点数印圈数字 (2026-11-17, 用户"能否用 ①②③④⑤⑥ 来专门指代骰子掷出的点数, 这样能清晰不少"): Roll/掷骰 表的结果标签一律印 ①②③④⑤⑥, 区间印 `①-②` (1..6 之外的数字不转), `/` 分隔保留. 三个入口: `_roll_lines` 的表头认 `Roll|Rolls|掷骰` + `-` `:` em dash (连续破折号一并吃掉, 否则 `-- 1-2:` 会漏在前一条); 散文式 roll 表 (`Roll. If ... roll 3x instead — 1-4:`) 由 `_circle_labels` 全篇扫, 守卫同 `_roll_chunks` (结果必须在 1..6, 不跟在 loot/gain/deal 这类量词动词后, 句点只用来关闭上一个结果). 字体: LM Roman 没有 U+2460 且 XeTeX 不自动 fallback, 所以英文用 `\pipfont` = Segoe UI Symbol 并 `\scalebox{1.2}` (Segoe 的圈只有 0.6 em, 10pt 正文旁边读成一个斑点), 中文用 `\pipsong` = SimSun 的原生全角圈, 不缩放. flip 卡不经 `build_tex()`, 语言靠环境变量 `CARD_PIP_FONT` / `CARD_STRAIGHT_QUOTE` 传入 (`build_flip_cn.py` 设 pipsong + 直引号), 否则中文 flip 的圈会落成 Segoe.
- translations.csv 顺序 = 印刷顺序 (2026-11-17, 用户"csv里的词条顺序能不能和PDF_all的一致, 要不找来找去的太费劲了"): `cn\deck\merge_translations.py` 里 `PAGE_ORDER` = character, treasure, monster, loot, room, soul, rule, flip, 按 `en\deck\cards_fronts_<stack>.csv` 的 slug 顺序建排名再排序 (不读 cards_final, 那里面还混着别的堆的行); flip 只有一张 `Trick/Treat`, 直接从 cards_final 取; 重复 slug 以首次出现为准 (书里同名不同版的两张共用一个 slug); 书里不印的 slug 排到末尾并保持原有相对顺序. 排序只改行序, 内容与 punct 幂等洗标点不动; `build_cn.py` 按 slug 查字典, 顺序不影响构建. 已核对 536 行与印序逐行一致.

- 汉字与西文之间那一个空格必须真的印出来 (2026-11-17, 用户"为什么汉字和西文的左右没有全都留 1 空格, 明明在 csv 里留了呀"): 病根在 preamble 的 `CJKecglue={\hskip 0.15em}` —— xeCJK 用 CJKecglue **替换**汉字/拉丁边界上的源空格, 于是 `查看 treasure` 印成 0.15em(1.49pt) 的细缝, 而反方向 `treasure 牌堆顶` 的空格照旧是 3.3pt, 两侧不等宽. 现在只留 `CJKglue` (给中文行内拉伸用), 不设 `CJKecglue`, 源空格在两侧都按 10pt 的 3.32pt 印出 (实测 3.32/3.32, 对称). 谁以后再往 preamble 里加 CJKecglue, 就会重新把空格吃掉. 改 preamble 后必须删 `en\deck\build\sizes_cn*.json` 再重渲染, 否则长文沿用旧字号、换行位置没重算.
- 云主机跑不了 OCR (2026-11-17 实测): 那台 Linux 云主机是 2 vCPU (Xeon 8457C) / 4032 MB 内存 / 无 swap / 10 GB overlay 盘 / 无 GPU; 网络倒是通 (pypi 200, modelscope 302). 装完 torch-cpu 1.6 + 模型 3.3 + 依赖约 1 GB 就吃掉 6 GB, 再加 934 MB 源书和同等量的成品就撑破 10 GB 盘; 3 GB 无 swap 也扛不住 2x 上采样后的单页位图. 算力只有本机的八分之一, 5029 页要按月计. 结论: 云主机不是"更快的备选", 而是更弱的机器 — 别在上面试, 白花时间. 另外跨机器没有共享盘, 1 GB 成品只能打包上传再下载, 不是"一键粘贴".

- 全套重译走意译 (2026-11-17, 用户"读起来不像人话, 重新翻译所有的牌...意译优先"): 初版译文是逐句贴着英文写的, 有翻译腔. 重译口径: 先读懂规则再用地道中文说一遍, 句序可以重排, 长句拆成短句, 但不许改规则含义 (数值/代价/时机/可选性一字不能动). 范围不变: 只翻正文非白名单部分, 牌名/类型行/卡背留英文. 新译文源 `cn\data\zh2\{treasure,monster,loot,room,soul,rule,character,flip}.txt`, 与旧 `zh` 并存; `cn\deck\apply_zh2.py` 把 zh2 覆写进 translations.csv (同 slug 覆盖, 缺的补, 仍按印刷顺序 + QUOTE_ALL + punct 幂等).
- 译文源里可以直接写 ①-⑥ (2026-11-17, 自己踩的坑): 渲染器原本只在 ASCII 数字标签上做 `_face()`, 裸 U+2460 会落进正文字体, 该字没有字形, 印出来是空框(抽取回读为 U+FFFF), 只剩分隔用的 `-`. 现在 `esc()` 里加了 `elif ch in PIPS: _face(...)`, 源码写圈数字也能进 `\pipsong` / `\pipfont`. 圈数字必须在 `esc()` 里转, 因为 `card()` 的调用顺序是 `format_body(esc(body))`, 在 format_body 里插 `{\pipsong X}` 会被 esc 把花括号转义掉.
- 改 renderer 后 flip 必须重建 (2026-11-17): `cn\print\cards_all_cn.pdf` 里的 flip 两面来自 `cn\print\cards_duplex_cnflip.pdf`, 而 merge_cn.py 只是把已存在的那个 PDF 追加进去, 不会重渲染. 所以动过 preamble / esc / 字号后, 中文全链要按 `apply_zh2.py -> build_cn.py -> 删 sizes_cn*.json -> render_cards_tex.py cn* -> build_flip_cn.py -> merge_cn.py` 顺序跑, 少了 build_flip_cn 这一句, flip 卡会沿用旧渲染结果 (实测就是这么漏掉圈数字的).
- 全库术语统一用中文讲 (2026-11-17): reward 不在白名单里(不印小型大写), 中文正文统一写"奖励", 不写 reward/rewards 混排; 规则卡的正文也一样(卡名 REWARD 本身仍是英文标题). 判定方法: 白名单外的一律中文, 白名单内的保留英文小写.

- reward 进白名单, 中文不译 (2026-11-18, 用户"别翻译, 并把它放在白名单里"): 上一轮把正文的 reward 统一译成"奖励"(理由是它不在白名单), 现在推翻. TERMS 追加 reward, 复数 rewards 由 _term_forms 自动生成; 中文正文 20 处"奖励"全部改回 reward, 印成粗体小型大写. 连带 monster 卡底部那行 `reward +2 Loot` 的标签也自动进入 caps 字体 (LMRomanCaps10 + LMRoman10-Bold), 中英一致.
- item 进白名单 + 新增 ITEM 规则卡 (2026-11-18, 用户"可以"): 起因是一张 loot 卡写 `直到回合结束他控制的每件物品都获得 eternal` —— "每件物品"在整套牌里没有任何一处定义, 而 item 在英文正文出现 106 处 / 85 张卡, 中文原译"物品/道具"113 处. 做法: TERMS 追加 item (复数 items); build_rules 的 CARDS 在 TREASURE 之后插入 ITEM 卡 (任何在场上的 treasure 卡都是一件 item, 商店那几件归游戏控制也算, 角色卡不是, loot 卡要等正文把它变成 item 才算); 中文 113 处"物品/道具"统一换成 item.
- 插卡会让 slug 位移, 中英必须同步 (2026-11-18): build_rules 的 slug 就是 `rule-<序号>`, 所以插在 rule-27 之后等于让 rule-28..36 全部 +1. 必须同时改 `cn\data\zh2\rule.txt` 与 `cn\data\translations.csv` 的 slug (脚本里对 `rule-(\d+)` 做 n>=28 加一, 再插新行), 否则 apply_zh2 会把旧 rule-28 的正文留在新 rule-28 (ITEM) 上. 代价: RULE 36->37 张, rule 堆 4->5 sheets, 全书 85->86 sheets / 170->172 页 (最后一张只放 1 张卡, 8 格空). 想要 36 张的话就把 ITEM 并进 TREASURE 卡 (标题写成 `TREASURE / ITEM`, 与 DICE / DC 同一做法).
- 不要为"item"去还原正面细分 (2026-11-18): treasure 的细分行 (Passive 107 / Active 39 / Eternal 35 / Trinket 23 / One-Use 11 / Paid 10 / Soul 2) 讲的是"怎么用/能不能被毁", 没有一条定义 item; 还原它们等于多写五六张规则卡解释子类, 而这些信息正文已经自证 (TAP: / ¢ 支付 / 用完毁灭 / Eternal 关键字行). 用户当时担心的"RULES 需要解释的更多"正是还原细分的代价.

- 最终目标只有中文版 (2026-11-18, 用户口径): 英文牌组只是搭建期的脚手架, 不是要交付的第二个版本. 中文版验收通过后再删除英文产物 (en\print\*.pdf 里的成品册、英文牌堆 csv/渲染中间件可留作回归测试基准, 但对外只说中文版). 后续不用再为"中英两版同步"而做双份维护, 也不要在中文卡上保留英文正文或英文牌名; 唯一例外是术语表里那几个专有词(视用户当时的术语表而定).

- 泛函作业集的人名译名表 (2026-11-18, week9 补齐): Riesz→里斯, Baire→贝尔, Lebesgue→勒贝格, Hölder→赫尔德, Banach→巴拿赫, Hahn→哈恩; 组合名照 科尔莫戈罗夫-里斯-弗雷歇 那样的连写, 不加间隔点.
- 把英文人名换成中文时, 必须连带删掉它前面那个半角空格 (第 62 条): 直接替 `Banach 空间`→`巴拿赫空间` 会留下 `是 巴拿赫空间` 这种汉字之间的空格, 要连同前一个汉字一起匹配 (如 `对 巴拿赫`→`对巴拿赫`); 改完用 `\p{Han} \p{Han}` 扫一遍, 命中 0 才算干净.
- 译名以同库既有文件为准, 不自创: 泛函集里 巴拿赫/勒贝格/赫尔德/里斯 早已在 week1,2,4,5,7 定型, 新写的人名先 grep 全库看有没有旧译, 没有才定.

- 放弃全面中文化, 回到原汁原味名词版 (2026-11-18, 用户口径): 试过按灰机 wiki 把牌名/类型行/卡背/术语全换中文, 结论是走不通 —— 四魂原创牌 (Devout Mom!, Masquerade, Police Lineup, Sibling Rivalry, Game Crash! 等 35 条) 在 wiki 上没有条目, 搜索返回的全是侧边栏/成就页; 逐名搜索固定不下来 (569 个里 353 个候选含 "你解锁了""这是一个消歧义页" 这类噪声). 最终口径: 牌名/类型行 (Treasure Card 等)/卡背堆名保留英文, 正文只翻非白名单部分, 白名单术语仍印粗体小型大写. 即 cn\print\cards_all_cn.pdf 已是终版形态, 不要再改动. cn\data\zh_names.json / zh_names.csv / cn\deck\build_zh_names.py 等对照表产物留档但不再使用.

- 清理脚本必须跳过 .git (2026-11-18, 自己踩的坑): 写"白名单保留、其余删除"的 os.walk 清理器时忘了排除 .git, 1427 个待删文件里混进了 .git/objects; 只读对象删不掉(WinError 5), 可写的 .git/config, HEAD, refs/heads, index 全被删, 仓库直接变成 "not a git repository". 修复路径: 重建最小 .git/config + HEAD -> git fsck 找到 dangling commit -> update-ref 挂回 refs -> git reset --mixed 重建 index. 教训: os.walk 的 dirnames 要先过滤 {".git"}, 或干脆只遍历已列的目录清单.
- 归档口径: 仓库只留不可再生的源 (卡表 csv / 译文 zh2 / 渲染与构建脚本 / 规则书 / 原始抓取 / 单个中文成品册), 中间件与英文成品册全删; 老历史用 `git bundle create <repo-外>.bundle --all` 备份后再压成一次 snapshot 提交, 这样仓库体积从 124 MB 降到 3.3 MB.

- 卡面自洽口径 (2026-11-18, 用户定的): 卡牌只翻译正文, 译后正文里出现的**每一个拉丁词**必须属于白名单(或其复数) 或是某张卡的牌名(正文会点名别的牌), 外加 x 这类变量; 白名单里每个词都由 RULE 卡解释一遍, 整套牌即自洽. 因此规则卡**不许引用卡面不会出现的英文串**——旧 ABILITY 卡写"触发型以 when, at 或 each time 开头"就是反例(中文正文里根本不出现这三个词), 已改成"触发型会交代触发时机, 例如 "每当一名玩家死亡"". 机器审计脚本 `cn\deck\audit_latin.py`, 现 0 违规.
- 命名 counter 的印法 (2026-11-18): 修饰语中文, 术语 counter 保留英文, 如 "恐惧 counter"/"把戏 counter"/"黄金 counter"/"蜘蛛 counter"; 与 "受到 1 damage" 同一套混排逻辑.
- .gitignore 要写 `**/deck/build/` (2026-11-18, 自己踩的坑): 写 `deck/build/` 只匹配仓库根下的, `en/deck/build/` 会漏掉, 结果 build 中间件被提交进去, 仓库从 3.3 MB 涨到 8.3 MB.

- 卡堆归属以规则书为准, 不看数据的 kind 字段 (2026-11-18): 规则书写 "The Lost Soul is a loot card that can become a soul when played", 但抓下来的 kind 按卡名归成了 soul, 结果 9 张 soul 里混进一张 loot。已在 make_duplex_csv.py 里加 PILE 覆盖(p-lost_soul -> loot)并把类型行保成它自己印的 "Lost Soul Card"; soul 8 张 / loot 73 张, 总页 174 / 87 张纸。
- 卡面漏印的括号要补 (2026-11-18): Lost Soul 原卡还有一句 "(It's no longer an item)", 抓取的 effect 字段没带, 但它解释的正是"从 item 变成 soul"的身份变化, 已补成 "(它不再是一件 item.)"。

- Minecraft 实例(Homestead DEV, 1.20.1 + Fabric Loader 0.19.5): `D:\Minecraft\.minecraft\versions\Homestead DEV`; 381 个 jar / 625 mods(含 JiJ) / 711 MB; 启动自报 `Game took 200.882 seconds`. 分项: mod 解析 79 s, mixin 应用 23 s, 客户端 init 55 s, 资源重载加图集 28 s, 数据包与配方约 30 s, EuphoriaPatcher 反射 10 s. 硬件 i7-13620H + 64 GB DDR5 + NVMe, 瓶颈全在软件层.
- 该整合包的装饰 mod 是任务书内容, 不能当"没意义"删 (2026-11-18, 实测): FTB Quests 的 snbt 里直接引用 perfectplushies(43 处, 整章 `squishy_friends` 收集毛绒玩具), squish(28), cozystudioscore(20), phomesteadplushies(3), modrinth_logo_mod(3), umbrellas(2, 钓鱼任务), camerapture(2), blahaj(1, `blahaj:bread`). 删这些会断任务链, 只剩紫黑格图标.
- 已按"只改观感不改玩法"移出 59 个 jar 到 `versions\Homestead DEV\mods-disabled`(207.8 MB, 余 322 jar): FancyMenu 系(fancymenu/drippyloadingscreen/welcomescreen, 三者互相依赖要一起删), HUD 类, 音效氛围类(ambientsounds 51 MB, soundscape 95 MB), 皮肤渲染类, 诊断类(stackdeobfuscator/mixintrace). 回滚脚本 `versions\Homestead DEV\恢复全部mod.ps1`, 移动而非删除.
- 移除 mod 前先建依赖图再动手: 解压每个 jar 的 `fabric.mod.json` 取 id/depends/provides, 反向统计"被谁依赖"; 无被依赖才算叶子; 还要查 provides 交叉与 FTB Quests 的 snbt 引用. 本轮 381 jar 里 312 个是叶子, 124 个 id 被依赖(fabric-api 模块, porting_lib, tweed5, architectury 等).
- Defender 排除必须管理员: 普通用户跑 `Add-MpPreference -ExclusionPath` 报 "你的权限不足"; 排除 `D:\Minecraft`,`D:\MicrosoftJDK`,`%APPDATA%\.hmcl`. 本机 Defender 实时保护开着, HVCI 也开着(`SecurityServicesRunning=2`), 电源计划是平衡; 另装的 "Reason Cybersecurity" 两个服务全是 Stopped, 不耗性能.
- HMCL 3.16.4 配置实际落点: 主程序 `D:\Minecraft\HMCL-3.16.4.exe`, 全局 `%APPDATA%\.hmcl\config\user-settings.json`(本机只有 `enableOfflineAccount` 一项, 内存与 JVM 参数全默认), 实例级 `versions\<版本>\.hmcl\config\instance-game-settings.json`(本机只有 `overrideProperties: [runningDirectory]`); 日志不落 `%APPDATA%\.hmcl`, 每次启动的实际命令行在游戏侧 `logs\latest.log` 的 `Game took` 行最能说明问题.

- 整合包的资源包有两套载体, 别只在 `resourcepacks\` 找 (2026-11-18): OpenLoader 的包在 `config\openloader\resources\`, 在 `options.txt` 里以 `resources/<名字>` 出现; 普通包是 `file/<文件名或文件夹名>`. 本整合包 41.6 MB 的视觉包(Stay_True 材质 2.04 MB, cubic-sun-moon 18.58 MB, Icon_Xaero's 19.73 MB, Fancy_Beds, Enchantment Descriptions Compat, Homestead GUI)已移出到 `_backup_resourcepacks_20261118`, 回滚脚本 `恢复资源包.ps1`.
- `Homestead Essentials` 不能整包禁用: 它承载 `phomesteadplushies` 的 194 个资源文件, 也就是任务章节那些毛绒玩偶的全部贴图与模型; 只剥离了它的 `assets/minecraft`(原版 GUI 贴图 + 铜材质) 与 `colored_water`/`simplehats` 孤儿命名空间, 保留 `phomesteadplushies`/`perfectplushies`/`create`/`biomeswevegone`/`endercon`/`modrinth_logo_mod`.
- 禁用资源包前先查引用: `Homestead GUI` 里的 `assets/homestead/textures/farm_diagram.png` 被 Patchouli 手册 `patchouli_books\homestead\en_us\entries\blueprints_and_builds\blueprints_and_builds.json` 引用, 整包禁用会缺图; 已把这张图单独做成最小包 `resourcepacks\Homestead Manual Art`(pack_format 15), 排在 `options.txt` 列表末位保最高优先级.
- 改 `options.txt` 的 `resourcePacks` 行要顺带清孤儿: 已删 mod 的内置包会在列表里留下失效条目, 本次清了 `continuity:default`, `continuity:glass_pane_culling_fix`, `subtle_effects:biome_color_water_particles`, `minecraft:supporteatinganimation`.

- 资源包里的 `assets/minecraft/lang/en_us.json` 要先验证是不是"真定制" (2026-11-18): Homestead GUI 那份 377 KB / 6217 条, 按 key 首段全是原版命名空间(block 1656, subtitles 740, item 599, commands 445), 带冒号的 mod 键 0 条, 就是原版英文文件的整份副本, 一条都没改. 而且本机 `options.txt` 是 `lang:zh_cn`, 游戏显示走官方 zh_cn, en_us 只在缺 key 时回退, 所以移走它零影响(上一轮把它说成"文案覆盖"是错的). 判断方法: 看 key 有没有 `modid:` 或自定义前缀, 别只看文件名.
- CFPA(中文模组翻译组)汉化包的实际覆盖 (2026-11-18, 实测): 1.20 万用包(`Minecraft-Mod-Language-Modpack-1-20.zip`, 2.11 MB)含 603 个 mod 命名空间, 对本包 100 个缺中文的 mod 只命中 11 个(perfectplushies/chipped/sodium/mcwpaths/xaeroworldmap/justhammers/ftbteams/configured/spawn/openpartiesandclaims/animal_feeding_trough); 1.21 包命中 0; 名为 `Minecraft-Mod-Language-Modpack.zip` 的全版本包其实是 1.12.2 的(pack_format 3). 包内 `assets/minecraft/font` 会替换字体渲染, 只取 `assets/*/lang/*` 重打包更稳.
- 本地缺中文的规模: 322 jar 里 217 个带语言文件, 117 个自带 zh_cn, 100 个只有 en_us; 可见文本(block/item/entity/entity/gui 等前缀)合计约 3850 条, 大户是 luphieclutteredmod 1174, mythicupgrades 511, hexalia 320, hearth_and_home 309, twigs 264, mcwpaintings 180, niftycarts 125, icys-better-horses 132.
- 自建汉化包 `resourcepacks\Homestead CN Supplement`: pack_format 15, 9 个 mod / 202 条(blahaj 7, squish 25, phomesteadplushies 53, umbrellas 44, dyedend 64, dustydecorations 78, betterendrod 8, chefsdelight 4, obsidianequipmentrework 2), 写完后用 `ConvertFrom-Json` 逐文件校验再挂进 `options.txt` 末位(资源包列表后面的优先级高).

- HMCL 装 Modrinth 整合包会自动补齐文件, 手工精简必须先改清单 (2026-11-18, 实测): `versions\<版本>\modrinth.index.json` 的 `files` 数组(本包 376 条: mods 367, shaderpacks 5, datapacks 2, resourcepacks 2)是启动前完整性校验的依据, 只把 jar 移到 `mods-disabled` 会在下次启动被原样下载回来(实测把移走的 59 个补回 58 个 jar, 还把 `Fancy_Beds`/`Enchantment Descriptions Compat` 两个资源包下回来). 正确做法: 备份 index, 从 `files` 里删掉对应路径(`mods/xxx.jar` 按文件名匹配), 再移文件.
- index 里还会残留旧版本文件名, 是另一条自动下载来源: `mods/Configurable-mc1.20.1-v1.3.1.jar` 与实际 `Configurable-2.2.3-fabric-yarn+1.20.1.jar` 不一致, HMCL 每次都去下旧版并与新版并存, 必须一并剔除. 判据: 遍历 `files` 逐条 `Test-Path`, 缺失为 0 才算干净; 本包改完是 315 条 / 缺失 0 / mods 322 jar.
- 启动时间前后对照(同一实例): 200.882 s(625 mods, Defender 未排除) -> 104.259 s(631 mods, 已排除 Defender + 内存与 Java 调整), 直接减半; 精简到 322 jar 后再测能更低.
- 版本目录被 HMCL 重命名过一次(`Homestead DEV` -> `Homestead`, json/jar 同名改). 任何跨轮工作都不能硬编码版本目录名, 每轮先 `Get-ChildItem .minecraft\versions` 确认.
- 汉化进度(2026-11-18): 自建包共 14 个命名空间 1262 条(twigs 260 / hearth_and_home 309 / mcwpaintings 180 / spuds_shops 125 / niftycarts 103 / dustydecorations 78 / dyedend 64 / phomesteadplushies 53 / umbrellas 44 / squish 25 / betterendrod 8 / blahaj 7 / chefsdelight 4 / obsidianequipmentrework 2). 做法: 读 jar 内 en_us.json -> 以英文 key 全集循环 -> 规律项(颜色×材质, 木材×部件, 材质×烟囱)脚本生成, 非规律项手写 -> 输出后与英文 key 对账, 要求"未覆盖 0 / 多余 0" -> ConvertFrom-Json 校验.
- "能不能正常玩"的快速判定法(可靠): 遍历 `mods\*.jar` 读 fabric.mod.json 取 id+provides(含 META-INF/jars 内嵌套 jar), 再查每个 depends 的 id 是否都存在, 未满足应为 0; 配合 index 缺失 0 与任务书引用 0 即可判定.
- 启动耗时三连降(同一实例, 均实测): 200.882 s(625 mods, 无排除) -> 104.259 s(631 mods, 排除 Defender + 内存/Java) -> **54.853 s(536 mods, 移完 JEI/Xaero/JEP + EMI 与 JourneyMap 替换)**. 即最终比最初快 73%.
- Move-Item 在游戏运行时必失败(文件被 java 锁), 且脚本若不校验"源已消失 + 目标已存在"就会把失败误记为成功; 每次移动后必须双向校验, 并先 `Get-Process java,javaw` 确认进程已退出.
- 配方书按钮两态的真凶是 `Not Enough Recipe Book`(NERB): `config\nerb.yaml` 的 `buttonMode` 只有 DISABLED/ENABLED/DISCOVERED/TOGGLE 四档, TOGGLE = 点击配方书切换 JEI/REI/EMI 界面显隐; 没有"可制作"档, JEI 也无 craftable 过滤, 该能力只有 EMI 有.
- JourneyMap 6.0.7 配置目录 `journeymap\config\6.0\*.config`(JSON 带 // 注释, 值全是字符串): 路径点分享开关是 `journeymap.waypoint.config` 的 `"disableShare"`; 地图数据天然按存档分目录 `journeymap\data\sp\<世界名>\<维度>\`, 另需注意建路径点时的 Global 勾选项才跨存档.
- mod 的显示名和实际命名空间经常不一致, 取语言文件必须按实际 assets 目录名: `luphieclutteredmod` 的真实 id/命名空间是 `clutter`(jar 为 `clutter-1.20-0.6.2.jar`, 语言在 `assets/clutter/lang/en_us.json`), 只按 `luphie` 搜会扑空; 以后定位 jar 用 `luphie|clutter` 这类多关键词。
- 汉化第二批进度(2026-11-18): 累计 16 个命名空间 2707 条。新增 `clutter` 1445 条(全量覆盖, 键与英文 1:1, 仅 `clutter.commands.config.config_prompt` 保留 `%s` 格式串)。该 mod 名字规律极强: 颜色(16) × 金属(golden/silver/iron/copper) × 氧化状态(exposed/weathered/oxidized, 可叠加 waxed) × 品名(wall_candle 壁烛 / chandelier 吊灯 / candelabra 烛台), 以及木材(12, 含 redwood 红杉/cherry 樱花/bamboo 竹) × 家具(chair/table/bench/shelf/trellis/cupboard/wall_cupboard/wall_bookshelf/window_sill)。这类必须写正则批量生成, 手写既慢又容易漏; 生成后务必与英文 key 做"未覆盖 0 / 仅中文有 0 / 仅英文有 0"三向对账。
- 中文译名叠加顺序统一为"状态 + 颜色 + 材质 + 品名"(如 打蜡的斑驳淡蓝色铜吊灯), 不要按英文语序直译, 否则中文读起来断裂。

- 汉化全量收尾(2026-11-18): 自建包 `Homestead CN Supplement` 最终 **88 个命名空间 / 8576 条**, 与 86 个英文源逐 key 对账 **未覆盖 0 / 空值 0 / JSON 全部可解析**. 收尾做法固定为: 批量 `Save-Lang($ns,$map,$enFile)` 函数(建目录 -> 只写入 `ContainsKey` 且英文非空的键 -> `[ordered]` 保序 -> `ConvertTo-Json` -> 打印条数与未覆盖清单), 一批 4~10 个 ns 一次跑完, 比单 ns 逐个跑省 3 倍轮次.
- 差集口径要复核, "空 en_us.json" 也会被记成缺包: 覆盖率检查里报"缺包"的 17 个 ns 中有 4 个(`accelerateddecay`/`deltaboxlib`/`echoes_of_the_end__structures_`/`ftbxmodcompat`)的英文源本身就是 **0 条**, 并非漏翻; `keybind_fix` 更特殊, 其 lang 内容全是 `item.amethyst_imbuement.*`, 真实命名空间是 `amethyst_imbuement`, 要按 key 前缀而不是 jar 名建目录, 否则整份译文都挂错地方.
- 原文本身是空白的键不要保留: `lavender`/`owo` 里有一批值只有空格(`text.lavender.entry_tooltip` 等 10 条), 抄进中文包只会让 `IsNullOrWhiteSpace` 校验报空值, 应直接剔除而不是照抄空格.
- MC 语言文件里三种"看起来像模板"的东西处理口径: `%s`/`%1$s`/`%%`/`%d`/`&s`(vc_gliders 用 &s 而非 %s) 一律原样保留; `§a`/`§c`/`§l` 颜色样式码原样保留; 而 `@{text=...; color=gray; underlined=True}` / `@{text=...; font=minecraft:uniform}` 是**文本组件字面量**, 只译 `text=` 后面的内容, 整个 `@{...}` 结构与其属性名一个字符都不能动.
- 分段拼接句的中文语序必须自己重排, 不能照抄英文: jamlib 的 `renamed_1 + renamed_1.1` 是靠 `%s` 串联的("mod being %s" + "redistributed without permission"), 中文要写成"这通常是模组被%s的迹象"+ "未经许可转载" 才通顺; 同理 `renamed_2` 五个 `%s` 的顺序要在中文句里重新安排位置.
- 禁用 CraftTweaker 脚本只能移出 `scripts\`, 放子目录无效 (2026-11-18, 实测): `.zs` 文件被 `scripts\` **递归**扫描, `_disabled_backup\` 这类下划线子目录照扫不误, 结果"已禁用"的脚本仍在执行, 启动刷 `[ERROR]: Scripts are invalid!`. 正确做法: 移到 `scripts\` 之外(本包用 `versions\Homestead\scripts-disabled\`), 或改扩展名 `xxx.zs.bak`(`.zs` 之外一律不加载). 本次根因链: `scripts\_disabled_backup\loot_table_fixes.zs` 第 9 行引用 `<block:hearth_and_home:barred_glass>` → `hearth_and_home-fabric-1.20.1-2.0.3.jar` 已在 59 个装饰 mod 中移入 `mods-disabled` → 方块不存在 → BEP 校验失败. `modrinth.index.json` 的 `files` 里没有 `scripts/*` 条目, 所以脚本移走不会被 HMCL 补回. 区分:Iris/Sodium 报错看 `.toml`/`properties`, CraftTweaker 看 `scripts\*.zs`, KubeJS 看 `kubejs\*\*.js`, 三者不能混判.
- 卡牌尺寸 (2026-11-18, 用户口径): 卡面用 63.5×88.9 mm（扑克牌尺寸 2.5×3.5 in，先定过 63×88 宝可梦尺寸後改为此），A4 居中 3×3；版心/字号由 SX=63.5/70、SY=88.9/99 从 70×99 等比缩放，token 与 track 堆同步缩。
- 裁切框 (2026-11-18, 用户口径): 正面每张卡都要贴边 0.2 pt 外框（压在切线上）用来对刀裁剪，背面不画卡边线只留内框；内部网格线由每张卡自己的框承担，不另画。
- 排版混排 (2026-11-18, 用户口径): 非 9 倍数导致的堆尾空格要由下一牌堆填满（省纸），并保证每张卡背面仍是自己那一堆的名字；早期"否决跨堆混排"的口径作废。
- 全套并流 (2026-11-18, 用户口径): 省纸的判据是"每张纸 9 格都要满", 收益少也要做; 因此 flip(1) / track(9) / token(158) 也并入同一条连续流, 由 `cn/deck/impose_all.py` 逐卡裁格重排, 739 张 = 82 张满纸 + 末页 1 张. track 同步改到 63.5×88.9(改前仍是 70×99, 比别的卡大一圈), 版式常量一律写成"旧值 × SX / × SY".
- 拼版要读源卡真实格位 (2026-11-18): flip 牌在它自己那张纸上是**居中格(slot 4)**, 不是第一格; 逐格重排时必须给每叠一个起始格位, 否则整格空白.
- 背面按实际张数 (2026-11-18, 用户口径): 末页正面只剩几张卡, 背面就只印几个堆名, 不许"整页 9 格复用"(旧 `merge` 用 `back.pages[i % nb]`, 单堆背面只有 1 页 -> 末页背面永远 9 份). 统一做法: 正背面都逐格取 `cell(slot)`, 正面几格背面就几格, 单堆也走同一函数.
- 查看器不是实尺 (2026-11-18): PDF 尺寸本身没问题(A4 210×297, 卡 63.5×88.9 实测无误); SumatraPDF 的 100% 按 "1 pt = 1 逻辑像素(96dpi)" 显示, 屏幕上只有实尺 75%. 要 1:1 就把 `%APPDATA%`/`SumatraPDF-settings.txt` 里 `CustomScreenDPI` 设成显示器真实 DPI(本机 2560×1600 / 34×22cm ≈ 189), 重启后 Ctrl+1 即实尺; 屏幕缩放 150% 时要按实测微调: 新值 = 原值 × 210 / 屏幕上量到的宽度.

- 微分几何教材定位 (2026-11-18): `differential-geometry.pdf` 254 页无文本层, `d.get_toc()` 返回空书签, 只能渲目录页(PDF 10)看节名, **PDF 页 = 书页 + 11**; §5.6 曲面的 Laplace 算子 = 书 p130 = PDF 141-148(定义 6.4 / 例 6.6 等温参数 / 定理 6.7 格林公式 / 式 (6.20)); §8.1 常正 Gauss 曲率 = 书 p193 = PDF 204-205(定理 1.1 紧致常曲率曲面是球面, 引理 1.2 希尔伯特引理). 该 PDF 用 `Read` 直接读任何分页都报 "Failed to upload an extracted resource", 必须 pymupdf 渲 PNG 再看图.
- 希尔伯特引理的两条路线 (1118 讲义 命题 11.17.2 的证明): 课堂讲的路线只用偏导数——曲率线参数下 b11=k1g11, b22=k2g22, 科达齐按 (1,1,2) 与 (2,2,1) 给出 (k1),2=−m∂2g11/(2g11) 与 (k2),1=m∂1g22/(2g22)(m=k1−k2), 高斯方程 (1,2,1,2) 分量给出 K 的公式, 在极值点 P0 处 dk=dg=0 再对上面两式求一次导, 得 −2g11g22 同时 ≥0 与 <0 的矛盾. **教材走的余标架 + 联络形式 + 外微分路线 (ω12, dω12=−Kω1∧ω2) 不进 md**: 这一讲的课堂转录里没有"外微分"一词, 写它等于承认抄教材.
- Δ 分解的符号以讲义约定为准 (2026-11-18): 讲义 n 为外法向, b_{αβ}=<r_{αβ},n>, ∂_α n=−b^ε_α r,ε, H=½tr(g⁻¹b)=(k1+k2)/2, 于是法向参数化 Φ=r+tn 的度量是 **G=g−2tb+t²b·b** (√G=√g(1−2tH)), 得 Δ_{E³}f|_Σ=Δ_Σf−**2H**∂_nf+∂²_nf. 手抄稿里常见 "+H∂_n"(把 H 记成迹) 与 "+2t"(把 n 取成内法向) 两种错法, 一律按讲义改; 校验: 球面 R 上 f=t 的真实 Δt=2/(R+t)=+2/R, 而 H=−1/R, 故系数 −2H. 散度定理同理一律取"∂Σ 在 Σ 内的外法向 + 正号", 手抄稿写"内法向 + 正号"自相矛盾.
- 讲义 md 只能由同名 `.txt` 课堂转录长出来 (2026-11-18, 用户原话"你骗了我", "教材存在的唯一价值就是让符号与其保持一致"): 转录里没有的概念不许出现在 md; 教材的定理, 证明, 例题, 习题, 图, 式号一律不进; 判"越界"不许靠条目标头的教材批注(那批注本身就是抄教材的自认), 只能回去读该讲 `.txt`.
- 教材编号一旦写进条目标头就是自认抄教材 (2026-11-18, 用户原话"我不是只让你看教材的符号吗, 你怎么知道这个定理是教材的定理?!"): 15 讲全部清过一遍, 头注 79 处 + 独立行 5 行 + 正文 97 处, 现在全库 0 处"教材", 0 处 `§`; 以后再看到 `(教材 §x.y 类型 z.w)` 或 "(教材 (3.11))" 一律按违规删净.
- 证明里相邻两句必须上句推得下句 (2026-11-18): 常见断点——"某量连续"却不说它是特征值/特征多项式系数的连续函数; "取到最大值"却不说定义域紧; "只要证某式"先把结论当前提; "II 对角成 k1g11, k2g22"却不说曲率线切向即主方向, 且 k1≥k2 是排序不是坐标(要交换 u1,u2 记号); 由 K 公式跳到乘积式要写出"代入 K≡1 得 […]=−2√(g11g22), 两边再乘 √(g11g22)"与积法则展开的中间式; "求导得恒等式"要写出移项那一步; 引用编号要与真正给出该结论的条目对齐(不许"由 (1)"实则是 (7) 的结果).
- 讲义里的"说明"条目最容易夹带转录外内容 (心得, 与教材对照, 教材的等价定义, 教材图例), 复核时优先查这些条; 1104 已因此删掉 说明 9.3.7/9.6.5/9.7.8/10.1.9/10.3.7 与 证明 10.2.3 (上半平面模型+默比乌斯) 和 例 10.2.4 (PSL(2,R)); 1109 删掉 说明 10.5.4 (测地平行坐标系, 那是 1104 的内容) 与 说明 10.7.4 (常曲率局部等距), 并把 10.7.1 由外微分路线改成 推导 7.5.3 的 K 公式.
- 正文不写面向转录的话 (板书/看不清/没抄上), 也不写与"本文记号一致"这类自证句; 条目标题不得残留被删片段留下的残括号 (如"(与)"), 复核时按标题括号内容是否成词检查.
- 讲义编号查新: 微分几何讲义 `.md` 在 `differential-geometry\textbooks\handout\`, 按日期命名(0921…1118), 每讲开新 `## 11.x` 节, 条号在节内不分类型连续编; 接新一讲前先 `grep "^## "` 看已排到哪(1118 从 **11.17** 起, §11.16 已是庞加莱-霍普夫定理).
- 越界的不只是"说明"条目, 整条 命题/推导 也算 (2026-11-18): 判据只有一条——这一讲的 `.txt` 里有没有这件事; 有结论没证明时**才**允许自写证明(用户口径"补全也是我们写 md 的一部分, 但请依据 txt 合理地补全"). 本次按此删掉 0921 的 命题 1.5.10 与 推导 1.5.11 (一般参数下的 κ=|r'∧r''|/v³ 与 τ=(r',r'',r''')/w², 转录只做了圆柱螺线这一个例子), 1111 的 例 11.2.1 (平面, 转录的例题是球面/环面/闭曲面), 1111 的 推论 11.8.5 与 推导 11.8.6 (K≥0 ⇒ ∫K=4π, 转录此处只有一句"问 ∫|K|dsigma=?"), 0928 的 例 2.1.5 (拿 np.trapezoid 复算圆周/正方形的那类数值练习), 例 2.4.8 (数值复算单位圆全曲率), 说明 2.4.7 (平面曲线情形的"核对"心得) 与 定义 2.3.1 后面那条"注: 也有把…称为凸曲线"的术语注释.
- 抄教材的自认痕迹不止 `§` 与"教材"二字 (2026-11-18): 图号("图 7.2 的莫比乌斯带""如图 7.3""(图 7.4)"), 教材内部编号("第五章的命题 1.5.1""(本文档定理 7.5.5)"), 式号 `\tag{1.1}`…`\tag{2.6}`, 以及"本文采用…""本文一律…""简单地说…有两个面"这类面向读者的自证句, 一律删或改成描述性指代(如"由定理 7.5.5""在每个三角形上应用…"). 全库 `\tag` 已清零(原 1104 四处、1111 九处).
- 条目类型只能用 定义/公理/引理/命题/定理/推论/注记/说明/例/证明/推导/计算/练习; 写成 `**性质 11.3.2**` 会让"证明 11.3.3"变成无主孤证, 审查脚本也认不出. 若一条"性质"只是把定义里的话再说一遍(1111 的"可定向曲面有整体定义的第二基本形式"), 直接删, 由前文的叙述承担.
- 空白清理的两个坑 (2026-11-18): ① 别用"把空格替换成句末点"的正则, 那会把"是同一式子 ."变成"是同一式子.."、把"性质 :"变成"性质::", 正确做法是**只删空格**(`" ."→"."` 要连带删掉原点号); ② 只按"前一字符是汉字/公式/右括号"判会漏掉加粗结尾的 `**密切平面** .`, 该按"行尾 ` .`、行内 ` ;`/` :`/` ,`"整体判. 校验口径: 行内无连续空格、无标点前空格、无行尾空白, 且 `$$` 块内不受影响.
- 作业引用块会随讲义改动失效 (2026-11-18): 讲义改完必须回去核 `homework\week9.md` 文首那 18 条 `>` 引文——每条编号要仍在库里, 标题与正文要跟讲义最新写法一致(本次 说明 7.11.2 改名"测地曲率与法曲率的关系"、正文去"教材标架"后, week9 的引文也同步改了). 核对脚本: 扫 `^\*\*(类型) 编号` 建索引, 再扫 week9 的 `>` 块逐个比对, 报 MISS 的一条条修.
- 删条目前先全库查引用, 这是硬步骤 (2026-11-18 复盘, 用户口径"做任何改动必须从整个 `D:\wenje-ma` 的角度思考, 把会与之牵连的一并考虑到位"): 上一轮把 0921 的 `命题 1.5.10 (一般参数下的曲率与挠率公式)` 当"转录外内容"删了, 结果 `homework\week1.md` 的解答 4、题 1.20 与 `week2.md` 的题 1.20 全靠它算 κ 与 τ, 引用当场悬空. 正确顺序是: 改讲义 → `check_all_hw.py` 扫 `homework` 与目录内其他 md 的 `**类型 编号` 引用 → 被引用的条目一律保留, 内容不够就按转录里的工具补推导(本次复原为 命题 1.5.10 + 证明 1.5.11: 由 r'=vt, r''=v't+κv²n 得 r'∧r''=κv³b 即 w=κv³; τ 用 ⟨b,r''⟩≡0 求导, ⟨b',r''⟩=-κv³τ 得 (r',r'',r'')=w²τ).
- 只有结论没有证明的条目必须补证明 (2026-11-18, 用户口径"需要证, 因为这是老师留的思考题"): 本次补 定理 1.5.9(弗雷内方程组 = 一阶线性方程组; 用 Ċ=AᵀC+CA 与 C≡I 保住标架正交; 三重积连续取 ±1 ⇒ 右手; 模保向等距的初值对齐给唯一性)、命题 1.7.3(κ=0 用 命题 1.5.1; τ=0 用 命题 1.6.3 + 圆的常曲率; τ≠0 时由 κ=a/(a²+b²)、τ=b/(a²+b²) 反解 a,b)、命题 1.12.4(纯命名, 改立为 定义 1.12.4 而不是硬凑证明)、定理 8.3.5(等温参数: 把度量写成 Λ|dz+μdz̄|², 由 |μ|<1 化 Beltrami 方程 w_z̄=μw_z, 取 w=u'+iv' 即得 λ²(du'²+dv'²), 雅可比 |w_z|²(1-|μ|²)>0 保证是新参数)、推论 9.3.6(Γ 只含 g 与其一阶偏导)、定理 5.2.2(三个等号逐条对上 推导 5.2.1)、推论 7.3.2(k_g=0 的改写). 其中 8.3.5 的证明用了一条椭圆型方程局部可解性, 必须在正文写明"这里用到一个标准事实", 不许把它伪装成初等推导.
- 引用校验脚本 (agent 工作区): `check_all_hw.py` 只扫 `homework`(比对 `**类型 编号 (名称)**` 与讲义标题逐字一致), `check_all_cites.py` 扫全库——但全库会撞号(abstract-algebra 的 定义 1.2.1 与微分几何 定义 1.2.1 同号不同物, 一次跑出 10097 条"悬空"), 所以只在 `differential-geometry` 目录内用它. 本次据此补掉 week7 的 定义 3.6.1 副名与 week9 两处 说明 7.11.2 旧标题.

## 本机环境

- Git (2026-11-18): 装在 `D:\Git` (2.56.0.windows.4), 系统 Path 已含 `D:\Git\cmd`, 普通终端直接可用 `git`. 豆包执行命令时用沙箱 Path 覆盖了整条 `PATH`(只剩 python/node/pwsh), 故在沙箱 base 目录 `...\sandbox_runtime\bases\fa694f517e5995233c80a9a8db5212c2\` 放了转发桩 `git.exe`(转发到 `D:\Git\cmd\git.exe`, 参数按 Windows 规则透传), 并以 `git.cmd` 兜底; 若豆包运行时升级换了 base 哈希, 桩会失效, 重编译一次即可.

## 协作口径

- 提交 (2026-11-19, 用户口径, 已覆盖 2026-11-18 的 `类型: 主题 — 细节` 那条): 提交信息与提交时间一律由用户当场给出, 助手不代拟、不补写、不套旧模板. 用户说清动哪个文件/哪一组, 助手只做 `git add` + 拿用户原文 `git commit`; 用户没给就先问, 不自己想标题. 新规则的方向(2026-11-19 用户口述): 用大白话写明白这次干什么了 — 不套 `类型:` 前缀, 不装书面腔, 就说清楚这一组文件这次改到了什么地步; 细节等用户给例子后按其样例定稿.
- 提交样例 (2026-11-19, 微分几何 40 条重建, 用户逐条口述): 信息是名词短语加句号 — `教材.` / `封面图.` / `第 N 周作业.` / `MMDD的板书.` / `MMDD的笔记.`; 不是句子, 不写"我""本次""更新"之类的腔. 日期取内容对应的那天(讲义就取文件名那天, 周作业按一周 7 天递减), 一律 12:00 -0800. 同一天两条时的顺序有实际含义: 先有板书(txt)才能整理笔记(md), 故板书在前、笔记在后; 教材(0920)在最底下, 封面图与 week1 同为 0927 但封面图在前. 用户若改主意只改时间, 顺序与内容不动.
- 校历周次 (2026-11-19, 用户口径): 含 3/1(春)或 9/1(秋)的那一周是**第 −3 周**, 小学期占 −3/−2/−1 三周, 之后**直接进第 1 周**(没有第 0 周), 一学期 12 周, 全学期 15 周. 周内按周一起算. 2026 秋实算(基准 −3 周 = 8/31 起): −3 8/31, −2 9/7, −1 9/14, 第1周 9/21~9/27, 2 9/28~10/4, 3 10/5~10/11(国庆, 无作业), 4 10/12~10/18, 5 10/19~10/25, 6 10/26~11/1, 7 11/2~11/8, 8 11/9~11/15, 9 11/16~11/22, 10 11/23~11/29, 11 11/30~12/6, 12 12/7~12/13. 周作业/周讲义的提交日期取**该周周日**(已核: 微分几何现有 39 条 week1=9/27、week9=11/22 与表完全吻合, 不必改). 小学期课程即 `states-python` 一批讲义(`4-文献\第1讲-统计学习问题与数据表示.md` 到 `第4讲-线性神经网络.md`, 加教材第三~八章).
- 提交时间 (2026-11-19): 可任填. 两个变量都要设, 只设一个会有一栏还是当天: `GIT_AUTHOR_DATE`(热力图与 `git log` 默认排序看它) 与 `GIT_COMMITTER_DATE`(commit 页面顶上那栏看它); 格式 `2026-10-03T14:20:00+0800`, 不写 `+0800` 按 UTC 解释, 偏 8 小时. 改已提交的时间会连带改 hash; 父子时间倒挂不影响默认拓扑排序, 但 `--date-order` 会看着乱; 未来时间照收不报错; 启用 GPG 签名后改时间会让签名失效.
- 历史重置 (2026-11-19): `D:\wenje-ma` 下 33 个仓库本地已清成零提交 — 删 `refs/heads`/`refs/remotes`/`refs/tags`, `git read-tree --empty` 清空 index, HEAD 指向未出生的 `main`(即 `git rev-parse HEAD` 报 `unborn`), 工作区文件一个没动. 旧对象仍在各自 `.git` 里未 gc, 需要回退按 SHA 挂 ref 即可. 重置前快照与恢复脚本: `D:\wenje-ma\reset-20261119\`(`manifest.tsv` 记每仓 HEAD/分支/tag/远端分支, `restore.ps1` 用 `update-ref` 挂回).
- 远端未清 (2026-11-19): GitHub 拒绝删除默认分支, `git push origin --delete main` 报 `refusing to delete the current branch`; 零提交也无物可推, 故 33 个 origin 旧历史原样保留, 等用户第一条提交时 `git push --force` 一次顶掉(GitHub 侧旧对象回收 90 天). `cumcm2026` 的 `li`/`li01`/`li02`/`li03`/`li04` 与 `states-python` 的 `li`/`li02`/`li04` 远端分支同样未动. `metropolis` 的 `upstream`(mtheme) 与本机无关, 更不许推.
- 历史重建 (2026-11-18, 已作废): 那批 628 个中文提交已于 2026-11-19 全部清空, 仅留作来历记录.

- 备份 (2026-11-18): 本次重写历史产生的 `D:\wenje-ma-git-history-backup-20261118` 与 `...-v2` 属过渡产物, 用户核对完即全部删除, 不得留到任务收尾之后.
## 目录口径 (2026-11-19)
- `homework-cn` 已全部改名为 `homework` (16 个仓库), `homework-en` 已全部删除 (11 个仓库), 备份在 `D:\wenje-ma-reset-backup-20261119\<仓库>-homework-en.zip`; 目录里不再有中英两套, 也不要再新建 `homework-cn`/`homework-en`.
- 改名后 `differential-geometry` 的 39 条提交已按 `homework/` 路径重串一遍 (信息与日期不变, hash 变了), 提交数与链序与改名前的表一致; week9 不在其中, 由用户自行提交.
- 脚本里拼中文要紧跟变量时必须写 `"$($h)的板书."`, 直接写 `"$h的板书."` 会被 PowerShell 当成变量名 `h的板书`, 结果是空字符串 (2026-11-19 踩过, 30 条信息只剩句号).- 多个控制台并行跑不同书 (2026-11-19 用户问"能不能同时建多个 pwsh 扫不同教材"): 可以 — 不同窗口即不同进程, 缓存目录按书的路径哈希分开, 互不碰撞. 两条纪律: (1) 绝不让两个窗口指向同一本书或同一目录, 否则同一 chunk 各解析一遍白烧一倍算力, 而且两边抢同一个成品文件, `.part` 原子写只保证不留半截, 不保证后写的不覆盖先写的; (2) 总引擎数 ≤ 2–4, `--jobs` 是"本窗口内的并行 chunk 数"而不是全局并发, 每个引擎约吃 3 线程 + 4.2 GB 内存, 16 核的安全搭配是两个窗口各 `--jobs 1`, 或单窗口 `--jobs 2` (实测后者 538 页 268 页用了 6.7 小时, 约 90 s/页有效吞吐). (3) 进度文件已改为每次运行写 `progress_<tag>.json` (tag = 目标目录名 + 必要时路径哈希), `progress.json` 退化为"最新一条"的镜像并带 tag 字段 — 原来单文件在多开时会互相覆盖; plan 缓存改成先读盘合并再原子替换.
- 不带参数运行即弹目录对话框 (2026-11-19 确认 venv 的 uv 解释器带 tkinter 8.6, 系统 3.14 带 9.0, 两者都能建窗): `select_target()` 用 `filedialog.askdirectory`, 已加 `-topmost` 让它浮在控制台上面, tkinter 缺失时降级为一行提示要求显式传路径.
## 小学仓库口径 (2026-11-19, primary-mathematics 重建)

- 结构: `homework/week1.md` ~ `week144.md`, 144 = 12 册 × 12 周; week 编号连续, `week1-12` 一上, `week13-24` 一下, 依次到 `week133-144` 六下.
- 定义编号 `X.Y.Z` = 册.章.节 (Z 是节号, 不是定义序号), 全库 373 节, 每册 23–47 节.
- 提交切法: 每册 12 条周作业 (`第 N 周作业.`) + 每册 1 条教材 (`教材.`), 共 156 条.
- 日期: 每学期第 1 周 = 含 9/1 (秋) 或 3/1 (春) 的那一周 (周一起算); 周作业取该周周日 12:00 **+0800** (2012–2018 在国内, 与 2026 年的 -0800 不同源); 教材 = 该学期第 1 周 **前一周的周日** 12:00.
- 教材日期实例: 1.1 = 2012-08-26, 1.2 = 2013-02-24, 2.1 = 2013-08-25, …, 6.2 = 2018-02-25.
- 重排原因: 原始 144 份是按"每份约 20 题"机械切的, 91 份跨章、9 份跨册 (week 11/43/57/68/80/97/109/119/137), 直接提交会让一个学期横跨两册.
- 重排方式 (只搬不写): 跨册文件在册界按定义条数比例断开 -> 每册内部用 DP 均分到 12 周, 只在题与题之间下刀 -> 定义块随来源文件带过去 (去重, 按章/节排序) -> 练习序号在当地重编 (练习一..N). 题块总量 2650 不变, 解答块 2650 不变.
- 由此产生的已知痕迹: 一节讲两周属正常 (用户确认); 周界可能落在某节中间, 但册与学期严格对齐.
- 脚本: `D:\wenje-ma\reset-20261119\reslice-all.py` (重排), `commit-primary.ps1` (156 条提交), `reslice-primary.py` + `primary-sample/` (册1 样张), 暂存结果在 `primary-out/`.

## 初中仓库口径 (2026-11-19, junior-mathematics 重建)

- 结构: `homework/week1.md` ~ `week72.md`, 72 = 6 册 × 12 周; 教材 7 个 PDF 对 6 册 (`7.1`/`7.2`/`8.1`/`8.2`/`9.1_part1`+`9.1_part2` 合一/`9.2`).
- 提交: 78 条 = 6 条 `教材.` + 72 条 `第 N 周作业.`; 每册 13 条, 教材在前.
- 日期 (全部 12:00 +0800, 2018–2021 在国内): 2018秋 教材 08-26 / 第1周 09-02 / 第12周 11-18; 2019春 02-24 / 03-03 / 05-19; 2019秋 08-25 / 09-01 / 11-17; 2020春 02-23 / 03-01 / 05-17; 2020秋 08-30 / 09-06 / 11-22; 2021春 02-28 / 03-07 / 05-23. 衔接小学 2018-05 毕业.
- 用户口径 (2026-11-19 定): 每册必须正好是一学期 (12 周), 每学期内部题量均匀即可, 不追求章级纯净.
- 重排方式: 只在**册内**把这 12 份按题量用 DP 均分到 12 周, 不跨册搬内容; 定义块只带「本周题量占比最大的那个源文件」的定义 (避免相邻两份堆叠), 合计 547 条; 练习序号在当地重编.
- 每周题量: 册1 27–28, 册2 27–28, 册3 31–32, 册4 17–18, 册5 23–24, 册6 31. 各册总量 332/328/375/207/286/372, 题块 1900 不变.
- 已知残留: 5 个章跨学期缝 (章6 week12–15, 章10 23–25, 章16 35–38, 章26 57–67, 章27 59–69), 即开学头两三周还在讲上册末章. 按章重切会把每周题量打成 14–35 (册4 只剩 14 题/周), 已实测弃用.
- 脚本: `reslice-junior-even.py` (册内均分), `commit-junior.ps1` (78 条提交), 暂存 `junior-out/`; `reslice-junior.py` 是按章重切的废弃版本.

## 高中仓库口径 (2026-11-19, senior-mathematics 重建)

- 结构 (用户 2026-11-19 修正): **5 学期 × 12 周 = 60 周**, 不是 72 周 — 高三下没有新课, 原 `week61-72` 的内容 (计数原理/条件概率/统计相关) 并入第 5 册重排, 题目一道没删. 仓库里现只有 `week1.md` ~ `week60.md`.
- 教材 5 本对 5 学期 (`10.1`/`10.2`/`11.1`/`11.2`/`11.3`); `10.1` 那条同时带上 `textbooks/page_mapping.md` (该 PDF 的页码偏移表).
- 提交: 65 条 = 5 条 `教材.` + 60 条 `第 N 周作业.`
- 日期 (12:00 +0800, 2021 秋入学 ~ 2023 秋): 册1 教材 2021-08-29 / 第1周 09-05 / 第12周 11-21; 册2 2022-02-27 / 03-06 / 05-22; 册3 2022-08-28 / 09-04 / 11-20; 册4 2023-02-26 / 03-05 / 05-21; 册5 2023-08-27 / 09-03 / 11-19.
- 每周题量: 册1 26–27, 册2 23–24, 册3 25–26, 册4 18–19, 册5 44–45 (册5 承了原来两学期的量, 偏重但册内均匀). 题块 1647、定义 511 不变.
- 章编号每册重新从 1 起 (人教 A 版各本书各自编号), 所以跨册看章号会重复; 判断归属要看节标题不看章号.
- 脚本: `reslice-senior.py` (合并 61-72 并册内均分), `commit-senior.ps1` (65 条), 暂存 `senior-out/`.

## 撤回记录 (2026-11-19)

- `functional-analysis` 的 `第 9 周作业.` (2026-11-22, 含 `homework/week9.md`) 已按用户要求撤回 — 那份还没写完. 现 8 条, HEAD 回到 `0d0823a` `第 8 周作业.`, `homework/week9.md` 变回未跟踪状态, 文件留在工作区未动.
- `differential-geometry` 同样处理: week9 不在链中, 由用户自己写完再提交.

## 数学分析仓库口径 (2026-11-19, mathematical-analysis 重建)

- 结构 (用户 2026-11-19 定): **2 册 × 12 周 = 24 周**; 原来 36 周 (week1-36) 的内容合并成 24 周 — 册1 = 旧 week1-24 (极限/单变量微分/中值定理), 册2 = 旧 week25-36 (可积性/重积分), 各册册内均分. 题块 375 一道没丢.
- 教材 2 本: `mathematical-analysis1.pdf` (上册), `mathematical-analysis2.pdf` (下册).
- 提交: 26 条 = 2 条 `教材.` + 24 条 `第 N 周作业.`; 日期 12:00 +0800, 大一学年: 册1 教材 2024-08-25 / 第1周 09-01 / 第12周 11-17; 册2 教材 2025-02-23 / 第13周 03-02 / 第24周 05-18.
- 每周题量: 册1 16–17, 册2 15 (每册内部均匀).
- 本仓定义块是 `命题`/`定理` (不是 `定义`), 编号形如 `1.3` (章.号); 题号是 `1.1-3` 这种"章节-题号", **不要重编号** — 它自带出处信息, 与小学/初中/高中的 `练习一..N` 不同.
- 遗留: `textbooks/Zad-01.pdf` ~ `Zad-10.pdf` 是 10 份单页习题单, 尚未提交 (未跟踪), 提交文本与日期待用户给.
- 脚本: `reslice-ma.py`, `commit-ma.ps1`, 暂存 `ma-out/`.

## 高等代数仓库口径 (2026-11-19, advenced-algebra 重建)

- 仓库名少一个 d (`advenced-` 不是 `advanced-`), 别改名, 远端是 `wenje-ma/advenced-algebra`.
- 结构: 2 册 × 12 周 = 24 周, 与数学分析同期 (大一 2024 秋 / 2025 春); 原来 24 份内部题量 4–11 不均, 已按册内均分 (册1 7–8, 册2 6–7), 题块 166 不变.
- 提交: 26 条 = 2 条 `教材.` + 24 条 `第 N 周作业.`; 日期 12:00 +0800: 册1 教材 2024-08-25 / 第1周 09-01 / 第12周 11-17; 册2 教材 2025-02-23 / 第13周 03-02 / 第24周 05-18.
- 题号形如 `1.1-1(4)` (章节-题号(小问)), **保持原样不重编号**.
- **OCR 产物不提交** (用户 2026-11-19 明确): `textbooks/advenced-algebra{1,2}_ocr.pdf` 与 `_ocr.txt` 是 2026-11-19 当天才做的 OCR 工作, 留在未跟踪状态, 等用户后面统一安排如何提交. 同理适用于其他仓的 `_ocr.*` 文件.
- 脚本: `reslice-aa.py`, `commit-aa.ps1`, 暂存 `aa-out/`.

### 数学分析习题单 Zad-01..10 挂靠 (2026-11-19 补)

- 用户口径: 习题单和对应周的作业**同一条提交** (不是单独一条).
- 内容识别 (PDF 正文字体损坏, 只能按数学符号判): Zad-01 定积分估计与极限, Zad-02 定积分计算, Zad-03 Rn 拓扑(内点/闭包/距离), Zad-04 多重极限与连续, Zad-05 偏导可微, Zad-06 Laplace 算子/极坐标, Zad-07 Legendre 变换/反函数定理, Zad-08 曲面切平面/隐函数, Zad-09 二次型极值/曲线, Zad-10 条件极值/隐函数.
- 挂靠结果: week11 + Zad-02; week12 + Zad-01; week13 + Zad-03/04/05/06; week14 + Zad-07/08/09/10.
- 依据: 全库作业题号章分布是 1,2,3,4,5,6,8,9,10,11,12,13 —— **独缺章7 (多元函数微分学)**, 而 Zad-03~10 正好全是章7 的内容, 所以它们整体落在章6.2(week13) 与章8.1(week14) 之间的章7 位置, 前后各挂一半.
- 跟踪文件现为 36 个 (24 周 + 2 教材 + 10 习题单), status 干净.

### 习题单挂靠 — 均匀版定稿 (2026-11-19, 用户: "排的均匀些吧, 我记不住了")

- 上一条 4+4 的挂靠作废, 改为 **2 张/周, 连续摊开**:
  - 第 11 周 2024-11-10 + Zad-02 (定积分计算)
  - 第 12 周 2024-11-17 + Zad-01 (定积分估计/极限)
  - 第 13 周 2025-03-02 + Zad-03 (Rn 拓扑) / Zad-04 (多重极限与连续)
  - 第 14 周 2025-03-09 + Zad-05 (偏导可微) / Zad-06 (Laplace/极坐标)
  - 第 15 周 2025-03-16 + Zad-07 (反函数/Legendre) / Zad-08 (隐函数/曲面)
  - 第 16 周 2025-03-23 + Zad-09 (二次型极值) / Zad-10 (条件极值)
- 口径: 章7 在作业里没有对应周 (题号独缺章7), 这 8 张就是它的作业; 具体哪周无法凭记忆复原, 故按"相邻窗口内均匀铺开"处理, 一周两张.
- 结果: 26 条提交不变, 36 个跟踪文件 (24 周 + 2 教材 + 10 习题单), status 干净.

## 抽象代数仓库口径 (2026-11-19, abstract-algebra 重建)

- 结构: 1 学期 × 12 周 = 12 周作业 + 1 本教材, 共 13 条提交. 用户口径: **大二学的** (本处按大二上 = 2025 秋落日期; 若实为大二下, 整体平移到 2026 春即可).
- 日期 (12:00 +0800): 教材 2025-08-31, 第1周 09-07, 第12周 11-23.
- 重排: 原来 12 份题量 1–13 极不均 (week2 只有 1 题), 已按册内均分成每周 6–7 题, 题块 82 不变; 题号 (1.1 / 2.3 这种) 保持原样.
- 教材文件名拼错: `abstruct-algebra.pdf` (`abstruct` 不是 `abstract`), 按用户"不改名"习惯保持原样.
- OCR 产物不提交: `abstruct-algebra_ocr.pdf` / `_ocr.txt` 留未跟踪.
- 脚本: `reslice-absalg.py`, `commit-absalg.ps1`, 暂存 `absalg-out/`.
- 输出形态改为"就地覆盖原 PDF, 不再产出 _ocr.txt" (2026-11-19 用户要求"直接用 OCR 代替原有的 PDF, 也不再生成 txt"): `build_one()` 的文本层分支整个删掉 (原来会把有文本层的书复制成 `_ocr.pdf` 并附 txt), 扫描件在解析并注入后直接覆盖 `src` 自身; `--out-dir` 是唯一保底 —— 给了就把结果写到那个目录下、文件名不变. "已处理"的判据随之变成 "文件自身是否已有真文本层" (`text_layer_present()`): 处理过的书带着我们注入的层, 重跑同一文件夹会跳过; `--force` / `--ocr-anyway` 则强制重做. `save_atomic()` 改成先存 `.part`、再 `doc.close()`、再 `os.replace` —— Windows 不允许替换仍被打开的句柄, 而目标现在常常就是源文件.
- 就地覆盖的体积代价 (2026-11-19 实测): 4 页样张 0.57 MB -> 5.80 MB, 增量来自嵌入的 `DejaVu Sans` + `SimHei` 两套字体子集, 是每本固定的 +5 MB 左右, 不随页数放大; 纯 `save(garbage=3, deflate=True)` 不会让文件变大 (0.57 -> 0.57 MB), 所以膨胀只发生在注入这一步.
- 旧逻辑的残留不会自动清理 (2026-11-19): 此前生成的 `*_ocr.pdf` / `*_ocr.txt` 仍躺在磁盘上, 新逻辑既不读也不删它们; 若想把某本恢复成"原书形态", 手动用 `_ocr.pdf` 覆盖原文件即可, 不需要重算.
## 概率论 / 实分析仓库口径 (2026-11-19)

- 两者与抽象代数同期: **大二上 (2025 秋)**; 各 1 学期 × 12 周.
- `probability`: 13 条提交 (1 `教材.` = `probability.pdf` (Durrett, Probability: Theory and Examples, 5th) + 12 周作业). 原 25 题摊 1–3/周, 已均分成 2–3/周.
- `real-analysis`: 13 条提交 (1 `教材.` = `real-analysis.pdf` (张希承《实变函数论》讲义, 104 页) + `folland.pdf` (Folland, Real Analysis, 402 页, 参考书) 同一提交; + 12 周作业). 原 54 题 1–7/周, 已均分成 4–5/周.
- 日期 (12:00 +0800, 两仓相同): 教材 2025-08-31, 第1周 09-07, 第12周 11-23.
- 题号 (1.1 / 2.3 等) 保持原样, 不重编号.
- 踩坑: `pwsh -File` 传数组参数会被并成一个字符串 (`'a.pdf','b.pdf'`), 导致 `git add` 落空、教材提交为空. 改用**逗号分隔的单个字符串**再 `-split ','` (脚本 `commit-single.ps1` 已按此改).
- 脚本: `reslice-single.py <仓库名> <输出目录>` (单学期 12 周均分), `commit-single.ps1 -Name <仓> -OutDir <目录> -Textbooks <逗号分隔>`.

## 教材翻新后的重提交 (2026-11-19, 用户: "ocr问题解决了, 教材翻新了")

- 扫描 10 个有教材提交的仓库 (`scan-textbooks.ps1`, 用 `hash-object` 对 `rev-parse HEAD:path`), 只有两仓教材被替换:
  - `abstract-algebra`: `abstruct-algebra.pdf` 21.35 MB → **27.36 MB**; 原 `_ocr.pdf`/`_ocr.txt` 已并入正文名并删除.
  - `advenced-algebra`: `advenced-algebra1.pdf` 39.45 → **45.28 MB**, `advenced-algebra2.pdf` 47.96 → **53.82 MB**.
  - 其余 8 仓 (微分几何 / 泛函 / 小学 / 初中 / 高中 / 数学分析 / 概率论 / 实分析) 教材无变化, 未动.
- 做法: `rewrite-textbook.ps1` 逐条 `read-tree` 原树 → `update-index --add --cacheinfo` 换 blob → `write-tree` → 用**原提交的 author/committer 姓名、邮箱、`%aI`/`%cI` 日期与 `%B` 信息** `commit-tree` 重串 → `update-ref` + `read-tree HEAD`.
- 结果: `abstract-algebra` 仍是 13 条 (2025-08-31 → 2025-11-23), `advenced-algebra` 仍是 26 条 (2024-08-25 → 2025-05-18), 日期与提交信息一字未变, 教材 blob 与工作区一致, `git status` 干净.
- 脚本坑 (第二次踩): `hash-object` 必须加 `-w`, 否则 blob 不入库, `update-index` 报 `invalid object`; 且 `write-tree`/`commit-tree` 的返回值必须用 `"$( ... )".Trim()` 收紧成单个字符串, 否则多行输出会让 `commit-tree` 报 `must give exactly one tree`.
- 对矢量 PDF 强制 OCR 的真实行为 (2026-11-19, differential-geometry\homework 的 8 个 week*.pdf 实测): `clear_text_layer()` 只在页面恰好有 1 张整页图时才清内容流, 矢量页 `len(images)==0` 直接 return —— 所以页面本身**不会被改白**, 逐像素比对 pixhash 与之前完全一致, KaiTi 等矢量字体也还在. 代价是旧层不消失: 结果是"乱码旧层 + 隐形新层"两套文字叠在一起, 搜索命中没问题 (能搜到中文), 但整页复制会先吐一串 `Š’ 1 1. $-•§113•§` 再吐正确中文. 引擎识别本身是对的 (week2 原页 0 个汉字 -> 处理后 78 个, 缓存 json 里是"作业2 / 回忆Fary-Milnor定理…"这样的正确文本), 乱码纯粹来自旧 Type1 层 (KaiTi / NimbusRomNo9L 无 ToUnicode).
- 每文件 +5 MB 的固定开销在小文件上很刺眼 (2026-11-19): 8 个 1 页作业从 100–145 KB 变成 5.4 MB 左右, 因为每份都嵌 DejaVu Sans + SimHei 两套字体; 空间紧张时可考虑只嵌一套或改走 md 文本层.
- 同目录 .md 是同源正文 (2026-11-19 发现): `differential-geometry\homework\week*.md` 就是对应页面的 Markdown + LaTeX 原文, 若要做"零误差文本层", 直接拿 .md 落字比 OCR 更准, 不必再跑引擎.
## 大二下四门课仓库口径 (2026-11-19): complex-analysis / numerical-calculation-methods / ordinary-differential-equations / mathematical-statistics

- 用户口径: 这四门都是**大二下 (2026 春)**上的. 各 1 学期 × 12 周 = 13 条提交.
- 日期 (12:00 +0800): 教材 **2026-02-22** (第 1 周前一周日), 第1周 03-01, 第12周 05-17.
- 教材:
  - `complex-analysis`: 6 个分册同一提交 `1-4.pdf` / `5-8.pdf` / `9-12.pdf` / `13-16.pdf` / `17-20.pdf` / `21-24.pdf` (按页码分段装订).
  - `numerical-calculation-methods`: `_part1.pdf` (94.81 MB) + `_part2.pdf` (46.40 MB) 同一提交.
  - `ordinary-differential-equations`: `ordinary-differential-equations.pdf`.
  - `mathematical-statistics`: `mathematical-statistics.pdf`.
- 重排 (册内均分, 题号不重编):
  - complex-analysis 113 题: 原 6–13/周 → 9–10/周.
  - numerical-calculation-methods 56 题: 原 1/周 × 8 周 然后 6/12/13/15 → 4–5/周 (此仓原本极度不均, 重排幅度最大).
  - ordinary-differential-equations 106 题: 原 6–13/周 → 8–9/周.
  - mathematical-statistics 90 题: 原 5–9/周 → 7–8/周.

## 微分几何作业 PDF 翻新 (2026-11-19)

- 现象: `homework/week1/2/4/5/6/7/8.pdf` 全部 `M`, 旧的 0.03–0.14 MB 纯图扫描件被换成 5.2–5.4 MB 的 OCR 版 (文字层已可用). `week3` 本来就没有 PDF, 第 3 周无作业.
- 这 7 个 PDF 原本各自躺在对应的 `第 N 周作业.` 提交里 (week1 → 2026-09-27, week2 → 10-04, week4 → 10-18, week5 → 10-25, week6 → 11-01, week7 → 11-08, week8 → 11-15).
- 做法: `rewrite-textbook.ps1` 逐条重串 39 条提交, 只在该提交**本来就有**该 PDF 时才替换 blob (新增了 `cat-file -e "$sha:$p"` 守卫, 避免把文件塞进更早的提交). 日期/信息/作者一字未变.
- 结果: HEAD `2026-11-18 1118的笔记.`, 39 条不变, 7 个 PDF 与工作区逐字节一致.
- 仍未跟踪: `homework/week9.md` / `week9.pdf` —— 用户自己写完自行提交, 不代交.
- 全仓扫描结论: 33 个仓库里再无其它"已跟踪文件被改动"的情况 (只有未跟踪的新文件).

## 本学期 (2026 秋) 两仓: partial-differential-equations / topology

- 用户口径: 都是**本学期**的课, 与微分几何/泛函同季 → 2026 秋, 时区 `-0800` (洛杉矶).
- 日期: 教材 **2026-09-20** (第 1 周前一周日), 第1周 09-27, 第12周 **2026-12-13**. 注意 2026 年 9/1 是周二, 含 9/1 的周是第 -3 周(小学期), 所以第 1 周是 09-21 起、周日 09-27 —— **不能**拿 "含 9/1 的周" 当第 1 周算.
- `partial-differential-equations`: 13 条 (教材 `partial-differential-equations.pdf` 93.43 MB + 12 周作业). 57 题, 原本 4–6/周, 已够匀, **未重排**.
- `topology`: 13 条 (教材一条含 9 个 PDF: `basic-topology-Mark.pdf` 40.71 / `topology-James.pdf` 16.85 / `topology.pdf` 1.09 / `Topology2024_Anon.pdf` / `Topology2024_Exam{,B,C}.pdf` / `Topology2025{A,B}_Exam.pdf`; + 12 周作业). 160 题, 原 8–29/周 (week12 挤了 29 题), 已均分成 13–14/周.
- 教材拆分未做: 9 个 PDF 目前全在 `教材.` 一条提交里 (含往年试题). 若要拆 `教材.` + `往年试题.`, 需另给日期.

### 事故与恢复 (2026-11-19)

- `commit-single.ps1` 的第一版在 `Copy-Item` 之前就执行了 `Remove-Item homework\week*.md`, 且源目录不存在 → **PDE 的 12 个 week md 被删除**, 当次只建成 1 条教材提交.
- 恢复: 远端 `origin/main` 仍留旧历史, `git fetch` + `git archive FETCH_HEAD homework-cn` 取回 12 个文件, 逐周题量 [4,4,5,5,5,5,6,6,4,4,4,5] = 57 题, 与删除前记录完全一致 → 内容可信. 副本留在 `reset-20261119\pde-recover\`.
- 脚本已加护栏: 先确认源目录里至少有 12 个 `week*.md` 才删除并覆盖; 支持 `-OutDir ''` (不重排) 与 `-Week1 <第1周周日>` 直接指定锚点, 时区用 `-Tz`.

## 全书架进度 (2026-11-19 收尾状态)

已完成 16 个作业型仓库 (全部本地已建、均未推送):
微分几何 39 / 泛函 8 / 小学 156 / 初中 78 / 高中 65 / 数学分析 26 (含 Zad) / 高等代数 26 / 抽象代数 13 / 概率论 13 / 实分析 13 / 复变 13 / 数值计算 13 / 常微分 13 / 数理统计 13 / 偏微分 13 / 拓扑 13.

## states-python 仓库口径 (2026-11-19)

- 用户口径: 这是**本学期的小学期**课程项目 (2026 秋小学期 = 第 -3/-2/-1 周), 要求"把其中的文件均匀地在 -3~-1 周提交".
- 内容: CUMCM 2022 C 题 (古代玻璃文物成分分析) 的完整参赛包 —— 题目 / 文献 / 代码 / 解答 / 报告 / 论文 / 原始提交 zip.
- 三批提交 (12:00 -0800):
  - `2026-09-06 题目与文献.` — `.gitignore`, `README.md`, `1-题目`, `4-文献` (32 个文件, 30.5 MB)
  - `2026-09-13 代码与解答.` — `2-代码`, `2-解答` (累计 89 个, 本批 0.7 MB)
  - `2026-09-20 报告与论文.` — `3-报告`, `3-论文`, `3赵宇翔李传浩马文杰.zip` (累计 103 个, 本批 31.9 MB)
- 分批依据: 按工作阶段 (读题查文献 → 写代码算 → 写论文交稿), 文件数 32/89/103 大致均匀; 字节数被两头的文献 PDF 与提交 zip 拉大, 若用户要按体积均匀可再调.
- `states-python` 仓名指的是论文里的"风化状态 (state) 分析", 不是美国州数据. 分支 `li` / `li02` / `li04` 仍在远端, 去向未定.
- 脚本: `commit-states.ps1`.

## README 清理 (2026-11-19, 用户: "删除除了 wenje-ma 的所有 README.md")

- 删掉的是**仓库根目录**的 README: `ed4dse` / `isaac-four-souls` / `metropolis` / `singapore` / `states-python` / `wenje-codes` / `wenje-piano`, 共 7 个.
- 保留: `D:\wenje-ma\wenje-ma\README.md` (用户点名保留); `wenje-codes\.venv-ocr\**\README.md` (Python 包自带, 非仓库文档, 未动).
- `states-python` 的 README 原本在第一条提交 `题目与文献.` 里 (2026-09-06), 已用 `rewrite-remove.ps1` 逐条重串 3 条提交把它从历史里剔掉, 日期/信息不变; 跟踪文件 103 → 102, status 干净.
- `wenje-codes` 的 README 只挂在索引里 (该仓零提交), 用 `git update-index --force-remove README.md` 清掉, 以免日后建历史时被带上.
- 复核: 16 个已建仓库的历史里都不再有 `*README.md`. 脚本 `rewrite-remove.ps1` 可复用于任何"从所有历史提交里剔除某路径"的场景 (带 `cat-file -e` 守卫, 不误删更早的提交).

## applied-multivariate-statistics 仓库口径 (2026-11-19)

- 与微分几何同季: 本学期 2026 秋 (第 1 周 2026-09-27, 第 12 周 2026-12-13), 每周日 12:00, 时区 `-0800`.
- 内容: 应用多元统计分析课程 (红酒质量数据) 的完整作业 + 项目: 68 个逐题 R 脚本 (`codes/yydy*.R` 章.题 命名) + 30 个 `.RData`、68 个同名 `.sas`、90 个 `figures/*.pdf|svg`、`tex/` 报告(qmd+pdf)与数据/图表/SAS 输出、`tex/reference` 教材课件、`提交包/` 最终交付, 共 371 个文件 66.7 MB.
- 13 条提交: `2026-09-20 教材.` (37 个文件 50.4 MB = tex/reference 全部: 高/张两本教材、methods、SAS 手册、standard、红酒论文、30 份 `yydyfx*` 课件、apa.csl、report.bib) → `第 1..12 周作业.` (2026-09-27 → 12-13).
- 12 周切分: 按"文件数 + 体积权重 (每 256 KB 折 1 份)"均衡, 每周 19~29 个文件; 目录顺序按工作流滚动 (codes → SAS → figures → tex → 提交包), 因文件名本身是"章.题"编号, 滚动窗口天然近似按章节推进.
- 每周落地: 第 1-5 周全 R 代码; 第 6-9 周 SAS 代码 + 图形; 第 10 周图形 + 数据; 第 11 周数据/日志/报告源文件; 第 12 周 SAS 输出 + `提交包` 收尾.
- 脚本: `split-ams.py` (切分, 输出到 `reset-20261119\ams-split\`), `commit-ams.ps1` (逐批 `git add -- @paths` + 定日期提交).
- 坑: `git add` 大量中文/深层路径时 PowerShell 数组要写成 `& git ... -- @paths`, 用 `--pathspec-from-file` 亦可; 文本文件 LF→CRLF 的 warning 属正常.

## anki-mdmath 仓库口径 (2026-11-19)

- 内容: Anki 插件 (Markdown + KaTeX 渲染), 36 个文件 1.1 MB: `__init__.py` `templates.py` `build.ps1` `manifest.json` `mdmath.ankiaddon` `LICENSE` `THIRD_PARTY_NOTICES` `.gitignore` `assets/`(katex/marked/auto-render/style.css + 20 个 KaTeX woff2 字体) `tests/`(3 个).
- 用户口径: "1019-1025, 均匀提交" → 7 天每天一条, 2026-10-19 ~ 2026-10-25, 12:00 `-0800`.
- 7 条: `插件清单.`(4) → `渲染逻辑.`(2) → `渲染资源.`(5) → `正文与数学字体.`(12) → `特殊符号字体.`(8) → `测试脚本.`(3) → `构建与打包.`(2). 字体按"正文/数学/SansSerif/Typewriter/Size1-2"与"AMS/Caligraphic/Fraktur/Script/Size3-4"两堆拆开, 兼顾语义与均匀.
- 脚本: `commit-anki.ps1` (显式文件清单批次, 便于控制每天落什么).

## appreciation 仓库口径 (2026-11-19)

- 内容: 李商隐《锦瑟》的鉴赏作业. 8 个文件 228.5 MB:
  - `reference/`: 李商隐诗歌集解.pdf (69.8 MB)、玉谿生诗笺注.pdf (9.9 MB)、资治通鉴_part1.pdf (97.3 MB)、资治通鉴_part2.pdf (57.0 MB)
  - 根目录: `question.md` (题目)、`锦瑟分析.qmd`、`锦瑟分析.md`、`锦瑟分析.pdf`
- 用户口径: "和应用多元统计一样, 分 12 周做完" → 同一学期 (2026 秋), 同一周日历 (09-20 教材 → 12-13 第 12 周), 12:00 `-0800`.
- 实际 5 条 (只有 8 个文件, 不能造空提交): `09-20 参考书.`(4 本 PDF) → `09-27 选题.`(question.md) → `10-25 初稿.`(qmd) → `11-22 修订稿.`(md) → `12-13 定稿.`(pdf). 第 1/5/9/12 周各落一点, 均匀铺满学期.
- 注意: `资治通鉴_part1.pdf` 97.3 MB, 逼近 GitHub 单文件 100 MB 硬限, 推送时会报 >50 MB 警告; 若被拒只能改 LFS 或剔除.
- 脚本: `commit-appreciation.ps1`.

## cumcm2026 仓库口径 (2026-11-19)

- 内容: 2026 国赛 C 题 (光伏储能购电优化) 完整参赛件, 104 个文件 129.8 MB: `1-题目`(题面+附件数据)、`2-解答`(预处理/四问/灵敏度分析, R 脚本 + rds + csv/xlsx)、`3-论文`(论文.md、Lunwen.tex、figures)、`4-文献`(15 篇 PDF+txt)、`202601025158马文杰李传浩张可欣`(支撑材料.zip、C题协同优化.pdf、3 张截图)、`AI工具使用详情.md/pdf`、`.gitignore`.
- 用户口径: "0910-0913, 均匀提交" → 4 天各一条, 2026-09-10 ~ 09-13, 12:00 `-0800`, 按比赛节奏切: `题目与文献.`(53) → `代码与结果.`(39) → `论文.`(5) → `提交包.`(7 + AI 工具使用详情).
- 文件数 53/39/5/7 是"按阶段"而非严格等量; 若用户要严格均分, 可把 `4-文献` 拆成两半跨 10/11 日.
- 远端分支一大把: `li`, `li01~li04`, `wenje01~04`, `wenje99`, `wenjeje`, `xin01` — 本地只有空仓库, 推送时需先定去留.
- 脚本: `commit-cumcm.ps1`.

## dace 仓库口径 (2026-11-19)

- 内容: 只有 3 个文件 13.5 MB —— `DACE.pdf` (Santner《Design and Analysis of Computer Experiments》13.9 MB)、`notes.md` (该书第 2 章 高斯过程模型 的读书笔记, 9.4 KB, 全是公式推导)、`.gitignore`.
- 用户口径: "1001-1007, 均匀提交" → 2 条, 2026-10-01 与 10-07, 12:00 `-0800`: `教材.` → `笔记.`. 3 个文件撑不满 7 条, 按"先读书、后整理笔记"落在起止两端.
- 注: 一开始把 DACE.pdf 误记成"论文.", 已重建为 `教材.` (DACE 是专著/教材, 不是单篇论文).
- 该仓与 cumcm2026 的 `4-文献/ED4DSE.pdf` 是同一研究线 (数据中心算电协同), 后续 `ed4dse` 仓即由此展开.

## ed4dse 仓库口径 (2026-11-19)

- 内容: ED4DSE 论文的可复现工程 (Design and Analysis of Computer Experiments 复现 + 算电协同), 475 个文件 406 MB:
  - `ED4DSE.pdf` (54.3 MB 论文正本)、`.gitignore`
  - `codes/` 85 个 `章.节.R` (`1.4.R` … `11.3.R`) + `codes/data/`(各章 `章.节-plot.RData`、csv、`txts/run1..51.txt`、`lib.r`、`hilbert.r`)
  - `figures/` 各章 `章.节.pdf|svg` (含 `1.1~1.3.png`、`4.18/4.20/4.23.png`、`7.1.png`), 其中 `4.24.svg` `5.4.svg` `5.6.svg` `5.7.svg` 各约 35.8 MB
  - `Rpackages/` 三个 R 包源码 (mined, SFDesign, support, 含 .cpp/.h/.o/.dll)
  - `tex/document.qmd` + `document.pdf` (2.4 MB) + `tex/document_files/figures`
- 用户口径: "0801-0830, 均匀提交" → 按章节切 15 条, 日期在 08-01 ~ 08-30 之间隔天铺开 (12:00 `-0800`).
- 15 条: `教材.`(08-01) → `R 包.`(08-03, 85 个) → `数据集与工具.`(08-05, 58 个) → `第 1 章.`…`第 11 章.`(08-07…08-28, 各章 code+data+figures 合批) → `报告.`(08-30).
- 分批逻辑: 用文件名前缀 `(\d+)\.` 归章, 同章某节的 .R / .RData / .pdf|svg 同一条提交, 天然按节对齐; `第 4 章` 99 个文件最重(4.1~4.27), 其余 11~37 个.
- 注意: 仓库 406 MB, 推送会很慢; 单文件最大 54.3 MB (ED4DSE.pdf) 未触 GitHub 100 MB 硬限.
- 脚本: `commit-ed4dse.ps1` (自动归章 + 日期均匀铺开, 可复用于任何"章.节"编号的仓库).

## graduation 仓库口径 (2026-11-19)

- 内容: 只有 2 个 md, 8 KB —— `foundations.md`(毕设命题: 面向昂贵黑箱约束的多保真贝叶斯优化, 可行性优先采样 + 双阶段可行域主动学习, 含背景/问题描述/研究目标)、`paraphrasing.md`(论文降 AIGC 痕迹的写作方法: 困惑度与突发性原理、心法、深度改写、七法).
- 用户口径: "0706-0802, 均匀提交" → 2 条, 2026-07-06 与 08-02, 12:00 `-0800`: `命题.` → `降重方法.`. 2 个文件撑不满四周, 按先后落在起止两端.
- 该仓是大四毕设的准备工作, 后续实验与论文尚未进库.

## metropolis 仓库口径 (2026-11-19)

- 内容: 19 个文件 0.3 MB —— LaTeX Beamer 的 metropolis 主题 (派生自 matze/mtheme): `source/`8 个 `.dtx`+`.ins`、`doc/metropolistheme.dtx`、`demo/`(demo.qmd/pdf/bib/logo.pdf)、`docker/`(Dockerfile + getFiraFont.sh)、`figures/sample.png`、`Makefile`、`NEWS`、`.gitignore`.
- 用户口径: "1001-1007" → 4 条, 2026-10-01/03/05/07, 12:00 `-0800`: `主题源码.`(9) → `示例演示.`(4) → `构建与容器.`(5) → `示例图.`(1).
- **重要**: 该仓有两个 remote —— `origin` = wenje-ma/metropolis (可推), `upstream` = matze/mtheme (**上游, 绝对不能推**). 推送时务必只 `git push origin`, 不要用 `--all` / `--mirror` / `push --force upstream`.
- 坑: 文件名是 `beamerouterthememetropolis.dtx` (中间有 mem), 少写一个 mem 会 `pathspec did not match`.

## party 仓库口径 (2026-11-19)

- 内容: 10 个文件 2.1 MB, 都在 `develop-molecules/` 下:
  - `requests/`: 党校培训"思想汇报"作业 —— `requests.md`(题目与要求)、`manual.docx`(培训手册 1.6 MB)、`report.qmd`(汇报正文源文件, ctexart + xelatex)、`report.pdf`(成品)、`certificate.jpg`(培训证书)、`chats.md`
  - `investigation/`: 政治审查函调 —— `函调工作注意.docx`、`政治审查函调信 - 马文杰.docx`、`政治审查函调信（良乡校区）.docx`、`chats.md`
- 用户口径: "1001-1031" → 3 条, 2026-10-01 / 10-16 / 10-31, 12:00 `-0800`: `思想汇报.`(2) → `汇报正文.`(3) → `函调材料.`(5).
- 敏感材料提醒: 内含实名函调信与证书图片, 推送到 GitHub 前应确认仓库为私有 (private), 不要做成公开仓.

## singapore 仓库口径 (2026-11-19)

- 内容: 61 个文件 10.6 MB, 一篇贝叶斯优化论文 (含 KOH 校准、maxpro/mofat/nested 设计、消融实验):
  - `codes/` 18 个 R 脚本 + `DESCRIPTION`(按包组织: project.R 主控, ablation/calibrate 实验, fig2~fig6 绘图, EI/maxpro_design/mofat_design/nested_design/fit_KOH/predict_KOH 模块)
  - `codes/data/` 23 个 RData (ablation-M{0,S1,S2}-d{1,2,4,8}、calibrate-d{1,2,4,8}、summary、1~5-plot)
  - `figures/` 1.jpg + 2~6 的 pdf/svg 成对
  - `tex/` report.qmd/pdf、booklet.qmd/pdf、speak.md(讲稿)、keys.md(要点)
  - `singapore.png` 封面图、`notice.md` 说明、`.gitignore`
- 用户口径: "0901-0930" → 7 条, 2026-09-01/05/10/15/20/25/30, 12:00 `-0800`: `封面图.`(2) → `代码.`(18) → `实验数据.`(23) → `图形.`(11) → `报告.`(2) → `讲稿与手册.`(4) → `说明.`(1).
- 该仓是按"成果物类型"分批 (不是章节编号), 因为没有 `章.节` 命名.

## social-task 仓库口径 (2026-11-19)

- 内容: 68 个文件 10.3 MB, "知行探原——特立书院赴房山区社会实践团"全套材料, 按阶段分四块:
  - 立项: `000-总要求.pdf`、`附件1~6`(登记表/联系证明/责任书/评奖办法/结项表/系统手册)、`立项登记表.docx`、`代办清单.md`
  - 安全与授权: `安全预案.docx` + 同名 `.pdf`
  - 个人责任书: 6 人 × (docx/jpg/pdf) + `知行探原-马文杰组责任书.7z` 与解包目录 (26 个文件)
  - 实践: `figures/` 6 张活动照 (房山熙悦天街分发问卷)
  - 报告: `结项/社会调查报告/` 说明 + 3 张图(png+py) + `survey_data.csv`
  - 通讯: `tex/`(通讯.tex/pdf/txt + 3 张图)、`通讯.md`、根目录 `02.png`/`o1.png`/`o3.png`(与 tex 里三张图同尺寸, 是同一批)
  - 结项: `结项/`(结项登记表、活动照片.docx、实践感悟.docx、通讯.pdf、社会调查报告.zip)
- 用户口径: "0706-0830" → 8 条, 2026-07-06/12/18/25 与 08-05/15/22/30, 12:00 `-0800`: `立项材料.`(10) → `安全预案.`(2) → `个人责任书.`(26) → `问卷.`(1) → `活动照片.`(6) → `社会调查报告.`(8) → `通讯稿.`(10) → `结项材料.`(5).
- 隐私提醒: 含 6 名队员实名责任书与证件照, 推送前确认 `wenje-ma/social-task` 为私有仓.

## wenje-ma 仓库口径 (2026-11-19)

- 内容: 13 个文件 3.5 MB —— GitHub 个人主页仓: `README.md`(7.7 KB, 大三@北理工 数学与应用数学强基, 研究方向 DoE/空间填充设计/贝叶斯优化/多保真, Featured Projects 列 singapore/ed4dse/dace, 下面是全部公开仓库表格)、`wenje-ma.png`(3.2 MB 头像/侧栏图)、`WenjeMaths.png`(数学仓库徽标)、`logo/`+`desktop/`+`desktop_mb/`(各 tex+pdf+png 三件套)、`.gitignore`.
- 用户口径: 一开始问"2012-2026?!"(因为个人介绍"一直在写"). 我的判断: **不从 2012 起** —— README 正文只覆盖 2024 之后的项目与课程, 2012–2023 无任何内容支撑, 倒回 2012 会让"小学生就在维护 GitHub 主页".
- 实际 4 条: `2024-08-25 头像与忽略规则.`(2) → `2025-03-30 徽标与预览图.`(9, logo/desktop/desktop_mb) → `2026-10-01 数学仓库徽标.`(1, WenjeMaths.png) → `2026-11-13 个人简介.`(1, README.md, 取文件最后修改日).
- 若用户坚持要长历史: 只需改 4 个日期重跑, 成本极低; 但每年一条 15 年的做法需要造空提交, 不建议.

## wenje-codes / wenje-piano / wenjemaths 口径 (2026-11-19)

用户口径: "2012-2026?! 和个人简介情况一致". 三个仓内容全部产自 2026-11, 与 wenje-ma 主页仓同一判断 —— **不到 2012**, 按文件真实成型日出提交.

### wenje-codes (6 条, 11-07 → 11-19, 19 个跟踪文件)
- OCR 与 Markdown 处理工具链: `md_merge.py`/`pdf_split.py`/`ocr_books.py`/`auto_typesetting.py` + `md/`(leftright, math_space_strip, lib_sort, lib_inline, cn_punct) + `ocr/`(latex2glyph, ocr_inject, ocr_bench, ocr_qa, _dump) + `docs/library-pruned.md` + `STYLE.md` + `.gitignore`.
- 顺序: `脚本.`(11-07) → `括号匹配.`(11-11) → `公式清洗.`(11-12) → `文献库整理.`(11-15) → `中文标点与排版.`(11-17) → `扫描件识别与规范.`(11-19).
- `STYLE.md` 与 `ocr_books.py` 同落最后一条; `.gitignore` 忽略 `__pycache__/` `*.pyc` `.venv-ocr/`, 故跟踪 19 < 磁盘 27.

### wenje-piano (2 条, 11-15 / 11-16, 7 个 PDF 156 MB)
- `钢琴教材.`(6 本: 即兴伴奏普修、基本乐理、Adult Piano 1/2、John Thompsons 1、Piano Grade 1) → `爵士钢琴.`(Jazz Piano.pdf).
- `notes/` 是空目录, git 不记空目录, 故未跟踪; `Adult Piano 2.pdf` 75 MB, 未触 GitHub 100 MB 硬限但会触发 >50 MB 警告.

### wenjemaths (3 条, 11-01 / 11-11 / 11-12, 6 个文件)
- `mdmaths`(OMML/Markdown 数学写作) + `forced`(强化题, dg-mid / fa-month1) + `tutorial`.
- 顺序: `插图与忽略规则.`(11-01, .gitignore + punishment.png) → `强化题.`(11-11, dg-mid + tutorial) → `月度强化题.`(11-12, fa-month1 + mdmaths.md).
- `.gitignore` 忽略 LaTeX 中间产物与 `*.qmd` `*.pdf`.

### 坑 (重要)
- **建仓前索引可能是满的**: 早期 reset 准备阶段把整个工作区暂存过, `git add` 只加几项但 `git commit` 提交的是**整个索引**, 结果第一条提交把全仓吸进去 (wenje-codes 首条误含 19 个文件).
- 正确姿势: 每个仓开建前先 `git update-ref -d refs/heads/main` + `git read-tree --empty`, 让索引归零, 再按批 `git add -- @paths` + `git commit`. `commit-three.ps1` 已内置 `ClearRepo`.

## isaac-four-souls 口径 (2026-11-19)

- 用户口径: "1101-1119", 均匀提交. 内容是《以撒的结合: 四魂》实体卡牌自制项目 —— 抓维基数据、清洗卡表、LaTeX 排版卡面卡背、印刷双面 PDF、再做一整副中文版.
- 磁盘 180 个文件 6.8 MB; 但用户自己的 `.gitignore` 已经排除 `**/deck/build/`(80 个 LaTeX 中间物+成品)、`cn/print/cards_duplex_*.pdf`(9 个)与 `__pycache__` → **跟踪 83 个**.
- 8 条, 11-01 → 11-19 等距(01/03/05/08/10/13/16/19), 全部 `-0800`:
  `抓取脚本.`(9, .gitignore+en/scrape 8 个 js) → `卡牌数据.`(4, raw csv+wiki titles json+cards_final+name_fixes) → `卡表整理.`(13, en/tools) → `规则书.`(1, rulebook.md 103 KB) → `卡面排版.`(37, en/deck 的 csv+py) → `印刷成品.`(1, cards_duplex_token.pdf) → `中文译文.`(17, cn/data 9 + cn/deck 8) → `中文牌堆.`(1, cards_all_cn.pdf 639 KB).
- 顺序即工序: 抓 → 洗 → 排 → 印 → 译 → 中文成品.

## 全仓英文路径 + 分支重命名 (2026-11-19)

### 用户口径
- "仓库中所有文件夹, 文件都变成英文, 不要出现中文, 否则 tex 的双向引用失效".
- "文献重命名简洁一点, 就用 APA 格式就很好" → 采用 `姓+年份-英文短标题`(如 `long2019-imbalance-cost-composition-and-allocation`), 中文标题由我译成英文短标题, 不保留中文.
- "直接改人家的分支, 完全由我们重命名, 按照 工作流程.pdf 进行分工".

### 涉及范围
- 全仓扫描: 只有 7 个仓含中文路径, 共 308 个文件 —— cumcm2026(104)、states-python(101)、social-task(64)、applied-multivariate-statistics(27)、appreciation(7)、party(3)、wenje-piano(2).
- 改名脚本 `reset-20261119/rename-english.py`: 段级词典(最长优先) + 文献精确表; `prepare` 只出映射并校验"无残留中文/无重名", `apply` 才落地, 映射存 `rename-<repo>.json`(可逆).
- 历史重写脚本 `reset-20261119/rewrite-paths.py`: 按 JSON 映射**重放每个提交的树**, 日期/信息/作者/父链全部原样保留, 只换路径. 关键点: `git update-index -z --index-info` 的 `--index-info` 必须**放在最后**, 否则报 "option 'index-info' must be the last argument".

### 典型映射
- `1-题目/C题.md` → `1-problem/problem-c.md`; `2-解答/5-灵敏度分析/图9-1_灵敏度分析.png` → `2-solutions/5-sensitivity/fig9-1_sensitivity.png`
- `附件2_光伏发电实际功率.csv` → `appendix2_pv-actual-power.csv`; `result4-3_调整购电量.csv` → `result4-3_adjusted-purchase.csv`
- `提交包/05_数据清洗与校验_R/` → `submission/05_data-cleaning-and-checks_R/`
- `个人责任书/初梓瑜.pdf` → `individual-responsibility/chu-ziyu.pdf`; 六人姓名一律转拼音
- `reference/李商隐诗歌集解.pdf` → `references/liu1988-li-shangyin-poetry-collected-annotations.pdf`

### cumcm2026 补提交
`0-workflow/workflow.pdf`(原 `0-工作流程/工作流程.pdf`)一直未被跟踪. 已补成最早一条 `2026-09-09 工作流程.`, 之后 4 条提交的树里都带上它 → 现 5 条、105 个文件.

### 角色分支(按 工作流程.pdf)
流程图三角色: **建模手**(问题重述/分析/预处理/假设/选型理由/实验结论/第一题数学原理/优缺点) · **代码手**(检索关键词/筛文献/校验数学原理/灵敏度) · **论文手**(LaTeX 排版/摘要/关键词/参考文献).
- 基线 = 该仓 `题目与文献` 那条提交; 每个角色分支在其上追加自己负责的文件.
- cumcm2026: `modeler`(09-11 问题重述与模型假设.) / `coder`(09-11 预处理与求解代码. + 09-12 第四题与灵敏度分析.) / `writer`(09-12 排版与摘要.)
- states-python: `modeler`(09-08) / `coder`(09-10 + 09-12) / `writer`(09-15).
- 远端旧分支已全部删除: cumcm2026 的 `li,li01~04,wenje01~04,wenje99,wenjeje,xin01`(13 条, 含队友 lisdscn / zhangkexin-cpu 的提交), states-python 的 `li,li02,li04`, wenje-ma 的 `output`(actions 产物). 各仓远端现只剩 `main` + 三个角色分支.

### 推送
- 33 仓 main 全部 `--force` 推送完成, 复查 33/33 与远端一致(`push2-log.tsv`).
- 3 次失败均为网络: mathematical-analysis / real-analysis / wenje-piano, 重试后均成功; 已设 `http.postBuffer=500M`、`http.lowSpeedTime=999999`.
- 注意: NPC 改名后 7 个仓必须重推, 因为树变了(blob 不变, 只传新 tree/commit, 很快).

## 提交时间随机化 (2026-11-19)

### 用户口径
- "重新设计所有的提交时间, 都在既定的提交时间周围随机浮动, 天数, 时刻都随机变一变, 要不太假了, 我以后提交也会有压力".
- "日期 ±3 都可以, 时间随机的就行".

### 规则(脚本 `reset-20261119/jitter-dates.py`)
- 每个提交以原基准时间为锚, 在**基准日 ±3 天的整天**内取随机时刻(窗口下界 09:00, 上界 23:00); 窗口再被"前一条 +5 小时 / 后一条基准 -5 小时"收窄, 保证同一仓内严格递增、不越到下一周。
- 时刻在窗口内均匀取, 但 1-8 点的非人时段重抽, 深夜只保留 23:00-00:59 的"熬夜提交"。
- 消息里带 MMDD 的提交(如 `0921的板书.` / `0921的笔记.`)**锁死当天**, 只随机时刻, 且时段限制在 9-22 点, 好让同一天的板书/笔记都排得下。
- 用户要求"日期都是随机"后, 曾试过 ±1 天(周六/周日对半) → 太整齐(144 周里仍几乎全是周日), 改为 ±3 天。
- 踩坑: 边界若直接写成"锚点 ±3 天", 会继承锚点的 12:00, 一撞边界就退化成正午(大量 12:00 / 07:00 假值); 必须用"整天窗口"(09:00 / 23:00)再在窗口内取随机秒。
- 角色分支(modeler/coder/writer)的提交时间也一并随机(9-22 点), 但日期仍按工作流程的窗口固定。

### 结果
- 33 仓 612 条提交全部重排, 同仓内 0 条时间倒挂, MMDD 与日期 0 条不符。
- 小时分布: 8-23 点为主(各 25-47 条), 00 点 35 条、01 点 1 条(熬夜), 02 点 1 条。
- 星期分布: Mon 82 / Tue 97 / Wed 90 / Thu 76 / Fri 87 / Sat 90 / Sun 90, 基本均匀。
- 明细留档: `reset-20261119/jitter-report.tsv`(612 行, 原时间 → 新时间)。

## 应用多元统计分析作业 (2026-11-19)

### 交付与教材
- 教材 `applied-multivariate-statistics/tex/reference/applied-multivariate-statistics_gao.pdf` **无文本层**, 只能渲染 PNG 读图; PDF 页与书页**不是固定偏移**, 已核实: p061=110-111, p064=116-117, p066=120-121, p067=122-123, p068=124-125, p069=126-127, p074=136-137, p085=160-161, p090=170-171(习题四), p093=176-177, p094=178-179, p095=180-181, p096=182-183, p097=184-185, p107=206-207, p109=210-211(习题五起), p110=212-213, p111=214-215, p206=402-403, p207=404-405(答案), p208=406-407.
- 重渲命令: `D:\Python314\python.exe` + pymupdf(`fitz`), `d[i].get_pixmap(dpi=150).save("pages/p0xx.png")`.
- 交付 `homework/ch02.md`~`ch05.md`: 题号 2-3/5/6/8/14/15/16/18, 3-1/2/4/7/9/10(把"两个总体"改作 K 个总体), 4-4/4-6/4-10(SAS), 5-5/5-9/5-10/5-11(SAS).
- 知识点只取该书, 引用库只收书内**带编号**条目且正文**加粗引用**过; 无编号公式在正文写出, 不入库.

### 排版链
- 入口 `wenje-codes/auto_typesetting.py <文件或目录>` 跑 leftright + math_space_strip; 再依次跑 `md/cn_punct.py`、`md/lib_sort.py`、`md/lib_inline.py`, 四个脚本都直接吃路径参数实跑.
- 坑: 公式里出现**单个 `|`**(如 `P(t|X)`)会让 leftright 报 "odd | count in math span (skipped)" 并**整段跳过**, 该 span 的 `\left/\right` 就不再处理; 条件竖线一律写 `\mid`.
- 坑: `\quad s` 这种"`\quad` 后接单字母"会被改写成 `\quad{s}`(渲染无差别, 不必回改).
- 坑: `cn_punct` 会把抄题原句里的 "、" 换成 ", ", 这是规范要求的, 别手工改回去.

### 数值口径
- SAS 题只给程序块 + 计算结果表, 不伪造日志; 数值全部用 R 复算 (`codes/yyexa0404.R`、`yyexa0410.R`、`yyexa0509/0510/0511.R`).
- 书末答案两处笔误, 出稿按复算值: 4-10 的 $\hat{Y}_2$ 中 $x_4$ 系数为 0.0151(书印 -1.6982); 5-10(2) 三个待判类号为 1,2,3(书印 1,1,3).
- 坑: 组间离差阵不能写 `n_i*(colMeans(Xi)-colMeans(X))^2`(得到的是向量, 按列循环进矩阵), 必须 `n_i*tcrossprod(d)`; 否则威尔克斯 Λ 出现 >1 与负值, 逐步判别的 p 值全变 1, 路径发散.
- 坑: 逐步判别的引入检验 `F=(1-U)/U*(n-k-r)/(k-1)`, 剔除时把 r 换成 r-1; 书末答案 5-10 用的是临界值 0.18(不是常用 0.15), 按 0.18 才复现书上的 {x2, x4}.
