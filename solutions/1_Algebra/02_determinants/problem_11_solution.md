### Essential Formulas

**Row Operation Invariance:**
Adding a scalar multiple of one row to another row preserves the value of the determinant:

$$
R_i \leftarrow R_i + c R_j \quad (i \neq j) \implies \det A' = \det A
$$

**Laplace (Cofactor) Expansion along a Row:**
For an $n \times n$ matrix $A$, expanding along row $i$ gives:

$$
\det A = \sum_{j=1}^n (-1)^{i+j} a_{ij} \det M_{ij}
$$

When a row contains mostly zeros, expanding along that row reduces the calculation to a single non-zero term.

**Invertibility and Singularity Condition:**
A matrix $A(t)$ depending on a parameter $t$ is **not invertible** if and only if its determinant is zero:

$$
\det A(t) = 0
$$

---

### Problem Statement

**Exercise 12. A Parameter Revealed by a Row Operation**

For

$$
A(t)=
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & t \\
0 & 1 & 1 \\
\end{pmatrix}
$$

find the values of $t$ for which the matrix is not invertible.

Before computing the determinant, perform the operation

$$
R_2\leftarrow R_2-2R_1
$$

and use the resulting structure. At the end, explain what special thing happens to the rows for the value of the parameter you found.

> **Why this exercise:** combines a parameter, row operations, and recognition of dependence in one short argument.

---

### Solution

**Step 1: Apply the specified row operation $R_2 \leftarrow R_2 - 2R_1$**

The original matrix is:

$$
A(t) = \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & t \\
0 & 1 & 1 \\
\end{pmatrix}
$$

Apply the row operation $R_2 \leftarrow R_2 - 2R_1$:

$$
R_2 = (2 - 2\cdot 1,\ 4 - 2\cdot 2,\ t - 2\cdot 3) = (0,\ 0,\ t - 6)
$$

The transformed matrix is:

$$
A'(t) = \begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & t - 6 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

Because adding a multiple of row 1 to row 2 does not change the determinant:

$$
\det A(t) = \det A'(t)
$$

**Step 2: Compute the determinant using the resulting structure**

The second row of $A'(t)$ has zeros in the first two positions. Expand $\det A'(t)$ along row 2:

$$
\det A'(t) = 0 \cdot C_{21} + 0 \cdot C_{22} + (t - 6) \cdot C_{23}
$$

The cofactor $C_{23}$ is given by:

$$
C_{23} = (-1)^{2+3} \det \begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
= -1 \cdot [(1)(1) - (2)(0)] = -1 \cdot 1 = -1
$$

Therefore:

$$
\det A(t) = (t - 6)(-1) = 6 - t
$$

**Step 3: Determine the value of $t$ for non-invertibility**

The matrix $A(t)$ is not invertible if and only if its determinant is zero:

$$
\det A(t) = 0
$$

Substitute $\det A(t) = 6 - t$:

$$
6 - t = 0 \implies t = 6
$$

Thus, $A(t)$ is not invertible precisely when $t = 6$.

**Step 4: Explain what happens to the rows at $t = 6$**

When $t = 6$:

1. In the transformed matrix $A'(6)$, the second row becomes completely zero:

   $$
   R_2 - 2R_1 = (0, 0, 6 - 6) = (0, 0, 0)
   $$

2. In the original matrix $A(6)$, row 2 is:

   $$
   R_2 = (2, 4, 6) = 2 \cdot (1, 2, 3) = 2 R_1
   $$

   This shows that row 2 is an exact scalar multiple of row 1.

*Conclusion:*
At $t = 6$, row 1 and row 2 are **linearly dependent** (parallel vectors in $\mathbb{R}^3$). The three row vectors span at most a 2D plane rather than all of $\mathbb{R}^3$, causing the rank of $A(6)$ to drop to $2 < 3$. This linear dependence collapses the 3D volume spanned by the rows to zero ($\det A(6) = 0$), making the matrix singular and non-invertible.

**Step 5: Verification using Sarrus' rule**

Compute $\det A(t)$ directly from the original matrix using Sarrus' rule:

* Downward diagonal products:

  $$
  (1)(4)(1) + (2)(t)(0) + (3)(2)(1) = 4 + 0 + 6 = 10
  $$

* Upward diagonal products:

  $$
  (3)(4)(0) + (1)(t)(1) + (2)(2)(1) = 0 + t + 4 = t + 4
  $$

* Difference:

  $$
  \det A(t) = 10 - (t + 4) = 6 - t
  $$

Setting $6 - t = 0$ confirms $t = 6$.

---

### Final Answer

Determinant formula:

$$
\det A(t) = 6 - t
$$

Value of $t$ for non-invertibility:

$$
t = 6
$$

Special row behavior:
At $t = 6$, row 2 becomes an exact multiple of row 1 ($R_2 = 2R_1$). The rows become linearly dependent and the rank drops to $2 < 3$, rendering the matrix non-invertible.
