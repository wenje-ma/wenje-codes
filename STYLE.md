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
- 以下一律不加粗: 标量; 集合与空间名(`K`,`A`,`E`,`\mathbb{R}^n`,`GL(n,\mathbb{R})`); 映射, 函数, 算子(即使在 `L(E,F)` 里, 也含路径与曲线 `\gamma`); 抽象赋范/拓扑向量空间与序列空间 `E`,`F`,`l^p`,`l^\infty`,`C([0,1])` 里的元素(按抽象点处理, 不逐个加粗); 元素分量 `v_i` 与矩阵元 `T_{ij}`; 点对与元组 `\left(x,y\right)`,`\left(u,v\right)`.`
- 巨型定界符一个都不许出现: `\big`, `\Big`, `\bigg`, `\Bigg` 连同 `l`/`r`/`m` 变体, 一律换成 `\left`/`\right`, 后者按内容自动取高, 更灵活. 三种写法: 成对的括号与竖线 `\big( ... \big)` → `\left( ... \right)`; 带下标的取值竖线 `f\big|_{x=0}` → `\left.f\right|_{x=0}`; 二元斜杠 `\frac{a}{b}\Big/\frac{c}{d}` → `\frac{a}{b}\left/\frac{c}{d}\right.`. 配对按整段一条栈算, 配不上只报 Warning 不改.
- 尖括号只在 `<` 紧接字母时才危险: `<x` 会被渲染器当成标签开头, 把后文吞掉, 由 `math_space_strip.py` 统一改写成 `<{}x`; `<\命令`(`<\alpha`, `<\left`)与 `>` 后接字母都安全, 不必处理. 因此不再给 `<>` 补空格: 补空格会把真正的 `<div>`/`<br>`, 自动链接 `<https://...>` 劈成非标签, 还会把 `<=`/`>=`/`<<`/`>>` 劈成两个半角符号分开的两截, 干这事的 `space_gt.py` 已删除. 正文(公式外)出现 `<字母` 时写进行内代码, 不写裸的 `<script>`.
- 公式里的 `>{}`(`$x>{}y$`)是旧 `space_gt.py` 留下的等值余噪, 已全库清除(868 处 / 213 个文件); 只有 `<{}x` 是该留的, 别再产出 `>{}`.

## 文档写作

- 抄写原题; 解答中任意相邻两句都能由上一句推出, 不跳步.
- 数学作业集文首引用库只收书内带编号条目, 正文引用须加粗条目名. 先写解答, 解答里用到哪条就把哪条抄到文首: 解答没加粗引用的条目一律不写, 不论与本周末章多相关.
- 文首引用库的排列一律按序号升序; 序号相同的, 按 定义 > 公理 > 引理 > 命题 > 定理 > 推论 > 注记 排(其余类型如 例, 性质, 公式, 结论, 习题 与中英对照的 判定定理, 基本结论 一并排在列出类型之后); 没有序号可排的条目(数学活动, 综合与实践, 只以名字出现的条目)排在库末, 内部保持原相对次序. 全部 homework 文稿的中英两版都适用. 工具:`D:\wenje-ma\wenje-codes\lib_sort.py`, 幂等, 先 `--dry-run` 看改动数再实跑.
- 教材里的任何文字——定义, 定理, 公式, 例题, 习题结论——都可作为现成结论直接引用使用, 不在解答中重新推导; 只交代它为何用得上, 不重算一遍.
- 证明按子结论收尾: 一题里有几个独立结论(必要性/充分性, 上界/下界, 各小问), 就各标一次 `$\blacksquare$`, 不等到全题结束才标一次, 末尾也不补第三次. 此条适用于全部泛函作业, 老周次一并回改.
- `$\blacksquare$` 单独占位, 不与别的记号挤在同一行: 证明以句子收尾时接在句末, 以行间公式收尾时单独成一段, 公式那一行不留 `\qquad\blacksquare` 这类填充.
- 一切学科的整理文档里, 加粗只用于引用编号条目, 步骤标签等不加粗.
- 正文只写题目与推导, 不写依据说明, 心得, 旁注; 正文里不出现 `>` 引用块(引用块只用于文首条目库).
- 英文人名一律改中文译名, 不保留英文原名.
- 笔记与教材不符处, 悄悄按教材改掉, 不写差异说明.
- 微分几何: 文首公式条目内附来历推导; 正文不重复推导, 也不另加骨架小节.

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
- 空格只在正文补: 终止符后, 开括号前, 闭括号或闭引号后接中文时各补一个; 标点前不留空格. 公式内部一律不补.
- 代码块, 行内代码与 `.tex` 的 `%` 注释不动; 那里出现中文标点不算违规.
- 工具:`D:\wenje-ma\wenje-codes\cn_punct.py`, 幂等, 先 `--dry-run` 看改动数再实跑.

## 编辑器

