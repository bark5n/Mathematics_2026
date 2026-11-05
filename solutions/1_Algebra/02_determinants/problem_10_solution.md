### Essential Formulas

**Linear Dependence and Determinants:**
If any row (or column) of a square matrix is a linear combination of other rows (or columns), the rows are linearly dependent and the determinant is zero:

$$
\det A = 0
$$

In particular, if one row is an exact scalar multiple of another row ($R_i = c R_j$ with $c \neq 0$):
* Subtracting $c R_j$ from $R_i$ produces an entire row of zeros.
* Any matrix with an entire row (or column) of zeros has a determinant of zero.

**The Invertible Matrix Theorem (Connection to Invertibility):**
For an $n \times n$ matrix $A$, the following statements are equivalent:
* $A$ is invertible ($A^{-1}$ exists).
* $\det A \neq 0$.
* The rows (and columns) of $A$ are linearly independent.
* $\mathrm{rank}(A) = n$ (full rank).

If $\det A = 0$, the rows are linearly dependent, $\mathrm{rank}(A) < n$, and the matrix is singular (not invertible).

---

### Problem Statement

**Exercise 10. Detecting Dependence**

Without carrying out a full determinant calculation, explain why

$$
\det
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 5 \\
\end{pmatrix}=0.
$$

Identify a specific dependence between the rows and connect it with noninvertibility of the matrix.

> **Why this exercise:** teaches how to recognize a zero determinant from the structure of a matrix.

---

### Solution

Let

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 5 \\
\end{pmatrix}
$$

**Step 1: Identify the specific dependence between the rows**

Label the rows of $A$:

$$
R_1 = (1, 2, 3), \qquad R_2 = (2, 4, 6), \qquad R_3 = (0, 1, 5)
$$

Compare row 1 and row 2:

$$
R_2 = (2, 4, 6) = 2 \cdot (1, 2, 3) = 2 R_1
$$

The second row is an exact scalar multiple of the first row ($R_2 - 2R_1 = 0$). Therefore, the rows of $A$ are **linearly dependent**.

**Step 2: Explain why this linear dependence implies $\det A = 0$**

Applying the elementary row operation $R_2 \leftarrow R_2 - 2R_1$ does not change the determinant:

$$
\det A = \det \begin{pmatrix}
1 & 2 & 3 \\
2 - 2(1) & 4 - 2(2) & 6 - 2(3) \\
0 & 1 & 5 \\
\end{pmatrix}
= \det \begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & 0 \\
0 & 1 & 5 \\
\end{pmatrix}
$$

Expanding along the second row (which consists entirely of zeros):

$$
\det A = 0 \cdot C_{21} + 0 \cdot C_{22} + 0 \cdot C_{23} = 0
$$

Thus, the determinant must equal $0$ without requiring any extensive calculation.

**Step 3: Connect linear dependence with noninvertibility**

By the Invertible Matrix Theorem:

1. **Deficiency of Rank:**
   Since $R_2 = 2R_1$, the row vectors do not span the three-dimensional space $\mathbb{R}^3$. The dimension of the row space (the rank) is at most $2$:

   $$
   \mathrm{rank}(A) \le 2 < 3
   $$

2. **Non-Trivial Null Space:**
   Because the columns are also linearly dependent, there exist non-zero vectors $x \neq 0$ such that $Ax = 0$. For an invertible matrix, $Ax = 0$ must have only the trivial solution $x = 0$.

3. **Geometric Collapse of Volume:**
   The determinant measures the signed volume of the parallelepiped spanned by the row (or column) vectors in $\mathbb{R}^3$. Because two of the vectors are parallel ($R_2 \parallel R_1$), the 3D parallelepiped is flattened into a 2D plane, having zero volume ($\det A = 0$).

Since $\det A = 0$, the inverse matrix $A^{-1} = \frac{1}{\det A}\mathrm{adj}(A)$ would require division by zero, confirming that $A$ is **not invertible** (singular).

**Step 4: Verification using Sarrus' rule**

Compute the determinant directly using Sarrus' rule to verify the conclusion:

* Downward diagonals:

  $$
  (1)(4)(5) + (2)(6)(0) + (3)(2)(1) = 20 + 0 + 6 = 26
  $$

* Upward diagonals:

  $$
  (3)(4)(0) + (1)(6)(1) + (2)(2)(5) = 0 + 6 + 20 = 26
  $$

* Difference:

  $$
  \det A = 26 - 26 = 0
  $$

The full calculation confirms $\det A = 0$.

---

### Final Answer

Specific row dependence:

$$
R_2 = 2 R_1
$$

Determinant:

$$
\det A = 0
$$

Connection to noninvertibility:
Because row 2 is a scalar multiple of row 1, the rows are linearly dependent, meaning $\mathrm{rank}(A) \le 2 < 3$. Since full rank and a non-zero determinant are required for invertibility, the matrix is **not invertible**.