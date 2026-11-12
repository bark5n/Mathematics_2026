### Essential Formulas

**Inverse of a Product of Invertible Matrices:**
If $A, B \in \mathbb{R}^{n \times n}$ are invertible square matrices of the same size, then their product $AB$ is invertible and its inverse reverses the order of the factors:

$$
(AB)^{-1} = B^{-1} A^{-1}
$$

**Explicit Inverse Formula for a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix

$$
M = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

with $\det M = ad - bc \neq 0$, its inverse is:

$$
M^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

**Composition of Linear Transformations:**
For matrices $H, S \in \mathbb{R}^{n \times n}$ and a vector $x \in \mathbb{R}^n$, the matrix-vector product $(HS)x = H(Sx)$ applies $S$ first and $H$ second (from right to left).

---

### Problem Statement

**Exercise 13. Undoing a Composite Transformation**

The matrices

$$
S = \begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix},
\qquad
H = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

describe nonuniform scaling and shear. For $T=HS$, find $T^{-1}$ in two ways:

1. first compute $T$, then its inverse,
2. use $(HS)^{-1}=S^{-1}H^{-1}$.

Compare the results. Additionally compute $H^{-1}S^{-1}$ and verify that the incorrect order gives a different matrix. Explain the rule: “when undoing a composition of operations, we undo them from the end.”

> **Why this exercise:** reinforces the inverse of a product in a less direct configuration.

---

### Solution

**Step 1: Way 1 — First compute $T = HS$, then find $T^{-1}$**

Multiply $H$ on the right by $S$:

$$
\begin{aligned}
T = HS &= \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 2 + 1 \cdot 0 & 1 \cdot 0 + 1 \cdot 1 \\
0 \cdot 2 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

Compute $\det T = 2 \cdot 1 - 1 \cdot 0 = 2 \neq 0$, and apply the $2 \times 2$ inverse formula to $T$:

$$
\begin{aligned}
T^{-1} &= \frac{1}{2}
\begin{pmatrix}
1 & -1 \\
0 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Way 2 — Compute $S^{-1}$, $H^{-1}$, and $S^{-1}H^{-1}$**

* Find $S^{-1}$ using $\det S = 2 \cdot 1 - 0 \cdot 0 = 2$:

$$
S^{-1} = \frac{1}{2}
\begin{pmatrix}
1 & 0 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix}
$$

* Find $H^{-1}$ using $\det H = 1 \cdot 1 - 1 \cdot 0 = 1$:

$$
H^{-1} = \frac{1}{1}
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
$$

* Multiply $S^{-1}$ on the right by $H^{-1}$:

$$
\begin{aligned}
S^{-1} H^{-1} &= \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} \cdot 1 + 0 \cdot 0 & \frac{1}{2} \cdot (-1) + 0 \cdot 1 \\
0 \cdot 1 + 1 \cdot 0 & 0 \cdot (-1) + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compare Way 1 and Way 2, then compute $H^{-1}S^{-1}$**

* **Comparison of Way 1 and Way 2:** Both methods produce the exact same inverse matrix:

$$
T^{-1} = (HS)^{-1} = S^{-1}H^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

* **Computation in the incorrect order ($H^{-1}S^{-1}$):**

$$
\begin{aligned}
H^{-1} S^{-1} &= \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot \frac{1}{2} + (-1) \cdot 0 & 1 \cdot 0 + (-1) \cdot 1 \\
0 \cdot \frac{1}{2} + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

  Comparing the $(1, 2)$-entries shows $-\frac{1}{2} \neq -1$, so $H^{-1}S^{-1} \neq T^{-1}$. Furthermore, multiplying $T$ by $H^{-1}S^{-1}$ fails to produce $I_2$:

$$
T(H^{-1}S^{-1}) = \begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
\neq I_2
$$

**Step 4: Explain the rule “when undoing a composition of operations, we undo them from the end”**

When $T = HS$ acts on a vector $x = (x_1, x_2)^T \in \mathbb{R}^2$, the transformations occur sequentially from right to left:

1. **First operation ($S$):** $S$ stretches the horizontal coordinate by $2$, mapping $(x_1, x_2)^T \mapsto (2x_1, x_2)^T$.
2. **Second (last) operation ($H$):** $H$ applies a horizontal shear that adds the second coordinate to the first, mapping $(2x_1, x_2)^T \mapsto (2x_1 + x_2, x_2)^T$.

To recover the original vector $x$ from the final output $z = H(Sx)$, we must reverse the steps in **last-in, first-out** order:

1. **Undo the last operation ($H$) first:** Apply $H^{-1}$ to subtract the second coordinate from the first, which cancels $H$ and returns $Sx = (2x_1, x_2)^T$.
2. **Undo the first operation ($S$) second:** Apply $S^{-1}$ to halve the first coordinate, which cancels $S$ and restores $x = (x_1, x_2)^T$.

Written in matrix notation, applying $H^{-1}$ first and $S^{-1}$ second to $z$ is $S^{-1}(H^{-1}z) = (S^{-1}H^{-1})z$, which algebraically matches $(HS)(S^{-1}H^{-1}) = H(SS^{-1})H^{-1} = H I_2 H^{-1} = I_2$.

**Step 5: Verification**

* **Direct matrix multiplication check ($T T^{-1}$ and $T^{-1} T$):**

$$
T T^{-1} = \begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 & -1 + 1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I_2
$$

* **Concrete vector check on $x = (3, 4)^T$:**
  * Forward transformation: $Sx = (6, 4)^T$, and $Tx = H(Sx) = (6 + 4, 4)^T = (10, 4)^T$.
  * Correct inverse $T^{-1} = S^{-1}H^{-1}$ applied to $(10, 4)^T$:

$$
T^{-1}\begin{pmatrix}
10 \\
4 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
10 \\
4 \\
\end{pmatrix}
= \begin{pmatrix}
5 - 2 \\
4 \\
\end{pmatrix}
= \begin{pmatrix}
3 \\
4 \\
\end{pmatrix}
= x
$$

  * Incorrect order $H^{-1}S^{-1}$ applied to $(10, 4)^T$ gives $(5 - 4, 4)^T = (1, 4)^T \neq (3, 4)^T$, confirming that undoing in forward order fails.

---

### Final Answer

1. **Both valid methods yield the same inverse $T^{-1}$:**

$$
T = HS = \begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix},
\qquad
T^{-1} = (HS)^{-1} = S^{-1}H^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & 1 \\
\end{pmatrix}
$$

2. **Incorrect order $H^{-1}S^{-1}$:**

$$
H^{-1}S^{-1} = \begin{pmatrix}
\frac{1}{2} & -1 \\
0 & 1 \\
\end{pmatrix}
\neq T^{-1}
$$

3. **Explanation of the rule:** Because $Tx = H(Sx)$ applies $S$ first and $H$ second, inverting the composite action requires peeling off the last operation ($H$) first via $H^{-1}$ and then undoing the initial operation ($S$) via $S^{-1}$, which corresponds to $(S^{-1}H^{-1})z$.