- LaTeX 的 PDF 不留在 VSCode 标签里看, 一律外置 `D:\SumatraPDF\SumatraPDF.exe`. `settings.json`: `latex-workshop.view.pdf.viewer` 为 `external`, `...external.viewer.command` 指 SumatraPDF, `...external.viewer.args` 为 `-reuse-instance`,`-inverse-search`,`"D:/Microsoft VS Code/bin/code.cmd" -g "%f:%l"`,`%PDF%`; `...external.synctex.command` 同上, `...external.synctex.args` 为 `-reuse-instance`,`-forward-search`,`%TEX%`,`%LINE%`,`%PDF%`. 正向: VSCode 里 "SyncTeX from cursor"; 反向: SumatraPDF 里双击(走的是 `code.cmd`, 会闪一下控制台). 前提是编译带 `-synctex=1`, 且 `autoBuild.run` 是 `never`, 要先手动编译.
- VSCode 分词:`_` 与 `^` 连着的左右两段算一个整体, 双击, 按词移动, 基于文档的词补全都按整体走. 词补全只认语言配置的 `wordPattern`, `editor.wordSeparators` 管不到它, 所以 `~\.vscode\extensions\wenje.caret-txt-0.0.1` 注册语言 `wenje-plaintext`(`wordPattern` 里删掉 `^`), 再由 settings 的 `files.associations` 把 `*.txt` 指过去; `editor.wordSeparators` 里的 `^` 一并删掉, 双击与按词移动才跟补全一致.

## 工作方式

- 有疑问先提问, 允许质疑和否定, 尽量减少返工.
- 用户说的一切都可以质疑: 有实测依据就当场指出并反驳, 不因是用户所说而默认接受.
- 涉及附件, 路径, 版本时先核对再动手; 不确定就停下来问, 不擅自猜.

## 常用位置

