### Essential Formulas

**Identity Matrix and Zero Matrix:**
The $n \times n$ identity matrix $I$ acts as the multiplicative neutral element for matrices of compatible size. For any $n \times n$ matrix $A$:

$$
AI = IA = A
$$

The $n \times n$ zero matrix $0$ acts as the additive neutral element. For any $n \times n$ matrix $A$:

$$
A + 0 = A
$$

**Matrix Powers:**
For a square matrix $A$, successive integer powers are defined by repeated multiplication:

$$
A^2 = AA, \qquad A^3 = A^2 A = AAA
$$

---

### Problem Statement

**Exercise 7. Identity Matrix, Zero Matrix, and Powers**

For

$$
A=
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

compute

$$
AI,\qquad IA,\qquad A+0,\qquad A^2,\qquad A^3.
$$

Explain the roles of the matrices $I$ and $0$, and describe the pattern you observe in successive powers of $A$.

> **Why this exercise:** organizes the roles of neutral elements and reveals regularity in successive powers of a matrix.

---

### Solution

**Step 1: Compute $AI$, $IA$, and $A + 0$**

For a $2 \times 2$ matrix $A$, the compatible identity matrix $I$ and zero matrix $0$ are:

$$
I =
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix},
\qquad
0 =
\begin{pmatrix}
0 & 0 \\
0 & 0 \\
\end{pmatrix}
$$

1. **Compute $AI$:**

$$
\begin{aligned}
AI &=
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2(1) + 1(0) & 2(0) + 1(1) \\
0(1) + 2(0) & 0(0) + 2(1) \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix} \\
&= A
\end{aligned}
$$

2. **Compute $IA$:**

$$
\begin{aligned}
IA &=
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
1(2) + 0(0) & 1(1) + 0(2) \\
0(2) + 1(0) & 0(1) + 1(2) \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix} \\
&= A
\end{aligned}
$$

3. **Compute $A + 0$:**

$$
\begin{aligned}
A + 0 &=
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
+
\begin{pmatrix}
0 & 0 \\
0 & 0 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2+0 & 1+0 \\
0+0 & 2+0 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix} \\
&= A
\end{aligned}
$$

**Step 2: Compute successive powers $A^2$ and $A^3$**

1. **Compute $A^2$:**

$$
\begin{aligned}
A^2 &= AA \\
&=
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2(2) + 1(0) & 2(1) + 1(2) \\
0(2) + 2(0) & 0(1) + 2(2) \\
\end{pmatrix} \\
&=
\begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix}
\end{aligned}
$$

2. **Compute $A^3$:**

$$
\begin{aligned}
A^3 &= A^2 A \\
&=
\begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
4(2) + 4(0) & 4(1) + 4(2) \\
0(2) + 4(0) & 0(1) + 4(2) \\
\end{pmatrix} \\
&=
\begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Explain roles of neutral elements and describe the power pattern**

* **Roles of $I$ and $0$:** The matrix $I$ acts as the **multiplicative identity** (neutral element for matrix multiplication); multiplying any matrix by $I$ (from either side, when dimensions match) leaves it completely unchanged ($AI = IA = A$). The matrix $0$ acts as the **additive identity** (neutral element for matrix addition); adding $0$ to any matrix leaves it unchanged ($A + 0 = A$).
* **Pattern in successive powers of $A$:**
  Observing the sequence:

$$
A^1 = \begin{pmatrix} 2^1 & 1\cdot 2^0 \\ 0 & 2^1 \end{pmatrix}, \qquad
A^2 = \begin{pmatrix} 2^2 & 2\cdot 2^1 \\ 0 & 2^2 \end{pmatrix}, \qquad
A^3 = \begin{pmatrix} 2^3 & 3\cdot 2^2 \\ 0 & 2^3 \end{pmatrix}
$$

  The main diagonal elements are simply $2^n$. The upper-right entry follows the pattern $n \cdot 2^{n-1}$. The $(2,1)$-entry remains permanently $0$. This suggests a general formula for the $n$-th power:

$$
A^n =
\begin{pmatrix}
2^n & n 2^{n-1} \\
0 & 2^n \\
\end{pmatrix}
$$

**Step 4: Verification**

* To verify the proposed pattern for $n=4$:
  Formula prediction: $A^4 = \begin{pmatrix} 2^4 & 4\cdot 2^3 \\ 0 & 2^4 \end{pmatrix} = \begin{pmatrix} 16 & 32 \\ 0 & 16 \end{pmatrix}$.
  Direct multiplication:

$$
A^4 = A^3 A =
\begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
=
\begin{pmatrix}
16 & 8 + 24 \\
0 & 16 \\
\end{pmatrix}
=
\begin{pmatrix}
16 & 32 \\
0 & 16 \\
\end{pmatrix}
$$

  The direct calculation matches the pattern prediction exactly.

---

### Final Answer

1. **Results of neutral operations:** $AI = A$, $IA = A$, and $A + 0 = A$.
2. **Matrix powers:**

$$
A^2 =
\begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix},
\qquad
A^3 =
\begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}
$$

3. **Roles:** $I$ is the neutral element for multiplication (identity), and $0$ is the neutral element for addition.
4. **Pattern:** In $A^n$, the diagonal entries are $2^n$, the lower-left entry is always $0$, and the upper-right entry grows as $n 2^{n-1}$.
