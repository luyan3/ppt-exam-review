# 高等固体物理·第四章 维度 — 完整复习材料

> 来源：assp4.pdf | 总页数：204 Slides | 四大章节

---

# 模块 1：考试情报卡

## 🎯 考试情报卡 — 第四章 维度

| 项目 | 内容 |
|------|------|
| 课程 | 高等固体物理（Advanced Solid State Physics） |
| 章节 | 第四章：维度（Dimensionality） |
| 子章节数 | 4 节（4.1-4.4） |
| 总页数 | 204 Slides |
| PPT 无明显"考点/重点/必考"标记 | 需从内容密度和深度自行判定 |

### 章节权重分布（估算）

| 章节 | 起止Slide | 页数 | P0核心知识点数 | 预估权重 |
|------|-----------|------|---------------|---------|
| **4.1** 半导体低维电子系统 | Slide 1-40 | 40 | 5 | ~25% |
| **4.2** 几何位相与拓扑态 | Slide 41-180 | 140 | 9 | ~50% |
| **4.3** 二维体系中的相变 | Slide 181-198 | 18 | 3 | ~15% |
| **4.4** 准一维Peierls/CDW | Slide 199-204 | 6 | 3 | ~10% |

### 考试趋势分析

| 题型 | 适用章节 | 频次预测 |
|------|---------|---------|
| 选择题（概念辨析） | 4.1~4.4 均有 | 高频 |
| 简答题（定义/机制） | 4.1 IQHE/FQHE, 4.2 Berry相/拓扑绝缘体, 4.3 KT相变, 4.4 Peierls/CDW | 高频 |
| 计算/推导题 | 4.1 Landau能级, 4.2 Chern数/缠绕数, 4.4 Peierls能隙 | 中频 |
| 论述/比较题 | IQHE vs FQHE, 拓扑绝缘体 vs 普通绝缘体, CDW vs SDW | 中频 |

### ⚠️ 核心提示

- **4.2 是全章绝对重点**，占一半以上篇幅，含Berry相、Chern数、拓扑绝缘体等核心概念
- **4.1 的 QHE（IQHE + FQHE）** 是经典考试题源，需掌握物理图像+Landau能级+平台机制
- **4.3 KT相变** 概念新颖（拓扑缺陷驱动的相变），是近年诺奖热点（2016）
- **4.4 Peierls/CDW** 概念较经典但结构清晰，易出简答题
- P0占比：约 40% 内容；P1占比：约 35%；P2占比：约 25%

---

# 模块 2：章节导航图

## 🗺 章节结构树

```
第四章 维度 (Slide 1-204)
│
├── 4.1 半导体低维电子系统 (Slide 1-40)  [P0×5, P1×3]
│   ├── 1. 维度与量子化 (Slide 2)                 P0
│   │   ├── 方势阱限制: ε_n = (nπℏ)²/(2mW²)
│   │   └── 抛物线势限制: ε_n = (n-½)ℏω₀
│   ├── 2. Si反型层及GaAs-AlGaAs异质结 (Slide 3-5) P1
│   │   ├── Si(100): m* = 0.2m_e, ε₂-ε₁≈20meV
│   │   └── GaAs-AlGaAs: m* = 0.067m_e, 高迁移率
│   ├── 3. Split-gate与1D电子气 (Slide 6)          P2
│   ├── 4. 量子霍尔效应基础 (Slide 7-12)           P1
│   │   ├── 霍尔效应 + 德鲁特模型 → 张量电导率
│   │   ├── ω_c = eB/mc, σ_xx/σ_xy 公式
│   │   ├── Landau能级量子力学解 (Slide 10-11)
│   │   └── Hall电流经典结果 j_y = -neEc/B (Slide 13)
│   ├── 5. 整数量子霍尔效应 IQHE (Slide 13-23)    P0
│   │   ├── Klitzing发现 (1980), Nobel 1985
│   │   ├── 霍尔电阻平台: R_H = h/(ie²)
│   │   ├── 扩展态/局域态机制 (Slide 19)
│   │   ├── Laughlin-Halperin 规范变换证明
│   │   └── 应用: 电阻标准 + 精细结构常数
│   └── 6. 分数量子霍尔效应 FQHE (Slide 24-40)    P0
│       ├── 崔琦/Stomer发现 (1982), Nobel 1998
│       ├── Laughlin波函数 ν = 1/m (Slide 29)
│       ├── 准粒子分数电荷 (Slide 30)
│       ├── 复合费米子模型 (Slide 32)
│       └── 石墨烯室温QHE (Slide 40)
│
├── 4.2 几何位相与拓扑态 (Slide 41-180)  [P0×9, P1×8]
│   ├── 拓扑学基础 (Slide 43)                      P2
│   │   └── Genus, Gauss-Bonnet Theorem
│   ├── SSH模型 (Slide 45-49)                      P0
│   │   ├── 1D dimerized chain, stagger hopping
│   │   ├── Winding number (缠绕数)
│   │   └── Bulk-boundary correspondence: 缠绕数=边缘态数
│   ├── Berry相位 (Slide 54-72)                    P0
│   │   ├── Berry connection A = i⟨u|∇_R|u⟩
│   │   ├── Berry curvature Ω = ∇×A
│   │   ├── Berry phase γ = ∮A·dR = ∫Ω·dS (Stokes)
│   │   ├── 规范不变性 + 几何/拓扑性质 (Slide 72)
│   │   └── 经典直观例子: 球面平行移动 (Slide 71)
│   ├── Chern数 (Slide 73-76)                      P0
│   │   ├── C = (1/2π)∫_BZ F d²k
│   │   └── σ_xy = e²/h · C (TKNN公式)
│   ├── 时间反演对称与Z₂拓扑 (Slide 83-85)         P0
│   │   ├── TRIM, Kramers简并
│   │   ├── Z₂ = (0,1) for 2D TI
│   │   ├── 边缘态自旋-动量锁定, 无背散射
│   │   └── Z₂可从奇偶性或自旋Chern数计算
│   ├── Kane-Mele模型: Graphene (Slide 89-96)      P0
│   │   ├── Dirac点打开拓扑能隙
│   │   ├── 内禀SOC: 2λ_I ~ 20-50 μeV (很小)
│   │   ├── 螺旋边缘态 (helical edge states)
│   │   └── 扩展: Silicene, Germanene (Slide 94)
│   ├── BHZ模型: HgTe量子阱 (Slide 105)            P1
│   │   ├── Band inversion: m/B < 0 for d > d_c
│   │   └── 能带反转机制
│   ├── 量子谷霍尔效应 (Slide 117-123)              P1
│   │   ├── Valley Chern number C_v = C_K - C_K'
│   │   ├── 谷极化: 圆偏振光激发
│   │   └── MoS₂单层谷极化 (Slide 120)
│   ├── 量子反常霍尔效应 QAHE (Slide 125-140)      P0
│   │   ├── 无需外磁场, TRS破缺
│   │   ├── Bi₂Se₃+磁性掺杂 (Slide 130, 139)
│   │   ├── C=1, C=2 模型
│   │   └── 实验验证 (Slide 139-140)
│   ├── 3D拓扑绝缘体 (Slide 141-150)               P0
│   │   ├── Bi₂Se₃: 拓扑表面态 (Slide 142)
│   │   ├── ARPES/STM探测 (Slide 143-145)
│   │   ├── 弱TI与强TI (Slide 146-148)
│   │   └── 半整数量子霍尔效应 (Slide 150)
│   ├── 拓扑半金属 (Slide 152-167)                  P1
│   │   ├── Dirac/Weyl/Nodal-line semimetal
│   │   ├── Weyl点 + Fermi弧 (Slide 160-163)
│   │   └── Type-I vs Type-II
│   ├── 高阶拓扑绝缘体 (Slide 168-172)              P2
│   ├── 新型费米子 (Slide 173-178)                  P2
│   │   ├── Hourglass fermion
│   │   ├── Three-component, Sixfold, Eightfold
│   │   └── Spin-1, Charge-2 fermion
│   └── 拓扑超导/马约拉纳费米子 (Slide 179)         P2
│
├── 4.3 二维体系中的相变 (Slide 181-198)  [P0×3, P1×1]
│   ├── 维度与相变: Mermin-Wagner定理 (Slide 181)   P1
│   │   ├── 1D: T>0时总是无序, 无长程序
│   │   ├── 2D: 序参量自由度N=1有相变(Ising)
│   │   │            N=2有KT相变(XY模型)
│   │   │            N=3无相变(Heisenberg)
│   │   └── 关联函数各维度行为对比
│   ├── 拓扑缺陷 (Slide 183-191)                   P0
│   │   ├── 涡旋(Vortex): 拓扑荷 n = ±1, ±2, ...
│   │   ├── Φ_L = ΣΔφ_i = n·2π (拓扑荷)
│   │   ├── 将速度场v = ∇φ分解为无旋场v_s+无源场v_v
│   │   └── 涡旋间相互作用类似二维点电荷
│   ├── Kosterlitz-Thouless相变 (Slide 193-198)     P0
│   │   ├── XY模型哈密顿量: H = -J Σ cos(φ_i-φ_j)
│   │   ├── 简谐近似: H = J/2 Σ (φ_i-φ_j)²
│   │   ├── 单涡旋能量: E_v = Jπ ln(L/a)
│   │   ├── 熵: S = k_B ln(L²/a²)
│   │   ├── 自由能: F_v = Jπ ln(L/a) - 2k_BT ln(L/a)
│   │   ├── 临界温度: T_c = πJ/(2k_B)
│   │   ├── T<T_c: 正负涡旋束缚对 (准长程序)
│   │   ├── T>T_c: 涡旋对解束缚 → 拓扑长程序破坏
│   │   └── 无穷级相变 (Slide 195)
│   └── 2D氦超流 (Slide 196-197)                   P2
│       └── KT transition explains 2D superfluid
│
└── 4.4 准一维体系的Peierls不稳定性和电荷密度波 (Slide 199-204)  [P0×3, P1×1]
    ├── 一维体系概述 (Slide 199)                    P1
    │   ├── 导电聚合物, KCP, TMTSF, 有机超导体等
    │   └── 自由电子能带: E(k) = ℏ²k²/(2m), k_F = n/(4a)
    ├── Peierls不稳定性 (Slide 200-201)             P0
    │   ├── 半满能带一维晶格 → 二聚化 → 晶格周期2a
    │   ├── 布里渊区边界与费米面重合 → 能隙打开
    │   ├── 低温: 半导体/绝缘体 (不导电)
    │   └── 高温: 能隙消失 → 导体 (Peierls相变)
    ├── 电荷密度波 CDW (Slide 202)                  P0
    │   ├── ρ(x) = n₀ + n_c cos(2πx/λ + φ)
    │   ├── k'_B = 1/(2a') = k_F, λ = 2a' = 2/k_F
    │   ├── 可公度相变 (a'/a有理数) 与非公度相变 (无理数)
    │   └── CDW基本特征: 空间调制电荷密度 + 费米能能隙 + 半导体电导
    └── 自旋密度波 SDW (Slide 203)                  P0
        ├── ρ↑(x) = n₀/2 + (n_c/2) cos(2πx/λ + φ↑)
        ├── ρ↓(x) = n₀/2 + (n_c/2) cos(2πx/λ + φ↓)
        ├── 总CDW: ρ(x) = ρ↑+ρ↓; SDW: S(x) = ρ↑-ρ↓
        ├── φ↑=φ↓ → 只有CDW, 无SDW
        └── φ↑=φ↓+π → 只有SDW, 无CDW
```

