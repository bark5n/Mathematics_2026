### Essential Formulas

**Sarrus' Rule for a $3 \times 3$ Matrix:**
For a $3 \times 3$ matrix

$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{pmatrix}
$$

its determinant is the sum of the products along the three downward (top-left to bottom-right) diagonals minus the sum of the products along the three upward (bottom-left to top-right) diagonals:

$$
\det A = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{31}a_{22}a_{13} - a_{32}a_{23}a_{11} - a_{33}a_{21}a_{12}
$$

**Row Replacement Property of Determinants:**
Adding a scalar multiple of one row to a different row ($R_i \leftarrow R_i + cR_j$ for $i \neq j$) leaves the value of the determinant unchanged.

**Determinant of a Triangular Matrix:**
If $U = (u_{ij})$ is an $n \times n$ upper (or lower) triangular matrix, its determinant equals the product of its main diagonal entries:

$$
\det U = u_{11} u_{22} \cdots u_{nn}
$$

---

### Problem Statement

**Exercise 2. Determinant of a 3×3 Matrix**

For

$$
A = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 4 \\
2 & 1 & 5 \\
\end{pmatrix}
$$

compute $\det A$ using Sarrus' rule. Then perform one simple check using a chosen property of the determinant.

> **Why this exercise:** teaches a basic method for $3\times3$ matrices and builds the habit of checking the result without adding a second full solution.

---

### Solution

**Step 1: Compute the products along the downward diagonals (positive terms)**

Form the three downward products by repeating the first two columns mentally to the right of $A$:

* First downward diagonal ($a_{11} a_{22} a_{33}$): $1 \cdot 3 \cdot 5 = 15$
* Second downward diagonal ($a_{12} a_{23} a_{31}$): $2 \cdot 4 \cdot 2 = 16$
* Third downward diagonal ($a_{13} a_{21} a_{32}$): $(-1) \cdot 0 \cdot 1 = 0$

Sum the three downward diagonal products:

$$
S_+ = 15 + 16 + 0 = 31
$$

**Step 2: Compute the products along the upward diagonals (negative terms)**

Form the three upward products from bottom-left to top-right:

* First upward diagonal ($a_{31} a_{22} a_{13}$): $2 \cdot 3 \cdot (-1) = -6$
* Second upward diagonal ($a_{32} a_{23} a_{11}$): $1 \cdot 4 \cdot 1 = 4$
* Third upward diagonal ($a_{33} a_{21} a_{12}$): $5 \cdot 0 \cdot 2 = 0$

Sum the three upward diagonal products:

$$
S_- = -6 + 4 + 0 = -2
$$

**Step 3: Combine the sums to obtain $\det A$**

Subtract the upward diagonal sum $S_-$ from the downward diagonal sum $S_+$:

$$
\begin{aligned}
\det A &= S_+ - S_- \\
&= 31 - (-2) \\
&= 31 + 2 \\
&= 33
\end{aligned}
$$

**Step 4: Verification using determinant properties**

Use the **row replacement property** (adding a multiple of one row to another row does not change the determinant) together with the **triangular matrix property**:

1. Apply $R_3 \leftarrow R_3 - 2R_1$ to eliminate the $(3, 1)$-entry without changing $\det A$:

$$
A_1 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 4 \\
0 & -3 & 7 \\
\end{pmatrix}
$$

2. Apply $R_3 \leftarrow R_3 + R_2$ to eliminate the $(3, 2)$-entry without changing $\det A$:

$$
U = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 4 \\
0 & 0 & 11 \\
\end{pmatrix}
$$

Because $U$ is upper triangular, its determinant is the product of its main diagonal entries:

$$
\det A = \det U = 1 \cdot 3 \cdot 11 = 33
$$

This confirms the value obtained via Sarrus' rule.

---

### Final Answer

1. **Determinant of $A$:**

$$
\det A = 33
$$

2. **Property check:** Applying row replacements $R_3 \leftarrow R_3 - 2R_1$ and $R_3 \leftarrow R_3 + R_2$ preserves the determinant and reduces $A$ to an upper triangular matrix with diagonal entries $1$, $3$, and $11$, whose product is $1 \cdot 3 \cdot 11 = 33$.
