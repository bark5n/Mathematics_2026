### Essential Formulas

**Determinant of a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix

$$
M = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

its determinant is the difference between the product of the main diagonal entries and the product of the anti-diagonal entries:

$$
\det M = \det \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
= ad - bc
$$

**Invertibility Criterion (Determinant Test):**
A square matrix $M \in \mathbb{R}^{n \times n}$ is invertible if and only if its determinant is nonzero:

$$
\det M \neq 0
$$

For an invertible $2 \times 2$ matrix with $ad - bc \neq 0$, its inverse is given explicitly by:

$$
M^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 1. Determinant of a 2×2 Matrix**

Compute

$$
\det
\begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix},
\qquad
\det
\begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}.
$$

Which matrix is invertible? Justify your answer.

> **Why this exercise:** introduces the simplest determinant calculation and immediately connects it with invertibility.

---

### Solution

**Step 1: Label the matrices and compute the first determinant**

Denote the first matrix by $A$:

$$
A = \begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix}
$$

Applying the $2 \times 2$ determinant formula $\det A = ad - bc$ with $a = 3$, $b = -2$, $c = 5$, and $d = 4$:

$$
\begin{aligned}
\det A &= \det \begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix} \\
&= 3 \cdot 4 - (-2) \cdot 5 \\
&= 12 - (-10) \\
&= 12 + 10 \\
&= 22
\end{aligned}
$$

**Step 2: Compute the second determinant**

Denote the second matrix by $B$:

$$
B = \begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}
$$

Applying the $2 \times 2$ determinant formula $\det B = ad - bc$ with $a = 1$, $b = 7$, $c = 2$, and $d = 14$:

$$
\begin{aligned}
\det B &= \det \begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix} \\
&= 1 \cdot 14 - 7 \cdot 2 \\
&= 14 - 14 \\
&= 0
\end{aligned}
$$

**Step 3: Determine which matrix is invertible and justify**

By the determinant criterion, a square matrix is invertible if and only if its determinant is nonzero:

* Matrix $A$ has $\det A = 22 \neq 0$, so **$A$ is invertible**.
* Matrix $B$ has $\det B = 0$, so **$B$ is not invertible** (it is singular).

**Step 4: Verification**

* **Explicit inverse check for $A$:** Since $\det A = 22 \neq 0$, the $2 \times 2$ inverse formula produces

$$
A^{-1} = \frac{1}{22}
\begin{pmatrix}
4 & 2 \\
-5 & 3 \\
\end{pmatrix}
$$

  Multiplying $A$ by $A^{-1}$ confirms that it yields the $2 \times 2$ identity matrix:

$$
\begin{aligned}
A A^{-1} &= \frac{1}{22}
\begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix}
\begin{pmatrix}
4 & 2 \\
-5 & 3 \\
\end{pmatrix} \\
&= \frac{1}{22}
\begin{pmatrix}
3 \cdot 4 + (-2) \cdot (-5) & 3 \cdot 2 + (-2) \cdot 3 \\
5 \cdot 4 + 4 \cdot (-5) & 5 \cdot 2 + 4 \cdot 3 \\
\end{pmatrix} \\
&= \frac{1}{22}
\begin{pmatrix}
22 & 0 \\
0 & 22 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
\end{aligned}
$$

* **Linear dependence check for $B$:** In matrix $B$, the second row $(2, 14)$ is twice the first row $(1, 7)$ ($R_2 = 2R_1$), and the second column is seven times the first column ($c_2 = 7c_1$). Because its rows and columns are linearly dependent, $\det B$ must equal $0$ and no inverse matrix $B^{-1}$ can exist.

---

### Final Answer

1. **Computed determinants:**

$$
\det \begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix}
= 22,
\qquad
\det \begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}
= 0
$$

2. **Invertibility conclusion:** Only the first matrix $A$ is invertible because $\det A = 22 \neq 0$. The second matrix $B$ is not invertible because $\det B = 0$.
