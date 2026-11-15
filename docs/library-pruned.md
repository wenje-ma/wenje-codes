# 从各周 homework 引用库里删掉的条目 (2026-11-15)

判定标准: 该条目的编号与其名字在本文件正文 (题面+解答) 中都不出现, 属于与本周题目无关的条目.


## ma\abstract-algebra\homework-cn\week10.md

> **定理 2.7.7 (贝祖等式)**
> 
> 设 $R$ 为主理想整环, $a,b\in{R}$, $d$ 为 $a,b$ 的一个最大公因子, 则存在 $u,v\in{R}$ 使 $d=ua+vb$.

> **定理 3.4.9 (扭模的 $p$-分支分解)**
> 
> 设 $M$ 为主理想整环 $D$ 上有限生成扭模, 则存在有限个互不相伴的不可约元素 $p_1,\cdots,p_m$ 使 $M=M_{p_1}\oplus\cdots\oplus{M}_{p_m}$, 其中 $M_p=\left\{x\in{M}\mid\exists{e},p^ex=0\right\}$ 为 $p$-分支. 特别地, 若 $\operatorname{ann}\left(y\right)=\left(ab\right)$ 且 $a,b$ 互素, 则 $Dy=Dy_1\oplus{D}y_2$, $\operatorname{ann}\left(y_1\right)=\left(a\right)$, $\operatorname{ann}\left(y_2\right)=\left(b\right)$.


## ma\abstract-algebra\homework-cn\week11.md

> **推论 3.4.12 (有限生成模的同构判定)**
> 
> 设 $M_1,M_2$ 为主理想整环 $D$ 上的有限生成模, 则 $M_1\cong{M}_2$ 当且仅当它们有相同的秩和不变因子, 当且仅当有相同的秩和初等因子.


## ma\abstract-algebra\homework-cn\week2.md

> **引理 1.2.12 (陪集重合条件)**
> 
> 设 $H$ 是群 $G$ 的子群, $a,b\in{G}$, 则 $aH$ 和 $bH$ 要么互不相交, 要么重合, 且 $aH=bH$ 当且仅当 $a^{-1}b\in{H}$.

> **推论 1.2.23 (指数的乘法)**
> 
> 设 $G$ 是有限群, $K<{}G$, $H<{}K$, 则 $\left[G:H\right]=\left[G:K\right]\cdot\left[K:H\right]$.


## ma\abstract-algebra\homework-cn\week4.md

> **定理 1.6.4 (轮换分解)**
> 
> $S_n$ 中的任何元素 $\sigma$ 都可表为 $S_n$ 中一些不相交轮换之积; 如果不计次序, 表法是唯一的.

> **引理 1.6.7 (轮换的对换分解)**
> 
> 任一个 $r$-轮换都可写成 $r-1$ 个对换的乘积: $\left(i_1i_2\cdots{i}_r\right)=\left(i_1i_r\right)\left(i_1i_{r-1}\right)\cdots\left(i_1i_3\right)\left(i_1i_2\right)$.


## ma\abstract-algebra\homework-cn\week5.md

> **定理 1.2.22 (拉格朗日定理)**
> 
> 设 $G$ 是有限群, $H<{}G$, 则 $\left|G\right|=\left[G:H\right]\cdot\left|H\right|$, 其中 $\left[G:H\right]$ 为 $H$ 在 $G$ 中的指数. 从而子群 $H$ 的阶是群 $G$ 的阶的因子, 特别地, 任何元素的阶也是 $\left|G\right|$ 的因子.

> **引理 1.4.13**
> 
> 设 $f:G\to{G}'$ 为群同态, 则 $\mathrm{Im}\,f<{}G'$, $\ker{f}\triangleleft{G}$.

> **例 1.4.17**
> 
> 设 $V$ 是数域 $P$ 上的 $n$ 维线性空间, 则映射 $\det\circ\pi:S_n\to{P}^{*}$, $\sigma\mapsto\det\left(\pi_\sigma\right)$ 是群同态, 其像集为 $\left\{1,-1\right\}$ (当 $n>1$ 时), 该同态的核记为 $A_n$.

> **定理 1.4.19 (群的同态基本定理)**
> 
> 设 $f:G\to{G}'$ 是群的满同态, 则 $G/\ker{f}\cong{G}'$.

> **定理 1.6.4 (轮换分解)**
> 
> $S_n$ 中的任何元素 $\sigma$ 都可表为 $S_n$ 中一些不相交轮换之积; 如果不计次序, 表法是唯一的.

> **引理 1.6.7 (轮换的对换分解)**
> 
> 任一个 $r$-轮换都可写成 $r-1$ 个对换的乘积: $\left(i_1i_2\cdots{i}_r\right)=\left(i_1i_r\right)\left(i_1i_{r-1}\right)\cdots\left(i_1i_3\right)\left(i_1i_2\right)$.

> **命题 1.6.8**
> 
> 任一 $n$ 元置换都可以表为一些对换的乘积.

> **定理 1.6.9 (交错群的单性)**
> 
> 当 $n\ge5$ 时, $A_n$ 是单群.

> **推论 1.9.15 (轨道-迷向子群定理)**
> 
> 设群 $G$ 作用在 $X$ 上, $x\in{X}$, 则 $\left|O_x\right|=\left|G/F_x\right|=\left[G:F_x\right]$; 从而 $\left|O_x\right|\mid\left|G\right|$.


## ma\abstract-algebra\homework-cn\week7.md

> **引理 1.7.7**
> 
> 设 $A,B$ 是 $G$ 的子群, $G=AB$, $A\cap{B}=\left\{e\right\}$, 则 $A,B$ 都是 $G$ 的正规子群当且仅当对任意 $a\in{A}$, $b\in{B}$ 有 $ab=ba$.

> **引理 1.8.8 (可解群的遗传性)**
> 
> 可解群的子群,商群都是可解群; 反之, 设 $N\trianglelefteq{G}$, 且 $N$ 与 $G/N$ 都可解, 则 $G$ 可解.

> **定理 1.10.8 (西罗第二定理)**
> 
> 设 $P$ 是 $G$ 的一个西罗 $p$-子群, $H$ 是 $G$ 的一个 $p^{k}$ 阶子群, $k\le{l}$ (其中 $\left|G\right|=p^{l}m$, $\left(p,m\right)=1$), 则存在 $g\in{G}$ 使 $H\subseteq{g}Pg^{-1}$. 特别地, $G$ 的西罗 $p$-子群相互共轭.


## ma\abstract-algebra\homework-en\week10.md

> **Theorem 2.7.7 (Bezout Identity)**
> 
> Let $R$ be a principal ideal domain, $a,b\in{R}$, and $d$ a greatest common divisor of $a,b$. Then there exist $u,v\in{R}$ such that $d=ua+vb$.

> **Theorem 3.4.9 ($p$-Primary Decomposition of Torsion Modules)**
> 
> Let $M$ be a finitely generated torsion module over a principal ideal domain $D$. Then there exist finitely many pairwise nonassociate irreducibles $p_1,\cdots,p_m$ such that $M=M_{p_1}\oplus\cdots\oplus{M}_{p_m}$, where $M_p=\left\{x\in{M}\mid\exists{e},p^ex=0\right\}$ is the $p$-primary component. In particular, if $\operatorname{ann}\left(y\right)=\left(ab\right)$ with $a,b$ coprime, then $Dy=Dy_1\oplus{D}y_2$, $\operatorname{ann}\left(y_1\right)=\left(a\right)$, $\operatorname{ann}\left(y_2\right)=\left(b\right)$.


## ma\abstract-algebra\homework-en\week11.md

> **Corollary 3.4.12 (Isomorphism Criterion for Finitely Generated Modules)**
> 
> Let $M_1,M_2$ be finitely generated modules over a principal ideal domain $D$. Then $M_1\cong{M}_2$ iff they have the same rank and invariant factors, iff they have the same rank and elementary divisors.


## ma\abstract-algebra\homework-en\week12.md

> **Definition 4.1.15 (Degree of an Extension)**
> 
> Let $E$ be an extension of $F$. The dimension of $E$ as an $F$-vector space is called the degree of $E$ over $F$, written $\left[E:F\right]$. If $\left[E:F\right]<\infty$, $E$ is a finite extension of $F$; otherwise it is an infinite extension.


## ma\abstract-algebra\homework-en\week2.md

> **Lemma 1.2.12 (Coset Coincidence Criterion)**
> 
> Let $H$ be a subgroup of a group $G$ and $a,b\in{G}$. Then $aH$ and $bH$ are either disjoint or identical, and $aH=bH$ if and only if $a^{-1}b\in{H}$.

> **Corollary 1.2.23 (Multiplicativity of the Index)**
> 
> Let $G$ be a finite group, $K<{}G$, $H<{}K$. Then $\left[G:H\right]=\left[G:K\right]\cdot\left[K:H\right]$.


## ma\abstract-algebra\homework-en\week4.md

> **Theorem 1.6.4 (Cycle Decomposition)**
> 
> Every element $\sigma$ of $S_n$ can be written as a product of some disjoint cycles of $S_n$; disregarding order, this representation is unique.

> **Lemma 1.6.7 (Decomposition of a Cycle into Transpositions)**
> 
> Every $r$-cycle can be written as a product of $r-1$ transpositions: $\left(i_1i_2\cdots{i}_r\right)=\left(i_1i_r\right)\left(i_1i_{r-1}\right)\cdots\left(i_1i_3\right)\left(i_1i_2\right)$.


## ma\abstract-algebra\homework-en\week5.md

