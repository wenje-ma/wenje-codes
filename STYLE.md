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

## 文档写作

- 抄写原题; 解答中任意相邻两句都能由上一句推出, 不跳步.
- 数学作业集文首引用库只收书内带编号条目, 正文引用须加粗条目名. 先写解答, 解答里用到哪条就把哪条抄到文首: 解答没加粗引用的条目一律不写, 不论与本周末章多相关.
- 教材里的任何文字——定义, 定理, 公式, 例题, 习题结论——都可作为现成结论直接引用使用, 不在解答中重新推导; 只交代它为何用得上, 不重算一遍.
- 一切学科的整理文档里, 加粗只用于引用编号条目, 步骤标签等不加粗.
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

- VSCode 分词:`_` 与 `^` 连着的左右两段算一个整体, 双击, 按词移动, 基于文档的词补全都按整体走. 词补全只认语言配置的 `wordPattern`, `editor.wordSeparators` 管不到它, 所以 `~\.vscode\extensions\wenje.caret-txt-0.0.1` 注册语言 `wenje-plaintext`(`wordPattern` 里删掉 `^`), 再由 settings 的 `files.associations` 把 `*.txt` 指过去; `editor.wordSeparators` 里的 `^` 一并删掉, 双击与按词移动才跟补全一致.

## 工作方式

- 有疑问先提问, 允许质疑和否定, 尽量减少返工.
- 涉及附件, 路径, 版本时先核对再动手; 不确定就停下来问, 不擅自猜.

## 常用位置

- 微分几何作业集:`D:\wenje-ma\differential-geometry\homework-cn\week6.md`,`week7.md`.
- 交接文档(给同学及其 AI, 讲装 Git/VSCode/MPE 并克隆全部仓库):`D:\wenje-ma\wenjemaths\tutorial\tutorial.md`.
- 微分几何条目库:`D:\wenje-ma\wenjemaths\forced\dg-mid.md`(按章编号, 引用前先核对条目原文与编号).
- 公式改写工具链:`D:\wenje-ma\wenje-codes\run_all.py`(`leftright.py` → `space_gt.py` → `math_space_strip.py`); 标点另跑 `cn_punct.py`.
- Minecraft 实例(anything form nothing,1.20.1 + Embeddium 0.3.31 + Oculus 1.8.0):`D:\Minecraft\.minecraft\versions\anything form nothing`;光影放其下 `shaderpacks`.
- Minecraft 备份目录:`D:\Minecraft\_backup\anything-form-nothing-<时间戳>`(含 `saves`,`config`,`kubejs`,`options.txt`);`latest.txt` 记最新一份.
- 堆叠模组已由 Overstack 换成 All Stacks Infinite 14.3.0.11,配置 `config\All-Stacks-Infinite.toml`(`global_stack_size=99000000`,`experimental=false`,附魔类物品走 `[items_custom_stack_size]` 压回 1).
- Minecraft 实例(magic,1.21.1 + NeoForge 21.1.265):`D:\Minecraft\.minecraft\versions\magic`;堆叠模组 All Stacks Infinite 14.1.0.11,配置 `config\All-Stacks-Infinite.toml`(`global_stack_size=99000000`,`experimental=false`),68 个可附魔物品走 `[items_custom_stack_size]` 压回 1,名单取 `minecraft:enchantable/*` 物品标签并集加 `enchanted_book`.
- HMCL 版本图标:在版本根目录放 `icon.png`(png/jpg/jpeg/bmp/gif/webp 皆可, 按 64 像素加载, 图最好 64 或 64 的整数倍);`versions\<实例>\.hmcl\config\instance-game-settings.json` 里的 `icon` 字段只管内置图标, 存在图标文件时优先用文件.
- 物品图标素材:游戏本体与模组 jar 内 `assets\<命名空间>\textures\item\*.png` 即 16x16 原图, 直接解压加最近邻放大即可, 不必进游戏截图.