---

# 模块 3：核心知识点精编

## 4.1 半导体低维电子系统

### [维度限制与量子化] 🔴 P0
**来源：** Slide 2

**📖 定义/表述：**
三维自由电子气体沿 z 方向尺寸限制，导致能级量子化：
- 方势阱限制：$\varepsilon_n = \frac{n^2\pi^2\hbar^2}{2mW^2}$，其中 $W = \frac{n\lambda}{2}$，$\lambda$ 为电子波长
- 抛物线势限制 $V(z) = \frac{1}{2}m\omega_0^2 z^2$：$\varepsilon_n = \left(n - \frac{1}{2}\right)\hbar\omega_0$

**💡 通俗理解：**
在某一维度上把电子"关"起来（尺寸缩小到与电子波长可比），该维度的运动就量子化了——能量不再连续，变成一系列分立的子带。只填最低子带(n=1)就是二维体系，填充多个子带就是准二维体系。

**📌 考试形态：** 选择题/简答题
- 问：方势阱限制下子带能量表达式
- 问：抛物线势与方势阱限制的区别
- 问：二维体系与准二维体系的区分标准

**⚠️ 易错警示：**
- 方势阱中 $\varepsilon_n \propto n^2$，抛物线势中 $\varepsilon_n \propto n$（线性）
- 勿将二维体系误认为"只有两个维度"，而是"在一维被量子化限制"

---

### [Si反型层与GaAs-AlGaAs异质结] 🟡 P1
**来源：** Slide 3-5

**📖 定义/表述：**
实现二维电子气（2DEG）的两种经典体系：

| 性质 | Si(100) 反型层 | GaAs-AlGaAs 异质结 |
|------|---------------|-------------------|
| 电子有效质量 | $0.2m_e$ | $0.067m_e$ |
| 子带间距 $\varepsilon_2-\varepsilon_1$ | $\approx 20$ meV | $\sim 0.3$ eV (导带底差) |
| 面电子密度 $n_s$ | $1\sim10\times10^{11}\text{cm}^{-2}$ | $\approx 4\times10^{11}\text{cm}^{-2}$ |
| 迁移率 $\mu$ | $10^4\ \text{cm}^2/\text{V}\cdot\text{s}$ | $10^4\sim10^6\ \text{cm}^2/\text{V}\cdot\text{s}$ |
| 弹性散射平均自由程 $l$ | $40\sim120$ nm | $10^2\sim10^4$ nm |

**💡 通俗理解：**
两种制造"电子薄饼"的方法。Si反型层像在硅表面"引诱"出一层电子；GaAs异质结像用两种半导体"三明治"把电子夹在界面上。后者迁移率更高，适合研究精细的量子效应。

**📌 考试形态：** 选择题
- 问：哪种体系迁移率更高？为什么GaAs异质结更适合FQHE研究？

**⚠️ 易错警示：**
- Si反型层由 MOSFET 栅压 $V_g$ 控制电子密度
- GaAs 中 $x \approx 0.3$（Al 组分），导带底能量差 $\sim 0.3$ eV

---

### [霍尔效应与电导率张量基础] 🟡 P1
**来源：** Slide 7-9

**📖 定义/表述：**
有磁场时，电导率和电阻率变为张量。德鲁特模型推导：

$\boldsymbol{j} = -ne\boldsymbol{v}_d$，$\boldsymbol{v}_d = -\frac{e\tau}{m}\left(\boldsymbol{E} + \frac{\boldsymbol{v}_d \times \boldsymbol{B}}{c}\right)$

$\sigma_{xx} = \sigma_{yy} = \frac{\sigma_0}{1+(\omega_c\tau)^2}$，$\sigma_{xy} = -\sigma_{yx} = -\sigma_0\frac{\omega_c\tau}{1+(\omega_c\tau)^2}$

其中 $\sigma_0 = ne^2\tau/m$，回旋频率 $\omega_c = eB/mc$

逆关系：$\rho_{xx} = \frac{\sigma_{xx}}{\sigma_{xx}^2+\sigma_{xy}^2}$，$\rho_{xy} = -\frac{\sigma_{xy}}{\sigma_{xx}^2+\sigma_{xy}^2}$

**📌 考试形态：** 推导题/选择题
- 给定 $\sigma_{xx}=0$ 时，$\sigma_H = \sigma_{xy} = -nec/B$
- 问：霍尔电阻与磁场强度的关系

**⚠️ 易错警示：**
- $\sigma_{xx}=0$ 时 $\rho_{xx}=0$ 也成立（重要：IQHE平台处纵向电阻为零）
- $\sigma_{xy}$ 与 $\rho_{xy}$ 的关系要注意符号

---

### [Landau能级的量子力学解] 🟡 P1
**来源：** Slide 10-11

**📖 定义/表述：**
量子力学下（E沿x方向），哈密顿量：
$H = \frac{1}{2m}\left(\boldsymbol{P} + \frac{e\boldsymbol{A}}{c}\right)^2 + eEx$

选择矢量势 $\boldsymbol{A} = (0, Bx, 0)$，波函数 $\Psi(x,y) = e^{-ik_y y}\phi(x)$

解出Landau能级：
$\varepsilon_i = \left(i+\frac{1}{2}\right)\hbar\omega_c + eE l_c^2 k_y - \frac{(eE)^2}{2m\omega_c^2}$

其中 $l_c = \sqrt{\frac{\hbar c}{eB}}$ 为经典回旋半径。

**📌 考试形态：** 推导题
- 问：Landau能级的简并度？答：$eB/(hc)$ 每单位面积
- 问：2D与3D中Landau能谱的区别？答：2D完全分立，3D沿B方向连续

**⚠️ 易错警示：**
- Landau能级能量与 $k_y$ 有关（有电场时），导致能级倾斜
- 经典回旋半径 $l_c = \sqrt{\hbar c/eB}$，随B增大而减小

---

### [整数量子霍尔效应 IQHE] 🔴 P0
**来源：** Slide 13-23

**📖 定义/表述：**
1980年 von Klitzing, Dorda, Pepper 在 Si-MOSFET 中发现。核心特征：
1. 霍尔电阻出现平台：$R_H = \frac{h}{ie^2}$，$i$ 为整数，精度 $\sim 5$ ppm
2. 平台处纵向电阻 $\rho_{xx} = 0$
3. 平台对应 Fermi 能级位于 Landau 能级间隙中

**机制**（Laughlin 1981, Halperin 1982）：
- 杂质展宽 Landau 能级 → 扩展态（导电）+ 局域态（不导电）
- Fermi 能级在能隙中时，扩展态占据数不变 → 霍尔电流不变
- 规范变换证明：$G_H = \frac{iec}{\hbar}\frac{\partial n}{\partial B}$ → $R_H = \frac{h}{e^2 i}$

**应用：**
- 电阻标准：$h/e^2 = 25812.806\ \Omega$（精度 $\sim 2\times10^{-8}$）
- 精细结构常数测量：$\alpha = e^2/(2hc\epsilon_0)$

**💡 通俗理解：**
强磁场下电子的动能"冻结"成离散的Landau能级。每填满一个能级，霍尔电阻就锁定在 $h/(ie^2)$，纵向电阻降为零——电子像在无摩擦的高速公路上沿着样品边缘奔驰。

**📌 考试形态：** 简答题/选择题
- 问：IQHE 的三大特征
- 问：为什么 Hall 电阻会有平台？
- 问：电阻标准的数值与精度

**⚠️ 易错警示：**
- 平台处 $\rho_{xx}=0$ 但 $\sigma_{xx}=0$ 也成立（不要搞混电阻和电导）
- IQHE 是单粒子效应（单电子在强磁场中的量子化），不需电子-电子相互作用
- Landau能级简并度 $g = eB/(hc)$，占据 $i$ 个能级时 $n = ieB/(hc)$

---

### [分数量子霍尔效应 FQHE] 🔴 P0
**来源：** Slide 24-32

**📖 定义/表述：**
1982年崔琦 (D.C. Tsui)、Stomer 在极纯 GaAs/AlGaAs 异质结中发现分数占据数的霍尔平台。1998年诺贝尔奖。

**Laughlin 波函数**（1983）：
$\Psi(\{z\}) = \prod_{i<j} (z_i - z_j)^m \exp\left(-\sum_k |z_k|^2/4l_c^2\right)$

占据数：$\nu = 1/m$（$m$ 为奇数）

**核心物理：**
- FQHE **不能**在单粒子图像下解释，必须引入电子-电子相互作用
- Laughlin态的能量低于同密度下的 CDW 态
- 激发态有能隙，准粒子带分数电荷（$e/3$, $e/5$）
- Laughlin态是不可压缩的量子液体状态

**复合费米子模型（CF）：**
- 一个复合费米子 = 一个电子 + 偶数个磁通线
- FQHE = CF 在有效磁场下的 IQHE
- CF 具有整数电荷
- 可解释所有观察到的分数态及其相对强度

**级联模型**（Haldane, Halperin）：
$\nu = \frac{1}{mp + \alpha}$，$\alpha = \pm 1$（$\alpha = +1$ 对应粒子型元激发，$\alpha = -1$ 对应空穴型）

**💡 通俗理解：**
电子们"商量"着形成了全新的量子流体——每个电子都抱着磁通线跳舞。这种集体舞只有特定的"节拍"（占据数 1/3, 1/5...）才能跳好，产生了带分数电荷的准粒子。

