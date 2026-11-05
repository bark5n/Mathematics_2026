### Essential Formulas

**Row Operation — Adding a Multiple of One Row to Another:**
The operation $R_i \leftarrow R_i + cR_j$ (with $i \ne j$) does not change the value of the determinant:

$$
\det(A_{\mathrm{new}}) = \det(A_{\mathrm{orig}})
$$

**Determinant of a Triangular Matrix:**
If a square matrix is upper or lower triangular (all entries below or above the main diagonal are zero), its determinant equals the product of the diagonal entries:

$$
\det A = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}
$$

---

### Problem Statement

**Exercise 11. Shortening the Calculation with Row Operations**

Compute

$$
\det
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

by first performing row operations that create as many zeros as possible. State which operations do not change the determinant.

---

### Solution

**Step 1: Identify the strategy**

The matrix has all ones in its first column. Subtracting the first row from both remaining rows will create zeros in the first column of rows 2 and 3. The operation $R_i \leftarrow R_i - R_1$ is of the form $R_i \leftarrow R_i + cR_j$ (with $c = -1$), so it does not change the determinant.

The original matrix is:

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

**Step 2: Apply $R_2 \leftarrow R_2 - R_1$**

Compute the new second row: $(1 - 1,\; 3 - 2,\; 4 - 3) = (0, 1, 1)$.

$$
A_1 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

This operation does not change the determinant, so $\det A_1 = \det A$.

**Step 3: Apply $R_3 \leftarrow R_3 - R_1$**

Compute the new third row: $(1 - 1,\; 4 - 2,\; 6 - 3) = (0, 2, 3)$.

$$
A_2 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 2 & 3 \\
\end{pmatrix}
$$

This operation does not change the determinant, so $\det A_2 = \det A$.

**Step 4: Apply $R_3 \leftarrow R_3 - 2R_2$**

Compute the new third row: $(0 - 0,\; 2 - 2,\; 3 - 2) = (0, 0, 1)$.

$$
A_3 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

This operation does not change the determinant, so $\det A_3 = \det A$.

**Step 5: Read off the determinant from the triangular matrix**

The matrix $A_3$ is upper triangular. Its determinant is the product of its diagonal entries:

$$
\det A_3 = 1 \cdot 1 \cdot 1 = 1
$$

Since every row operation used was of the form $R_i \leftarrow R_i + cR_j$, which preserves the determinant, the value has remained unchanged throughout.

**Step 6: Verification using Sarrus' rule**

As a check, apply Sarrus' rule directly to the original matrix:

$$
\begin{aligned}
\det A &= (1)(3)(6) + (2)(4)(1) + (3)(1)(4) - (3)(3)(1) - (2)(1)(6) - (1)(4)(4) \\
&= 18 + 8 + 12 - 9 - 12 - 16 \\
&= 1
\end{aligned}
$$

The result agrees with the elimination method.

---

### Final Answer

$$
\det
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
= 1
$$

All three row operations used ($R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - R_1$, $R_3 \leftarrow R_3 - 2R_2$) are of the form $R_i \leftarrow R_i + cR_j$ and do not change the determinant.