- 微分几何作业集:`D:\wenje-ma\differential-geometry\homework-cn\week6.md`,`week7.md`.
- 书稿(英文, Quarto book, 只出 PDF):`D:\wenje-ma\ed4dse\tex`;骨架 `_quarto.yml`,`preamble.tex`,`index.qmd`,`chapters/`;编译在 `tex` 下跑 `quarto render`,产物 `_book\Experimental-Design-for-Data-Science-and-Engineering.pdf`;图从章内引 `../../figures\N.M.pdf`;结构与引用写法见 `tex\README.md`.
- 交接文档(给同学及其 AI, 讲装 Git/VSCode/MPE 并克隆全部仓库):`D:\wenje-ma\wenjemaths\tutorial\tutorial.md`.
- 微分几何条目库:`D:\wenje-ma\wenjemaths\forced\dg-mid.md`(按章编号, 引用前先核对条目原文与编号).
- 公式改写工具链:`D:\wenje-ma\wenje-codes\auto_typesetting.py`(`leftright.py` → `math_space_strip.py`); 标点另跑 `cn_punct.py`; 文首引用库排序另跑 `lib_sort.py`.
- `math_space_strip.py` 认公式区之前先屏蔽围栏代码, 行内代码与 `.tex` 注释; 公式区里若混进反引号, 或出现"词 空格 词", 判为散文误判, 整文件跳过并报 Warning(`wenje-codes` 自己的 `.md` 是讲代码的散文, 每次都被跳过, 属正常), 因为压缩空白正是把散文空格抹平的那一步.
- `lib_sort.py` 认的库区: 首个 `>` 行到首个 `## ` 小标题之间的全部内容; 块首行是 `> **类型 编号 (名称)**`, 块内可含未加引用的 `$$...$$` 行间公式, 随块一起搬. 编号取类型词之后的第一串阿拉伯数字(`4.2.M` 按 `4.2` 排), 括号里只写编号的(`公式 (4.2.17)`)按括号内的编号排.
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
- Java 工具链:`D:\MicrosoftJDK` 是 Microsoft OpenJDK 25.0.4 完整 JDK, `javac` 与 `java` 都在其 `bin` 下, `PATH` 已含该目录, 用户级 `JAVA_HOME` 也指它. `D:\Downloads\jre-8u511-windows-x64.exe` 只是 JRE 不含 `javac`, 未安装, 写代码用不上; 要 Java 8 语义时用 `javac --release 8` 而不是换 JDK.
- VSCode Java:扩展 `vscjava.vscode-java-pack`(`redhat.java` 1.58.0, JDT LS 3.48, 支持 Java 25);`settings.json` 里 `java.jdt.ls.java.home` 与 `java.configuration.runtimes`(`JavaSE-25`, `default`)都指 `D:\MicrosoftJDK`;格式化 profile 取 `GoogleStyle`,`[java]` 缩进 2 格并关掉 `detectIndentation`;保存只整理 import, 不自动格式化和不自动组织代码.
- VSCode Java 卡在 "Loading Java progress" 的根因:JDT LS 导入 `D:\wenje-ma` 下 `SpellEngine` 与 `wizards` 时, Gradle wrapper 要先下载发行包, 而 `services.gradle.org` 307 跳到 GitHub release assets, 国内实测 30 KB/s, 每次 4 分钟超时后无限重试. 已把 Gradle 8.14 预置进 `C:\Users\wenje\.gradle\wrapper\dists\gradle-8.14-bin\38aieal9i53h9rfe7vjup95b9`(解压目录 `gradle-8.14` 加空标记文件 `gradle-8.14-bin.zip.ok`, wrapper 见到标记即跳过下载), `D:\wenje-ma\SpellEngine\gradlew.bat --version` 528 ms 通过. 之后换 gradle 版本用 `https://mirrors.huaweicloud.com/gradle/gradle-<版本>-bin.zip`(1-4 MB/s) 或 `mirrors.cloud.tencent.com/gradle`, 不要用官方链接.
- Gradle 当前版本状态:`SpellEngine` 的 wrapper 于 2026-11-11 11:15 自行升到 9.7.1(dist 已完整装在 `dists\gradle-9.7.1-bin`, 带 `.ok`), `wizards` 仍用 8.14; `gradlew help` 在 9.7.1 上 16 秒通过, Architectury Loom 1.11.458 正常加载, 只报 "incompatible with Gradle 10" 的弃用警告. 回退只需把 `gradle\wrapper\gradle-wrapper.properties` 的 `distributionUrl` 改回 8.14(8.14 的预置仍在, 不会再下载). 两个工程版本分叉会同时跑两套 daemon, 尽量对齐.
- 2026-11-11 已彻底移除 VSCode 的 Java 支持:`vscjava.vscode-java-pack` 连同 `redhat.java`,`vscjava.vscode-gradle`,`java-debug`,`java-test`,`java-dependency`,`vscjava.vscode-maven` 一并卸载并删掉扩展目录, `settings.json` 里整段 `java.*` 与 `[java]` 也删了, 同时删掉 `C:\Users\wenje\.gradle`(1012 MB) 与 `globalStorage\redhat.java`(18 MB). 以后不要在 VSCode 里开 Java/Gradle 工程; 若要用命令行构建 `wizards` 或 `SpellEngine`, Gradle 依赖需重新下载(约 1 GB). `SpellEngine` 源码与改 `wizards` 无关: `wizards` 走的是 `maven.modrinth:spell-engine:1.10.0+1.21.1` 成品 jar, 只有要同步改 SpellEngine 本身时才需要它.
- 显卡与独显设置(i7-13620H + Intel UHD + RTX 4060 Laptop, 驱动 610.60, 屏 2560x1600@120Hz 挂在核显上): 全局首选图形处理器在 NVIDIA App 11.0.9.585 的 `图形 → 全局设置 → "GPU 应用程序分配"` 里设为 RTX 4060, 该项就是旧版 NVIDIA 控制面板 "首选图形处理器" 的改名, 旧 `nvcplui.exe` 已不再随驱动安装. Windows 侧另有 HKCU `Software\Microsoft\DirectX\UserGpuPreferences` 逐 exe 写 `GpuPreference=2;`(Windows 的逐程序设置优先于驱动全局项, NVIDIA 官方文档明说), 现 21 条, 覆盖全部 Java 运行时与 Steam 各游戏. 批量登记脚本 `C:\Users\wenje\Doubao\chats\2026-11-12\new-chat-5\force-dgpu.ps1`(可传 `-Paths`, 只写 HKCU, 不需要管理员).
- Minecraft 实例(miniature-shader-2.19, 26.3 Fabric + Iris 1.11.7 + Sodium 0.9.2): `D:\Minecraft\.minecraft\versions\26.3`. 此前画面闪烁的根因是 GL 上下文落在 Intel 核显(日志里 `Preferring discrete GPU` 之后仍 `Using graphics device: Intel`), 2026-11-12 改走 4060 后消失; `config\iris.properties` 的 `maxShadowRenderDistance=32` 与包 NORMAL 档 `shadowDistance=128` 仍不一致, 未改动.
- Clash Verge(`D:\Clash Verge\clash-verge.exe`, 2.5.10, 数据目录 `%APPDATA%\io.github.clash-verge-rev.clash-verge-rev`): 全局 GPU 分配改成 4060 之后, 它的 WebView2 前端不渲染, 日志停在 `新窗口创建成功, 等待前端渲染后显示` 就再无下文, 表现为"打不开". 已给 clash-verge.exe 单独写 `GpuPreference=1;` 钉回核显, 恢复 `Clash Verge` 窗口正常渲染. 它开着 `enable_silent_start: true`, 启动只进托盘不出窗口, 且 2026-11-12 16:25 那次托盘图标创建失败(`os error -2147467259`), 两者叠加才像彻底打不开; 唤醒方式就是再运行一次 exe 走 secondary instance 或点托盘图标. 排查看 `logs\latest.log`.