**📌 考试形态：** 简答题/论述题
- 问：IQHE 和 FQHE 的根本区别（能隙来源不同）
- 问：Laughlin 波函数的形式及意义
- 问：复合费米子图像

**⚠️ 易错警示：**
- FQHE 的能隙来自 **多体关联**，IQHE 的能隙来自 **单粒子 Landau 能级量子化**
- Laughlin 波函数中 $m$ 是奇数
- CF 模型的核心：$\nu = 1/2$ 态对应有效磁场为零 → 金属行为

---

## 4.2 几何位相与拓扑态

### [SSH模型与缠绕数] 🔴 P0
**来源：** Slide 45-49

**📖 定义/表述：**
Su-Schrieffer-Heeger (SSH) 模型：一维链，每个原胞两个原子，交错跃迁。
- 能带色散关系可写为一般两带哈密顿量（$2\times2$ 矩阵）
- Bulk winding number（缠绕数）：表征 $d_x\text{-}d_y$ 平面中 $d$ 矢量环绕原点的次数
- 拓扑相变条件：体能隙关闭并重新打开；子晶格（手征）对称性被破坏

**Bulk-boundary correspondence（体-边对应）：**
缠绕数 = 边缘态数目。完全二聚化极限：
- 平庸态（trivial）：链两端无边缘态
- 非平庸态（nontrivial）：链两端各有一个零能边缘态

**💡 通俗理解：**
SSH 模型是拓扑物理的"Hello World"。通过改变原子间跳跃的强弱，可以让整条链变成"正常的"绝缘体或"拓扑的"绝缘体——后者会在两端出现"躲不掉"的电子态。

**📌 考试形态：** 简答题
- 问：缠绕数的定义及其物理意义
- 问：什么是体-边对应？
- 问：SSH 模型的拓扑相变条件

**⚠️ 易错警示：**
- 缠绕数在体能隙关闭时才能改变
- 边缘态的能量为零（位于能隙中间）
- 非平庸态的边缘态只出现在 A 或 B 子格上

---

### [Berry 相位] 🔴 P0
**来源：** Slide 54-72

**📖 定义/表述：**
Berry 相位：系统参数绝热循环一周，波函数获得的几何相位。

Berry 连接（Berry connection）：$\boldsymbol{A}(\boldsymbol{R}) = i\langle u(\boldsymbol{R}) | \nabla_{\boldsymbol{R}} | u(\boldsymbol{R})\rangle$

Berry 曲率（Berry curvature）：$\boldsymbol{\Omega}(\boldsymbol{R}) = \nabla_{\boldsymbol{R}} \times \boldsymbol{A}(\boldsymbol{R})$

Berry 相位：$\gamma = \oint_C \boldsymbol{A} \cdot d\boldsymbol{R} = \int_S \boldsymbol{\Omega} \cdot d\boldsymbol{S}$（斯托克斯定理）

**核心性质：**
1. **规范不变性** — 使得 Berry 相更加物理化（Slide 72）
2. **几何性质** — 可表示为参数空间闭合回路线积分，与路径变化率无关
3. **拓扑性质** — 这种"拓扑性"使其广泛应用于量子霍尔效应和拓扑绝缘体研究
4. 与规范场论和微分几何有密切联系

**直观例子**（Slide 71）：
球面上平行移动矢量，回到出发点后矢量旋转了一定角度。这个角度是球面固有曲率的表现，正是直观感受的 Berry 相。

**离散版本**（Slides 65-66）：Berry 相位可以用离散格式计算。

**二能级系统示例**（Slides 67-70）：
本征态只依赖于矢量 $d$ 的方向；Berry curvature = 1/2 of the monopole field。

**💡 通俗理解：**
一个量子态在参数空间中走一圈回来，不仅会获得能量随时间积累的"动力学相"，还会获得一个纯粹由"路径的形状"决定的几何相——这就是Berry相。好比在弯曲的地球表面平移一个箭头，走一圈回到原点会发现箭头指向变了。

**📌 考试形态：** 选择题/简答题
- 问：Berry 相的定义公式
- 问：Berry 相与动力学相的区别
- 问：Berry 相的规范不变性意味着什么？

**⚠️ 易错警示：**
- 不要混淆 Berry 相（几何/拓扑）与动力学相（依赖于能量和演化时间）
- Stokes 定理要求 Berry 曲率 $\boldsymbol{\Omega}$ 在曲面 $S$ 上处处有定义
- Berry 相位不依赖参数变化速度（绝热条件下），只依赖闭合路径的几何

---

### [Chern 数（陈数）] 🔴 P0
**来源：** Slide 73-76

**📖 定义/表述：**
固体中参数空间是电子动量，Berry 曲率在 Brillouin 区的积分给出 Chern 数：
$C = \frac{1}{2\pi} \int_{\text{BZ}} \Omega(\boldsymbol{k})\ d^2k$

Hall 电导（TKNN 公式）：$\sigma_{xy} = \frac{e^2}{h} \cdot C$

**物理意义：**
- Chern 数是整数拓扑不变量
- 在绝热变形下不变，只要体能隙不关闭
- 决定量子霍尔电导的量子化值
- IQHE：Chern 数为整数 = 填充的 Landau 能级数

**💡 通俗理解：**
Chern 数是 Berry 曲率在整个 Brillouin 区的"总流量"——一个只能取整数的拓扑量子数。它像一把尺子，告诉你这个体系的霍尔电导是 $e^2/h$ 的多少倍。

**📌 考试形态：** 简答题/选择题
- 问：Chern 数的定义公式
- 问：Chern 数与 Hall 电导的关系
- 问：为什么 Chern 数是整数？

**⚠️ 易错警示：**
- Chern 数对平庸绝缘体为 0，对 QHE 体系为非零整数
- 3D 体系有 3 个 Chern 数（每个方向一个）
- 有自旋时用 Spin Chern number

---

### [Z₂ 拓扑不变量与 2D 拓扑绝缘体] 🔴 P0
**来源：** Slide 83-85

**📖 定义/表述：**
时间反演对称系统用 Z₂ 拓扑不变量 $\nu = (0,1)$ 分类。

**时间反演对称性**（Slide 83）：
- 反幺正时间反演算符
- 时间反演不变动量点（TRIM）
- Kramers 简并：TRIM 处态能量简并
- 边缘态交叉受保护（即使自旋不守恒）
- 无背散射 → 强无序下也没有 Anderson 局域化

**Z₂ 数的计算方法**（Slide 85）：
1. **自旋守恒**（$S_z$ 是好量子数）：$Z_2 = \text{mod}(C_{\text{up}}, 2)$，其中 $C_{\text{up}} = -C_{\text{down}}$
2. **反演对称性守恒**：从所有 TRIM 点的占据 Bloch 态的**宇称**计算

**体-边对应图像**（Slide 84）：
- 普通绝缘体：偶数条能带穿过 Fermi 能级
- 拓扑绝缘体：奇数条能带穿过 Fermi 能级

**💡 通俗理解：**
时间反演对称性给电子自旋上了一道"保险"：在拓扑绝缘体的边缘，自旋向上和向下的电子必须向相反方向运动且不能被杂质散射回头。这就是 Z₂ 拓扑绝缘体的"单向高速公路"。

**📌 考试形态：** 简答题/选择题
- 问：Z₂ 拓扑不变量的物理含义
- 问：时间反演对称下边缘态有哪些性质？
- 问：如何从宇称计算 Z₂ 数？

**⚠️ 易错警示：**
- Z₂ 只有 0 和 1 两个值（Z₂ 因此得名）
- 自旋守恒时用 spin Chern 数，不守恒时需用更复杂的 PFaffian 方法
- Kramers 简并保护边缘态交叉不被打开能隙

---

### [Kane-Mele 模型：Graphene 中的 2D 拓扑绝缘体] 🔴 P0
**来源：** Slide 89-96

**📖 定义/表述：**
Kane-Mele 模型在石墨烯中通过内禀自旋-轨道耦合（SOC）打开拓扑非平庸能隙，实现量子自旋霍尔（QSH）效应。

哈密顿量：
$H = -t \sum_{\langle i,j\rangle} c_i^\dagger c_j + i\lambda_{SO} \sum_{\langle\langle i,j\rangle\rangle} \nu_{ij} s^z c_i^\dagger c_j + \lambda_v \sum_i \xi_i c_i^\dagger c_i + \lambda_R \sum_{\langle i,j\rangle} c_i^\dagger (s \times \hat{d}_{ij})_z c_j$

- $\lambda_{SO}$：内禀自旋-轨道耦合 → Z₂ 拓扑非平庸
- $\lambda_v$：交错子格势（stagger sublattice potential）
- $\lambda_R$：Rashba SOC

**关键特征：**
- Dirac 锥已然是拓扑非平庸的（Slide 91）
- SOC 引入能隙，无需能带反转
- 产生螺旋边缘态（helical edge states）——自旋滤波的一维导电通道
- 石墨烯中 SOC 能隙很小：$2\lambda_I \sim 20\text{-}50\ \mu\text{eV}$

**扩展材料**（Slides 94-96）：
- Silicene, Germanene：低翘曲蜂窝结构，SOC 增强
- 重金属增强 SOC（Slide 95）
- 衬底增强 SOC（Slide 96）

**💡 通俗理解：**
石墨烯的电子本来像无质量 Dirac 费米子一样飞奔。加上自旋-轨道耦合后，体能带虽然打开了"缝隙"，但边缘处出现了自旋向上只能向右、自旋向下只能向左的"单行道"——这就是量子自旋霍尔效应。

**📌 考试形态：** 简答题
- 问：Kane-Mele 模型的物理图像
- 问：Dirac 点的拓扑性质
- 问：SOC 在石墨烯中起什么作用？

**⚠️ 易错警示：**
- 石墨烯 SOC 能隙极小（$\mu$eV 量级），无法室温观测
- 螺旋边缘态的自旋-动量锁定：自旋与运动方向刚性耦合
- SOC → Z₂ = 1；交错势 → QVH（量子谷霍尔）；交换场 → QAH（量子反常霍尔）

---

### [BHZ 模型：HgTe 量子阱] 🟡 P1
**来源：** Slide 105

**📖 定义/表述：**
Bernevig-Hughes-Zhang (BHZ) 模型描述 HgTe/CdTe 量子阱中的能带反转机制。

- 量子阱厚度 $d$ 临界值 $d_c$
- $d < d_c$：正常能带顺序（平庸绝缘体）
- $d > d_c$：$m/B < 0$，能带反转 → 拓扑绝缘体
- Science 314, 1757 (2006)