> **Theorem 1.2.22 (Lagrange's Theorem)**
> 
> Let $G$ be a finite group and $H<{}G$. Then $\left|G\right|=\left[G:H\right]\cdot\left|H\right|$, where $\left[G:H\right]$ is the index of $H$ in $G$. Hence the order of the subgroup $H$ is a divisor of the order of the group $G$; in particular, the order of any element is also a divisor of $\left|G\right|$.

> **Lemma 1.4.13**
> 
> Let $f:G\to{G}'$ be a group homomorphism. Then $\mathrm{Im}\,f<{}G'$ and $\ker{f}\triangleleft{G}$.

> **Example 1.4.17**
> 
> Let $V$ be an $n$-dimensional vector space over a field $P$. Then the map $\det\circ\pi:S_n\to{P}^{*}$, $\sigma\mapsto\det\left(\pi_\sigma\right)$ is a group homomorphism whose image is $\left\{1,-1\right\}$ (for $n>1$); its kernel is denoted $A_n$.

> **Theorem 1.4.19 (Fundamental Theorem of Group Homomorphisms)**
> 
> Let $f:G\to{G}'$ be a surjective group homomorphism. Then $G/\ker{f}\cong{G}'$.

> **Definition 1.6.1 (Cycle)**
> 
> Let $\left\{i_1,i_2,\cdots,i_r\right\}\subseteq\left\{1,2,\cdots,n\right\}$. If $\sigma\in{S}_n$ satisfies $\sigma\left(i_1\right)=i_2$, $\sigma\left(i_2\right)=i_3$, ..., $\sigma\left(i_r\right)=i_1$ and fixes all other letters, then $\sigma$ is called an $r$-cycle, denoted $\sigma=\left(i_1i_2\cdots{i}_r\right)$. In particular, a $2$-cycle is called a transposition.

> **Theorem 1.6.4 (Cycle Decomposition)**
> 
> Every element $\sigma$ of $S_n$ can be written as a product of some disjoint cycles of $S_n$; disregarding order, this representation is unique.

> **Lemma 1.6.7 (Decomposition of a Cycle into Transpositions)**
> 
> Every $r$-cycle can be written as a product of $r-1$ transpositions: $\left(i_1i_2\cdots{i}_r\right)=\left(i_1i_r\right)\left(i_1i_{r-1}\right)\cdots\left(i_1i_3\right)\left(i_1i_2\right)$.

> **Proposition 1.6.8**
> 
> Every permutation of $n$ elements can be written as a product of transpositions.

> **Theorem 1.6.9 (Simplicity of the Alternating Group)**
> 
> For $n\ge5$, $A_n$ is a simple group.

> **Corollary 1.9.15 (Orbit-Stabilizer Theorem)**
> 
> Let a group $G$ act on $X$ and $x\in{X}$. Then $\left|O_x\right|=\left|G/F_x\right|=\left[G:F_x\right]$; hence $\left|O_x\right|\mid\left|G\right|$.


## ma\abstract-algebra\homework-en\week7.md

> **Lemma 1.7.7**
> 
> Let $A,B$ be subgroups of $G$ with $G=AB$ and $A\cap{B}=\left\{e\right\}$. Then $A$ and $B$ are both normal subgroups of $G$ if and only if $ab=ba$ for all $a\in{A}$ and $b\in{B}$.

> **Lemma 1.8.8 (Heredity of Solvability)**
> 
> Subgroups and quotient groups of a solvable group are solvable; conversely, if $N\trianglelefteq{G}$ and both $N$ and $G/N$ are solvable, then $G$ is solvable.

> **Theorem 1.10.8 (Sylow's Second Theorem)**
> 
> Let $P$ be a Sylow $p$-subgroup of $G$, and let $H$ be a subgroup of $G$ of order $p^{k}$, $k\le{l}$ (where $\left|G\right|=p^{l}m$, $\left(p,m\right)=1$). Then there exists $g\in{G}$ with $H\subseteq{g}Pg^{-1}$. In particular, the Sylow $p$-subgroups of $G$ are conjugate to one another.


## ma\abstract-algebra\homework-en\week8.md

> **Definition 2.5.2 (Associates)**
> 
> Let $R$ be an integral domain and $a,b\in{R}$. If there exists a unit $u$ in $R$ such that $a=ub$, then $a$ and $b$ are called associates, written $a\sim{b}$.


## ma\abstract-algebra\homework-en\week9.md

> **Definition 2.5.6 (Irreducible Element)**
> 
> Let $R$ be an integral domain and $\alpha\in{R}^{*}\setminus{U}$ (i.e. nonzero and not a unit). If $\alpha$ has no nontrivial divisors, then $\alpha$ is called an irreducible element.


## ma\advenced-algebra\homework-cn\week10.md

> **定理 3.6.2 (解的个数判别)**
> 
> 设线性方程组有解, 如果系数矩阵的秩等于未知量数目 $n$, 则方程组有唯一解; 如果系数矩阵的秩小于 $n$, 则方程组有无穷多个解.


## ma\advenced-algebra\homework-cn\week12.md

> **定义 4.1.1 (矩阵的加法)**
> 
> 设 $A=\left(a_{ij}\right),B=\left(b_{ij}\right)$ 都是数域 $K$ 上 $s\times{n}$ 矩阵, 令 $C=\left(a_{ij}+b_{ij}\right)_{s\times{n}}$, 则称 $C$ 是矩阵 $A$ 与 $B$ 的和, 记作 $C=A+B$.

> **定义 4.1.2 (矩阵的数量乘法)**
> 
> 设 $k\in{K}$, 令 $M=\left(ka_{ij}\right)_{s\times{n}}$, 则称 $M$ 是 $k$ 与矩阵 $A$ 的数量乘积, 记作 $M=kA$.

> **命题 4.3.2 (实矩阵 $A^{\top}Az=0$ 与 $z=0$ 同解)**
> 
> 设 $A$ 是实数域上的矩阵, 则齐次线性方程组 $A^{\top}Az=0$ 与 $z=0$ 同解.

> **定理 4.3.3 (乘积的行列式)**
> 
> 设 $A,B$ 都是 $n$ 级矩阵, 则 $\left|AB\right|=\left|A\right|\left|B\right|$.


## ma\advenced-algebra\homework-cn\week14.md

> **定义 4.6.2 (标准内积)**
> 
> 在 $\mathbb{R}^{n}$ 中, 任给 $\alpha=\left(a_{1},a_{2},\cdots,a_{n}\right)$, $\beta=\left(b_{1},b_{2},\cdots,b_{n}\right)$, 规定 $\left(\alpha,\beta\right)=a_{1}b_{1}+a_{2}b_{2}+\cdots+a_{n}b_{n}$, 称为 $\mathbb{R}^{n}$ 的标准内积.

> **命题 4.6.2 (正交向量组线性无关)**
> 
> 欧几里得空间 $\mathbb{R}^{n}$ 中, 正交向量组一定是线性无关的.


## ma\advenced-algebra\homework-cn\week15.md

> **定义 4.6.2 (标准内积)**
> 
> 在 $\mathbb{R}^{n}$ 中, 任给 $\alpha=\left(a_{1},a_{2},\cdots,a_{n}\right)$, $\beta=\left(b_{1},b_{2},\cdots,b_{n}\right)$, 规定

> **命题 4.6.2 (正交向量组线性无关)**
> 
> 欧几里得空间 $\mathbb{R}^{n}$ 中, 正交向量组一定是线性无关的.


## ma\advenced-algebra\homework-cn\week16.md

> **定理 5.2.2 (相抵的充要条件)**
> 
> 数域 $K$ 上两个 $s\times{n}$ 矩阵 $A$ 与 $B$ 相抵当且仅当它们的秩相等.

> **定理 5.3.1 (广义逆的存在性)**
> 
> 设 $A$ 是数域 $K$ 上 $s\times{n}$ 非零矩阵, 则矩阵方程 $AXA=A$ 一定有解.


## ma\advenced-algebra\homework-cn\week18.md

> **定义 5.5.1 (特征值与特征向量)**
> 
> 设 $A$ 是数域 $K$ 上的 $n$ 级矩阵, 如果 $K^{n}$ 中有非零列向量 $\alpha$, 使得 $A\alpha=\lambda_{0}\alpha$, 且 $\lambda_{0}\in{K}$, 则称 $\lambda_{0}$ 是 $A$ 的一个特征值, 称 $\alpha$ 是 $A$ 的属于特征值 $\lambda_{0}$ 的一个特征向量.

> **推论 5.6.6 (有 $n$ 个不同特征值则可对角化)**
> 
> 如果数域 $K$ 上 $n$ 级矩阵 $A$ 有 $n$ 个不同的特征值, 则 $A$ 可对角化.


## ma\advenced-algebra\homework-cn\week19.md

> **定理 5.6.1 (可对角化的充要条件)**
> 
> 数域 $K$ 上 $n$ 级矩阵 $A$ 可对角化的充分必要条件是 $A$ 有 $n$ 个线性无关的特征向量.

> **推论 5.6.6 (有 $n$ 个不同特征值则可对角化)**
> 
> 如果数域 $K$ 上 $n$ 级矩阵 $A$ 有 $n$ 个不同的特征值, 则 $A$ 可对角化.

> **定理 5.7.1 (实对称矩阵的特征值)**
> 
> 实对称矩阵的特征多项式在复数域中的每一个根都是实数.

> **定义 6.1.2 (规范形)**
> 
> 实二次型 $X^{\top}AX$ 的规范形为 $z_{1}^{2}+\cdots+z_{p}^{2}-z_{p+1}^{2}-\cdots-z_{r}^{2}$, 其中 $p$ 是正惯性指数, $r$ 是二次型的秩.


## ma\advenced-algebra\homework-cn\week2.md

> **定理 1.2.1 (线性方程组解的判别准则)**
> 
> 把 $n$ 元线性方程组的增广矩阵经过初等行变换化成阶梯形矩阵: (1) 若相应的阶梯形方程组出现 $0=d$($d\ne0$), 则原方程组无解; (2) 若不出现 $0=d$, 则有解, 且当阶梯形矩阵的非零行数目等于未知量数目 $n$ 时有唯一解, 当非零行数目 $r<{}n$ 时有无穷多个解.


## ma\advenced-algebra\homework-cn\week20.md

> **推论 6.2.4 (合同的充要条件)**
> 
> 两个 $n$ 级实对称矩阵合同当且仅当它们的秩相等, 并且正惯性指数也相等.

> **定义 7.2.1 (整除)**
> 
> 设 $f\left(x\right),g\left(x\right)\in{K}\left[x\right]$, 如果存在 $h\left(x\right)\in{K}\left[x\right]$, 使得 $f\left(x\right)=h\left(x\right)g\left(x\right)$, 则称 $g\left(x\right)$ 整除 $f\left(x\right)$, 记作 $g\left(x\right)\mid{f}\left(x\right)$.


## ma\advenced-algebra\homework-cn\week21.md

> **定理 7.2.1 (带余除法)**
> 
> 在 $K\left[x\right]$ 中, 对于任意两个多项式 $f\left(x\right),g\left(x\right)$, 其中 $g\left(x\right)\ne0$, 存在唯一的一对多项式 $h\left(x\right),r\left(x\right)$, 使得


## ma\advenced-algebra\homework-cn\week22.md

> **定义 7.3.1 (最大公因式)**
> 
> 设 $f\left(x\right),g\left(x\right)\in{K}\left[x\right]$, $d\left(x\right)$ 是 $f\left(x\right)$ 与 $g\left(x\right)$ 的一个公因式. 如果 $f\left(x\right)$ 与 $g\left(x\right)$ 的任一公因式都能整除 $d\left(x\right)$, 则称 $d\left(x\right)$ 是 $f\left(x\right)$ 与 $g\left(x\right)$ 的一个最大公因式.

> **定理 7.3.1 (最大公因式的存在性与倍式和)**
> 
> 对于 $K\left[x\right]$ 中任意两个多项式 $f\left(x\right)$ 与 $g\left(x\right)$, 存在它们的一个最大公因式 $d\left(x\right)$, 并且 $d\left(x\right)$ 可以表示成 $f\left(x\right)$ 与 $g\left(x\right)$ 的倍式和, 即有 $u\left(x\right),v\left(x\right)\in{K}\left[x\right]$, 使得


## ma\advenced-algebra\homework-cn\week23.md

> **定义 7.6.1 (多项式的根)**
> 
> 设 $K$ 是一个数域, 设 $R$ 是一个有单位元的交换环, 且 $R$ 可看成是 $K$ 的一个扩环. 对于 $K\left[x\right]$ 中一个多项式 $f\left(x\right)$, 如果 $R$ 中有一个元素 $c$ 使得 $f\left(c\right)=0$, 则称 $c$ 是 $f\left(x\right)$ 在 $R$ 中的一个根.

> **定理 7.6.1 (余数定理)**
> 
> 在 $K\left[x\right]$ 中, 用 $x-a$ 去除 $f\left(x\right)$ 所得的余式是 $f\left(a\right)$.

> **定理 7.7.1 (实系数多项式唯一因式分解定理)**
> 
> 每个次数大于零的实系数多项式在实数域上都可以唯一地分解成一次因式与判别式小于零的二次因式的乘积.


## ma\advenced-algebra\homework-cn\week3.md

> **性质 2.3.5 (两行相同则行列式为零)**
> 
> 行列式中有两行相同, 则行列式的值为 $0$; 进而若两行成比例, 行列式的值也为 $0$.


## ma\advenced-algebra\homework-cn\week4.md

> **性质 2.3.3 (某行为两组数之和则可拆分)**
> 
> 行列式中若有某一行是两组数的和, 则此行列式等于两个行列式的和, 这两个行列式的这一行分别是第一组数和第二组数, 而其余各行与原来行列式的相应各行相同.


## ma\advenced-algebra\homework-cn\week6.md

> **定义 3.1.1 (线性组合与线性表出)**
> 
> $K^{n}$ 中, 给定向量组 $\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$, 任给 $K$ 中一组数 $k_{1},k_{2},\cdots,k_{s}$, 称 $k_{1}\alpha_{1}+k_{2}\alpha_{2}+\cdots+k_{s}\alpha_{s}$ 为向量组 $\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$ 的一个线性组合. 如果 $\beta=k_{1}\alpha_{1}+k_{2}\alpha_{2}+\cdots+k_{s}\alpha_{s}$, 则称 $\beta$ 可以由 $\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$ 线性表出.


## ma\advenced-algebra\homework-cn\week7.md

> **命题 3.2.1 (线性表出与线性相关的关系)**
> 
> 设向量组 $\alpha_{1},\cdots,\alpha_{s}$ 线性无关, 则向量 $\beta$ 可以由 $\alpha_{1},\cdots,\alpha_{s}$ 线性表出的充分必要条件是 $\alpha_{1},\cdots,\alpha_{s},\beta$ 线性相关.


## ma\advenced-algebra\homework-cn\week8.md

> **命题 3.2.1 (线性表出与线性相关的关系)**
> 
> 设向量组 $\alpha_{1},\cdots,\alpha_{s}$ 线性无关, 则向量 $\beta$ 可以由 $\alpha_{1},\cdots,\alpha_{s}$ 线性表出的充分必要条件是 $\alpha_{1},\cdots,\alpha_{s},\beta$ 线性相关.


## ma\advenced-algebra\homework-en\week10.md

> **Theorem 3.6.2 (Criterion for the Number of Solutions)**
> 
> Suppose a linear system is solvable. If the rank of the coefficient matrix equals the number $n$ of unknowns, the system has a unique solution; if the rank is less than $n$, the system has infinitely many solutions.


## ma\advenced-algebra\homework-en\week12.md

> **Definition 4.1.1 (Matrix Addition)**
> 
> Let $A=\left(a_{ij}\right),B=\left(b_{ij}\right)$ both be $s\times{n}$ matrices over a number field $K$, and set $C=\left(a_{ij}+b_{ij}\right)_{s\times{n}}$. Then $C$ is called the sum of the matrices $A$ and $B$, denoted $C=A+B$.

> **Definition 4.1.2 (Scalar Multiplication of Matrices)**
> 
> Let $k\in{K}$ and set $M=\left(ka_{ij}\right)_{s\times{n}}$. Then $M$ is called the scalar product of $k$ and the matrix $A$, denoted $M=kA$.

> **Proposition 4.3.2 (Over $\mathbb{R}$, $A^{\top}Az=0$ Has the Same Solutions as $z=0$)**
> 
> Let $A$ be a matrix over the real number field. Then the homogeneous system $A^{\top}Az=0$ and $z=0$ have the same solutions.

> **Theorem 4.3.3 (Determinant of a Product)**
> 
> Let $A,B$ both be $n\times{n}$ matrices. Then $\left|AB\right|=\left|A\right|\left|B\right|$.


## ma\advenced-algebra\homework-en\week14.md

> **Definition 4.6.2 (Standard Inner Product)**
> 
> In $\mathbb{R}^{n}$, for any $\alpha=\left(a_{1},a_{2},\cdots,a_{n}\right)$ and $\beta=\left(b_{1},b_{2},\cdots,b_{n}\right)$, define $\left(\alpha,\beta\right)=a_{1}b_{1}+a_{2}b_{2}+\cdots+a_{n}b_{n}$, which is called the standard inner product on $\mathbb{R}^{n}$.

> **Proposition 4.6.2 (An Orthogonal Vector Group Is Linearly Independent)**
> 
> In the Euclidean space $\mathbb{R}^{n}$, an orthogonal vector group is always linearly independent.


## ma\advenced-algebra\homework-en\week15.md

> **Definition 4.6.2 (Standard Inner Product)**
> 
> In $\mathbb{R}^{n}$, for any $\alpha=\left(a_{1},a_{2},\cdots,a_{n}\right)$ and $\beta=\left(b_{1},b_{2},\cdots,b_{n}\right)$, define

> **Proposition 4.6.2 (An Orthogonal Vector Group Is Linearly Independent)**
> 
> In the Euclidean space $\mathbb{R}^{n}$, an orthogonal vector group is always linearly independent.


## ma\advenced-algebra\homework-en\week16.md

> **Definition 5.1.1 (Binary Relation)**
> 
> Let $S$ be a nonempty set. A subset $W$ of $S\times{S}$ is called a binary relation on $S$. If $\left(a,b\right)\in{W}$, we say $a$ and $b$ are in the relation $W$.

> **Theorem 5.2.2 (Necessary and Sufficient Condition for Equivalence)**
> 
> Two $s\times{n}$ matrices $A$ and $B$ over a number field $K$ are equivalent if and only if they have the same rank.

> **Theorem 5.3.1 (Existence of a Generalized Inverse)**
> 
> Let $A$ be a nonzero $s\times{n}$ matrix over a number field $K$. Then the matrix equation $AXA=A$ always has a solution.


## ma\advenced-algebra\homework-en\week18.md

> **Definition 5.5.1 (Eigenvalue and Eigenvector)**
> 
> Let $A$ be an $n\times{n}$ matrix over a number field $K$. If there is a nonzero column vector $\alpha$ in $K^{n}$ such that $A\alpha=\lambda_{0}\alpha$ with $\lambda_{0}\in{K}$, then $\lambda_{0}$ is called an eigenvalue of $A$, and $\alpha$ is called an eigenvector of $A$ belonging to the eigenvalue $\lambda_{0}$.

> **Corollary 5.6.6 (Distinct Eigenvalues Imply Diagonalizability)**
> 
> If an $n\times{n}$ matrix $A$ over a number field $K$ has $n$ distinct eigenvalues, then $A$ is diagonalizable.


## ma\advenced-algebra\homework-en\week19.md

> **Theorem 5.6.1 (Necessary and Sufficient Condition for Diagonalizability)**
> 
> An $n\times{n}$ matrix $A$ over a number field $K$ is diagonalizable if and only if $A$ has $n$ linearly independent eigenvectors.

> **Corollary 5.6.6 (Distinct Eigenvalues Imply Diagonalizability)**
> 
> If an $n\times{n}$ matrix $A$ over a number field $K$ has $n$ distinct eigenvalues, then $A$ is diagonalizable.

> **Theorem 5.7.1 (Eigenvalues of a Real Symmetric Matrix)**
> 
> Every root of the characteristic polynomial of a real symmetric matrix, over the complex number field, is a real number.


## ma\advenced-algebra\homework-en\week2.md

> **Theorem 1.2.1 (Criterion for the Number of Solutions of a Linear System)**
> 
> Reduce the augmented matrix of an $n$-variable linear system to a row echelon matrix by elementary row operations: (1) if the corresponding echelon system exhibits $0=d$ ($d\ne0$), then the original system has no solution; (2) if $0=d$ does not appear, then there is a solution: when the number of nonzero rows of the echelon matrix equals the number $n$ of unknowns there is a unique solution, and when the number of nonzero rows is $r<{}n$ there are infinitely many solutions.


## ma\advenced-algebra\homework-en\week20.md

> **Definition 6.1.1 (Quadratic Form)**
> 
> A homogeneous quadratic polynomial in $n$ variables $x_{1},x_{2},\cdots,x_{n}$ with coefficients in a number field $K$ is called an $n$-variable quadratic form over $K$.

> **Definition 6.1.2 (Canonical Form)**
> 
> The canonical form of a real quadratic form $X^{\top}AX$ is

> **Theorem 6.1.3 (Canonical Form of a Quadratic Form)**
> 
> Every quadratic form over a number field $K$ is equivalent to a quadratic form containing only square terms.

> **Corollary 6.2.4 (Necessary and Sufficient Condition for Congruence)**
> 
> Two $n\times{n}$ real symmetric matrices are congruent if and only if they have the same rank and the same positive index of inertia.

> **Definition 7.2.1 (Divisibility)**
> 
> Let $f\left(x\right),g\left(x\right)\in{K}\left[x\right]$. If there exists $h\left(x\right)\in{K}\left[x\right]$ such that $f\left(x\right)=h\left(x\right)g\left(x\right)$, then $g\left(x\right)$ divides $f\left(x\right)$, written $g\left(x\right)\mid{f}\left(x\right)$.


## ma\advenced-algebra\homework-en\week21.md

> **Definition 7.2.1 (Divisibility)**
> 
> Let $f\left(x\right),g\left(x\right)\in{K}\left[x\right]$. If there exists $h\left(x\right)\in{K}\left[x\right]$ such that $f\left(x\right)=h\left(x\right)g\left(x\right)$, then $g\left(x\right)$ divides $f\left(x\right)$, written $g\left(x\right)\mid{f}\left(x\right)$.

> **Theorem 7.2.1 (Division with Remainder)**
> 
> In $K\left[x\right]$, for any two polynomials $f\left(x\right),g\left(x\right)$ with $g\left(x\right)\ne0$, there exists a unique pair of polynomials $h\left(x\right),r\left(x\right)$ such that

> **Definition 7.3.2 (Coprime)**
> 
> In $K\left[x\right]$, if the greatest common divisor of $f\left(x\right)$ and $g\left(x\right)$ is a zero-degree polynomial, then $f\left(x\right)$ and $g\left(x\right)$ are said to be coprime.


## ma\advenced-algebra\homework-en\week22.md

> **Definition 7.3.1 (Greatest Common Divisor)**
> 
> Let $f\left(x\right),g\left(x\right)\in{K}\left[x\right]$, and let $d\left(x\right)$ be a common divisor of $f\left(x\right)$ and $g\left(x\right)$. If every common divisor of $f\left(x\right)$ and $g\left(x\right)$ divides $d\left(x\right)$, then $d\left(x\right)$ is called a greatest common divisor of $f\left(x\right)$ and $g\left(x\right)$.

> **Theorem 7.3.1 (Existence of the Greatest Common Divisor and Bezout Identity)**
> 
> For any two polynomials $f\left(x\right)$ and $g\left(x\right)$ in $K\left[x\right]$, there exists a greatest common divisor $d\left(x\right)$, and $d\left(x\right)$ can be expressed as a linear combination of $f\left(x\right)$ and $g\left(x\right)$, i.e. there exist $u\left(x\right),v\left(x\right)\in{K}\left[x\right]$ such that

> **Definition 7.3.2 (Coprime)**
> 
> In $K\left[x\right]$, if the greatest common divisor of $f\left(x\right)$ and $g\left(x\right)$ is a zero-degree polynomial, then $f\left(x\right)$ and $g\left(x\right)$ are said to be coprime.


## ma\advenced-algebra\homework-en\week23.md

> **Definition 7.6.1 (Root of a Polynomial)**
> 
> Let $K$ be a number field, and let $R$ be a commutative ring with identity that can be viewed as an extension ring of $K$. For a polynomial $f\left(x\right)$ in $K\left[x\right]$, if there is an element $c$ in $R$ such that $f\left(c\right)=0$, then $c$ is called a root of $f\left(x\right)$ in $R$.

> **Theorem 7.6.1 (Remainder Theorem)**
> 
> In $K\left[x\right]$, the remainder when $f\left(x\right)$ is divided by $x-a$ is $f\left(a\right)$.

> **Theorem 7.7.1 (Unique Factorization Theorem for Real Polynomials)**
> 
> Every real-coefficient polynomial of positive degree can be uniquely factored over $\mathbb{R}$ into a product of linear factors and quadratic factors with negative discriminant.


## ma\advenced-algebra\homework-en\week3.md

> **Property 2.3.5 (Two Identical Rows Make the Determinant Zero)**
> 
> If a determinant has two identical rows, its value is $0$; consequently, if two rows are proportional, the determinant is also $0$.


## ma\advenced-algebra\homework-en\week4.md

> **Property 2.3.3 (Splitting When a Row Is a Sum of Two Groups)**
> 
> If a row of a determinant is the sum of two groups of numbers, then the determinant equals the sum of two determinants: in these two determinants that row is respectively the first group and the second group of numbers, while all other rows are the same as the corresponding rows of the original determinant.


## ma\advenced-algebra\homework-en\week6.md

> **Definition 3.1.1 (Linear Combination and Linear Representation)**
> 
> In $K^{n}$, given a vector group $\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$ and any numbers $k_{1},k_{2},\cdots,k_{s}$ in $K$, we call $k_{1}\alpha_{1}+k_{2}\alpha_{2}+\cdots+k_{s}\alpha_{s}$ a linear combination of the vector group $\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$. If $\beta=k_{1}\alpha_{1}+k_{2}\alpha_{2}+\cdots+k_{s}\alpha_{s}$, then we say that $\beta$ can be linearly represented by $\alpha_{1},\alpha_{2},\cdots,\alpha_{s}$.


## ma\advenced-algebra\homework-en\week7.md

> **Proposition 3.2.1 (Relation Between Linear Representability and Linear Dependence)**
> 
> Suppose the vector group $\alpha_{1},\cdots,\alpha_{s}$ is linearly independent. Then the vector $\beta$ can be linearly represented by $\alpha_{1},\cdots,\alpha_{s}$ if and only if $\alpha_{1},\cdots,\alpha_{s},\beta$ is linearly dependent.


## ma\advenced-algebra\homework-en\week8.md

> **Definition 3.2.1 (Linear Dependence)**
> 
> A vector group $\alpha_{1},\cdots,\alpha_{s}$ in $K^{n}$ is called linearly dependent if there exist numbers $k_{1},\cdots,k_{s}$ in $K$, not all zero, such that $k_{1}\alpha_{1}+\cdots+k_{s}\alpha_{s}=0$.

> **Proposition 3.2.1 (Relation Between Linear Representability and Linear Dependence)**
> 
> Suppose the vector group $\alpha_{1},\cdots,\alpha_{s}$ is linearly independent. Then the vector $\beta$ can be linearly represented by $\alpha_{1},\cdots,\alpha_{s}$ if and only if $\alpha_{1},\cdots,\alpha_{s},\beta$ is linearly dependent.


## ma\complex-analysis\homework-cn\week1.md

> **定义 2.2.7 (单连通与多连通性)**
> 
> 设 $D$ 是复平面 $\mathbb{C}$ 上的区域, 称 $D$ 为单连通的, 如果 $D$ 内任意若当闭曲线的内区域都包含在 $D$ 内; 否则称它是多连通的.

> **定义 2.4.1 (函数沿某集合的极限)**
> 
> 设函数 $f$ 在集合 $M\subset\overline{\mathbb{C}}$ 上有定义, 点 $a\in\overline{\mathbb{C}}$ 是 $M$ 的极限点. 称 $A\in\mathbb{C}$ 为 $f$ 当 $z$ 沿 $M$ 趋向 $a$ 时的极限, 记为 $\lim_{z\to{a},z\in{M}}f\left(z\right)=A$, 如果对任意 $\varepsilon>0$ 存在 $\delta>0$ 使对任意 $z\in{M}$, 若 $0<\rho\left(z,a\right)<\delta$ 则 $\rho\left(f\left(z\right),A\right)<\varepsilon$.

> **定义 2.4.2 (函数的有界性和连续性)**
> 
> 若存在 $C>0$ 使 $\forall{z}\in{M}$ 有 $\left|f\left(z\right)\right|\le{C}$, 则称 $f$ 在 $M$ 上有界; 若 $\lim_{z\to{a},z\in{M}}f\left(z\right)=f\left(a\right)$, 则称 $f$ 在点 $a$ 处 (沿 $M$) 连续; 若对 $\forall{a}\in{M}$ 均连续, 则称 $f$ 在 $M$ 上连续.


## ma\complex-analysis\homework-cn\week10.md

> **命题 16.1.6 (均值性质)**
> 
> 调和函数 $u$ 于 $B\left(a,R\right)$ 有

> **定理 16.2.10 (有界若当域上的狄利克雷问题)**
> 
> 有界若当域上的狄利克雷问题可解.

> **定理 17.3.6 (单值性定理)**
> 
> 若 $D$ 是单连通区域且 $\left(f,U\right)$ 沿 $D$ 内每条道路都可全纯延拓, 则 $f$ 延拓为 $D$ 上的单值全纯函数.

> **引理 18.1.1 (拼接引理)**
> 
> 区域 $D_{1},D_{2}$ 不相交且有公共边界线段 $\gamma$, $f_{1},f_{2}$ 分别在其上全纯并连续到 $\gamma$, 若 $f_{1}=f_{2}$ 于 $\gamma$, 则拼接的函数在 $D_{1}\cup\gamma\cup{D}_{2}$ 上全纯.


## ma\complex-analysis\homework-cn\week11.md

> **引理 18.1.1 (拼接引理)**
> 
> 区域 $D_{1},D_{2}$ 不相交且有公共边界线段 $\gamma$, $f_{1},f_{2}$ 分别在其上全纯并连续到 $\gamma$, 若 $f_{1}=f_{2}$ 于 $\gamma$, 则拼接的函数在 $D_{1}\cup\gamma\cup{D}_{2}$ 上全纯.

> **定理 19.2.1 (反射公式)**
> 
> 伽玛函数满足反射公式 $\Gamma\left(z\right)\Gamma\left(1-z\right)=\frac{\pi}{\sin\pi{z}},\quad{z}\in\mathbb{C}\setminus\mathbb{Z}$.

> **定理 19.2.3 (魏尔斯特拉斯无穷乘积)**
> 
> 伽玛函数的倒数有魏尔斯特拉斯无穷乘积展开 $\frac{1}{\Gamma\left(z\right)}=ze^{\gamma{z}}\prod_{n=1}^{+\infty}\left(1+\frac{z}{n}\right)e^{-\frac{z}{n}}$, 其中 $\gamma$ 为欧拉常数.

> **定义 20.1.1 (黎曼 $\zeta$-函数)**
> 
> 黎曼 $\zeta$-函数对 $\operatorname{Re}z>1$ 由狄利克雷级数定义 $\zeta\left(z\right)=\sum_{n=1}^{+\infty}\frac1{n^{z}},\quad\operatorname{Re}z>1$; 由欧拉乘积 $\zeta\left(z\right)=\prod_{p}\left(1-p^{-z}\right)^{-1}$ 知其无零点.

> **定理 20.1.6 (亚纯延拓)**
> 
> $\zeta$ 亚纯延拓到 $\mathbb{C}$, 只在 $z=1$ 有简单极点, 且 $\lim_{z\to1}\left(\zeta\left(z\right)-\frac1{z-1}\right)=\gamma$ (欧拉常数).

> **推论 20.2.3 (平凡零点与临界带)**
> 
> $\zeta$ 的平凡零点恰为 $-2,-4,-6,\ldots$; 非平凡零点全落在临界带 $0<\operatorname{Re}z<1$ 内.


## ma\complex-analysis\homework-cn\week12.md

> **定理 20.1.6 (亚纯延拓)**
> 
> $\zeta$ 亚纯延拓到 $\mathbb{C}$, 只在 $z=1$ 有简单极点, 且

> **定理 21.1.3 (布洛克定理)**
> 
> 存在常数 $B>0$: 若 $f$ 在单位圆盘上全纯且 $f'\left(0\right)=1$, 则 $f\left(\mathbb{D}\right)$ 含一个半径至少 $B$ 的圆盘.

> **定理 21.2.4 (毕卡小定理, 亚纯形式)**
> 
> 非常值亚纯函数至多漏掉两个值.

> **定理 21.4 (毕卡大定理)**
> 
> 全纯函数在本性奇点的任意去心邻域内取每个值无穷多次 (至多漏一个值).

> **定理 22.2.3 (蒙泰尔定理)**
> 
> 区域 $D$ 上一致漏掉三个不同值 (扩充复平面上的点) 的亚纯函数族是正规的.


## ma\complex-analysis\homework-cn\week2.md

> **定义 2.1.2 (道路的重参数化)**
> 
> 称道路 $\gamma_{1}:\left[a_{1},b_{1}\right]\to\mathbb{C}$ 是道路 $\gamma_{2}:\left[a_{2},b_{2}\right]\to\mathbb{C}$ 的重参数化, 如果存在单调递增函数 $\tau:\left[a_{1},b_{1}\right]\to\left[a_{2},b_{2}\right]$ 满足 $\tau\left(a_{1}\right)=a_{2}$, $\tau\left(b_{1}\right)=b_{2}$, 使得对任意 $t\in\left[a_{1},b_{1}\right]$ 有 $\gamma_{1}\left(t\right)=\gamma_{2}\left(\tau\left(t\right)\right)$; 若 $\tau$ 在某点 $\overline{t}$ 处不连续, 即 $\tau\left(\overline{t}-0\right)<\tau\left(\overline{t}+0\right)$, 还要求 $\gamma_{2}$ 在区间 $\left[\tau\left(\overline{t}-0\right),\tau\left(\overline{t}+0\right)\right]$ 上为常值.

> **定义 2.1.4 (路径)**
> 
> 在道路重参数化意义下的一个道路等价类称为路径.

> **定理 2.2.6 (若当曲线定理)**
> 
> 复平面上的任一条若当闭曲线把整个平面分成两个没有公共点的区域: 一个有界的称为它的内区域, 一个无界的称为它的外区域.

> **定义 2.4.1 (函数沿某集合的极限)**
> 
> 设函数 $f$ 在集合 $M\subset\overline{\mathbb{C}}$ 上有定义, 点 $a\in\overline{\mathbb{C}}$ 是 $M$ 的极限点. 称 $A\in\mathbb{C}$ 为 $f$ 当 $z$ 沿 $M$ 趋向 $a$ 时的极限, 记为 $\lim_{z\to{a},z\in{M}}f\left(z\right)=A$, 如果对任意 $\varepsilon>0$ 存在 $\delta>0$ 使对任意 $z\in{M}$, 若 $0<\rho\left(z,a\right)<\delta$ 则 $\rho\left(f\left(z\right),A\right)<\varepsilon$.

> **定义 2.4.2 (函数的有界性和连续性)**
> 
> 若存在 $C>0$ 使 $\forall{z}\in{M}$ 有 $\left|f\left(z\right)\right|\le{C}$, 则称 $f$ 在 $M$ 上有界; 若 $\lim_{z\to{a},z\in{M}}f\left(z\right)=f\left(a\right)$, 则称 $f$ 在点 $a$ 处 (沿 $M$) 连续; 若对 $\forall{a}\in{M}$ 均连续, 则称 $f$ 在 $M$ 上连续.

> **定义 3.1.1 ($\mathbb{R}$-线性与 $\mathbb{C}$-线性)**
> 
> 称 $\ell:\mathbb{C}\to\mathbb{C}$ 为 $\mathbb{R}$-线性 (或 $\mathbb{C}$-线性), 若 $\ell\left(a+b\right)=\ell\left(a\right)+\ell\left(b\right)$, 且对 $\lambda\in\mathbb{R}$ (或 $\mathbb{C}$) 有 $\ell\left(\lambda{z}\right)=\lambda\ell\left(z\right)$; $\mathbb{C}$-线性函数必然是 $\mathbb{R}$-线性的.

> **定义 3.3.1 (可导性)**
> 
> 称 $f$ 在 $a$ 处可导, 若 $\lim_{z\to{a}}\frac{f\left(z\right)-f\left(a\right)}{z-a}=A$ 存在, 记 $A=f'\left(a\right)$.


## ma\complex-analysis\homework-cn\week3.md

> **定义 4.1.2 (共形)**
> 
> 称 $f$ 在 $z$ 处共形, 若 $f$ 在 $z$ 的某邻域上全纯, 单叶且 $f'\left(z\right)\ne0$.

> **定理 4.1.5 (共形判别)**
> 
> $f$ 在 $z$ 处共形当且仅当 $f$ 在 $z$ 处 $\mathbb{C}$-可微且 $f'\left(z\right)\ne0$.

> **定理 4.3.4 (保圆性)**
> 
> 莫比乌斯变换把扩充复平面上的广义圆 (圆或直线) 映成广义圆, 并保持切角.

> **定义 4.4.1 (单叶)**
> 
> 称 $f$ 在区域 $D$ 上单叶, 若 $f$ 在 $D$ 上是单射.

> **定理 4.4.2**
> 
> 若 $f$ 在 $z_{0}$ 处全纯且 $f'\left(z_{0}\right)=0$, 则 $f$ 在 $z_{0}$ 的任意邻域上都不是单叶的.

> **定理 5.1.2 (代数学基本定理)**
> 
> 任意 $n\ge1$ 次多项式在复数域 $\mathbb{C}$ 中至少有一个根.

> **命题 5.4.2 (三角函数的导数)**
> 
> $\sin{z},\cos{z}$ 在 $\mathbb{C}$ 上全纯, $\left(\sin{z}\right)'=\cos{z}$, $\left(\cos{z}\right)'=-\sin{z}$.

> **定义 6.1.1 (幅角函数的连续分支)**
> 
> 称区域 $D\subset\mathbb{C}\setminus\left\{0\right\}$ 上的单值连续函数为 $\operatorname{Arg}z$ 的连续分支, 若 $\forall{z}\in{D}$ 存在 $k\in\mathbb{Z}$ 使 $f\left(z\right)=\arg{z}+2k\pi$.

> **定义 6.2.1 (复变对数函数)**
> 
> 满足 $e^{w}=z$ 的复数 $w$ 称为 $z$ 的对数, 记为 $\operatorname{Ln}z$; 它是无穷多值的.

> **命题 6.2.5 (对数的全纯分支)**
> 
> 区域 $D\subset\mathbb{C}\setminus\left\{0\right\}$ 上的连续对数分支必全纯, 故对数函数的单值连续分支即全纯分支.

> **定义 6.3.1 (幂函数)**
> 
> $z^{\alpha}=e^{\alpha\operatorname{Ln}z}$; 在 $\mathbb{C}\setminus\left(-\infty,0\right]$ 上取主分支, 即 $z^{\alpha}=e^{\alpha\operatorname{Log}z}$.

> **定理 7.2.3**
> 
> $\frac{1}{z}$ 在区域 $D\subset\mathbb{C}\setminus\left\{0\right\}$ 上有原函数当且仅当 $D$ 上存在 $\operatorname{Ln}z$ 的全纯分支.


## ma\complex-analysis\homework-cn\week4.md

> **定义 3.2.2 (形式导数)**
> 
> 形式导数算符为 $\frac{\partial{f}}{\partial{z}}=\frac{1}{2}\left(\frac{\partial{f}}{\partial{x}}-i\frac{\partial{f}}{\partial{y}}\right),\quad\frac{\partial{f}}{\partial\overline{z}}=\frac{1}{2}\left(\frac{\partial{f}}{\partial{x}}+i\frac{\partial{f}}{\partial{y}}\right)$.

> **定义 7.1.1 (路径积分)**
> 
> $f$ 沿分段光滑道路 $\gamma:\left[a,b\right]\to\mathbb{C}$ 的积分为

> **定理 8.1.4 (柯西定理)**
> 
> 若 $f$ 在区域 $D$ 上全纯且 $\gamma_{0},\gamma_{1}$ 是 $D$ 内具有相同端点的同伦道路 (或同伦闭道路), 则 $\int_{\gamma_{0}}f\,dz=\int_{\gamma_{1}}f\,dz$; 特别地 $f$ 沿 $D$ 内闭道路积分为零.

> **定理 9.1.3 (刘维尔定理)**
> 
> $\mathbb{C}$ 上的有界整函数必为常值函数.

> **定理 9.3.3 (唯一性定理)**
> 
> 若区域 $D$ 上的两个全纯函数 $f,g$ 在 $D$ 内有聚点的点集上相等, 则 $f\equiv{g}$.

> **定理 10.1.4 (开映射定理)**
> 
> 非常值的全纯函数把区域映成区域.


## ma\complex-analysis\homework-cn\week5.md

> **定理 8.3.3 (高阶导数公式)**
> 
> 若 $f$ 在单连通区域 $D$ 上全纯, $\gamma$ 是 $D$ 内的分段光滑若当闭曲线, $z$ 在其内区域, 则 $f$ 在 $z$ 处有任意阶导数且

> **定理 9.3.3 (唯一性定理)**
> 
> 若区域 $D$ 上的两个全纯函数 $f,g$ 在 $D$ 内有聚点的点集上相等, 则 $f\equiv{g}$.

> **定理 10.3.1 (施瓦茨引理)**
> 
> 若 $f:\mathbb{D}\to\mathbb{D}$ 全纯且 $f\left(0\right)=0$, 则 $\left|f\left(z\right)\right|\le\left|z\right|$ 且 $\left|f'\left(0\right)\right|\le1$; 等号当且仅当 $f\left(z\right)=e^{i\theta}z$.


## ma\complex-analysis\homework-cn\week6.md

> **定理 10.1.1 (最大模原理)**
> 
> 若区域 $D$ 上的全纯函数 $f$ 的模 $\left|f\right|$ 在 $z_{0}\in{D}$ 处有局部极大值, 则 $f$ 在 $D$ 上为常值.

> **定理 11.2.2 (黎曼映射定理)**
> 
> 任意不为全平面的单连通区域都与开单位圆盘共形等价.

> **定义 11.2.6 (映射半径)**
> 
> 对单连通区域 $D$ 且 $\mathbb{C}\setminus{D}\ne\emptyset$ 及 $a\in{D}$, 称使存在唯一共形等价 $f:D\to\mathbb{D}_{\rho}:=\left\{\left|z\right|<\rho\right\}$, $f\left(a\right)=0$, $f'\left(a\right)=1$ 的正数 $\rho$ 为 $D$ 相对 $a$ 的映射半径 $\rho\left(D,a\right)$.


## ma\complex-analysis\homework-cn\week7.md

> **定理 4.3.4 (保圆性)**
> 
> 莫比乌斯变换把扩充复平面上的广义圆 (圆或直线) 映成广义圆, 并保持切角.

> **命题 5.2.2 (指数映射的带区域)**
> 
> $z\mapsto{e}^{z}$ 把水平带 $\left\{0<\operatorname{Im}z<2\pi\right\}$ 共形地映成 $\mathbb{C}\setminus\left[0,+\infty\right)$.

> **命题 5.2.3 (阿波罗尼奥斯圆)**
> 
> 莫比乌斯变换 $z\mapsto\frac{z-\alpha}{z-\beta}$ ($\alpha,\beta\in\mathbb{C}$) 把不含 $\alpha,\beta$ 的圆映成圆, 且 $\left|z-\alpha\right|/\left|z-\beta\right|$ 在阿波罗尼奥斯圆上为常数.

> **定理 8.3.3 (高阶导数公式)**
> 
> 若 $f$ 在单连通区域 $D$ 上全纯, $\gamma$ 是 $D$ 内的分段光滑若当闭曲线, $z$ 在其内区域, 则 $f$ 在 $z$ 处有任意阶导数且 $f^{\left(n\right)}\left(z\right)=\frac{n!}{2\pi{i}}\int_{\gamma}\frac{f\left(\zeta\right)}{\left(\zeta-z\right)^{n+1}}\,d\zeta$.

> **定理 10.1.1 (最大模原理)**
> 
> 若区域 $D$ 上的全纯函数 $f$ 的模 $\left|f\right|$ 在 $z_{0}\in{D}$ 处有局部极大值, 则 $f$ 在 $D$ 上为常值.

> **定义 10.3.2 (布拉施克因子)**
> 
> 对 $a\in\mathbb{D}$, 称

> **定理 10.3.4 (施瓦茨-皮克引理)**
> 
> 对 $\mathbb{D}\to\mathbb{D}$ 的全纯 $f$,


## ma\complex-analysis\homework-cn\week9.md

> **定理 15.2.7 (幅角原理)**
> 
> 若 $f$ 在区域 $D$ 上亚纯, 零点 $a_{j}$ 的阶为 $r_{j}$, 极点 $p_{k}$ 的阶为 $s_{k}$, $\Gamma$ 是 $D$ 内的若当闭曲线且避开这些点, 则 $\frac{1}{2\pi{i}}\int_{\Gamma}\frac{f'}{f}\,dz=\sum{r}_{j}-\sum{s}_{k}$.

> **定理 16.2.9 (泊松积分)**
> 
> 圆盘 $B\left(a,R\right)$ 上狄利克雷问题有解 $u\left(z\right)=\frac{R^{2}-\left|z-a\right|^{2}}{2\pi{R}}\int_{0}^{2\pi}\frac{f\left(a+Re^{i\theta}\right)}{\left|z-a-Re^{i\theta}\right|^{2}}d\theta$.

> **定理 16.2.10 (有界若当域上的狄利克雷问题)**
> 
> 有界若当域上的狄利克雷问题可解.


## ma\complex-analysis\homework-en\week1.md

> **Definition 1.3.1 (Stereographic Projection)**
> 
> On the unit sphere $S:\xi^{2}+\eta^{2}+\zeta^{2}=1$, the point $z=\left(x,y\right)$ in the complex plane corresponds to $Z=\left(\xi,\eta,\zeta\right),\quad\xi=\frac{2x}{1+\left|z\right|^{2}},\eta=\frac{2y}{1+\left|z\right|^{2}},\zeta=\frac{\left|z\right|^{2}-1}{1+\left|z\right|^{2}}$, establishing a bijection between $\mathbb{C}$ and $S\setminus\left\{N\right\}$ (the sphere minus the north pole).

> **Definition 2.2.4 (Domain)**
> 
> A set $D\subset\mathbb{C}$ (or $\overline{\mathbb{C}}$) is called a domain if: (i-1) $D$ is open; (i-2) $D$ is path-connected, i.e. for any $a,b\in{D}$ there is a path in $D$ with endpoints $a,b$.

> **Definition 2.2.7 (Simply Connected and Multiply Connected)**
> 
> A domain $D\subset\mathbb{C}$ is called simply connected if the interior of every Jordan curve in $D$ is contained in $D$; otherwise it is multiply connected.

> **Definition 2.4.1 (Limit of a Function Along a Set)**
> 
> Let $f$ be defined on $M\subset\overline{\mathbb{C}}$, and let $a\in\overline{\mathbb{C}}$ be a limit point of $M$. We say $A\in\mathbb{C}$ is the limit of $f$ as $z\to{a}$ along $M$, written $\lim_{z\to{a},z\in{M}}f\left(z\right)=A$, if for every $\varepsilon>0$ there exists $\delta>0$ such that for all $z\in{M}$, $0<\rho\left(z,a\right)<\delta$ implies $\rho\left(f\left(z\right),A\right)<\varepsilon$.

> **Definition 2.4.2 (Boundedness and Continuity)**
> 
> If there exists $C>0$ such that $\left|f\left(z\right)\right|\le{C}$ for all $z\in{M}$, then $f$ is bounded on $M$; if $\lim_{z\to{a},z\in{M}}f\left(z\right)=f\left(a\right)$, then $f$ is continuous at $a$ (along $M$); if $f$ is continuous at every $a\in{M}$, then $f$ is continuous on $M$.


## ma\complex-analysis\homework-en\week10.md

> **Definition 16.1.1 (Harmonic Function)**
> 
> A real-valued $C^{2}$ function $u$ on a domain $D$ is called harmonic if $\Delta{u}=u_{xx}+u_{yy}=0$ on $D$.

> **Proposition 16.1.6 (Mean Value Property)**
> 
> A harmonic function $u$ on $B\left(a,R\right)$ satisfies

> **Theorem 16.2.10 (Dirichlet Problem on Bounded Jordan Domains)**
> 
> The Dirichlet problem on a bounded Jordan domain is solvable.

> **Definition 17.2.1 (Function Element)**
> 
> A pair $\left(f,U\right)$ is called a function element if $U$ is a nonempty open set in $\mathbb{C}$ and $f$ is holomorphic on $U$.

> **Theorem 17.3.6 (Monodromy Theorem)**
> 
> If $D$ is simply connected and $\left(f,U\right)$ can be holomorphically continued along every path in $D$, then $f$ extends to a single-valued holomorphic function on $D$.

> **Lemma 18.1.1 (Pasting Lemma)**
> 
> If domains $D_{1},D_{2}$ are disjoint with a common boundary segment $\gamma$, $f_{1},f_{2}$ are holomorphic on them and continuous to $\gamma$, and $f_{1}=f_{2}$ on $\gamma$, then the pasted function is holomorphic on $D_{1}\cup\gamma\cup{D}_{2}$.


## ma\complex-analysis\homework-en\week11.md

> **Lemma 18.1.1 (Pasting Lemma)**
> 
> If domains $D_{1},D_{2}$ are disjoint with a common boundary segment $\gamma$, $f_{1},f_{2}$ are holomorphic on them and continuous to $\gamma$, and $f_{1}=f_{2}$ on $\gamma$, then the pasted function is holomorphic on $D_{1}\cup\gamma\cup{D}_{2}$.

> **Definition 19.1.1 (Gamma Function)**
> 
> The Gamma function is defined by Euler's integral (for real $s>0$): $\Gamma\left(s\right)=\int_{0}^{+\infty}e^{-t}t^{s-1}dt,\quad{s}>0$.

> **Theorem 19.2.1 (Reflection Formula)**
> 
> The Gamma function satisfies the reflection formula $\Gamma\left(z\right)\Gamma\left(1-z\right)=\frac{\pi}{\sin\pi{z}},\quad{z}\in\mathbb{C}\setminus\mathbb{Z}$.

> **Theorem 19.2.3 (Weierstrass Product)**
> 
> The reciprocal of the Gamma function has the Weierstrass infinite product expansion $\frac{1}{\Gamma\left(z\right)}=ze^{\gamma{z}}\prod_{n=1}^{+\infty}\left(1+\frac{z}{n}\right)e^{-\frac{z}{n}}$, where $\gamma$ is the Euler-Mascheroni constant.

> **Definition 20.1.1 (Riemann Zeta Function)**
> 
> The Riemann zeta function is defined for $\operatorname{Re}z>1$ by the Dirichlet series $\zeta\left(z\right)=\sum_{n=1}^{+\infty}\frac1{n^{z}},\quad\operatorname{Re}z>1$; by the Euler product $\zeta\left(z\right)=\prod_{p}\left(1-p^{-z}\right)^{-1}$ it has no zeros.

> **Theorem 20.1.6 (Meromorphic Continuation)**
> 
> $\zeta$ extends meromorphically to $\mathbb{C}$, with only a simple pole at $z=1$, and $\lim_{z\to1}\left(\zeta\left(z\right)-\frac1{z-1}\right)=\gamma$ (Euler constant).

> **Corollary 20.2.3 (Trivial Zeros and Critical Strip)**
> 
> The trivial zeros of $\zeta$ are exactly $-2,-4,-6,\ldots$; all nontrivial zeros lie in the critical strip $0<\operatorname{Re}z<1$.


## ma\complex-analysis\homework-en\week12.md

> **Theorem 20.1.6 (Meromorphic Continuation)**
> 
> $\zeta$ extends meromorphically to $\mathbb{C}$, with only a simple pole at $z=1$, and

> **Theorem 21.1.3 (Bloch's Theorem)**
> 
> There is a constant $B>0$ such that if $f$ is holomorphic on the unit disk with $f'\left(0\right)=1$, then $f\left(\mathbb{D}\right)$ contains a disk of radius at least $B$.

> **Theorem 21.2.4 (Picard's Little Theorem, Meromorphic Form)**
> 
> A nonconstant meromorphic function omits at most two values.

> **Theorem 21.4 (Picard's Great Theorem)**
> 
> In any punctured neighborhood of an essential singularity, a holomorphic function takes every value infinitely often (with at most one exception).

> **Theorem 22.2.3 (Montel's Theorem)**
> 
> A family of meromorphic functions on a domain $D$ that uniformly omits three distinct values (points of the extended plane) is normal.


## ma\complex-analysis\homework-en\week2.md

> **Definition 2.1.2 (Reparametrization of a Path)**
> 
> A path $\gamma_{1}:\left[a_{1},b_{1}\right]\to\mathbb{C}$ is a reparametrization of $\gamma_{2}:\left[a_{2},b_{2}\right]\to\mathbb{C}$ if there is a monotonically increasing function $\tau:\left[a_{1},b_{1}\right]\to\left[a_{2},b_{2}\right]$ with $\tau\left(a_{1}\right)=a_{2}$, $\tau\left(b_{1}\right)=b_{2}$, such that $\gamma_{1}\left(t\right)=\gamma_{2}\left(\tau\left(t\right)\right)$ for all $t\in\left[a_{1},b_{1}\right]$; if $\tau$ has a jump discontinuity at $\overline{t}$, i.e. $\tau\left(\overline{t}-0\right)<\tau\left(\overline{t}+0\right)$, then $\gamma_{2}$ must be constant on the interval $\left[\tau\left(\overline{t}-0\right),\tau\left(\overline{t}+0\right)\right]$.

> **Definition 2.1.4 (Curve)**
> 
> An equivalence class of paths under reparametrization is called a curve.

> **Theorem 2.2.6 (Jordan Curve Theorem)**
> 
> Every Jordan curve in the complex plane divides the plane into two disjoint domains: a bounded one called its interior, and an unbounded one called its exterior.

> **Definition 2.4.1 (Limit of a Function Along a Set)**
> 
> Let $f$ be defined on $M\subset\overline{\mathbb{C}}$, and let $a\in\overline{\mathbb{C}}$ be a limit point of $M$. We say $A\in\mathbb{C}$ is the limit of $f$ as $z\to{a}$ along $M$, written $\lim_{z\to{a},z\in{M}}f\left(z\right)=A$, if for every $\varepsilon>0$ there exists $\delta>0$ such that for all $z\in{M}$, $0<\rho\left(z,a\right)<\delta$ implies $\rho\left(f\left(z\right),A\right)<\varepsilon$.

> **Definition 2.4.2 (Boundedness and Continuity)**
> 
> If there exists $C>0$ such that $\left|f\left(z\right)\right|\le{C}$ for all $z\in{M}$, then $f$ is bounded on $M$; if $\lim_{z\to{a},z\in{M}}f\left(z\right)=f\left(a\right)$, then $f$ is continuous at $a$ (along $M$); if $f$ is continuous at every $a\in{M}$, then $f$ is continuous on $M$.

> **Definition 3.1.1 ($\mathbb{R}$-linear and $\mathbb{C}$-linear)**
> 
> A map $\ell:\mathbb{C}\to\mathbb{C}$ is called $\mathbb{R}$-linear (or $\mathbb{C}$-linear) if $\ell\left(a+b\right)=\ell\left(a\right)+\ell\left(b\right)$ and $\ell\left(\lambda{z}\right)=\lambda\ell\left(z\right)$ for $\lambda\in\mathbb{R}$ (or $\mathbb{C}$); a $\mathbb{C}$-linear map is necessarily $\mathbb{R}$-linear.

> **Definition 3.3.1 (Complex Differentiability)**
> 
> $f$ is differentiable at $a$ if $\lim_{z\to{a}}\frac{f\left(z\right)-f\left(a\right)}{z-a}=A$ exists; write $A=f'\left(a\right)$.

> **Definition 4.2.1 (Mobius Transformation)**
> 
> A function of the form $f\left(z\right)=\frac{az+b}{cz+d}$ (where $a,b,c,d\in\mathbb{C}$ and $ad-bc\ne0$) is called a Mobius transformation (or fractional linear transformation); it is a bijection of the extended complex plane onto itself, and its inverse is also a Mobius transformation.


## ma\complex-analysis\homework-en\week3.md

> **Definition 4.1.2 (Conformal)**
> 
> $f$ is conformal at $z$ if it is holomorphic and univalent on a neighborhood of $z$ and $f'\left(z\right)\ne0$.

> **Theorem 4.1.5 (Criterion for Conformality)**
> 
> $f$ is conformal at $z$ if and only if $f$ is $\mathbb{C}$-differentiable at $z$ and $f'\left(z\right)\ne0$.

> **Definition 4.2.1 (Mobius Transformation)**
> 
> A function of the form

> **Theorem 4.3.4 (Circles Map to Circles)**
> 
> A Mobius transformation maps generalized circles (circles or lines) in the extended plane to generalized circles, and preserves angles of intersection.

> **Definition 4.4.1 (Univalent)**
> 
> $f$ is univalent on a domain $D$ if it is injective on $D$.

> **Theorem 4.4.2**
> 
> If $f$ is holomorphic at $z_{0}$ and $f'\left(z_{0}\right)=0$, then $f$ is not univalent on any neighborhood of $z_{0}$.

> **Theorem 5.1.2 (Fundamental Theorem of Algebra)**
> 
> Every polynomial of degree $n\ge1$ has at least one root in $\mathbb{C}$.

> **Proposition 5.4.2 (Derivatives of Trigonometric Functions)**
> 
> $\sin{z},\cos{z}$ are holomorphic on $\mathbb{C}$, with $\left(\sin{z}\right)'=\cos{z}$, $\left(\cos{z}\right)'=-\sin{z}$.

> **Definition 6.1.1 (Continuous Branch of the Argument)**
> 
> A single-valued continuous function on a domain $D\subset\mathbb{C}\setminus\left\{0\right\}$ is called a continuous branch of $\operatorname{Arg}z$ if for every $z\in{D}$ there exists $k\in\mathbb{Z}$ such that $f\left(z\right)=\arg{z}+2k\pi$.

> **Definition 6.2.1 (Complex Logarithm)**
> 
> A complex number $w$ satisfying $e^{w}=z$ is called a logarithm of $z$, denoted $\operatorname{Ln}z$; it is infinitely many-valued.

> **Proposition 6.2.5 (Holomorphic Branches of the Logarithm)**
> 
> Any continuous branch of the logarithm on a domain $D\subset\mathbb{C}\setminus\left\{0\right\}$ is holomorphic, so a single-valued continuous branch of the logarithm is a holomorphic branch.

> **Definition 6.2.7 (Branch Points)**
> 
> The branch points of the multivalued function $\operatorname{Ln}z$ (or of power functions) are $0$ and $\infty$; single-valued branches can be defined along any cut joining them.

> **Definition 6.3.1 (Power Function)**
> 
> $z^{\alpha}=e^{\alpha\operatorname{Ln}z}$; on $\mathbb{C}\setminus\left(-\infty,0\right]$ take the principal branch, i.e. $z^{\alpha}=e^{\alpha\operatorname{Log}z}$.

> **Definition 7.2.1 (Antiderivative)**
> 
> A holomorphic function $F$ on a domain $D$ is called an antiderivative of $f$ if $F'=f$ on $D$; $f$ has an antiderivative if and only if its integral along every closed path in $D$ is zero.

> **Theorem 7.2.3**
> 
> $\frac{1}{z}$ has an antiderivative on a domain $D\subset\mathbb{C}\setminus\left\{0\right\}$ if and only if $D$ admits a holomorphic branch of $\operatorname{Ln}z$.


## ma\complex-analysis\homework-en\week4.md

> **Definition 3.2.2 (Formal Derivatives)**
> 
> The formal derivative operators are $\frac{\partial{f}}{\partial{z}}=\frac{1}{2}\left(\frac{\partial{f}}{\partial{x}}-i\frac{\partial{f}}{\partial{y}}\right),\quad\frac{\partial{f}}{\partial\overline{z}}=\frac{1}{2}\left(\frac{\partial{f}}{\partial{x}}+i\frac{\partial{f}}{\partial{y}}\right)$.

> **Definition 7.1.1 (Path Integral)**
> 
> The integral of $f$ along a piecewise smooth path $\gamma:\left[a,b\right]\to\mathbb{C}$ is

> **Theorem 8.1.4 (Cauchy's Theorem)**
> 
> If $f$ is holomorphic on a domain $D$ and $\gamma_{0},\gamma_{1}$ are homotopic paths in $D$ with the same endpoints (or homotopic closed paths), then $\int_{\gamma_{0}}f\,dz=\int_{\gamma_{1}}f\,dz$; in particular, the integral of $f$ along any closed path in $D$ is zero.

> **Theorem 9.1.3 (Liouville's Theorem)**
> 
> Every bounded entire function on $\mathbb{C}$ is constant.

> **Theorem 9.3.3 (Uniqueness Theorem)**
> 
> If two holomorphic functions $f,g$ on a domain $D$ agree on a set with an accumulation point in $D$, then $f\equiv{g}$.

> **Theorem 10.1.4 (Open Mapping Theorem)**
> 
> A nonconstant holomorphic function maps domains onto domains.


## ma\complex-analysis\homework-en\week5.md

> **Theorem 8.3.3 (Higher Derivative Formula)**
> 
> If $f$ is holomorphic on a simply connected domain $D$, $\gamma$ is a piecewise smooth Jordan closed curve in $D$, and $z$ lies in its interior, then $f$ has derivatives of all orders at $z$ and

> **Theorem 9.3.3 (Uniqueness Theorem)**
> 
> If two holomorphic functions $f,g$ on a domain $D$ agree on a set with an accumulation point in $D$, then $f\equiv{g}$.

> **Theorem 10.3.1 (Schwarz Lemma)**
> 
> If $f:\mathbb{D}\to\mathbb{D}$ is holomorphic with $f\left(0\right)=0$, then $\left|f\left(z\right)\right|\le\left|z\right|$ and $\left|f'\left(0\right)\right|\le1$; equality holds if and only if $f\left(z\right)=e^{i\theta}z$.


## ma\complex-analysis\homework-en\week6.md

> **Theorem 10.1.1 (Maximum Modulus Principle)**
> 
> If the modulus $\left|f\right|$ of a holomorphic function $f$ on a domain $D$ has a local maximum at $z_{0}\in{D}$, then $f$ is constant on $D$.

> **Definition 11.1.1 (Locally Uniform Convergence)**
> 
> A sequence $\left\{f_{n}\right\}$ of holomorphic functions converges locally uniformly to $f$ on a domain $\Omega$ if it converges uniformly to $f$ on every compact subset of $\Omega$.

> **Theorem 11.2.2 (Riemann Mapping Theorem)**
> 
> Every simply connected domain other than the whole plane is conformally equivalent to the open unit disk.

> **Definition 11.2.6 (Mapping Radius)**
> 
> For a simply connected domain $D$ with $\mathbb{C}\setminus{D}\ne\emptyset$ and $a\in{D}$, the positive number $\rho$ for which there exists a unique conformal equivalence $f:D\to\mathbb{D}_{\rho}:=\left\{\left|z\right|<\rho\right\}$ with $f\left(a\right)=0$, $f'\left(a\right)=1$, is called the mapping radius of $D$ at $a$, denoted $\rho\left(D,a\right)$.


## ma\complex-analysis\homework-en\week7.md

> **Theorem 4.3.4 (Circles Map to Circles)**
> 
> A Mobius transformation maps generalized circles (circles or lines) in the extended plane to generalized circles, and preserves angles of intersection.

> **Proposition 5.2.2 (Exponential Map on a Strip)**
> 
> $z\mapsto{e}^{z}$ maps the horizontal strip $\left\{0<\operatorname{Im}z<2\pi\right\}$ conformally onto $\mathbb{C}\setminus\left[0,+\infty\right)$.

> **Proposition 5.2.3 (Apollonius Circles)**
> 
> The Mobius transformation $z\mapsto\frac{z-\alpha}{z-\beta}$ ($\alpha,\beta\in\mathbb{C}$) maps circles not containing $\alpha,\beta$ to circles, and $\left|z-\alpha\right|/\left|z-\beta\right|$ is constant on Apollonius circles.

> **Definition 6.2.4 (Power Function)**
> 
> $z^{\alpha}=e^{\alpha\log{z}}$ maps the angular sector $\left\{0<\arg{z}<\beta\right\}$ conformally onto the sector $\left\{0<\arg{w}<\alpha\beta\right\}$ (with a suitable holomorphic branch).

> **Theorem 8.3.3 (Higher Derivative Formula)**
> 
> If $f$ is holomorphic on a simply connected domain $D$, $\gamma$ is a piecewise smooth Jordan closed curve in $D$, and $z$ lies in its interior, then $f$ has derivatives of all orders at $z$ and $f^{\left(n\right)}\left(z\right)=\frac{n!}{2\pi{i}}\int_{\gamma}\frac{f\left(\zeta\right)}{\left(\zeta-z\right)^{n+1}}\,d\zeta$.

> **Theorem 10.1.1 (Maximum Modulus Principle)**
> 
> If the modulus $\left|f\right|$ of a holomorphic function $f$ on a domain $D$ has a local maximum at $z_{0}\in{D}$, then $f$ is constant on $D$.

> **Definition 10.3.2 (Blaschke Factor)**
> 
> For $a\in\mathbb{D}$, the function

> **Theorem 10.3.4 (Schwarz-Pick Lemma)**
> 
> For holomorphic $f:\mathbb{D}\to\mathbb{D}$,

> **Definition 11.2.6 (Mapping Radius)**
> 
> For a simply connected domain $D$ with $\mathbb{C}\setminus{D}\ne\emptyset$ and $a\in{D}$, the positive number $\rho$ for which there exists a unique conformal equivalence $f:D\to\mathbb{D}_{\rho}:=\left\{\left|z\right|<\rho\right\}$ with $f\left(a\right)=0$, $f'\left(a\right)=1$, is called the mapping radius of $D$ at $a$, denoted $\rho\left(D,a\right)$.


## ma\complex-analysis\homework-en\week9.md

> **Theorem 15.2.7 (Argument Principle)**
> 
> If $f$ is meromorphic on a domain $D$, the zeros $a_{j}$ have order $r_{j}$, the poles $p_{k}$ have order $s_{k}$, and $\Gamma$ is a Jordan closed curve in $D$ avoiding these points, then $\frac{1}{2\pi{i}}\int_{\Gamma}\frac{f'}{f}\,dz=\sum{r}_{j}-\sum{s}_{k}$.

> **Theorem 16.2.9 (Poisson Integral)**
> 
> The Dirichlet problem on the disk $B\left(a,R\right)$ has solution $u\left(z\right)=\frac{R^{2}-\left|z-a\right|^{2}}{2\pi{R}}\int_{0}^{2\pi}\frac{f\left(a+Re^{i\theta}\right)}{\left|z-a-Re^{i\theta}\right|^{2}}d\theta$.

> **Theorem 16.2.10 (Dirichlet Problem on Bounded Jordan Domains)**
> 
> The Dirichlet problem on a bounded Jordan domain is solvable.


## ma\functional-analysis\homework-cn\week7.md

> **定理 2.2.1 (线性泛函有界 $\Leftrightarrow$ 核闭)**
> 
> 设 $f$ 是赋范线性空间 $X$ 上的线性泛函, 则 $f$ 有界的充要条件是 $\ker{f}$ 是闭的.

> **定理 2.2.6 (埃尔米特泛函的有界性)**
> 
> 设 $\varphi\left(\cdot,\cdot\right)$ 是复希尔伯特空间 $H$ 上的共轭双线性埃尔米特泛函, 且存在常数 $c$ 使得 $\left|\varphi\left(x,x\right)\right|\le{c}\left\|x\right\|^2,\quad\forall{x}\in{H}$, 那么 $\varphi$ 是有界的, 且 $\left\|\varphi\right\|\le{c}$.


## ma\probability\homework-cn\week1.md

> **定理 1.1.1 (概率测度的性质)**
> 
> 设 $\mu$ 为概率测度. 则: (1) $\mu\left(\emptyset\right)=0$; (2) 可数可加性: 对两两不交 $\left\{E_{n}\right\}$, $\mu\left(\bigcup_{n}E_{n}\right)=\sum_{n}\mu\left(E_{n}\right)$; (3) 下连续性: 若 $E_{n}\uparrow{E}$, 则 $\mu\left(E_{n}\right)\uparrow\mu\left(E\right)$.


## ma\probability\homework-cn\week10.md

> **定理 1.5.7 (单调收敛定理)**
> 
> 若 $0\le{f}_{n}$ 且 $f_{n}\uparrow{f}$ 逐点, 则 $\int{f}_{n}\,\mathrm{d}\mu\uparrow\int{f}\,\mathrm{d}\mu$.


## ma\probability\homework-cn\week12.md

> **定义 3.2.1 (依分布收敛)**
> 
> $X_{n}\Rightarrow{X}_{\infty}$ (依分布收敛) 指分布函数 $F_{n}\left(x\right)\to{F}_{\infty}\left(x\right)$ 在 $F_{\infty}$ 的一切连续点上成立.

> **定理 3.3.1 (特征函数的性质)**
> 
> (1) $\phi\left(0\right)=1$; (2) $\phi\left(-t\right)=\overline{\phi\left(t\right)}$; (3) $\left|\phi\left(t\right)\right|\le1$; (4) $\left|\phi\left(t+h\right)-\phi\left(t\right)\right|\le{E}\left|e^{ihX}-1\right|$, 故 $\phi$ 在 $\mathbb{R}$ 上一致连续; (5) $Ee^{it\left(aX+b\right)}=e^{itb}\phi\left(at\right)$.

> **定理 3.3.2 (独立和的特征函数)**
> 
> 若 $X_{1},X_{2}$ 独立且特征函数为 $\phi_{1},\phi_{2}$, 则 $X_{1}+X_{2}$ 的特征函数为 $\phi_{1}\left(t\right)\phi_{2}\left(t\right)$.


## ma\probability\homework-cn\week2.md

> **定理 1.2.1 (分布函数的性质)**
> 
> 设 $F\left(x\right)=P\left(X\le{x}\right)$, 则: (1) $F$ 非降; (2) $\lim_{x\to\infty}F\left(x\right)=1$, $\lim_{x\to-\infty}F\left(x\right)=0$; (3) $F$ 右连续, 即 $\lim_{y\downarrow{x}}F\left(y\right)=F\left(x\right)$; (4) 若 $F\left(x-\right)=\lim_{y\uparrow{x}}F\left(y\right)$, 则 $F\left(x-\right)=P\left(X<{}x\right)$; (5) $P\left(X=x\right)=F\left(x\right)-F\left(x-\right)$.

> **定义 1.2.2 (分布与分布函数)**
> 
> $X$ 在 $\left(\mathbb{R},\mathcal{R}\right)$ 上诱导的概率测度 $\mu\left(A\right)=P\left(X\in{A}\right)$ 称为 $X$ 的分布; 其分布函数为 $F\left(x\right)=P\left(X\le{x}\right)$.

> **定理 1.2.2 (分布函数的逆)**
> 
> 设 $F$ 是分布函数. 定义其逆 $F^{-1}\left(y\right)=\sup\left\{x:F\left(x\right)<{}y\right\}$, $y\in\left(0,1\right)$. 若 $U$ 服从 $\left(0,1\right)$ 上的均匀分布, 则 $F^{-1}\left(U\right)$ 以 $F$ 为分布函数. 该构造也是计算机生成随机变量的标准方法.

> **定理 1.3.4 (复合可测)**
> 
> 若 $X:\left(\Omega,\mathcal{F}\right)\to\left(S,\mathcal{S}\right)$ 与 $f:\left(S,\mathcal{S}\right)\to\left(T,\mathcal{T}\right)$ 均可测, 则 $f\left(X\right)$ 是 $\left(\Omega,\mathcal{F}\right)\to\left(T,\mathcal{T}\right)$ 的可测映射. 特别地, $cX$, $X^{2}$, $\sin{X}$ 等均为随机变量.


## ma\probability\homework-cn\week4.md

> **公式 1.3.1 (由 $X$ 生成的 $\sigma$-代数)**
> 
> $\sigma\left(X\right)=\left\{\left\{X\in{B}\right\}:B\in\mathcal{S}\right\}$ 是使 $X$ 可测的最小 $\sigma$-代数.


## ma\probability\homework-cn\week6.md

> **例 1.6.13 (泊松分布)**
> 
> $Z$ 服从参数为 $\lambda$ 的泊松分布, 记 $Z\sim\mathrm{泊松}\left(\lambda\right)$, 指 $P\left(Z=k\right)=e^{-\lambda}\lambda^{k}/k!$, $k=0,1,2,\dots$.

> **定义 2.1.1 (独立事件)**
> 
> 事件 $A,B\in\mathcal{F}$ 独立指 $P\left(A\cap{B}\right)=P\left(A\right)P\left(B\right)$. 事件列 $A_{1},\dots,A_{n}$ 独立指对任意 $I\subset\left\{1,\dots,n\right\}$ 有 $P\left(\cap_{i\in{I}}A_{i}\right)=\prod_{i\in{I}}P\left(A_{i}\right)$.

> **定理 2.1.1 (独立与 $\sigma$-代数)**
> 
> (1) 若 $X,Y$ 独立, 则 $\sigma\left(X\right)$ 与 $\sigma\left(Y\right)$ 独立; (2) 若 $\mathcal{A}_{1},\dots,\mathcal{A}_{n}$ 独立, 则 $\sigma\left(\mathcal{A}_{1}\right),\dots,\sigma\left(\mathcal{A}_{n}\right)$ 独立. 故验证随机变量独立可只对生成元进行.

> **定义 2.1.3 (不相关)**
> 
> 若 $EX^{2},EY^{2}<\infty$ 且 $EXY=EX\cdot{E}Y$, 称 $X,Y$ 不相关. 独立蕴含不相关, 但不相关不蕴含独立.

> **习题 2.1.10 (卷积公式)**
> 
> 若 $X,Y$ 独立且取整数值, 则 $P\left(X+Y=n\right)=\sum_{m}P\left(X=m\right)P\left(Y=n-m\right)$.

> **定理 2.1.13 (独立变量的乘积期望)**
> 
> 若 $X_{1},\dots,X_{n}$ 独立且 (a) 各 $X_{i}\ge0$, 或 (b) 各 $E\left|X_{i}\right|<\infty$, 则 $E\left(\prod_{i=1}^{n}X_{i}\right)=\prod_{i=1}^{n}EX_{i}$.

> **定理 2.1.16 (密度与独立)**
> 
> 设 $X_{1},\dots,X_{n}$ 有联合密度 $f$. 若 $f$ 可写成 $f\left(x_{1},\dots,x_{n}\right)=g_{1}\left(x_{1}\right)\cdots{g}_{n}\left(x_{n}\right)$ ($g_{i}\ge0$ 可测), 则 $X_{1},\dots,X_{n}$ 独立; 反之, 若 $X_{1},\dots,X_{n}$ 独立且各有密度, 则联合密度为边缘密度之积.


## ma\probability\homework-cn\week7.md

> **定理 1.7.2 (富比尼定理)**
> 
> 若 $f\ge0$, 则 (托内利)

> **定理 2.1.13 (独立变量的乘积期望)**
> 
> 若 $X_{1},\dots,X_{n}$ 独立且 (a) 各 $X_{i}\ge0$, 或 (b) 各 $E\left|X_{i}\right|<\infty$, 则

> **定理 2.1.16 (密度与独立)**
> 
> 设 $X_{1},\dots,X_{n}$ 有联合密度 $f$. 若 $f$ 可写成 $f\left(x_{1},\dots,x_{n}\right)=g_{1}\left(x_{1}\right)\cdots{g}_{n}\left(x_{n}\right)$ ($g_{i}\ge0$ 可测), 则 $X_{1},\dots,X_{n}$ 独立; 反之, 若 $X_{1},\dots,X_{n}$ 独立且各有密度, 则联合密度为边缘密度之积.


## ma\probability\homework-cn\week8.md

> **定理 1.6.4 (切比雪夫不等式)**
> 
> 若 $\phi:\mathbb{R}\to\mathbb{R}$ 非负, 非降, $\phi\left(a\right)>0$, 则 $P\left(X\ge{a}\right)\le{E}\phi\left(X\right)/\phi\left(a\right)$. 取 $\phi\left(y\right)=y$ 得马尔可夫不等式 $P\left(Y>a\right)\le{E}Y/a$.


## ma\probability\homework-cn\week9.md

> **定理 1.7.2 (富比尼/托内利定理)**
> 
> 对非负可测 $h$ 与任意随机变量 $X$, 若 $H\left(x\right)=\int_{\left(-\infty,x\right]}h\left(y\right)\,\mathrm{d}y$, 则由托内利定理 $EH\left(X\right)=\int_{-\infty}^{\infty}h\left(y\right)P\left(X\ge{y}\right)\,\mathrm{d}y$. (半开区间含右端点, 故尾部用 $X\ge{y}$; 这是引理 2.2.13 的推广, 取 $h\left(y\right)=py^{p-1}\mathbf{1}_{\left\{y\ge0\right\}}$ 即还原.)

> **引理 2.2.13 (矩的尾部公式)**
> 
> 若 $Y\ge0$ 且 $p>0$, 则 $E\left(Y^{p}\right)=\int_{0}^{\infty}py^{p-1}P\left(Y>y\right)\,\mathrm{d}y$. 它是"对尾部 $P\left(Y>y\right)$ 逐层积分"思想的体现.


## ma\probability\homework-en\week10.md

> **Theorem 1.5.7 (Monotone Convergence Theorem)**
> 
> If $0\le{f}_{n}$ and $f_{n}\uparrow{f}$ pointwise, then $\int{f}_{n}\,\mathrm{d}\mu\uparrow\int{f}\,\mathrm{d}\mu$.


## ma\probability\homework-en\week12.md

> **Definition 3.2.1 (Convergence in Distribution)**
> 
> $X_{n}\Rightarrow{X}_{\infty}$ (convergence in distribution) means that the distribution functions satisfy $F_{n}\left(x\right)\to{F}_{\infty}\left(x\right)$ at every continuity point $x$ of $F_{\infty}$.

> **Definition 3.3.1 (Characteristic Function)**
> 
> The characteristic function of a random variable $X$ is $\phi_{X}\left(t\right)=Ee^{itX}=\int{e}^{itx}\,\mu\left(\mathrm{d}x\right)$, where $\mu$ is the distribution of $X$.

> **Theorem 3.3.1 (Properties of Characteristic Functions)**
> 
> (1) $\phi\left(0\right)=1$; (2) $\phi\left(-t\right)=\overline{\phi\left(t\right)}$; (3) $\left|\phi\left(t\right)\right|\le1$; (4) $\left|\phi\left(t+h\right)-\phi\left(t\right)\right|\le{E}\left|e^{ihX}-1\right|$, so $\phi$ is uniformly continuous on $\mathbb{R}$; (5) $Ee^{it\left(aX+b\right)}=e^{itb}\phi\left(at\right)$.

> **Theorem 3.3.2 (Characteristic Function of a Sum of Independent Variables)**
> 
> If $X_{1},X_{2}$ are independent with characteristic functions $\phi_{1},\phi_{2}$, then the characteristic function of $X_{1}+X_{2}$ is $\phi_{1}\left(t\right)\phi_{2}\left(t\right)$.


## ma\probability\homework-en\week2.md

> **Theorem 1.2.1 (Properties of a Distribution Function)**
> 
> Let $F\left(x\right)=P\left(X\le{x}\right)$. Then: (1) $F$ is nondecreasing; (2) $\lim_{x\to\infty}F\left(x\right)=1$, $\lim_{x\to-\infty}F\left(x\right)=0$; (3) $F$ is right-continuous, i.e. $\lim_{y\downarrow{x}}F\left(y\right)=F\left(x\right)$; (4) if $F\left(x-\right)=\lim_{y\uparrow{x}}F\left(y\right)$, then $F\left(x-\right)=P\left(X<{}x\right)$; (5) $P\left(X=x\right)=F\left(x\right)-F\left(x-\right)$.

> **Definition 1.2.2 (Distribution and Distribution Function)**
> 
> The probability measure $\mu\left(A\right)=P\left(X\in{A}\right)$ induced by $X$ on $\left(\mathbb{R},\mathcal{R}\right)$ is called the distribution of $X$; its distribution function is $F\left(x\right)=P\left(X\le{x}\right)$.

> **Theorem 1.2.2 (Inverse of a Distribution Function)**
> 
> Let $F$ be a distribution function. Define its inverse by $F^{-1}\left(y\right)=\sup\left\{x:F\left(x\right)<{}y\right\}$, $y\in\left(0,1\right)$. If $U$ is uniform on $\left(0,1\right))$, then $F^{-1}\left(U\right)$ has distribution function $F$. This construction is also the standard method for generating random variables on a computer.

> **Theorem 1.3.4 (Composition of Measurable Maps)**
> 
> If $X:\left(\Omega,\mathcal{F}\right)\to\left(S,\mathcal{S}\right)$ and $f:\left(S,\mathcal{S}\right)\to\left(T,\mathcal{T}\right)$ are both measurable, then $f\left(X\right)$ is a measurable map from $\left(\Omega,\mathcal{F}\right)$ to $\left(T,\mathcal{T}\right)$. In particular, $cX$, $X^{2}$, $\sin{X}$, etc. are all random variables.


## ma\probability\homework-en\week4.md

> **Formula 1.3.1 (The $\sigma$-algebra Generated by $X$)**
> 
> $\sigma\left(X\right)=\left\{\left\{X\in{B}\right\}:B\in\mathcal{S}\right\}$ is the smallest $\sigma$-algebra making $X$ measurable.

> **Definition 1.3.3 (Simple Function)**
> 
> A function $\phi:\Omega\to\mathbb{R}$ is called a simple function if $\phi\left(\omega\right)=\sum_{m=1}^{n}c_{m}\mathbf{1}_{A_{m}}\left(\omega\right)$, where $c_{m}\in\mathbb{R}$ and $A_{m}\in\mathcal{F}$.


## ma\probability\homework-en\week6.md

> **Example 1.6.13 (Poisson Distribution)**
> 
> $Z$ has the Poisson distribution with parameter $\lambda$, written $Z\sim\mathrm{Poisson}\left(\lambda\right)$, meaning $P\left(Z=k\right)=e^{-\lambda}\lambda^{k}/k!$ for $k=0,1,2,\dots$.

> **Definition 2.1.1 (Independent Events)**
> 
> Events $A,B\in\mathcal{F}$ are independent if $P\left(A\cap{B}\right)=P\left(A\right)P\left(B\right)$. A sequence $A_{1},\dots,A_{n}$ is independent if for every $I\subset\left\{1,\dots,n\right\}$, $P\left(\cap_{i\in{I}}A_{i}\right)=\prod_{i\in{I}}P\left(A_{i}\right)$.

> **Theorem 2.1.1 (Independence and $\sigma$-algebras)**
> 
> (1) If $X,Y$ are independent, then $\sigma\left(X\right)$ and $\sigma\left(Y\right)$ are independent; (2) if $\mathcal{A}_{1},\dots,\mathcal{A}_{n}$ are independent, then $\sigma\left(\mathcal{A}_{1}\right),\dots,\sigma\left(\mathcal{A}_{n}\right)$ are independent. Hence to verify independence of random variables it suffices to check on generators.

> **Definition 2.1.3 (Uncorrelated)**
> 
> If $EX^{2},EY^{2}<\infty$ and $EXY=EX\cdot{E}Y$, then $X,Y$ are uncorrelated. Independence implies uncorrelatedness, but uncorrelatedness does not imply independence.

> **Exercise 2.1.10 (Convolution Formula)**
> 
> If $X,Y$ are independent and integer-valued, then $P\left(X+Y=n\right)=\sum_{m}P\left(X=m\right)P\left(Y=n-m\right)$.

> **Theorem 2.1.13 (Expectation of a Product of Independent Variables)**
> 
> If $X_{1},\dots,X_{n}$ are independent and either (a) each $X_{i}\ge0$, or (b) each $E\left|X_{i}\right|<\infty$, then $E\left(\prod_{i=1}^{n}X_{i}\right)=\prod_{i=1}^{n}EX_{i}$.

> **Theorem 2.1.16 (Density and Independence)**
> 
> Let $X_{1},\dots,X_{n}$ have joint density $f$. If $f$ can be written as $f\left(x_{1},\dots,x_{n}\right)=g_{1}\left(x_{1}\right)\cdots{g}_{n}\left(x_{n}\right)$ ($g_{i}\ge0$ measurable), then $X_{1},\dots,X_{n}$ are independent; conversely, if $X_{1},\dots,X_{n}$ are independent and each has a density, then the joint density is the product of the marginal densities.


## ma\probability\homework-en\week7.md

> **Theorem 1.7.2 (Fubini's Theorem)**
> 
> If $f\ge0$, then (Tonelli)

> **Theorem 2.1.13 (Expectation of a Product of Independent Variables)**
> 
> If $X_{1},\dots,X_{n}$ are independent and either (a) each $X_{i}\ge0$, or (b) each $E\left|X_{i}\right|<\infty$, then

> **Theorem 2.1.16 (Density and Independence)**
> 
> Let $X_{1},\dots,X_{n}$ have joint density $f$. If $f$ can be written as $f\left(x_{1},\dots,x_{n}\right)=g_{1}\left(x_{1}\right)\cdots{g}_{n}\left(x_{n}\right)$ ($g_{i}\ge0$ measurable), then $X_{1},\dots,X_{n}$ are independent; conversely, if $X_{1},\dots,X_{n}$ are independent and each has a density, then the joint density is the product of the marginal densities.


## ma\probability\homework-en\week8.md

> **Theorem 1.6.4 (Chebyshev's Inequality)**
> 
> If $\phi:\mathbb{R}\to\mathbb{R}$ is nonnegative and nondecreasing with $\phi\left(a\right)>0$, then $P\left(X\ge{a}\right)\le{E}\phi\left(X\right)/\phi\left(a\right)$. Taking $\phi\left(y\right)=y$ gives Markov's inequality $P\left(Y>a\right)\le{E}Y/a$.

> **Theorem 2.2.3 ($L^{2}$ Weak Law of Large Numbers)**
> 
> If $X_{1},X_{2},\dots$ are pairwise uncorrelated, $EX_{i}=\mu$, $\mathrm{var}\left(X_{i}\right)\le{C}<\infty$, and $S_{n}=X_{1}+\dots+X_{n}$, then as $n\to\infty$, $S_{n}/n\to\mu$ in $L^{2}$ and in probability.


## ma\probability\homework-en\week9.md

> **Theorem 1.7.2 (Fubini/Tonelli Theorem)**
> 
> For a nonnegative measurable $h$ and any random variable $X$, if $H\left(x\right)=\int_{\left(-\infty,x\right]}h\left(y\right)\,\mathrm{d}y$, then by Tonelli's theorem $EH\left(X\right)=\int_{-\infty}^{\infty}h\left(y\right)P\left(X\ge{y}\right)\,\mathrm{d}y$. (The half-open interval includes the right endpoint, so the tail uses $X\ge{y}$; this generalizes Lemma 2.2.13, recovered by taking $h\left(y\right)=py^{p-1}\mathbf{1}_{\left\{y\ge0\right\}}$.)

> **Lemma 2.2.13 (Tail Formula for Moments)**
> 
> If $Y\ge0$ and $p>0$, then $E\left(Y^{p}\right)=\int_{0}^{\infty}py^{p-1}P\left(Y>y\right)\,\mathrm{d}y$. This embodies the idea of "integrating layer by layer over the tail $P\left(Y>y\right)$".


## ma\real-analysis\homework-cn\week1.md

> **定义 4.5.7 (任意乘积 $\sigma$-代数)**
> 
> 设 $\left\{\left(X_{\alpha},\mathcal{F}_{\alpha}\right)\right\}_{\alpha\in{I}}$ 是一族可测空间, 乘积 $\sigma$-代数 $\bigotimes_{\alpha\in{I}}\mathcal{F}_{\alpha}$ 是由所有柱集 $\left\{x=\left(x_{\alpha}\right)_{\alpha\in{I}}\in\prod_{\alpha\in{I}}X_{\alpha}:x_{\beta}\in{A}_{\beta}\right\},A_{\beta}\in\mathcal{F}_{\beta},\beta\in{I}$ 生成的 $\sigma$-代数.


## ma\real-analysis\homework-cn\week10.md

> **定理 10.2.2 (托内利定理)**
> 
> 如果 $f:X\times{Y}\to\left[0,\infty\right]$ 是 $\mathcal{A}\otimes\mathcal{B}$-可测的, 则 $\int_{X\times{Y}}f\,\mathrm{d}\left(\mu\times\nu\right)=\int_{X}\left(\int_{Y}f\left(x,y\right)\mathrm{d}\nu\left(y\right)\right)\mathrm{d}\mu\left(x\right)=\int_{Y}\left(\int_{X}f\left(x,y\right)\mathrm{d}\mu\left(x\right)\right)\mathrm{d}\nu\left(y\right)$, 其中所有积分值都在 $\left[0,\infty\right]$ 中.

> **定理 11.5.5 (拉东-尼科迪姆定理)**
> 
> 设 $\mu$ 是 $\sigma$-有限正测度, $\nu$ 是符号测度且 $\nu\ll\mu$, 则存在可测函数 $f:X\to\mathbb{R}$ 使得 $\nu\left(E\right)=\int_{E}f\,\mathrm{d}\mu$ 对一切 $E\in\mathcal{F}$ 成立; 且 $\nu^{+}\left(E\right)=\int_{E}f^{+}\mathrm{d}\mu$, $\nu^{-}\left(E\right)=\int_{E}f^{-}\mathrm{d}\mu$, $\left|\nu\right|\left(E\right)=\int_{E}\left|f\right|\mathrm{d}\mu$. 函数 $f$ 称为 $\nu$ 关于 $\mu$ 的拉东-尼科迪姆导数, 记作 $f=\frac{\mathrm{d}\nu}{\mathrm{d}\mu}$.


## ma\real-analysis\homework-cn\week11.md

> **命题 11.1.2 (符号测度的基本性质)**
> 
> 设 $\nu$ 是符号测度, 则: (1) 有限可加性: 对任意有限个互不相交的 $E_{1},\dots,E_{n}\in\mathcal{F}$, 有 $\nu\left(\bigcup_{i=1}^{n}E_{i}\right)=\sum_{i=1}^{n}\nu\left(E_{i}\right)$; (2) 下连续性: 若 $\left\{E_{j}\right\}$ 单调上升可测, 则 $\lim_{j\to\infty}\nu\left(E_{j}\right)=\nu\left(\bigcup_{j}E_{j}\right)$; (3) 上连续性: 若 $\left\{E_{j}\right\}$ 单调下降可测且 $\nu\left(E_{1}\right)<\infty$, 则 $\lim_{j\to\infty}\nu\left(E_{j}\right)=\nu\left(\bigcap_{j}E_{j}\right)$.

> **定义 11.2.1 (正集,负集,零集)**
> 
> 设 $\nu$ 是 $\left(X,\mathcal{F}\right)$ 上的符号测度. 称 $P\in\mathcal{F}$ 为正集 (记为 $P\gtrsim0$), 若对任意 $E\in\mathcal{F}$ 且 $E\subset{P}$, 有 $\nu\left(E\right)\ge0$; 称 $N\in\mathcal{F}$ 为负集 (记为 $N\lesssim0$), 若对任意 $E\in\mathcal{F}$ 且 $E\subset{N}$, 有 $\nu\left(E\right)\le0$; 称 $Z\in\mathcal{F}$ 为零集, 若对任意 $E\in\mathcal{F}$ 且 $E\subset{Z}$, 有 $\nu\left(E\right)=0$.

> **引理 11.2.2 (正集的性质)**
> 
> (1) 正集的任意可测子集是正集; (2) 正集的可列并是正集; (3) 若 $\left\{P_{n}\right\}$ 是正集列, 则 $\bigcap_{n=1}^{\infty}P_{n}$ 是正集. 上述性质对负集仍然成立.

> **引理 11.2.4 (非负集的判定)**
> 
> 设 $\nu$ 是符号测度. 若 $E$ 不是负集, 则存在正集 $F\subset{E}$ 使得 $\nu\left(F\right)>0$.

> **定理 11.3.2 (哈恩分解定理)**
> 
> 设 $\nu$ 是 $\left(X,\mathcal{F}\right)$ 上的符号测度, 则存在 $X$ 的分解 $X=P\cup{N}$, 其中 $P$ 是正集, $N$ 是负集, $P\cap{N}=\emptyset$; 并且该分解在相差一个 $\nu$-零集的意义下是唯一的.

> **定理 11.4.3 (若尔当分解定理)**
> 
> 设 $\nu$ 是 $\left(X,\mathcal{F}\right)$ 上的符号测度, 则存在唯一的一对相互奇异的正测度 $\nu^{+}$ 和 $\nu^{-}$, 使得 $\nu=\nu^{+}-\nu^{-}$.

> **定义 11.4.4 (变差测度)**
> 
> 设 $\nu$ 是符号测度, 其若尔当分解为 $\nu=\nu^{+}-\nu^{-}$. 称 $\nu^{+}$ 为 $\nu$ 的正变差, $\nu^{-}$ 为 $\nu$ 的负变差, $\left|\nu\right|=\nu^{+}+\nu^{-}$ 为 $\nu$ 的全变差测度.

> **注 11.5.3 (积分关于测度的绝对连续)**
> 
> 设 $f\in{L}^{1}\left(\mu\right)$, 则 $\lim_{\mu\left(E\right)\to0}\int_{E}f\,\mathrm{d}\mu=0$.


## ma\real-analysis\homework-cn\week12.md

> **定理 14.0.10 (有界变差函数的间断点性质)**
> 
> 若 $f\in{B}V\left(\left[a,b\right]\right)$, 则: (1) $f$ 的不连续点至多可数; (2) 所有不连续点都是第一类间断点.


## ma\real-analysis\homework-cn\week2.md

> **定理 1.2.9 (德摩根定律)**
> 
> $\left(A\cup{B}\right)^{c}=A^{c}\cap{B}^{c}$, $\left(A\cap{B}\right)^{c}=A^{c}\cup{B}^{c}$.

> **定理 3.2.1 (实数中开集的构造)**
> 
> 设 $U\subset\mathbb{R}$ 是非空开集, 则存在一列互不相交的开区间 $\left\{I_{n}\right\}_{n=1}^{\infty}$, 使 $U=\bigcup_{n=1}^{\infty}I_{n}$; 且此表示在重排意义下唯一.

> **定义 4.1.1 (集合代数)**
> 
> 设 $X$ 是非空集合, $\mathcal{A}\subset\mathcal{P}\left(X\right)$. 称 $\mathcal{A}$ 为 $X$ 上的一个集合代数, 若满足: (1) $X\in\mathcal{A}$; (2) 对差运算封闭: $A,B\in\mathcal{A}\Rightarrow{A}\setminus{B}\in\mathcal{A}$; (3) 对有限并封闭: $A,B\in\mathcal{A}\Rightarrow{A}\cup{B}\in\mathcal{A}$.

> **命题 4.1.2 (代数的等价定义)**
> 
> 设 $\mathcal{A}\subset\mathcal{P}\left(X\right)$, 则以下条件等价: (1) $\mathcal{A}$ 是代数; (2) $\mathcal{A}$ 满足: (a) $X\in\mathcal{A}$; (b) 对补运算封闭: $A\in\mathcal{A}\Rightarrow{A}^{c}=X\setminus{A}\in\mathcal{A}$; (c) 对有限并封闭: $A,B\in\mathcal{A}\Rightarrow{A}\cup{B}\in\mathcal{A}$.

> **定义 4.2.1 (生成代数)**
> 
> 包含 $\mathcal{E}\subset\mathcal{P}\left(X\right)$ 的最小代数称为由 $\mathcal{E}$ 生成的代数, 记作 $\alpha\left(\mathcal{E}\right)$:

> **定义 4.2.2 (生成 $\sigma$-代数)**
> 
> 包含 $\mathcal{E}\subset\mathcal{P}\left(X\right)$ 的最小 $\sigma$-代数称为由 $\mathcal{E}$ 生成的 $\sigma$-代数, 记作 $\sigma\left(\mathcal{E}\right)$:

> **定义 4.3.2 (博雷尔 $\sigma$-代数)**
> 
> 设 $\left(X,\tau\right)$ 是拓扑空间, 由所有开集生成的 $\sigma$-代数称为博雷尔 $\sigma$-代数, 记作 $\mathcal{B}\left(X\right)$, 其中元素称为博雷尔集.

> **例 4.3.3 (实数上的博雷尔代数)**
> 
> 在 $\mathbb{R}$ 上, 以下集合族生成相同的博雷尔 $\sigma$-代数 $\mathcal{B}\left(\mathbb{R}\right)$: 所有开集 $\tau$, 所有闭集 $\mathcal{F}$, 所有开区间 $\left\{\left(a,b\right)\right\}$, 所有闭区间 $\left\{\left[a,b\right]\right\}$, 所有左开右闭区间 $\left\{\left(a,b\right]\right\}$, 即

> **定义 4.5.1 (可测矩形与乘积 $\sigma$-代数)**
> 
> 设 $\left(X,\mathcal{F}\right)$, $\left(Y,\mathcal{G}\right)$ 为可测空间. $A\times{B}\subseteq{X}\times{Y}$ 称为可测矩形, 若 $A\in\mathcal{F}$ 且 $B\in\mathcal{G}$. 乘积 $\sigma$-代数为包含所有可测矩形的最小 $\sigma$-代数:

> **定理 4.5.3 (截面可测性)**
> 
> 若 $E\in\mathcal{F}\otimes\mathcal{G}$, 则对任意 $x\in{X}$, $y\in{Y}$, 其截面都可测:

> **定理 4.5.4 (博雷尔集的乘积)**
> 
> 对欧氏空间中的博雷尔 $\sigma$-代数, 有


## ma\real-analysis\homework-cn\week3.md

> **定义 1.3.1 (上极限)**
> 
> 集列 $\left\{E_{n}\right\}$ 的上极限定义为

> **定义 1.3.3 (下极限)**
> 
> 集列 $\left\{E_{n}\right\}$ 的下极限定义为

> **定义 5.4.1 (零集)**
> 
> 设 $\left(X,\mathcal{F},\mu\right)$ 是测度空间. 集合 $N\in\mathcal{F}$ 称为零集, 若 $\mu\left(N\right)=0$.

> **定义 5.4.2 (零测度集)**
> 
> 集合 $A\subset{X}$ 称为零测度集, 若存在 $N\in\mathcal{F}$ 使得 $A\subset{N}$ 且 $\mu\left(N\right)=0$.

> **定理 5.4.6 (测度完备化定理)**
> 
> 任意测度空间 $\left(X,\mathcal{F},\mu\right)$ 都可以完备化, 即存在完备测度空间 $\left(X,\mathcal{M},\overline\mu\right)$ 使得: (1) $\mathcal{F}\subset\mathcal{M}$; (2) $\overline\mu|_{\mathcal{F}}=\mu$; (3) $\mathcal{M}$ 是包含 $\mathcal{F}$ 的最小完备 $\sigma$-代数. 具体地, 令 $\mathcal{N}=\left\{N\in\mathcal{F}:\mu\left(N\right)=0\right\}$, $\mathcal{M}=\left\{A\subset{X}:\exists\,B\in\mathcal{F},\exists\,N\in\mathcal{N},B\subset{A}\subset{B}\cup{N}\right\}$, 并定义 $\overline\mu\left(A\right)=\mu\left(B\right)$.

> **定理 6.4.5 (勒贝格-斯蒂尔杰斯测度的正则性)**
> 
> 设 $\mu_{F}$ 是由增右连续函数 $F$ 生成的勒贝格-斯蒂尔杰斯测度, $\mathcal{M}^{*}$ 是 $\mu_{F}$-可测集的 $\sigma$-代数. 若 $E\in\mathcal{M}^{*}$, 则 $\mu_{F}\left(E\right)=\inf\left\{\mu_{F}\left(U\right):E\subset{U},U\text{~开}\right\}=\sup\left\{\mu_{F}\left(K\right):K\subset{E},K\text{~紧}\right\}$.

> **定义 6.4.6 (勒贝格测度)**
> 
> 由 $F\left(x\right)=x$ 生成的测度称为勒贝格测度, 记作 $m$; 相应外测度定义的可测集称为勒贝格可测集, 全体记作 $\mathcal{L}$.

> **定义 6.5.1 (康托尔集的递归构造)**
> 
> 设 $C_{0}=\left[0,1\right]$. 对每个 $n\ge0$, 定义 $C_{n+1}=\frac{1}{3}C_{n}\cup\left(\frac{2}{3}+\frac{1}{3}C_{n}\right)$. 则康托尔集定义为 $C=\bigcap_{n=0}^{\infty}C_{n}$.

> **定理 6.5.2 (康托尔集的三进制刻画)**
> 
> 点 $x\in\left[0,1\right]$ 属于康托尔集 $C$ 当且仅当它的三进制展开 $x=\sum_{k=1}^{\infty}\frac{a_{k}}{3^{k}}$ 中不含数字 $1$ (即 $a_{k}\in\left\{0,2\right\}$).


## ma\real-analysis\homework-cn\week4.md

> **定义 4.1.1 (集合代数)**
> 
> 设 $X$ 是非空集合, $\mathcal{A}\subset\mathcal{P}\left(X\right)$. 称 $\mathcal{A}$ 为 $X$ 上的一个集合代数, 若满足: (1) $X\in\mathcal{A}$; (2) 对差运算封闭: $A,B\in\mathcal{A}\Rightarrow{A}\setminus{B}\in\mathcal{A}$; (3) 对有限并封闭: $A,B\in\mathcal{A}\Rightarrow{A}\cup{B}\in\mathcal{A}$.

> **定义 4.4.1 (单调类)**
> 
> 设 $\mathcal{M}\subset\mathcal{P}\left(X\right)$. 称 $\mathcal{M}$ 为单调类, 若满足: (1) 对单调递增序列封闭: $A_{1}\subset{A}_{2}\subset\cdots$ 且 $A_{n}\in\mathcal{M}\Rightarrow\bigcup_{n=1}^{\infty}A_{n}\in\mathcal{M}$; (2) 对单调递减序列封闭: $A_{1}\supset{A}_{2}\supset\cdots$ 且 $A_{n}\in\mathcal{M}\Rightarrow\bigcap_{n=1}^{\infty}A_{n}\in\mathcal{M}$.

> **定理 4.4.2 (单调类定理)**
> 
> 设 $\mathcal{A}$ 是一个代数, $\mathcal{M}$ 是一个包含 $\mathcal{A}$ 的单调类, 则 $\sigma\left(\mathcal{A}\right)\subset\mathcal{M}$.

> **命题 5.2.1 (有限可加性)**
> 
> 设 $\mu$ 是 $\left(X,\mathcal{F}\right)$ 上的测度, $E_{1},\dots,E_{n}\in\mathcal{F}$ 是两两不交的集合, 则

> **命题 5.2.3 (次可数可加性)**
> 
> 设 $\mu$ 是测度, $\left\{E_{n}\right\}_{n=1}^{\infty}\subset\mathcal{F}$ 是任意可数个集合 (不一定两两不交), 则

> **命题 5.2.4 (下连续性)**
> 
> 设 $\mu$ 是测度, $\left\{E_{n}\right\}_{n=1}^{\infty}\subset\mathcal{F}$ 是单调递增的集合序列 (即 $E_{1}\subset{E}_{2}\subset\cdots$), 则

> **引理 6.3.2 (代数含于可测集)**
> 
> 如果 $\mathcal{E}$ 是代数, $\mu_{0}$ 是准测度, 则 $\mathcal{E}\subset\mathcal{M}_{\mu^{*}}$.

> **定理 6.3.3 (卡拉西奥多里定理)**
> 
> 设 $\mu^{*}$ 是 $X$ 上的外测度, 则: (1) $\mathcal{M}$ 是一个 $\sigma$-代数; (2) $\mu^{*}|_{\mathcal{M}}$ 是一个完备测度; (3) 如果 $\mu^{*}$ 是由准测度 $\mu_{0}$ 生成的, 且 $\mu_{0}$ 是 $\sigma$-有限的, 则 $\mu^{*}|_{\mathcal{M}}$ 是 $\mu_{0}$ 的唯一延拓.


## ma\real-analysis\homework-cn\week5.md

> **定理 8.2.7 (法图引理)**
> 
> 设 $\left(X,\mathcal{F},\mu\right)$ 是测度空间, $\left\{f_{n}\right\}$ 是一列非负可测函数, 则 $\int_{X}\liminf_{n\to\infty}f_{n}\,\mathrm{d}\mu\le\liminf_{n\to\infty}\int_{X}f_{n}\,\mathrm{d}\mu$.

> **定理 8.2.9 (控制收敛定理)**
> 
> 设 $\left(X,\mathcal{F},\mu\right)$ 是测度空间, $\left\{f_{n}\right\}$ 是一列可测函数, 若存在可积函数 $g$ 使 $\left|f_{n}\right|\le{g}$ 对所有 $n$ 成立, 且 $f_{n}\to{f}$ 几乎处处, 则 $f$ 可积且 $\int{f}\,\mathrm{d}\mu=\lim_{n\to\infty}\int{f}_{n}\,\mathrm{d}\mu$.

> **引理 8.2.13 (级数逐项积分)**
> 
> 设 $\left\{f_{n}\right\}$ 是一列可测函数, 且 $\sum_{n=1}^{\infty}\int_{X}\left|f_{n}\right|\mathrm{d}\mu<\infty$, 则 $\int_{X}\left(\sum_{n=1}^{\infty}f_{n}\right)\mathrm{d}\mu=\sum_{n=1}^{\infty}\int_{X}f_{n}\,\mathrm{d}\mu$.

> **定理 8.2.17 (参数积分)**
> 
> 设 $f:X\times\left[a,b\right]\to\mathbb{R}$, 且对每个 $t\in\left[a,b\right]$, 函数 $f\left(\cdot,t\right):X\to\mathbb{R}$ 可积. 令 $F\left(t\right)=\int_{X}f\left(x,t\right)\mathrm{d}\mu\left(x\right)$. (a) 若存在 $g\in{L}^{1}\left(\mu\right)$ 使得对所有 $x,t$ 有 $\left|f\left(x,t\right)\right|\le{g}\left(x\right)$, 且对每个 $x$ 有 $\lim_{t\to{t}_{0}}f\left(x,t\right)=f\left(x,t_{0}\right)$, 则 $\lim_{t\to{t}_{0}}F\left(t\right)=F\left(t_{0}\right)$; (b) 若偏导数 $\partial{f}/\partial{t}$ 存在, 且存在 $g\in{L}^{1}\left(\mu\right)$ 使得对所有 $x,t$ 有 $\left|\frac{\partial{f}}{\partial{t}}\left(x,t\right)\right|\le{g}\left(x\right)$, 则 $F$ 可微, 且 $F'\left(t\right)=\int\frac{\partial{f}}{\partial{t}}\left(x,t\right)\mathrm{d}\mu\left(x\right)$.


## ma\real-analysis\homework-cn\week6.md

> **定义 4.1.3 ($\sigma$-代数)**
> 
> 设 $X$ 非空, $\mathcal{F}\subset\mathcal{P}\left(X\right)$. 称 $\mathcal{F}$ 为 $X$ 上的一个 $\sigma$-代数, 若满足: (1) $X\in\mathcal{F}$; (2) 对补运算封闭: $A\in\mathcal{F}\Rightarrow{A}^{c}\in\mathcal{F}$; (3) 对可数并封闭: $\left\{A_{n}\right\}_{n=1}^{\infty}\subset\mathcal{F}\Rightarrow\bigcup_{n=1}^{\infty}A_{n}\in\mathcal{F}$.

> **定义 5.1.5 ($\sigma$-有限测度)**
> 
> 设 $\left(X,\mathcal{F},\mu\right)$ 是测度空间. 如果存在一列可测集 $\left\{E_{n}\right\}_{n=1}^{\infty}\subset\mathcal{F}$ 使得 $X=\bigcup_{n=1}^{\infty}E_{n}$ 且 $\mu\left(E_{n}\right)<+\infty$ 对所有 $n\in\mathbb{N}$ 成立, 则称 $\mu$ 为 $\sigma$-有限测度.

> **定理 6.4.5 (勒贝格-斯蒂尔杰斯测度的正则性)**
> 
> 设 $\mu_{F}$ 是由增右连续函数 $F$ 生成的勒贝格-斯蒂尔杰斯测度, $\mathcal{M}^{*}$ 是 $\mu_{F}$-可测集的 $\sigma$-代数. 若 $E\in\mathcal{M}^{*}$, 则 $\mu_{F}\left(E\right)=\inf\left\{\mu_{F}\left(U\right):E\subset{U},U\text{~开}\right\}=\sup\left\{\mu_{F}\left(K\right):K\subset{E},K\text{~紧}\right\}$. 特别地, 勒贝格测度在 $\left[a,b\right]$ 上内正则.

> **定理 7.1.8 (实值可测函数的运算封闭性)**
> 
> 设 $f,g:X\to\mathbb{R}$ 可测, $c\in\mathbb{R}$, 则 $cf$, $f+g$, $fg$, $\max\left(f,g\right)$, $\min\left(f,g\right)$ 可测; 若 $\left\{f_{n}\right\}$ 可测且点点收敛, 则极限函数可测.

> **定理 7.2.2 (可测函数的构造)**
> 
> 若 $f:X\to\left[0,+\infty\right]$ 是非负可测函数, 则存在一列非负简单函数 $\left\{f_{n}\right\}$ 满足 $0\le{f}_{1}\le{f}_{2}\le\cdots\le{f}$ 且 $\lim_{n\to\infty}f_{n}\left(x\right)=f\left(x\right)$ 对每个 $x\in{X}$ 成立.

> **定义 8.1.1 (非负简单函数的积分)**
> 
> 设 $f=\sum_{i=1}^{n}c_{i}\chi_{A_{i}}$ 是非负简单函数, 其中 $c_{i}\ge0$, $A_{i}\in\mathcal{F}$ 互不相交且 $\bigcup_{i}A_{i}=X$. 定义 $f$ 关于 $\mu$ 的积分为 $\int_{X}f\,\mathrm{d}\mu=\sum_{i=1}^{n}c_{i}\mu\left(A_{i}\right)$, 并约定 $0\cdot\infty=0$.

> **命题 8.1.2 (简单函数积分的线性性)**
> 
> 设 $f,g$ 为非负简单函数, $\alpha,\beta\ge0$, 则 $\int_{X}\left(\alpha{f}+\beta{g}\right)\mathrm{d}\mu=\alpha\int_{X}f\,\mathrm{d}\mu+\beta\int_{X}g\,\mathrm{d}\mu$.

> **定义 8.2.1 (非负可测函数的积分)**
> 
> 设 $f:X\to\left[0,+\infty\right]$ 是非负可测函数. 定义 $f$ 关于 $\mu$ 的积分为 $\int_{X}f\,\mathrm{d}\mu=\sup\left\{\int_{X}\phi\,\mathrm{d}\mu:\phi\text{~是简单函数},0\le\phi\le{f}\right\}$. 若 $\int_{X}f\,\mathrm{d}\mu<\infty$, 则称 $f$ 是可积的.

> **定理 8.2.2 (单调收敛定理)**
> 
> 设 $\left(X,\mathcal{F},\mu\right)$ 是测度空间, $\left\{f_{n}\right\}$ 是一列非负可测函数, 满足 $0\le{f}_{1}\left(x\right)\le{f}_{2}\left(x\right)\le\cdots$ 对所有 $x\in{X}$ 成立, 且 $f_{n}\to{f}$ 点点收敛. 则 $\lim_{n\to\infty}\int_{X}f_{n}\,\mathrm{d}\mu=\int_{X}f\,\mathrm{d}\mu$.

> **注 8.2.3 (简单函数逼近)**
> 
> 单调收敛定理告诉我们积分可以用简单函数逼近.

> **命题 8.2.4 (积分关于集合的绝对连续性)**
> 
> 设 $f$ 为非负可测函数, 则 $A\mapsto\int_{A}f\,\mathrm{d}\mu$ 为一个测度; 若 $\mu\left(A\right)=0$, 则 $\int_{A}f\,\mathrm{d}\mu=0$.

> **定义 8.2.5 (一般可测函数的积分)**
> 
> 设 $f:X\to\left[-\infty,+\infty\right]$ 是可测函数. 定义 $f$ 的正部和负部分别为 $f^{+}\left(x\right)=\max\left\{f\left(x\right),0\right\}$, $f^{-}\left(x\right)=\max\left\{-f\left(x\right),0\right\}$. 若至少有一个积分 $\int_{X}f^{+}\mathrm{d}\mu$, $\int_{X}f^{-}\mathrm{d}\mu$ 有限, 则定义 $f$ 的积分为 $\int_{X}f\,\mathrm{d}\mu=\int_{X}f^{+}\mathrm{d}\mu-\int_{X}f^{-}\mathrm{d}\mu$. 若 $\int_{X}f^{+}\mathrm{d}\mu<\infty$ 且 $\int_{X}f^{-}\mathrm{d}\mu<\infty$, 则称 $f$ 是可积的.

> **定理 9.1.15 (叶戈罗夫定理)**
> 
> 设 $\mu\left(X\right)<\infty$ 且 $f_{n}\to{f}$ 几乎处处. 则对任意 $\delta>0$ 存在可测集 $E\subset{X}$ 使得 $\mu\left(E\right)<\delta$, 且在 $X\setminus{E}$ 上 $f_{n}$ 一致收敛到 $f$. 特别地, 在有限测度空间中, 几乎处处收敛蕴含依测度收敛.


## ma\real-analysis\homework-cn\week7.md

> **命题 7.1.5 (复合保持可测性)**
> 
> 若 $f:X\to{Y}$ 是 $\left(\mathcal{F},\mathcal{G}\right)$-可测的, $g:Y\to{Z}$ 是 $\left(\mathcal{G},\mathcal{H}\right)$-可测的, 则 $g\circ{f}:X\to{Z}$ 是 $\left(\mathcal{F},\mathcal{H}\right)$-可测的.

> **命题 7.1.7 (乘积空间的可测性)**
> 
> 设 $f=\left(f_{1},\dots,f_{n}\right):X\to{Y}_{1}\times\cdots\times{Y}_{n}$. 在乘积空间配备乘积 $\sigma$-代数下, $f$ 可测当且仅当每个坐标映射 $f_{i}:X\to{Y}_{i}$ 可测.

> **命题 9.1.2 (几乎处处收敛的刻画)**
> 
> $f_{n}\xrightarrow{\text{a.e.}}f$ 当且仅当对任意的 $\varepsilon>0$,

> **定理 9.1.8 (子序列性质)**
> 
> 如果 $f_{n}\xrightarrow{\mu}f$, 则存在子序列 $\left\{f_{n_{k}}\right\}$ 使得 $f_{n_{k}}\to{f}$ 几乎处处.

> **定理 10.2.2 (托内利定理)**
> 
> 如果 $f:X\times{Y}\to\left[0,\infty\right]$ 是 $\mathcal{A}\otimes\mathcal{B}$-可测的, 则 $\int_{X\times{Y}}f\,\mathrm{d}\left(\mu\times\nu\right)=\int_{X}\left(\int_{Y}f\left(x,y\right)\mathrm{d}\nu\left(y\right)\right)\mathrm{d}\mu\left(x\right)=\int_{Y}\left(\int_{X}f\left(x,y\right)\mathrm{d}\mu\left(x\right)\right)\mathrm{d}\nu\left(y\right)$, 其中所有积分值都在 $\left[0,\infty\right]$ 中.


## ma\real-analysis\homework-cn\week8.md

> **定义 6.2.1 (准测度)**
> 
> 设 $X$ 是非空集合, $\mathcal{E}\subset\mathcal{P}\left(X\right)$ 是一个代数. 函数 $\mu_{0}:\mathcal{E}\to\left[0,+\infty\right]$ 称为一个准测度, 如果 $\mu_{0}\left(\emptyset\right)=0$, 且若 $\left\{E_{n}\right\}_{n=1}^{\infty}\subset\mathcal{E}$ 两两不交且 $\bigcup_{n=1}^{\infty}E_{n}\in\mathcal{E}$, 则 $\mu_{0}\left(\bigcup_{n=1}^{\infty}E_{n}\right)=\sum_{n=1}^{\infty}\mu_{0}\left(E_{n}\right)$.

> **定理 6.3.3 (卡拉西奥多里定理)**
> 
> 设 $\mu^{*}$ 是 $X$ 上的外测度, 则: (1) $\mathcal{M}$ 是一个 $\sigma$-代数; (2) $\mu^{*}|_{\mathcal{M}}$ 是一个完备测度; (3) 如果 $\mu^{*}$ 是由准测度 $\mu_{0}$ 生成的, 且 $\mu_{0}$ 是 $\sigma$-有限的, 则 $\mu^{*}|_{\mathcal{M}}$ 是 $\mu_{0}$ 的唯一延拓.

> **定理 8.2.9 (控制收敛定理)**
> 
> 设 $\left(X,\mathcal{F},\mu\right)$ 是测度空间, $\left\{f_{n}\right\}$ 是一列可测函数, 若存在可积函数 $g$ 使 $\left|f_{n}\right|\le{g}$ 对所有 $n$ 成立, 且 $f_{n}\to{f}$ 几乎处处, 则 $f$ 可积且 $\int{f}\,\mathrm{d}\mu=\lim_{n\to\infty}\int{f}_{n}\,\mathrm{d}\mu$.

> **定义 10.1.2 (截面)**
> 
> 对于 $E\subseteq{X}\times{Y}$, 定义 $E$ 的 x-截面 $E_{x}=\left\{y\in{Y}:\left(x,y\right)\in{E}\right\}$ 和 y-截面 $E^{y}=\left\{x\in{X}:\left(x,y\right)\in{E}\right\}$.

> **定理 10.1.4 (乘积测度的存在唯一性)**
> 
> 设 $\left(X,\mathcal{A},\mu\right)$ 和 $\left(Y,\mathcal{B},\nu\right)$ 是 $\sigma$-有限的测度空间. 存在唯一的测度 $\mu\times\nu$ 在 $\left(X\times{Y},\mathcal{A}\otimes\mathcal{B}\right)$ 上, 使得对所有 $A\in\mathcal{A}$, $B\in\mathcal{B}$ 有 $\left(\mu\times\nu\right)\left(A\times{B}\right)=\mu\left(A\right)\nu\left(B\right)$. 其构造为 $\phi\left(E\right)=\int_{X}\nu\left(E_{x}\right)\mathrm{d}\mu\left(x\right)$ 对 $E\in\mathcal{A}\otimes\mathcal{B}$.

> **定理 11.4.1 (极坐标下的积分公式)**
> 
> 存在 $S^{n-1}$ 上唯一的博雷尔测度 $\sigma=\sigma_{n-1}$, 使得 $m^{*}=\rho\times\sigma$. 若 $f$ 是 $\mathbb{R}^{n}$ 上的博雷尔可测函数, 且 $f\ge0$ 或 $f\in{L}^{1}\left(m\right)$, 则 $\int_{\mathbb{R}^{n}}f\left(x\right)\mathrm{d}x=\int_{0}^{\infty}\int_{S^{n-1}}f\left(rx'\right)r^{n-1}\mathrm{d}\sigma\left(x'\right)\mathrm{d}r$.


## ma\real-analysis\homework-cn\week9.md

> **定理 8.2.16 (可积简单函数在 $L^{1}$ 中稠密)**
> 
> 如果 $f\in{L}^{1}\left(\mu\right)$ 且 $\varepsilon>0$, 则存在可积简单函数 $\varphi=\sum{a}_{j}\chi_{E_{j}}$ 使得 $\int\left|f-\varphi\right|\mathrm{d}\mu<\varepsilon$.

> **定理 11.1.1 (勒贝格测度的正则性与矩形逼近)**
> 
> 假设 $E\in\mathcal{L}^{n}$. (a)


## ma\real-analysis\homework-en\week1.md

> **Definition 4.5.7 (Arbitrary Product $\sigma$-Algebra)**
> 
> Let $\left\{\left(X_{\alpha},\mathcal{F}_{\alpha}\right)\right\}_{\alpha\in{I}}$ be a family of measurable spaces. The product $\sigma$-algebra $\bigotimes_{\alpha\in{I}}\mathcal{F}_{\alpha}$ is the $\sigma$-algebra generated by all cylinder sets $\left\{x=\left(x_{\alpha}\right)_{\alpha\in{I}}\in\prod_{\alpha\in{I}}X_{\alpha}:x_{\beta}\in{A}_{\beta}\right\},A_{\beta}\in\mathcal{F}_{\beta},\beta\in{I}$.


## ma\real-analysis\homework-en\week10.md

> **Theorem 10.2.2 (Tonelli's Theorem)**
> 
> If $f:X\times{Y}\to\left[0,\infty\right]$ is $\mathcal{A}\otimes\mathcal{B}$-measurable, then $\int_{X\times{Y}}f\,\mathrm{d}\left(\mu\times\nu\right)=\int_{X}\left(\int_{Y}f\left(x,y\right)\mathrm{d}\nu\left(y\right)\right)\mathrm{d}\mu\left(x\right)=\int_{Y}\left(\int_{X}f\left(x,y\right)\mathrm{d}\mu\left(x\right)\right)\mathrm{d}\nu\left(y\right)$, with all integral values in $\left[0,\infty\right]$.

> **Theorem 11.5.5 (Radon-Nikodym Theorem)**
> 
> Let $\mu$ be a $\sigma$-finite positive measure and $\nu$ a signed measure with $\nu\ll\mu$. Then there exists a measurable function $f:X\to\mathbb{R}$ such that $\nu\left(E\right)=\int_{E}f\,\mathrm{d}\mu$ for every $E\in\mathcal{F}$; and $\nu^{+}\left(E\right)=\int_{E}f^{+}\mathrm{d}\mu$, $\nu^{-}\left(E\right)=\int_{E}f^{-}\mathrm{d}\mu$, $\left|\nu\right|\left(E\right)=\int_{E}\left|f\right|\mathrm{d}\mu$. The function $f$ is the Radon-Nikodym derivative of $\nu$ w.r.t. $\mu$, written $f=\frac{\mathrm{d}\nu}{\mathrm{d}\mu}$.


## ma\real-analysis\homework-en\week11.md

> **Definition 11.1.1 (Signed Measure)**
> 
> Let $\left(X,\mathcal{F}\right)$ be a measurable space. A function $\nu:\mathcal{F}\to\mathbb{R}\cup\left\{+\infty\right\}$ or $\mathbb{R}\cup\left\{-\infty\right\}$ is called a signed measure if: (1) $\nu\left(\emptyset\right)=0$; (2) countable additivity: for every sequence of pairwise-disjoint measurable sets $\left\{E_{i}\right\}_{i=1}^{\infty}\subset\mathcal{F}$, $\nu\left(\bigcup_{i=1}^{\infty}E_{i}\right)=\sum_{i=1}^{\infty}\nu\left(E_{i}\right)$; (3) $\nu$ cannot take both $+\infty$ and $-\infty$.

> **Proposition 11.1.2 (Basic Properties of Signed Measures)**
> 
> Let $\nu$ be a signed measure. Then: (1) finite additivity: for any finitely many pairwise-disjoint $E_{1},\dots,E_{n}\in\mathcal{F}$, $\nu\left(\bigcup_{i=1}^{n}E_{i}\right)=\sum_{i=1}^{n}\nu\left(E_{i}\right)$; (2) lower continuity: if $\left\{E_{j}\right\}$ is increasing measurable, then $\lim_{j\to\infty}\nu\left(E_{j}\right)=\nu\left(\bigcup_{j}E_{j}\right)$; (3) upper continuity: if $\left\{E_{j}\right\}$ is decreasing measurable and $\nu\left(E_{1}\right)<\infty$, then $\lim_{j\to\infty}\nu\left(E_{j}\right)=\nu\left(\bigcap_{j}E_{j}\right)$.

> **Definition 11.2.1 (Positive Set, Negative Set, Null Set)**
> 
> Let $\nu$ be a signed measure on $\left(X,\mathcal{F}\right)$. A set $P\in\mathcal{F}$ is positive (written $P\gtrsim0$) if $\nu\left(E\right)\ge0$ for every $E\in\mathcal{F}$ with $E\subset{P}$; a set $N\in\mathcal{F}$ is negative (written $N\lesssim0$) if $\nu\left(E\right)\le0$ for every $E\in\mathcal{F}$ with $E\subset{N}$; a set $Z\in\mathcal{F}$ is a null set if $\nu\left(E\right)=0$ for every $E\in\mathcal{F}$ with $E\subset{Z}$.

> **Lemma 11.2.2 (Properties of Positive Sets)**
> 
> (1) Any measurable subset of a positive set is positive; (2) a countable union of positive sets is positive; (3) if $\left\{P_{n}\right\}$ is a sequence of positive sets, then $\bigcap_{n=1}^{\infty}P_{n}$ is positive. The same holds for negative sets.

> **Lemma 11.2.4 (Criterion for a Non-Negative Set)**
> 
> Let $\nu$ be a signed measure. If $E$ is not a negative set, then there exists a positive set $F\subset{E}$ with $\nu\left(F\right)>0$.

> **Theorem 11.3.2 (Hahn Decomposition Theorem)**
> 
> Let $\nu$ be a signed measure on $\left(X,\mathcal{F}\right)$. Then there is a decomposition $X=P\cup{N}$, where $P$ is positive, $N$ is negative, and $P\cap{N}=\emptyset$; and this decomposition is unique up to a $\nu$-null set.

> **Theorem 11.4.3 (Jordan Decomposition Theorem)**
> 
> Let $\nu$ be a signed measure on $\left(X,\mathcal{F}\right)$. Then there is a unique pair of mutually singular positive measures $\nu^{+}$ and $\nu^{-}$ such that $\nu=\nu^{+}-\nu^{-}$.

> **Definition 11.4.4 (Variation Measure)**
> 
> Let $\nu$ be a signed measure with Jordan decomposition $\nu=\nu^{+}-\nu^{-}$. $\nu^{+}$ is the positive variation, $\nu^{-}$ the negative variation, and $\left|\nu\right|=\nu^{+}+\nu^{-}$ the total variation measure.

> **Remark 11.5.3 (Absolute Continuity of the Integral w.r.t. the Measure)**
> 
> If $f\in{L}^{1}\left(\mu\right)$, then $\lim_{\mu\left(E\right)\to0}\int_{E}f\,\mathrm{d}\mu=0$.

> **Definition 14.0.6 (Functions of Bounded Variation)**
> 
> Let $f:\left[a,b\right]\to\mathbb{R}$. For any partition $P:a=x_{0}<{}x_{1}<\cdots<{}x_{n}=b$ of $\left[a,b\right]$, define the variation $V\left(f,P\right)=\sum_{i=1}^{n}\left|f\left(x_{i}\right)-f\left(x_{i-1}\right)\right|$. The total variation of $f$ on $\left[a,b\right]$ is $V_{a}^{b}\left(f\right)=\sup_{P}V\left(f,P\right)$. If $V_{a}^{b}\left(f\right)<+\infty$, $f$ is called a bounded-variation function, written $f\in{B}V\left(\left[a,b\right]\right)$.


## ma\real-analysis\homework-en\week12.md

> **Theorem 14.0.10 (Discontinuity Properties of Bounded-Variation Functions)**
> 
> If $f\in{B}V\left(\left[a,b\right]\right)$, then: (1) $f$ has at most countably many discontinuities; (2) all discontinuities are jump discontinuities.


## ma\real-analysis\homework-en\week2.md

> **Theorem 1.2.9 (De Morgan's Laws)**
> 
> $\left(A\cup{B}\right)^{c}=A^{c}\cap{B}^{c}$, $\left(A\cap{B}\right)^{c}=A^{c}\cup{B}^{c}$.

> **Theorem 3.2.1 (Structure of Open Sets in $\mathbb{R}$)**
> 
> If $U\subset\mathbb{R}$ is a nonempty open set, then there exists a sequence of pairwise disjoint open intervals $\left\{I_{n}\right\}_{n=1}^{\infty}$ such that $U=\bigcup_{n=1}^{\infty}I_{n}$; this representation is unique up to reordering.

> **Definition 4.1.1 (Algebra of Sets)**
> 
> Let $X$ be a nonempty set and $\mathcal{A}\subset\mathcal{P}\left(X\right)$. $\mathcal{A}$ is called an algebra of sets on $X$ if: (1) $X\in\mathcal{A}$; (2) closed under differences: $A,B\in\mathcal{A}\Rightarrow{A}\setminus{B}\in\mathcal{A}$; (3) closed under finite unions: $A,B\in\mathcal{A}\Rightarrow{A}\cup{B}\in\mathcal{A}$.

> **Proposition 4.1.2 (Equivalent Definition of an Algebra)**
> 
> Let $\mathcal{A}\subset\mathcal{P}\left(X\right)$. The following are equivalent: (1) $\mathcal{A}$ is an algebra; (2) $\mathcal{A}$ satisfies: (a) $X\in\mathcal{A}$; (b) closed under complements: $A\in\mathcal{A}\Rightarrow{A}^{c}=X\setminus{A}\in\mathcal{A}$; (c) closed under finite unions: $A,B\in\mathcal{A}\Rightarrow{A}\cup{B}\in\mathcal{A}$.

> **Definition 4.2.1 (Generated Algebra)**
> 
> The smallest algebra containing $\mathcal{E}\subset\mathcal{P}\left(X\right)$ is called the algebra generated by $\mathcal{E}$, denoted $\alpha\left(\mathcal{E}\right)$:

> **Definition 4.2.2 (Generated $\sigma$-Algebra)**
> 
> The smallest $\sigma$-algebra containing $\mathcal{E}\subset\mathcal{P}\left(X\right)$ is called the $\sigma$-algebra generated by $\mathcal{E}$, denoted $\sigma\left(\mathcal{E}\right)$:

> **Definition 4.3.2 (Borel $\sigma$-Algebra)**
> 
> Let $\left(X,\tau\right)$ be a topological space. The $\sigma$-algebra generated by all open sets is called the Borel $\sigma$-algebra, denoted $\mathcal{B}\left(X\right)$; its elements are called Borel sets.

> **Example 4.3.3 (Borel Algebra on $\mathbb{R}$)**
> 
> On $\mathbb{R}$, the following families generate the same Borel $\sigma$-algebra $\mathcal{B}\left(\mathbb{R}\right)$: all open sets $\tau$, all closed sets $\mathcal{F}$, all open intervals $\left\{\left(a,b\right)\right\}$, all closed intervals $\left\{\left[a,b\right]\right\}$, all half-open intervals $\left\{\left(a,b\right]\right\}$, i.e.

> **Definition 4.5.1 (Measurable Rectangles and Product $\sigma$-Algebra)**
> 
> Let $\left(X,\mathcal{F}\right)$ and $\left(Y,\mathcal{G}\right)$ be measurable spaces. $A\times{B}\subseteq{X}\times{Y}$ is called a measurable rectangle if $A\in\mathcal{F}$ and $B\in\mathcal{G}$. The product $\sigma$-algebra is the smallest $\sigma$-algebra containing all measurable rectangles:

> **Theorem 4.5.3 (Section Measurability)**
> 
> If $E\in\mathcal{F}\otimes\mathcal{G}$, then for every $x\in{X}$ and $y\in{Y}$, its sections are measurable:

> **Theorem 4.5.4 (Product of Borel $\sigma$-Algebras)**
> 
> For Borel $\sigma$-algebras in Euclidean space,


## ma\real-analysis\homework-en\week3.md

> **Definition 1.3.1 (Limit Superior)**
> 
> The limit superior of a sequence of sets $\left\{E_{n}\right\}$ is

> **Definition 1.3.3 (Limit Inferior)**
> 
> The limit inferior of a sequence of sets $\left\{E_{n}\right\}$ is

> **Proposition 5.2.5 (Continuity from Above)**
> 
> Let $\mu$ be a measure and $\left\{E_{n}\right\}_{n=1}^{\infty}\subset\mathcal{F}$ be a decreasing sequence of sets (i.e. $E_{1}\supset{E}_{2}\supset\cdots$), and suppose there exists $m$ with $\mu\left(E_{m}\right)<+\infty$. Then

> **Definition 5.4.1 (Null Set)**
> 
> Let $\left(X,\mathcal{F},\mu\right)$ be a measure space. A set $N\in\mathcal{F}$ is called a null set if $\mu\left(N\right)=0$.

> **Definition 5.4.2 (Zero-Measure Set)**
> 
> A set $A\subset{X}$ is called a zero-measure set if there exists $N\in\mathcal{F}$ such that $A\subset{N}$ and $\mu\left(N\right)=0$.

> **Definition 5.4.4 (Complete Measure)**
> 
> A measure space $\left(X,\mathcal{F},\mu\right)$ is called complete if for every $N\in\mathcal{F}$ with $\mu\left(N\right)=0$ and every $A\subset{N}$, we have $A\in\mathcal{F}$.

> **Theorem 5.4.6 (Completion Theorem for Measures)**
> 
> Every measure space $\left(X,\mathcal{F},\mu\right)$ can be completed, i.e. there exists a complete measure space $\left(X,\mathcal{M},\overline\mu\right)$ such that: (1) $\mathcal{F}\subset\mathcal{M}$; (2) $\overline\mu|_{\mathcal{F}}=\mu$; (3) $\mathcal{M}$ is the smallest complete $\sigma$-algebra containing $\mathcal{F}$. Explicitly, let $\mathcal{N}=\left\{N\in\mathcal{F}:\mu\left(N\right)=0\right\}$, $\mathcal{M}=\left\{A\subset{X}:\exists\,B\in\mathcal{F},\exists\,N\in\mathcal{N},B\subset{A}\subset{B}\cup{N}\right\}$, and define $\overline\mu\left(A\right)=\mu\left(B\right)$.

> **Proposition 6.4.2 (Premeasure on $\mathcal{E}$)**
> 
> Let $F:\mathbb{R}\to\mathbb{R}$ be increasing and right-continuous. For disjoint intervals $\left(a_{i},b_{i}\right]$, $i=1,\dots,n$, define $\mu_{0}\left(\bigcup_{i=1}^{n}\left(a_{i},b_{i}\right]\right):=\sum_{i=1}^{n}\left[F\left(b_{i}\right)-F\left(a_{i}\right)\right]$, and set $\mu_{0}\left(\emptyset\right)=0$. Then $\mu_{0}$ is a premeasure on $\mathcal{E}$.

> **Theorem 6.4.5 (Regularity of Lebesgue-Stieltjes Measure)**
> 
> Let $F:\mathbb{R}\to\mathbb{R}$ be right-continuous and increasing, $\mu_{F}$ the Lebesgue-Stieltjes measure generated by $F$, and $\mathcal{M}^{*}$ the $\sigma$-algebra of $\mu_{F}$-measurable sets. If $E\in\mathcal{M}^{*}$, then $\mu_{F}\left(E\right)=\inf\left\{\mu_{F}\left(U\right):E\subset{U},U\text{~open}\right\}=\sup\left\{\mu_{F}\left(K\right):K\subset{E},K\text{~compact}\right\}$.

> **Definition 6.4.6 (Lebesgue Measure)**
> 
> The measure generated by $F\left(x\right)=x$ is called Lebesgue measure, denoted $m$; the measurable sets defined via the corresponding outer measure are called Lebesgue measurable sets, and their collection is denoted $\mathcal{L}$.

> **Definition 6.5.1 (Recursive Construction of the Cantor Set)**
> 
> Let $C_{0}=\left[0,1\right]$. For each $n\ge0$, define $C_{n+1}=\frac{1}{3}C_{n}\cup\left(\frac{2}{3}+\frac{1}{3}C_{n}\right)$. The Cantor set is defined as $C=\bigcap_{n=0}^{\infty}C_{n}$.

> **Theorem 6.5.2 (Ternary Characterization of the Cantor Set)**
> 
> A point $x\in\left[0,1\right]$ belongs to the Cantor set $C$ iff its ternary expansion $x=\sum_{k=1}^{\infty}\frac{a_{k}}{3^{k}}$ contains no digit $1$ (i.e. $a_{k}\in\left\{0,2\right\}$).


## ma\real-analysis\homework-en\week4.md

> **Definition 4.1.1 (Algebra of Sets)**
> 
> Let $X$ be a nonempty set and $\mathcal{A}\subset\mathcal{P}\left(X\right)$. $\mathcal{A}$ is called an algebra of sets on $X$ if: (1) $X\in\mathcal{A}$; (2) closed under differences: $A,B\in\mathcal{A}\Rightarrow{A}\setminus{B}\in\mathcal{A}$; (3) closed under finite unions: $A,B\in\mathcal{A}\Rightarrow{A}\cup{B}\in\mathcal{A}$.

> **Definition 4.4.1 (Monotone Class)**
> 
> Let $\mathcal{M}\subset\mathcal{P}\left(X\right)$. $\mathcal{M}$ is called a monotone class if: (1) closed under increasing sequences: $A_{1}\subset{A}_{2}\subset\cdots$ and $A_{n}\in\mathcal{M}\Rightarrow\bigcup_{n=1}^{\infty}A_{n}\in\mathcal{M}$; (2) closed under decreasing sequences: $A_{1}\supset{A}_{2}\supset\cdots$ and $A_{n}\in\mathcal{M}\Rightarrow\bigcap_{n=1}^{\infty}A_{n}\in\mathcal{M}$.

> **Theorem 4.4.2 (Monotone Class Theorem)**
> 
> Let $\mathcal{A}$ be an algebra and $\mathcal{M}$ a monotone class containing $\mathcal{A}$. Then $\sigma\left(\mathcal{A}\right)\subset\mathcal{M}$.

> **Proposition 5.2.1 (Finite Additivity)**
> 
> Let $\mu$ be a measure on $\left(X,\mathcal{F}\right)$ and $E_{1},\dots,E_{n}\in\mathcal{F}$ be pairwise disjoint. Then

> **Proposition 5.2.3 (Countable Subadditivity)**
> 
> Let $\mu$ be a measure and $\left\{E_{n}\right\}_{n=1}^{\infty}\subset\mathcal{F}$ be any countable collection of sets (not necessarily pairwise disjoint). Then

> **Proposition 5.2.4 (Continuity from Below)**
> 
> Let $\mu$ be a measure and $\left\{E_{n}\right\}$ increasing. Then $\mu\left(\bigcup_{n=1}^{\infty}E_{n}\right)=\lim_{n\to\infty}\mu\left(E_{n}\right)$.

> **Lemma 6.3.2 (Algebra Contained in Measurable Sets)**
> 
> If $\mathcal{E}$ is an algebra and $\mu_{0}$ is a premeasure, then $\mathcal{E}\subset\mathcal{M}_{\mu^{*}}$.

> **Theorem 6.3.3 (Carathéodory's Theorem)**
> 
> Let $\mu^{*}$ be an outer measure on $X$. Then: (1) $\mathcal{M}$ is a $\sigma$-algebra; (2) $\mu^{*}|_{\mathcal{M}}$ is a complete measure; (3) if $\mu^{*}$ is generated by a premeasure $\mu_{0}$ and $\mu_{0}$ is $\sigma$-finite, then $\mu^{*}|_{\mathcal{M}}$ is the unique extension of $\mu_{0}$.

> **Definition 6.4.1 (h-Interval)**
> 
> Let $-\infty\le{a}<{}b<\infty$. All half-open intervals $\left(a,b\right]$, together with $\left(a,\infty\right)$ and $\emptyset$, are called h-intervals. The family of finite disjoint unions of h-intervals forms an algebra $\mathcal{E}$.


## ma\real-analysis\homework-en\week5.md

> **Theorem 8.2.7 (Fatou's Lemma)**
> 
> Let $\left(X,\mathcal{F},\mu\right)$ be a measure space and $\left\{f_{n}\right\}$ a sequence of nonnegative measurable functions. Then $\int_{X}\liminf_{n\to\infty}f_{n}\,\mathrm{d}\mu\le\liminf_{n\to\infty}\int_{X}f_{n}\,\mathrm{d}\mu$.

> **Theorem 8.2.9 (Dominated Convergence Theorem)**
> 
> Let $\left(X,\mathcal{F},\mu\right)$ be a measure space and $\left\{f_{n}\right\}$ a sequence of measurable functions. If there exists an integrable $g$ with $\left|f_{n}\right|\le{g}$ for all $n$ and $f_{n}\to{f}$ a.e., then $f$ is integrable and $\int{f}\,\mathrm{d}\mu=\lim_{n\to\infty}\int{f}_{n}\,\mathrm{d}\mu$.

> **Lemma 8.2.13 (Termwise Integration of Series)**
> 
> Let $\left\{f_{n}\right\}$ be a sequence of measurable functions with $\sum_{n=1}^{\infty}\int_{X}\left|f_{n}\right|\mathrm{d}\mu<\infty$. Then $\int_{X}\left(\sum_{n=1}^{\infty}f_{n}\right)\mathrm{d}\mu=\sum_{n=1}^{\infty}\int_{X}f_{n}\,\mathrm{d}\mu$.

> **Theorem 8.2.17 (Parameter Integrals)**
> 
> Let $f:X\times\left[a,b\right]\to\mathbb{R}$, and for each $t\in\left[a,b\right]$ let $f\left(\cdot,t\right):X\to\mathbb{R}$ be integrable. Set $F\left(t\right)=\int_{X}f\left(x,t\right)\mathrm{d}\mu\left(x\right)$. (a) If there exists $g\in{L}^{1}\left(\mu\right)$ with $\left|f\left(x,t\right)\right|\le{g}\left(x\right)$ for all $x,t$, and $\lim_{t\to{t}_{0}}f\left(x,t\right)=f\left(x,t_{0}\right)$ for each $x$, then $\lim_{t\to{t}_{0}}F\left(t\right)=F\left(t_{0}\right)$; (b) if the partial derivative $\partial{f}/\partial{t}$ exists and there is $g\in{L}^{1}\left(\mu\right)$ with $\left|\frac{\partial{f}}{\partial{t}}\left(x,t\right)\right|\le{g}\left(x\right)$ for all $x,t$, then $F$ is differentiable and $F'\left(t\right)=\int\frac{\partial{f}}{\partial{t}}\left(x,t\right)\mathrm{d}\mu\left(x\right)$.


## ma\real-analysis\homework-en\week6.md

> **Definition 4.1.3 ($\sigma$-Algebra)**
> 
> Let $X$ be nonempty and $\mathcal{F}\subset\mathcal{P}\left(X\right)$. $\mathcal{F}$ is called a $\sigma$-algebra on $X$ if: (1) $X\in\mathcal{F}$; (2) closed under complements: $A\in\mathcal{F}\Rightarrow{A}^{c}\in\mathcal{F}$; (3) closed under countable unions: $\left\{A_{n}\right\}_{n=1}^{\infty}\subset\mathcal{F}\Rightarrow\bigcup_{n=1}^{\infty}A_{n}\in\mathcal{F}$.

> **Definition 5.1.5 ($\sigma$-Finite Measure)**
> 
> Let $\left(X,\mathcal{F},\mu\right)$ be a measure space. If there exists a sequence of measurable sets $\left\{E_{n}\right\}_{n=1}^{\infty}\subset\mathcal{F}$ such that $X=\bigcup_{n=1}^{\infty}E_{n}$ and $\mu\left(E_{n}\right)<+\infty$ for all $n\in\mathbb{N}$, then $\mu$ is called $\sigma$-finite.

> **Theorem 6.4.5 (Regularity of Lebesgue-Stieltjes Measures)**
> 
> Let $\mu_{F}$ be the Lebesgue-Stieltjes measure generated by an increasing right-continuous function $F$, and let $\mathcal{M}^{*}$ be the $\sigma$-algebra of $\mu_{F}$-measurable sets. If $E\in\mathcal{M}^{*}$, then $\mu_{F}\left(E\right)=\inf\left\{\mu_{F}\left(U\right):E\subset{U},U\text{~open}\right\}=\sup\left\{\mu_{F}\left(K\right):K\subset{E},K\text{~compact}\right\}$. In particular, Lebesgue measure on $\left[a,b\right]$ is inner regular.

> **Theorem 7.1.8 (Closure of Real-Valued Measurable Functions Under Operations)**
> 
> Let $f,g:X\to\mathbb{R}$ be measurable and $c\in\mathbb{R}$. Then $cf$, $f+g$, $fg$, $\max\left(f,g\right)$, and $\min\left(f,g\right)$ are measurable; if $\left\{f_{n}\right\}$ are measurable and converge pointwise, the limit function is measurable.

> **Theorem 7.2.2 (Construction of Measurable Functions)**
> 
> If $f:X\to\left[0,+\infty\right]$ is a nonnegative measurable function, then there exists a sequence of nonnegative simple functions $\left\{f_{n}\right\}$ with $0\le{f}_{1}\le{f}_{2}\le\cdots\le{f}$ and $\lim_{n\to\infty}f_{n}\left(x\right)=f\left(x\right)$ for every $x\in{X}$.

> **Definition 8.1.1 (Integral of a Nonnegative Simple Function)**
> 
> Let $f=\sum_{i=1}^{n}c_{i}\chi_{A_{i}}$ be a nonnegative simple function, where $c_{i}\ge0$, the $A_{i}\in\mathcal{F}$ are pairwise disjoint and $\bigcup_{i}A_{i}=X$. The integral of $f$ with respect to $\mu$ is $\int_{X}f\,\mathrm{d}\mu=\sum_{i=1}^{n}c_{i}\mu\left(A_{i}\right)$, with the convention $0\cdot\infty=0$.

> **Proposition 8.1.2 (Linearity of the Integral for Simple Functions)**
> 
> Let $f,g$ be nonnegative simple functions and $\alpha,\beta\ge0$. Then $\int_{X}\left(\alpha{f}+\beta{g}\right)\mathrm{d}\mu=\alpha\int_{X}f\,\mathrm{d}\mu+\beta\int_{X}g\,\mathrm{d}\mu$.

> **Definition 8.2.1 (Integral of a Nonnegative Measurable Function)**
> 
> Let $f:X\to\left[0,+\infty\right]$ be a nonnegative measurable function. The integral of $f$ with respect to $\mu$ is $\int_{X}f\,\mathrm{d}\mu=\sup\left\{\int_{X}\phi\,\mathrm{d}\mu:\phi\text{~simple},0\le\phi\le{f}\right\}$. If $\int_{X}f\,\mathrm{d}\mu<\infty$, $f$ is called integrable.

> **Theorem 8.2.2 (Monotone Convergence Theorem)**
> 
> Let $\left(X,\mathcal{F},\mu\right)$ be a measure space and $\left\{f_{n}\right\}$ a sequence of nonnegative measurable functions with $0\le{f}_{1}\left(x\right)\le{f}_{2}\left(x\right)\le\cdots$ for all $x\in{X}$, and $f_{n}\to{f}$ pointwise. Then $\lim_{n\to\infty}\int_{X}f_{n}\,\mathrm{d}\mu=\int_{X}f\,\mathrm{d}\mu$.

> **Remark 8.2.3 (Approximation by Simple Functions)**
> 
> The monotone convergence theorem tells us that the integral can be approximated by simple functions.

> **Proposition 8.2.4 (Absolute Continuity of the Integral with Respect to the Set)**
> 
> Let $f$ be a nonnegative measurable function. Then $A\mapsto\int_{A}f\,\mathrm{d}\mu$ is a measure; if $\mu\left(A\right)=0$, then $\int_{A}f\,\mathrm{d}\mu=0$.

> **Definition 8.2.5 (Integral of a General Measurable Function)**
> 
> Let $f:X\to\left[-\infty,+\infty\right]$ be measurable. Define its positive and negative parts by $f^{+}\left(x\right)=\max\left\{f\left(x\right),0\right\}$, $f^{-}\left(x\right)=\max\left\{-f\left(x\right),0\right\}$. If at least one of $\int_{X}f^{+}\mathrm{d}\mu$, $\int_{X}f^{-}\mathrm{d}\mu$ is finite, define the integral by $\int_{X}f\,\mathrm{d}\mu=\int_{X}f^{+}\mathrm{d}\mu-\int_{X}f^{-}\mathrm{d}\mu$. If both are finite, $f$ is called integrable.

> **Theorem 9.1.15 (Egorov's Theorem)**
> 
> Let $\mu\left(X\right)<\infty$ and $f_{n}\to{f}$ almost everywhere. Then for every $\delta>0$ there exists a measurable set $E\subset{X}$ with $\mu\left(E\right)<\delta$ such that $f_{n}$ converges uniformly to $f$ on $X\setminus{E}$. In particular, on a finite-measure space, almost-everywhere convergence implies convergence in measure.


## ma\real-analysis\homework-en\week7.md

> **Proposition 7.1.5 (Composition Preserves Measurability)**
> 
> If $f:X\to{Y}$ is $\left(\mathcal{F},\mathcal{G}\right)$-measurable and $g:Y\to{Z}$ is $\left(\mathcal{G},\mathcal{H}\right)$-measurable, then $g\circ{f}:X\to{Z}$ is $\left(\mathcal{F},\mathcal{H}\right)$-measurable.

> **Proposition 7.1.7 (Measurability on Product Spaces)**
> 
> Let $f=\left(f_{1},\dots,f_{n}\right):X\to{Y}_{1}\times\cdots\times{Y}_{n}$. With the product $\sigma$-algebra on the product space, $f$ is measurable iff each coordinate map $f_{i}:X\to{Y}_{i}$ is measurable.

> **Proposition 9.1.2 (Characterization of Almost-Everywhere Convergence)**
> 
> $f_{n}\xrightarrow{\text{a.e.}}f$ iff for every $\varepsilon>0$,

> **Theorem 9.1.8 (Subsequence Property)**
> 
> If $f_{n}\xrightarrow{\mu}f$, then there exists a subsequence $\left\{f_{n_{k}}\right\}$ such that $f_{n_{k}}\to{f}$ almost everywhere.

> **Theorem 10.2.2 (Tonelli's Theorem)**
> 
> If $f:X\times{Y}\to\left[0,\infty\right]$ is $\mathcal{A}\otimes\mathcal{B}$-measurable, then $\int_{X\times{Y}}f\,\mathrm{d}\left(\mu\times\nu\right)=\int_{X}\left(\int_{Y}f\left(x,y\right)\mathrm{d}\nu\left(y\right)\right)\mathrm{d}\mu\left(x\right)=\int_{Y}\left(\int_{X}f\left(x,y\right)\mathrm{d}\mu\left(x\right)\right)\mathrm{d}\nu\left(y\right)$, with all integral values in $\left[0,\infty\right]$.


## ma\real-analysis\homework-en\week8.md

> **Definition 6.2.1 (Premeasure)**
> 
> Let $X$ be nonempty and $\mathcal{E}\subset\mathcal{P}\left(X\right)$ an algebra. A function $\mu_{0}:\mathcal{E}\to\left[0,+\infty\right]$ is called a premeasure if: (1) $\mu_{0}\left(\emptyset\right)=0$; (2) if $\left\{E_{n}\right\}_{n=1}^{\infty}\subset\mathcal{E}$ are pairwise disjoint and $\bigcup_{n=1}^{\infty}E_{n}\in\mathcal{E}$, then $\mu_{0}\left(\bigcup_{n=1}^{\infty}E_{n}\right)=\sum_{n=1}^{\infty}\mu_{0}\left(E_{n}\right)$.

> **Theorem 6.3.3 (Carathéodory's Theorem)**
> 
> Let $\mu^{*}$ be an outer measure on $X$. Then: (1) $\mathcal{M}$ is a $\sigma$-algebra; (2) $\mu^{*}|_{\mathcal{M}}$ is a complete measure; (3) if $\mu^{*}$ is generated by a premeasure $\mu_{0}$ and $\mu_{0}$ is $\sigma$-finite, then $\mu^{*}|_{\mathcal{M}}$ is the unique extension of $\mu_{0}$.

> **Theorem 8.2.9 (Dominated Convergence Theorem)**
> 
> Let $\left(X,\mathcal{F},\mu\right)$ be a measure space and $\left\{f_{n}\right\}$ a sequence of measurable functions. If there exists an integrable $g$ with $\left|f_{n}\right|\le{g}$ for all $n$ and $f_{n}\to{f}$ a.e., then $f$ is integrable and $\int{f}\,\mathrm{d}\mu=\lim_{n\to\infty}\int{f}_{n}\,\mathrm{d}\mu$.

> **Definition 10.1.2 (Sections)**
> 
> For $E\subseteq{X}\times{Y}$, define its x-section $E_{x}=\left\{y\in{Y}:\left(x,y\right)\in{E}\right\}$ and y-section $E^{y}=\left\{x\in{X}:\left(x,y\right)\in{E}\right\}$.

> **Theorem 10.1.4 (Existence and Uniqueness of the Product Measure)**
> 
> Let $\left(X,\mathcal{A},\mu\right)$ and $\left(Y,\mathcal{B},\nu\right)$ be $\sigma$-finite measure spaces. There is a unique measure $\mu\times\nu$ on $\left(X\times{Y},\mathcal{A}\otimes\mathcal{B}\right)$ such that $\left(\mu\times\nu\right)\left(A\times{B}\right)=\mu\left(A\right)\nu\left(B\right)$ for all $A\in\mathcal{A}$, $B\in\mathcal{B}$. It is constructed as $\phi\left(E\right)=\int_{X}\nu\left(E_{x}\right)\mathrm{d}\mu\left(x\right)$ for $E\in\mathcal{A}\otimes\mathcal{B}$.

> **Theorem 11.4.1 (Integration in Polar Coordinates)**
> 
> There is a unique Borel measure $\sigma=\sigma_{n-1}$ on $S^{n-1}$ such that $m^{*}=\rho\times\sigma$. If $f$ is Borel measurable on $\mathbb{R}^{n}$ and either $f\ge0$ or $f\in{L}^{1}\left(m\right)$, then $\int_{\mathbb{R}^{n}}f\left(x\right)\mathrm{d}x=\int_{0}^{\infty}\int_{S^{n-1}}f\left(rx'\right)r^{n-1}\mathrm{d}\sigma\left(x'\right)\mathrm{d}r$.


## ma\real-analysis\homework-en\week9.md

> **Theorem 8.2.16 (Integrable Simple Functions Are Dense in $L^{1}$)**
> 
> If $f\in{L}^{1}\left(\mu\right)$ and $\varepsilon>0$, then there exists an integrable simple function $\varphi=\sum{a}_{j}\chi_{E_{j}}$ with $\int\left|f-\varphi\right|\mathrm{d}\mu<\varepsilon$.

> **Theorem 11.1.1 (Regularity of Lebesgue Measure and Rectangle Approximation)**
> 
> Let $E\in\mathcal{L}^{n}$. (a)

