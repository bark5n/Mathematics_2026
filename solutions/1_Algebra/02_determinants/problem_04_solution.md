### Essential Formulas

**Determinant of a Triangular Matrix:**
For any upper triangular, lower triangular, or diagonal matrix $T = (t_{ij}) \in \mathbb{R}^{n \times n}$, all entries below or above the main diagonal are zero. The determinant is simply the product of the diagonal entries:

$$
\det T = \prod_{i=1}^{n} t_{ii} = t_{11} t_{22} \cdots t_{nn}
$$

---

### Problem Statement

**Exercise 4. Triangular Matrix**

Without expanding the determinant, compute

$$
\det
\begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}.
$$

State the rule for an arbitrary triangular matrix and explain it using this example.

> **Why this exercise:** reinforces an important property of triangular matrices.

---

### Solution

**Step 1: Identify the matrix type**

Let

$$
A =
\begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}
$$

All entries below the main diagonal are zero ($a_{21} = 0$, $a_{31} = 0$, $a_{32} = 0$). Therefore, $A$ is an upper triangular matrix.

**Step 2: State the general rule**

For any $n \times n$ triangular matrix (upper or lower), the determinant equals the product of its diagonal elements:

$$
\det A = a_{11} \cdot a_{22} \cdots a_{nn}
$$

**Step 3: Compute the determinant**

Applying the rule directly to matrix $A$:

$$
\begin{aligned}
\det A &= 2 \cdot (-3) \cdot 7 \\
&= -6 \cdot 7 \\
&= -42
\end{aligned}
$$

**Step 4: Explanation using Laplace expansion**

This rule holds because expanding along the first column (where all entries below $a_{11}$ are zero) gives:

$$
\det A = 2 \cdot \det \begin{pmatrix}
-3 & 5 \\
0 & 7 \\
\end{pmatrix}
- 0 + 0
$$

The remaining $2 \times 2$ determinant is also upper triangular. Expanding again along its first column yields $(-3) \cdot 7$. Consequently:

$$
\det A = 2 \cdot (-3) \cdot 7 = -42
$$

Every off-diagonal term in the complete determinant expansion involves at least one factor of zero, leaving only the product along the main diagonal.

---

### Final Answer

1. Rule:
For any triangular matrix $T \in \mathbb{R}^{n \times n}$, the determinant equals the product of its main diagonal entries: $\det T = \prod_{i=1}^{n} t_{ii}$.

2. Computed determinant:

$$
\det
\begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}
= -42
$$