**💡 通俗理解：**
HgTe 量子阱像一块"跷跷板"——厚度超过某个临界值时，导带和价带的位置会互换。这个"反转"就是拓扑非平庸的根源。

**📌 考试形态：** 简答题
- 问：能带反转的含义和后果

---

### [量子谷霍尔效应 QVH] 🟡 P1
**来源：** Slide 117-123

**📖 定义/表述：**
在石墨烯中加入交错子格势（如与 BN 衬底耦合），打破反演对称性，实现谷极化。

$E(q) = \pm \sqrt{\left(\frac{3}{2} a t q\right)^2 + \Delta^2}$

**谷 Chern 数：**
- $C_K = 1$, $C_{K'} = -1$
- 总 Chern 数：$C = C_K + C_{K'} = 0$
- Valley Chern 数：$C_v = C_K - C_{K'} = 2C_K$

**谷极化的产生**（Slide 119）：
- 左旋圆偏振光 → 激发 K 谷
- 右旋圆偏振光 → 激发 K' 谷

**MoS₂ 单层**（Slide 120-121）：圆偏振光激发下产生谷极化，通过光致发光（PL）谱探测。

**💡 通俗理解：**
石墨烯有两个"谷"（K 和 K'），像两个山谷。加上交错势后，两个谷的物理性质变得不同——每个谷有自己的 Chern 数，可以分别操控。

**📌 考试形态：** 选择题/简答题
- 问：总 Chern 数与 Valley Chern 数的区别
- 问：如何实现谷极化？

---

### [量子反常霍尔效应 QAHE] 🔴 P0
**来源：** Slide 125-140

**📖 定义/表述：**
量子反常霍尔效应（QAHE）——不需要外磁场的量子霍尔效应，通过打破时间反演对称性实现。

**实现途径**（Slide 125）：
1. 周期性磁场（零磁通）→ 破缺 TRS
2. 磁性掺杂 → 内禀交换场
3. 衬底近邻效应 → 诱导磁性

**技术路线**（Slide 139）：
- TI 薄膜（如 Bi₂Se₃）适当厚度 + MBE 生长
- 磁性掺杂（Cr, V 等）产生垂直磁各向异性 → 铁磁绝缘体
- 化学掺杂/场效应调节化学势
- 实验验证：Science 340, 167 (2013)

**主要模型：**
- 石墨烯 + Rashba SOC + 交换场 → $C = 2$（Slides 127-129）
- Bi₂Se₃ 薄膜 → $C = 1$（Slide 130）
- 有机体系 Mn₂C₁₂H₁₂ → $C = 1$（Slide 131）

**面内磁化 QAHE**（Slide 135）：需破缺所有镜面对称性（面内和面外）。

**实验确认**（Slide 140）：5QL 样品在 1.4K 下观测到零场 QAH 效应；外加磁场可将量子化温度提升至 6.5K。

**💡 通俗理解：**
普通 QHE 需要巨大磁场才能看到。QAHE 就像"自带磁铁"——材料内部的磁性原子提供了等效磁场，让量子霍尔效应在零外磁场下也能发生。

**📌 考试形态：** 简答题/选择题
- 问：QAHE 需要什么条件？与 IQHE 的区别？
- 问：QAHE 中 C=1 和 C=2 的区别

**⚠️ 易错警示：**
- QAH 与 QSH 的区别：QAH 破缺 TRS，QSH 保护 TRS
- 实现 QAHE 需要同时满足：TI + 磁性 + 绝缘体

---

### [3D 拓扑绝缘体] 🔴 P0
**来源：** Slide 141-150

**📖 定义/表述：**
3D 拓扑绝缘体：具有绝缘体能隙但表面存在拓扑保护的金属态。

**Bi₂Se₃ 原型**（Slide 142）：
- 含 SOC → 奇偶性反转 → 拓扑表面态
- 无 SOC → 普通绝缘体

**探测手段**（Slide 143）：
- ARPES（角分辨光电子能谱）：探测表面能带结构和自旋纹理
- STM（扫描隧道显微镜）：探测实空间表面态

**主要特征**（Slides 144-145）：
- 螺旋自旋纹理（Helical spin texture）
- 拓扑表面态 Dirac 锥

**弱 TI**（Slides 146-148）：由堆叠 2D TI 层构成，具有 1D 边缘态（非 2D 表面态）。

**半整数量子霍尔效应**（Slide 150）：Bi₂Se₃ 上/下表面共同贡献，表现为 $\nu = \pm 1/2$ 的量子霍尔效应。

**💡 通俗理解：**
3D 拓扑绝缘体像穿了"绝缘盔甲"——内部完全不导电，但表面有一层"盔甲"可以导电。这层表面导电"盔甲"因为拓扑保护，不会被划伤或污染破坏。

**📌 考试形态：** 简答题
- 问：3D 拓扑绝缘体的特征
- 问：ARPES 和 STM 如何探测拓扑表面态？
- 问：强 TI 与弱 TI 的区别

**⚠️ 易错警示：**
- 3D TI 的表面态是 2D 的，不是 1D 的
- 强 TI 在所有表面都有金属态；弱 TI 只在特定方向的表面出现
- 3D TI 的表面态受时间反演对称性保护

---

### [拓扑半金属] 🟡 P1
**来源：** Slide 152-167

**📖 定义/表述：**
拓扑半金属：体态无能隙但拓扑非平庸。

| 类型 | 简并度 | 特征 | 示例 |
|------|--------|------|------|
| Dirac 半金属 | 4 重简并 | Dirac 锥 | Na₃Bi, Cd₃As₂ |
| Weyl 半金属 | 2 重简并 | Weyl 点 + Fermi 弧 | TaAs |
| Nodal-line 半金属 | 连续简并线 | 节点线 | ZrSiS |

**关键物理**：
- Weyl 点：贝利曲率的磁单极（源或汇）
- Fermi 弧：连接相反手性 Weyl 点的表面态
- Type-II：倾斜的 Dirac/Weyl 锥，打破洛伦兹不变性

**💡 通俗理解：**
拓扑半金属是"半绝缘半金属"——体内允许电子通过（不像绝缘体），但又和普通金属不同：电子必须经过特定的"Weyl 点"才能穿梭，这些点像微观磁单极。

**📌 考试形态：** 选择题/简答题
- 问：三种拓扑半金属的区别
- 问：Fermi 弧是什么？

---

### [拓扑超导与马约拉纳费米子] 🟡 P2
**来源：** Slide 179

**简介：** 拓扑超导体 + 马约拉纳费米子（Majorana fermion）是当前热点。FeSeTe 体系：超导能隙很小，QAHE + SC。

---

## 4.3 二维体系中的相变

### [维度与相变：Mermin-Wagner 定理] 🟡 P1
**来源：** Slide 181

**📖 定义/表述：**
维度对相变和临界行为有重要影响。

- **1D**：$T>0$ 时体系总是无序，不存在长程序，无相变
- **2D**：取决于序参量自由度数 $N$
  - $N=1$：有相变，如二维 Ising 模型
  - $N=2$：无长程序但有准长程序，可发生 KT 相变
  - $N=3$：无相变，如二维 Heisenberg 模型

**关联函数对比：**
$G(r) \sim \begin{cases} e^{-r/\xi(T)} & \text{(1D)} \\ r^{-\eta(T)} & \text{(2D, KT相)} \\ \text{常数} & \text{(3D)} \end{cases}$

---

### [拓扑缺陷与涡旋] 🔴 P0
**来源：** Slide 183-191

**📖 定义/表述：**
拓扑缺陷：无法通过连续形变消除的不连续性。

以二维自旋体系为例：
- 二维格点上自旋与 X 轴夹角为 $\phi_i$
- 闭合回路 $L$：$\Phi_L = \sum_i \Delta\phi_i$
- $\Phi_L = 0$：非拓扑性激发，每个自旋方向角单值确定
- $\Phi_L = n \cdot 2\pi$，$n = \pm 1, \pm 2, \dots$：拓扑性激发，$n$ 为拓扑荷

**速度场分解**（将 $\phi(r)$ 视为速度势）：
$v(r) = \nabla\phi(r)$
- $v = v_s + v_v$（无旋场 + 无源场）
- $\nabla \times v_s = 0$，$\nabla \cdot v_v = 0$
- $v_s$ 和 $v_v$ 之间无相互作用：$\int v_s \cdot v_v\ dr = 0$

**涡旋相互作用**（Slide 192）：
- 拓扑性元激发之间相互作用在形式上等价于二维点电荷
- $U(r_i, r_j) = -2q_i q_j \ln \frac{|r_i - r_j|}{a}$

---

### [Kosterlitz-Thouless (K-T) 相变] 🔴 P0
**来源：** Slide 193-198

**📖 定义/表述：**
K-T 相变：由拓扑缺陷（涡旋）驱动的二维相变，2016 年诺贝尔物理学奖。

**X-Y 模型**：
$H = -J \sum_{\langle ij\rangle} \cos(\varphi_i - \varphi_j)$

简谐近似：$H = \frac{J}{2} \sum_{\langle ij\rangle} (\varphi_i - \varphi_j)^2$

**单涡旋能量和熵**：
- $E_v = J\pi \ln \frac{L}{a}$（$a$：点阵间距，$L$：系统尺寸）
- $S = k_B \ln \frac{L^2}{a^2}$（涡旋可在 $L^2/a^2$ 个位置上放置）
- $F_v = E_v - TS = J\pi \ln \frac{L}{a} - 2k_B T \ln \frac{L}{a}$

**临界温度**：$F_v = 0 \Rightarrow T_c = \frac{\pi J}{2k_B}$
- $T < T_c$：$F_v > 0$，正负涡旋束缚对（准长程序）
- $T > T_c$：$F_v < 0$，大量自由涡旋产生 → 拓扑长程序破坏

**K-T 相变的本质**（Slide 195）：
- 涡旋对屏蔽效应 → 重正化群处理
- 自由能的第 $n$ 级微商在相变点出现突变 → **无穷级相变**

**验证体系**（Slide 196-197）：二维氦超流膜，超流-正常流体转变由涡旋-反涡旋解束缚驱动。

**💡 通俗理解：**
普通相变是"有序→无序"，KT 相变是"绑在一起的涡旋对 → 自由涡旋"。温度低了，正/负涡旋成双成对，互不干扰；温度高了，对子解开，单个涡旋到处破坏秩序。

**📌 考试形态：** 简答题/计算题
- 问：K-T 相变的基本物理图像
- 问：$T_c$ 的推导（自由能 = 0 条件）
- 问：KT 相变与普通相变的区别
- 问：涡旋相互作用的对数形式

**⚠️ 易错警示：**
- KT 相变**不是**对称性破缺相变，而是拓扑缺陷驱动
- 准长程序（algebraic order）的关联函数是幂律衰减，不是常数
- KT 相变是**无穷级相变**（不是一级也不是二级）

---

## 4.4 准一维体系的 Peierls 不稳定性和电荷密度波

### [一维体系概述] 🟡 P1
**来源：** Slide 199

**📖 定义/表述：**
一维体系实例：导电聚合物、金属卤化物、KCP 晶体、过渡金属三硫化合物、电荷转移有机复合物、有机超导体 Bechgaard 盐 (TMTSF)₂X、有机铁磁体 m-PDPC、半导体纳米线/量子线。

能带：$E(k) = \frac{\hbar^2 k^2}{2m}$，$k_F = \frac{n}{4a}$

---

### [Peierls 不稳定性] 🔴 P0
**来源：** Slide 200-201

**📖 定义/表述：**
对于半满能带的一维晶格，等距离原子排列是不稳定的，会发生**二聚化**（dimerization）。

**机制：**
- 波长为 $\lambda = 1/k$ 的电子受格点反射，相邻格点反射波位相差 $\Delta\varphi = \Delta l \cdot 2\pi / \lambda = 2a \cdot 2\pi / \lambda$
- $\lambda = 2a$ 时：$\Delta\varphi = 2\pi$ → 电子波不能继续传播 → 能隙打开
- 能隙对应的布里渊区边界：$k_B = 1/(2a)$
- Peierls 不稳定性要求：$k_B = k_F$（费米面与布里渊区边界重合）

**结果：**
- 低温：体系处于二聚化的半导体/绝缘体状态，不导电
- 高温：电子获得热能 → 费米面上能隙消失 → 一维体系变成导体

**💡 通俗理解：**
想象一排等距原子，电子刚好填满一半的能带。原子们发现"两两配对"（二聚化）能让体系的能量更低，于是就自动形成了"二人组"的排列，同时打开了一个能隙。

**📌 考试形态：** 简答题/选择题
- 问：Peierls 不稳定性的条件和后果
- 问：为什么一维体系特别容易发生 Peierls 相变？

**⚠️ 易错警示：**
- Peierls 不稳定性是**一维专有**现象（二维和三维的屏蔽效应抑制了它）
- 不是所有一维晶体都发生 Peierls 相变，需要半满能带

---

### [电荷密度波 CDW] 🔴 P0
**来源：** Slide 202

**📖 定义/表述：**
电荷密度波（CDW）：Peierls 相变后晶格周期从 $a$ 变为 $a'$，形成超晶格。电子密度在新周期场中重新分布：

$\rho(x) = n_0 + n_c \cos\left(\frac{2\pi x}{\lambda} + \varphi\right)$

其中 $\lambda = 2a'$，$n_c$ 为密度起伏幅度，$\varphi$ 为初位相。

**关键条件**：$k'_B = 1/(2a') = k_F \Rightarrow a' = 1/(2k_F) = \lambda/2$

**基本特征**：空间调制电荷密度 + 费米能处能隙 + 半导体电导

**两种类型**：
1. **可公度相变**：$a'/a =$ 有理数，晶格整体仍具有周期性
2. **非公度相变**：$a'/a =$ 无理数，晶格整体无周期性

**💡 通俗理解：**
Peierls 相变后，原子重新排列（周期变了），电子密度也跟着"起浪"——在空间上周期性地浓淡分布，这就是电荷密度波（CDW）。

**📌 考试形态：** 简答题
- 问：CDW 的定义和公式
- 问：可公度和非公度相变的区别

**⚠️ 易错警示：**
- CDW 的波长 $\lambda$（或超晶格常数 $a'$）只取决于电子密度（$k_F$），与原晶格常数 $a$ 无关
- CDW 同时具备：电荷调制 + 能隙 + 半导体行为

---

### [自旋密度波 SDW] 🔴 P0
**来源：** Slide 203

**📖 定义/表述：**
考虑电子相互作用后，正负自旋电子的 CDW 位形可以不同，导致自旋密度起伏。

$\rho_\uparrow(x) = \frac{n_0}{2} + \frac{n_c}{2} \cos\left(\frac{2\pi x}{\lambda} + \varphi_\uparrow\right)$

$\rho_\downarrow(x) = \frac{n_0}{2} + \frac{n_c}{2} \cos\left(\frac{2\pi x}{\lambda} + \varphi_\downarrow\right)$

总 CDW：$\rho(x) = \rho_\uparrow(x) + \rho_\downarrow(x) = n_0 + n_c \cos\frac{\varphi_\uparrow-\varphi_\downarrow}{2} \cos\left(2\pi\frac{x}{\lambda} + \frac{\varphi_\uparrow+\varphi_\downarrow}{2}\right)$

SDW：$S(x) = \rho_\uparrow(x) - \rho_\downarrow(x) = \frac{n_c}{2} \sin\frac{\varphi_\uparrow-\varphi_\downarrow}{2} \cos\left(2\pi\frac{x}{\lambda} + \frac{\varphi_\uparrow+\varphi_\downarrow-\pi}{2}\right)$

**两种极限**：
- $\varphi_\uparrow = \varphi_\downarrow$：只有 CDW，无 SDW
- $\varphi_\uparrow = \varphi_\downarrow + \pi$：只有 SDW，无 CDW

**💡 通俗理解：**
CDW 是电荷密度在空间上"起浪"，SDW 是自旋密度在空间上"起浪"。两者是同一物理（电子-电子相互作用 + Peierls）的一体两面——取决于自旋向上和向下电子的位相关系。

**📌 考试形态：** 简答题
- 问：CDW 和 SDW 的关系
- 问：什么条件下只有 CDW？什么条件下只有 SDW？

**⚠️ 易错警示：**
- SDW 和 CDW 可以共存（一般情况），也可以独立存在
- 一维电子-晶格相互作用体系不是 CDW 的唯一来源

---

# 模块 4：公式/定理速查表

## 4.1 半导体低维电子系统

| 编号 | 公式 | 说明 | 适用条件 | 来源 |
|------|------|------|---------|------|
| F1 | $\varepsilon_n = \frac{n^2\pi^2\hbar^2}{2mW^2}$ | 方势阱子带能级 | $W = n\lambda/2$ | Slide 2 |
| F2 | $\varepsilon_n = (n-\frac12)\hbar\omega_0$ | 抛物线势子带能级 | $V(z) = \frac12 m\omega_0^2 z^2$ | Slide 2 |
| F3 | $\sigma_0 = ne^2\tau/m$ | 德鲁特电导率 | 无磁场 | Slide 8 |
| F4 | $\sigma_{xx} = \frac{\sigma_0}{1+(\omega_c\tau)^2}$ | 纵向电导率 | 有磁场 | Slide 9 |
| F5 | $\sigma_{xy} = -\sigma_0\frac{\omega_c\tau}{1+(\omega_c\tau)^2}$ | 霍尔电导率 | 有磁场 | Slide 9 |
| F6 | $\rho_{xx} = \frac{\sigma_{xx}}{\sigma_{xx}^2+\sigma_{xy}^2}$ | 纵向电阻率与电导关系 | 通用 | Slide 9 |
| F7 | $\rho_{xy} = -\frac{\sigma_{xy}}{\sigma_{xx}^2+\sigma_{xy}^2}$ | 霍尔电阻率与电导关系 | 通用 | Slide 9 |
| F8 | $\omega_c = eB/mc$ | 回旋频率 | 磁场B下 | Slide 9 |
| F9 | $\sigma_H = \sigma_{xy} = -\frac{nec}{B}$ | 霍尔电导（$\sigma_{xx}=0$时） | $\sigma_{xx}=0$ | Slide 10 |
| F10 | $\boldsymbol{j} = \boldsymbol{\sigma}\cdot\boldsymbol{E}$ | 电流密度-电场关系 | 张量形式 | Slide 8 |
| F11 | $\varepsilon_i = (i+\frac12)\hbar\omega_c + eEl_c^2k_y - \frac{(eE)^2}{2m\omega_c^2}$ | Landau能级（有电场） | 2DEG, 磁场B | Slide 11 |
| F12 | $l_c = \sqrt{\frac{\hbar c}{eB}}$ | 经典回旋半径（磁长度） | 磁场B | Slide 10 |
| F13 | $\sigma_H = \frac{ie^2}{h}$ | IQHE霍尔电导 | $i$个Landau能级填满 | Slide 19 |
| F14 | $R_H = \frac{h}{ie^2}$ | IQHE霍尔电阻 | $i$个Landau能级填满 | Slide 19 |
| F15 | $\frac{h}{e^2} = 25812.806\ \Omega$ | 电阻量子 | 自1990年电阻标准 | Slide 22 |
| F16 | $\alpha = \frac{e^2}{2hc\epsilon_0}$ | 精细结构常数 | 可由QHE精确测量 | Slide 23 |
| F17 | $n = \frac{ieB}{hc}$ | 二维电子密度（$i$个Landau能级） | 2D, 磁场B | Slide 19 |
| F18 | $\Psi = \prod_{i<j}(z_i-z_j)^m \exp(-\sum_k|z_k|^2/4l_c^2)$ | Laughlin波函数 | FQHE, $m$奇数 | Slide 29 |
| F19 | $\nu = 1/m$ | FQHE占据数 | Laughlin态 | Slide 29 |
| F20 | $\nu = \frac{1}{mp+\alpha}$ | FQHE级联模型 | $\alpha = \pm 1$ | Slide 31 |

## 4.2 几何位相与拓扑态

| 编号 | 公式 | 说明 | 适用条件 | 来源 |
|------|------|------|---------|------|
| F21 | $\boldsymbol{A}(\boldsymbol{R}) = i\langle u(\boldsymbol{R}) | \nabla_{\boldsymbol{R}} | u(\boldsymbol{R})\rangle$ | Berry连接 | 参数空间 | Slide 55 |
| F22 | $\boldsymbol{\Omega}(\boldsymbol{R}) = \nabla_{\boldsymbol{R}} \times \boldsymbol{A}(\boldsymbol{R})$ | Berry曲率 | 参数空间 | Slide 57 |
| F23 | $\gamma = \oint_C \boldsymbol{A} \cdot d\boldsymbol{R}$ | Berry相位（回路积分） | 绝热循环 | Slide 55 |
| F24 | $\gamma = \int_S \boldsymbol{\Omega} \cdot d\boldsymbol{S}$ | Berry相位（面积分） | Stokes定理 | Slide 57 |
| F25 | $C = \frac{1}{2\pi} \int_{\text{BZ}} \boldsymbol{\Omega}(\boldsymbol{k})\ d^2k$ | Chern数 | 2D Brillouin区 | Slide 73 |
| F26 | $\sigma_{xy} = \frac{e^2}{h} \cdot C$ | TKNN公式（Chern数→Hall电导） | 2D绝缘体 | Slide 75 |
| F27 | $E(q) = \pm \sqrt{(\frac32 a t q)^2 + \Delta^2}$ | 石墨烯能谱（有能隙） | 交错势$\Delta$ | Slide 117 |
| F28 | $C_K = 1, C_{K'} = -1$ | 谷Chern数 | 石墨烯K/K'点 | Slide 118 |
| F29 | $C_v = C_K - C_{K'}$ | Valley Chern数 | 谷霍尔效应 | Slide 118 |

## 4.3 二维体系中的相变

| 编号 | 公式 | 说明 | 适用条件 | 来源 |
|------|------|------|---------|------|
| F30 | $H = -J \sum_{\langle ij\rangle} \cos(\varphi_i - \varphi_j)$ | X-Y模型哈密顿量 | 最近邻相互作用 | Slide 194 |
| F31 | $H = \frac{J}{2} \sum_{\langle ij\rangle} (\varphi_i - \varphi_j)^2$ | X-Y模型（简谐近似） | 低温近似 | Slide 194 |
| F32 | $\Phi_L = \sum_i \Delta\phi_i = n\cdot 2\pi$ | 拓扑荷（涡旋强度） | 闭合回路 | Slide 190 |
| F33 | $E_v = J\pi \ln(L/a)$ | 单涡旋能量 | 二维 | Slide 194 |
| F34 | $S = k_B \ln(L^2/a^2)$ | 单涡旋熵 | 二维 | Slide 194 |
| F35 | $F_v = J\pi\ln(L/a) - 2k_B T\ln(L/a)$ | 单涡旋自由能 | 二维 | Slide 194 |
| F36 | $T_c = \pi J/(2k_B)$ | K-T相变临界温度 | X-Y模型 | Slide 194 |
| F37 | $U(r_i, r_j) = -2q_i q_j \ln(|r_i-r_j|/a)$ | 涡旋对相互作用 | 形如2D Coulomb | Slide 192 |
| F38 | $G(r) \sim r^{-\eta(T)}$ | 准长程序关联函数（代数衰减） | KT相低温 | Slide 181 |

## 4.4 Peierls 不稳定性和电荷密度波

| 编号 | 公式 | 说明 | 适用条件 | 来源 |
|------|------|------|---------|------|
| F39 | $E(k) = \hbar^2 k^2/(2m)$ | 一维自由电子能带 | 自由电子 | Slide 199 |
| F40 | $k_F = n/(4a)$ | 一维费米波矢 | 电子密度$n$ | Slide 199 |
| F41 | $k_B = 1/(2a)$ | 一维布里渊区边界 | 晶格常数$a$ | Slide 200 |
| F42 | $\rho(x) = n_0 + n_c \cos(2\pi x/\lambda + \varphi)$ | 电荷密度波 | CDW态 | Slide 202 |
| F43 | $k'_B = k_F \Rightarrow a' = 1/(2k_F) = \lambda/2$ | Peierls/CDW条件 | Fermi面与BZ边界重合 | Slide 202 |
| F44 | $\rho_\uparrow(x) = \frac{n_0}{2} + \frac{n_c}{2} \cos(2\pi x/\lambda + \varphi_\uparrow)$ | 自旋↑的CDW | 计入电子自旋 | Slide 203 |
| F45 | $\rho_\downarrow(x) = \frac{n_0}{2} + \frac{n_c}{2} \cos(2\pi x/\lambda + \varphi_\downarrow)$ | 自旋↓的CDW | 计入电子自旋 | Slide 203 |

---

# 模块 5：对比辨析表

## 5.1 IQHE vs FQHE

| 对比维度 | IQHE（整数量子霍尔效应） | FQHE（分数量子霍尔效应） |
|---------|------------------------|------------------------|
| **发现年份** | 1980 (von Klitzing) | 1982 (崔琦/Stomer) |
| **Hall平台值** | $R_H = h/(ie^2)$, $i$为整数 | $R_H = h/(\nu e^2)$, $\nu = p/m$ 分数 |
| **能隙来源** | **单粒子** Landau能级量子化 | **多体关联**效应 |
| **样品要求** | Si-MOSFET, 界面足够纯 | GaAs/AlGaAs异质结, 极高迁移率 |
| **理论解释** | 扩展态/局域态 + Laughlin规范变换 | Laughlin波函数 + 复合费米子 |
| **准粒子** | 整数电荷 | 分数电荷 ($e/3$, $e/5$...) |
| **物态** | 单粒子量子化态 | 不可压缩的量子液体 |
| **诺奖** | 1985 (von Klitzing) | 1998 (崔琦/Stomer/Laughlin) |
| **拓扑不变量** | Chern数 = 整数 | 复合费米子有效Chern数 |

**考试要点：核心区别是能隙来源（单粒子 vs 多体）**

---

## 5.2 CDW vs SDW

| 对比维度 | CDW（电荷密度波） | SDW（自旋密度波） |
|---------|------------------|------------------|
| **物理量** | 电荷密度 $\rho(x)$ 在空间调制 | 自旋密度 $S(x)$ 在空间调制 |
| **数学形式** | $\rho(x)=n_0+n_c\cos(2\pi x/\lambda+\varphi)$ | $S(x)=\frac{n_c}{2}\sin\frac{\varphi_\uparrow-\varphi_\downarrow}{2}\cos(2\pi x/\lambda+\cdots)$ |
| **条件** | $\varphi_\uparrow = \varphi_\downarrow$ 时纯CDW | $\varphi_\uparrow = \varphi_\downarrow+\pi$ 时纯SDW |
| **价电荷** | 电子密度不均匀 | 总电荷均匀，自旋密度不均匀 |
| **物理起源** | 电子-晶格相互作用（Peierls） | 电子-电子相互作用 |
| **能隙** | 有（Fermi面附近） | 有 |
| **共同点** | 都是Peierls不稳定性的结果，源于一维Fermi面嵌套 |

---

## 5.3 拓扑绝缘体 vs 普通绝缘体

| 对比维度 | 普通绝缘体 | 拓扑绝缘体 |
|---------|-----------|-----------|
| **体能隙** | 有 | 有 |
| **表面/边缘态** | 无 | 有（拓扑保护） |
| **Chern数/Z₂** | 0 | 非零 |
| **抗扰动能力** | 易受杂质影响 | 拓扑保护（无背散射） |
| **量子化的物理量** | 无 | 量子化霍尔电导 |
| **对称性保护** | 无 | 时间反演对称性（Z₂ TI） |
| **结构特征** | 平凡能带结构 | 能带反转或拓扑非平凡缠绕 |
| **电子输运** | 无导电通道 | 边缘/表面态导电 |

---

## 5.4 Berry 相 vs 动力学相

| 对比维度 | Berry 相（几何/拓扑相） | 动力学相 |
|---------|----------------------|---------|
| **起源** | 参数空间的几何性质（曲率） | 能量随时间积累：$e^{-iEt/\hbar}$ |
| **依赖因素** | 闭合路径的形状（拓扑） | 能量大小和演化时间 |
| **参数变化速度** | 不依赖（只需绝热） | 依赖 |
| **规范不变性** | 是（可观测） | 是（但含时） |
| **数学形式** | $\gamma = \oint i\langle u|\nabla_R u\rangle \cdot dR$ | $\theta = -\frac{1}{\hbar}\int E(t)dt$ |
| **应用** | QHE, 拓扑绝缘体, 极化, 反常速度 | 量子振荡, 干涉 |

---

## 5.5 2D 拓扑绝缘体 vs 3D 拓扑绝缘体

| 对比维度 | 2D 拓扑绝缘体 | 3D 拓扑绝缘体 |
|---------|--------------|--------------|
| **导电通道维度** | 1D 边缘态（helical edge state） | 2D 表面态（Dirac cone） |
| **拓扑不变量** | Z₂ (0 or 1) | Z₂ (4个指标: $\nu_0; \nu_1\nu_2\nu_3$) |
| **强/弱分类** | 只有一种 | 强TI（$\nu_0=1$）和弱TI（$\nu_0=0$） |
| **原型材料** | HgTe/CdTe QW, Kane-Mele graphene | Bi₂Se₃, Bi₂Te₃ |
| **探测手段** | 量子输运（边缘态电导） | ARPES（表面能带）, STM |
| **自旋纹理** | 螺旋边缘态（自旋-动量锁定） | 螺旋表面态（自旋-动量锁定） |
| **实验验证** | Science 318, 767 (2007) | Nature Phys. 5, 438 (2009) |
| **Hall效应** | 量子自旋Hall效应 | 半整数量子Hall效应 |

---

## 5.6 其他易混淆概念

| 对比 | Concept A | Concept B | 关键区别 |
|------|----------|----------|---------|
| QSH vs QVH vs QAH | 量子自旋Hall (TRS保护) | 量子谷Hall (反演破缺) | 量子反常Hall (TRS破缺) | 保护的对称性不同 |
| Dirac vs Weyl vs Nodal-line | 四重简并Dirac点 | 二重简并Weyl点 | 连续简并节点线 | 简并度和拓扑性质 |
| Type-I vs Type-II Weyl | 正常Weyl锥 | 倾斜Weyl锥（打破Lorentz） | 能谱倾斜方向 |

---

# 模块 6：一页纸终极总结

## 第四章 维度 — 考前速览（~500字）

### 🔴 P0 必杀技

**4.1 量子霍尔效应**
- **IQHE**：$R_H = h/(ie^2)$（整数平台），单粒子Landau能级量子化 → 扩展态/局域态 → 平台
- **FQHE**：$\nu = 1/m$（分数平台），Laughlin波函数 $\Psi = \prod(z_i-z_j)^m\exp(-\sum|z|^2/4l_c^2)$，多体关联能隙
- 核心区别：IQHE能隙=单粒子，FQHE能隙=多体；CF模型：FQHE=CF在有效磁场下的IQHE

**4.2 拓扑（** **全章绝对重点）**
- **Berry相**：$\gamma = \oint i\langle u|\nabla u\rangle\cdot dR$，几何相位，规范不变
- **Chern数**：$C = (1/2\pi)\int_{\text{BZ}}\Omega(k)d^2k$，$\sigma_{xy} = (e^2/h)C$
- **Z₂ TI**：$\nu = 0,1$，时间反演对称保护，helical edge state，无背散射
- **QAHE**：TRS破缺 + TI + 磁性 → 零场QHE
- **体-边对应**：缠绕数=边缘态数目

**4.3 K-T 相变**
- 2D XY模型：涡旋束缚对 $\xrightarrow{T>T_c}$ 解束缚
- $T_c = \pi J/(2k_B)$，准长程序，无穷级相变

**4.4 Peierls/CDW/SDW**
- Peierls：半满能带一维晶格二聚化 → 能隙打开
- CDW：$\rho(x) = n_0 + n_c\cos(2\pi x/\lambda + \varphi)$
- SDW：自旋↑/↓位相不同 → 自旋密度调制

### 📐 核心公式
| 公式 | 解释 |
|------|------|
| $\sigma_{xy} = -nec/B$ | 经典霍尔电导 |
| $\varepsilon_i = (i+1/2)\hbar\omega_c$ | Landau能级 |
| $\gamma = \oint A\cdot dR$ | Berry相 |
| $C = (1/2\pi)\int \Omega\ d^2k$ | Chern数 |
| $T_c = \pi J/(2k_B)$ | K-T相变温度 |
| $\rho(x) = n_0+n_c\cos(2\pi x/\lambda+\varphi)$ | CDW |

### ⚠️ 混淆点
1. **IQHE vs FQHE**：能隙来源不同（单粒子 vs 多体）
2. **CDW vs SDW**：相位关系 $\varphi_\uparrow - \varphi_\downarrow$ 决定
3. **QSH vs QVH vs QAH**：保护的对称性不同

---

# 模块 7：Anki 卡片（TSV 格式）

```tsv
"assp4::维度::4.1","Q: IQHE 霍尔电阻平台的公式是什么？","A: R_H = h/(ie^2)，i为整数（填满的Landau能级数）。当Fermi能级位于Landau能级间隙时出现平台。 来源：Slide 16","P0 formula"
"assp4::维度::4.1","Q: IQHE 和 FQHE 的能隙来源有什么根本区别？","A: IQHE的能隙来源于单粒子Landau能级在强磁场中的量子化；FQHE的能隙来源于多体关联效应。 来源：Slide 31","P0 confuse"
"assp4::维度::4.1","Q: Laughlin 波函数的形式是什么？适用于什么体系？","A: Ψ = ∏(z_i-z_j)^m exp(-∑|z_k|^2/4l_c^2)，适用于ν=1/m的FQHE态（m为奇数）。 来源：Slide 29","P0 formula"
"assp4::维度::4.1","Q: 什么是复合费米子？","A: 一个复合费米子由一个电子和偶数个磁通线构成。FQHE是复合费米子在有效磁场下的IQHE。复合费米子具有整数电荷。 来源：Slide 32","P0 concept"
"assp4::维度::4.1","Q: 量子霍尔效应的电阻标准值是多少？","A: h/e^2 = 25812.806 Ω，自1990年起作为电阻标准，精度约2×10^-8。 来源：Slide 22","P0 fact"
"assp4::维度::4.1","Q: 方势阱和抛物线势限制下子带能量的公式分别是什么？","A: 方势阱：ε_n = n²π²ℏ²/(2mW²)；抛物线势：ε_n = (n-1/2)ℏω₀。 来源：Slide 2","P1 formula"
"assp4::维度::4.1","Q: GaAs-AlGaAs异质结中二维电子气的典型迁移率和平均自由程是多少？","A: 迁移率10⁴~10⁶ cm²/V·s，弹性散射平均自由程10²~10⁴ nm。 来源：Slide 5","P1 fact"
"assp4::维度::4.2","Q: Berry相的定义公式是什么？它有什么核心性质？","A: γ = ∮_C i⟨u(R)|∇_R|u(R)⟩·dR。核心性质：规范不变性、几何性质（路径形状决定）、拓扑性质（与路径变化率无关）。 来源：Slide 55-72","P0 definition"
"assp4::维度::4.2","Q: Chern数的定义及其与量子霍尔电导的关系是什么？","A: C = (1/2π)∫_{BZ} Ω(k) d²k，σ_xy = (e²/h)·C（TKNN公式）。Chern数是整数拓扑不变量。 来源：Slide 73-76","P0 formula"
"assp4::维度::4.2","Q: 什么是体-边对应（bulk-boundary correspondence）？","A: 体系体态的拓扑不变量（如缠绕数、Chern数）等于其边缘上拓扑保护边缘态的数目。例如SSH模型中缠绕数=边缘态数目。 来源：Slide 53","P0 concept"
"assp4::维度::4.2","Q: 2D拓扑绝缘体的Z₂拓扑不变量有什么物理含义？","A: Z₂ = 0（平庸绝缘体，偶数条边缘态能带穿过Fermi能级）或1（拓扑绝缘体，奇数条）。受时间反演对称性保护，边缘态无背散射。 来源：Slide 84-85","P0 concept"
"assp4::维度::4.2","Q: Kane-Mele模型中石墨烯如何成为二维拓扑绝缘体？","A: 通过内禀自旋-轨道耦合(λ_SO)在Dirac点打开拓扑非平庸能隙（Z₂=1），产生helical edge states。但石墨烯中SOC能隙极小（2λ_I~20-50 μeV）。 来源：Slide 89-91","P0 concept"
"assp4::维度::4.2","Q: QAHE（量子反常霍尔效应）的实现条件是什么？","A: (1)拓扑绝缘体薄膜，适当厚度；(2)磁性掺杂产生垂直磁各向异性 → 铁磁绝缘体；(3)调节化学势至能隙中。无需外磁场。 来源：Slide 139","P0 concept"
"assp4::维度::4.2","Q: 3D拓扑绝缘体Bi₂Se₃的拓扑表面态有哪些特征？","A: (1)受时间反演对称保护的2D表面Dirac锥；(2)螺旋自旋纹理（自旋-动量锁定）；(3)可通过ARPES和STM探测。 来源：Slide 142-145","P0 concept"
"assp4::维度::4.2","Q: 什么是拓扑半金属的三种主要类型？","A: (1)Dirac半金属（4重简并Dirac锥）；(2)Weyl半金属（2重简并Weyl点+Fermi弧）；(3)Nodal-line半金属（连续简并线）。体态无能隙但拓扑非平庸。 来源：Slide 152","P1 concept"
"assp4::维度::4.2","Q: Berry相与动力学相有什么区别？","A: Berry相是几何/拓扑相位（参数空间闭合路径）γ=∮A·dR，不依赖演化速率；动力学相是能量随时间积累θ=-∫E(t)dt/ℏ，依赖时间和能量。 来源：Slide 63","P0 confuse"
"assp4::维度::4.3","Q: K-T相变的基本物理图像是什么？","A: 2D XY模型中，低温下正负涡旋形成束缚对（准长程序），温度升高到T_c=πJ/(2k_B)时涡旋对解束缚，产生大量自由涡旋破坏拓扑长程序。无穷级相变。 来源：Slide 193-195","P0 concept"
"assp4::维度::4.3","Q: 为什么一维体系T>0时总是无序、无长程序？","A: Mermin-Wagner定理：低维体系中热涨落会破坏长程有序。1D关联函数指数衰减G(r)~e^{-r/ξ}，不存在相变。 来源：Slide 181","P1 theorem"
"assp4::维度::4.4","Q: Peierls不稳定性的条件和后果是什么？","A: 条件：半满能带的一维晶格。后果：等距离原子排列不稳定，发生二聚化（周期变为2a），BZ边界与Fermi面重合，能隙打开。低温绝缘体/半导体，高温导体。 来源：Slide 201","P0 concept"
"assp4::维度::4.4","Q: CDW和SDW的关系是什么？相位差如何决定？","A: ρ(x)=ρ↑+ρ↓（总CDW），S(x)=ρ↑-ρ↓（SDW）。φ↑=φ↓→只有CDW无SDW，φ↑=φ↓+π→只有SDW无CDW。一般情况两者共存。 来源：Slide 203","P0 concept"
"assp4::维度::4.4","Q: CDW的波长λ由什么决定？","A: λ = 2a' = 2/k_F，只取决于电子密度（费米波矢k_F），与原晶格常数a无关。a'/a为有理数时可公度，无理数时非公度。 来源：Slide 202","P0 concept"
"assp4::维度::4.2","Q: 什么是量子谷霍尔效应（QVH）？如何实现谷极化？","A: 打破反演对称性（如石墨烯加BN衬底），使K和K'谷具有相反Chern数（C_K=1, C_K'=-1）。谷极化通过圆偏振光实现：左旋光激发K谷，右旋光激发K'谷。 来源：Slide 117-119","P1 concept"
```

---

# 模块 8：练习题

## 选择题（共5题）

### Q1. 关于整数量子霍尔效应（IQHE），下列说法正确的是？
A. 霍尔平台出现在所有磁场强度下
B. 能隙来源于电子-电子多体相互作用
C. 纵向电阻 $\rho_{xx}$ 在平台处为零
D. 不需外磁场也能观测到

**答案：C**

**解析：** IQHE 中霍尔平台只在特定磁场范围出现（Landau能级间隙对应 $\rho_{xx}=0$）。能隙来源于单粒子Landau能级量子化（非多体）。需要强外磁场（非零场）。平台处纵向电阻和纵向电导同时为零。

---

### Q2. 关于 Berry 相位，下列表述错误的是？
A. 是绝热循环中波函数获得的几何相位
B. Berry 曲率在参数空间的积分等于 Chern 数
C. 与动力学相一样依赖于系统演化的时间
D. 具有规范不变性

**答案：C**

**解析：** Berry 相不依赖演化时间（只依赖于参数空间的闭合路径），而动力学相 $e^{-iEt/\hbar}$ 依赖于演化时间。A、B、D 都是 Berry 相的正确性质。

---

### Q3. 对于二维 XY 模型，Kosterlitz-Thouless 相变的临界温度是？
A. $T_c = J/k_B$
B. $T_c = \pi J/(2k_B)$
C. $T_c = 2\pi J/k_B$
D. $T_c = 0$（不存在有限温度相变）

**答案：B**

**解析：** 由单涡旋自由能 $F_v = J\pi\ln(L/a) - 2k_BT\ln(L/a)$ 在 $F_v = 0$ 时得到 $T_c = \pi J/(2k_B)$。这是 KT 相变的特征温度，涡旋在此温度以上自由能为负，大量自发产生。

---

### Q4. 一维 Peierls 不稳定性中，下列哪个条件必须满足？
A. 晶格必须处于半满能带状态
B. 系统必须是三维的
C. 必须有强电子-电子关联
D. 费米面必须与布里渊区边界垂直

**答案：A**

**解析：** Peierls 不稳定性要求能带半满，这样二聚化后的布里渊区边界（$k_B = 1/(2a')$）恰好与费米波矢 $k_F$ 重合，打开能隙使电子能量降低。这是**一维专有**现象，与三维无关；不一定需要强电子关联；关键条件是 $k_B = k_F$。

---

### Q5. 关于 CDW 和 SDW，下列说法正确的是？
A. CDW 和 SDW 不能共存
B. SDW 仅在三维体系中存在
C. 当 $\varphi_\uparrow = \varphi_\downarrow$ 时，只有 CDW，没有 SDW
D. CDW 的波长由晶格常数决定

**答案：C**

**解析：** 当自旋↑和↓的 CDW 位相相等时，总自旋密度 $S(x) = \rho_\uparrow - \rho_\downarrow = 0$，只有 CDW 无 SDW（见 Slide 203 公式）。A：CDW 和 SDW 完全可以共存。B：SDW 在一维电子体系中出现。D：CDW 波长 $\lambda = 2/k_F$ 只由电子密度决定，与原晶格常数无关。

---

## 简答题（共3题）

### Q6. 简述 IQHE 和 FQHE 的核心区别（至少3点）。

**答题要点：**
1. **能隙来源不同**：IQHE 能隙来自单粒子 Landau 能级的量子化（单电子效应）；FQHE 能隙来自多体关联效应（电子-电子相互作用）
2. **霍尔平台值不同**：IQHE 为 $h/(ie^2)$（整数）；FQHE 为 $h/(\nu e^2)$ 其中 $\nu = p/m$（分数）
3. **准粒子电荷不同**：IQHE 为准粒子带整数电荷；FQHE 的准粒子带分数电荷（$e/3$, $e/5$ 等）
4. **理论描述不同**：IQHE 用扩展态/局域态 + 规范变换描述；FQHE 用 Laughlin 波函数 + 复合费米子模型描述
5. **样品要求不同**：FQHE 需要更高纯度和迁移率的样品（GaAs/AlGaAs 异质结）

---

### Q7. 解释什么是 bulk-boundary correspondence（体-边对应），并以 SSH 模型为例说明。

**答题要点：**
- **定义**：体系的体态拓扑不变量（如缠绕数、Chern 数、Z₂ 数）等于其边界上拓扑保护的边缘态数目。
- **SSH 模型**：
  - 一维交错跃迁链，拓扑不变量是缠绕数（winding number）$n$
  - 缠绕数通过体态的 $d$ 矢量在 $d_x\text{-}d_y$ 平面绕原点圈数计算
  - 非平庸相（$n \neq 0$）：链两端各出现一个零能边缘态
  - 平庸相（$n = 0$）：链两端无边缘态
  - 边缘态数目 = 缠绕数
- **一般化**：对 2D TI，Chern 数 = 边缘手征通道数；对 Z₂ TI，Z₂ 奇偶性决定 helical edge state 的奇偶性
- **意义**：可以用体态计算来预测边界物理性质（如边缘态数量、导电通道量子化值）

---

### Q8. 一维体系发生 Peierls 不稳定性后，产生电荷密度波（CDW），请回答：（1）CDW 的数学表达式及各参数含义；（2）可公度相变与非公度相变的区别。

**答题要点：**

（1）CDW 数学表达式：
$\rho(x) = n_0 + n_c \cos\left(\frac{2\pi x}{\lambda} + \varphi\right)$
- $n_0$：平均电子密度
- $n_c$：密度起伏的幅度
- $\lambda = 2a'$：CDW 波长（超晶格周期的两倍）
- $\varphi$：初位相
- 其中 $\lambda = 2/k_F$，只由电子密度决定

（2）可公度 vs 非公度：
- **可公度相变**：$a'/a =$ 有理数（比值是有理数），相变后的晶格整体仍具有周期性，CDW 周期与原晶格周期通约
- **非公度相变**：$a'/a =$ 无理数，相变后的晶格整体无周期性，CDW 周期与原晶格周期不通约
- 区分依赖于电子密度与晶格常数的比值

---

## 论述/计算题（共1题）

### Q9. 从 Berry 相位出发，论述拓扑绝缘体的理论基础，并比较 2D 拓扑绝缘体与 3D 拓扑绝缘体的异同。

**思路与解答要点：**

#### 第一部分：Berry 相位 → Chern 数 → 拓扑分类

**Berry 相位基础：**
参数空间绝热循环一周，波函数获得的几何相位：
$\gamma = \oint_C \boldsymbol{A}(\boldsymbol{R}) \cdot d\boldsymbol{R} = \oint_C i\langle u(\boldsymbol{R})|\nabla_{\boldsymbol{R}}|u(\boldsymbol{R})\rangle \cdot d\boldsymbol{R}$

根据 Stokes 定理可转化为 Berry 曲率的面积分：
$\gamma = \int_S \boldsymbol{\Omega}(\boldsymbol{R}) \cdot d\boldsymbol{S}$，其中 $\boldsymbol{\Omega}(\boldsymbol{R}) = \nabla_{\boldsymbol{R}} \times \boldsymbol{A}(\boldsymbol{R})$

**Chern 数（TKNN 不变量）：**
在 Bloch 电子体系中，参数空间是 Brillouin 区动量 $\boldsymbol{k}$：
$C = \frac{1}{2\pi} \int_{\text{BZ}} \boldsymbol{\Omega}(\boldsymbol{k})\ d^2k$

Chern 数是整数拓扑不变量，在体能隙不关闭的绝热变形下不变。量子霍尔电导：
$\sigma_{xy} = \frac{e^2}{h} \cdot C$

#### 第二部分：时间反演对称与 Z₂ 拓扑绝缘体

对于时间反演对称的系统，总 Chern 数 $C = 0$，需要用 Z₂ 分类。

**Z₂ 不变量 ($\nu = 0, 1$)：**
- 时间反演对称性 → Kramers 简并 → TRIM 点
- 自旋守恒时：$Z_2 = \text{mod}(C_{\text{up}}, 2)$
- 反演对称时：从 TRIM 的 Parity 计算

**物理含意：**
- $\nu = 0$：平庸绝缘体（偶数条边缘态能带穿过 EF）
- $\nu = 1$：拓扑绝缘体（奇数条边缘态能带穿过 EF）
- 螺旋边缘态：自旋与动量锁定，拓扑保护，无背散射
- 不能通过连续形变变成原子绝缘体

#### 第三部分：2D vs 3D 拓扑绝缘体对比

**相同点：**
1. 都由拓扑不变量分类（Z₂）
2. 都有受时间反演对称保护的无能隙边界态
3. 都有自旋-动量锁定的螺旋结构
4. 边界态都不受背散射影响

**不同点：**

| 特征 | 2D TI | 3D TI |
|------|-------|-------|
| 边界态维度 | 1D 边缘态 | 2D 表面态 |
| Z₂ 指标 | 1个 ($\nu$) | 4个 ($\nu_0; \nu_1\nu_2\nu_3$) |
| 强/弱 | 单一 | 强TI ($\nu_0=1$) / 弱TI ($\nu_0=0$) |
| 探测 | 边缘态电导（量子输运） | 表面态能带（ARPES, STM） |
| 原型 | HgTe/CdTe QW, 石墨烯+SOC | Bi₂Se₃, Bi₂Te₃ |
| 量子Hall | 量子自旋Hall (QSHE) | 半整数量子Hall (top/bottom surface) |

**计算推导示例（以 2D Kane-Mele 模型为例）：**

Kane-Mele 哈密顿量核心部分：
$H_{SO} = i\lambda_{SO} \sum_{\langle\langle i,j\rangle\rangle} \nu_{ij} s^z c_i^\dagger c_j$

在 Dirac 点展开（$K, K'$ 附近）：
$H_K = \hbar v_F (\tau_z k_x \sigma_x + k_y \sigma_y) + \lambda_{SO} \tau_z \sigma_z s_z$

其中 $\tau_z$ 标记谷，$\sigma_z$ 标记子格，$s_z$ 标记自旋。

Berry curvature 计算（对于 $K$ 谷、自旋↑ 的价带）：
$\Omega_{K\uparrow}(k) = \frac{\lambda_{SO} v_F^2}{2[(\hbar v_F k)^2 + \lambda_{SO}^2]^{3/2}}$

Chern 数求和：$C_K = \frac{1}{2\pi}\int \Omega_{K\uparrow} d^2k + \frac{1}{2\pi}\int \Omega_{K\downarrow} d^2k = 1 + (-1) = 0$

自旋 Chern 数：$C_{\text{spin}} = \frac{1}{2\pi}\int (\Omega_{\uparrow} - \Omega_{\downarrow}) d^2k$
$= \frac{1}{2}(1-0) = 1$ （归一化后，$Z_2 = 1$）

因此体系是拓扑非平庸的（Z₂ = 1），边缘将出现 helical edge states。

---

# 附录：使用说明

## 导航
- **模块 1-2**：全局概览 — 考前 1 小时快速浏览
- **模块 3**：核心知识点 — 系统复习主力
- **模块 4**：公式速查 — 做题时快速查找
- **模块 5**：对比辨析 — 突破混淆点
- **模块 6**：一页纸 — 进考场前 5 分钟
- **模块 7**：Anki 卡片 — 导入 Anki 碎片化记忆
- **模块 8**：练习题 — 自测检验

## 优先级标记
- 🔴 **P0**：必考核心
- 🟡 **P1**：重要理解
- 无标记：P2 补充了解

## 补充说明
- 所有标注 [提取不完整，请核对原PPT] 的公式来自 PDF 提取过程中的模糊文本，建议核对原始 PPT 确认细节
- Slide 4, 15, 17-18, 20, 27-28, 33-37, 39, 78-81, 186, 188-189, 204 等为纯图像或无提取文本的页面
- 4.2 节为全章篇幅最重部分（~140页，占全章~50% 权重），建议重点投入
