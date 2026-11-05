### Essential Formulas

**Row Operation — Adding a Multiple of One Row to Another:**
The operation $R_i \leftarrow R_i + cR_j$ (with $i \ne j$) does not change the value of the determinant:

$$
\det(A_{\mathrm{new}}) = \det(A_{\mathrm{orig}})
$$

**Determinant of a Triangular Matrix:**
If a square matrix is upper or lower triangular, its determinant equals the product of the diagonal entries:

$$
\det A = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}
$$

**Gaussian Elimination and Determinants:**
Reducing a matrix to upper triangular form via row operations of the type $R_i \leftarrow R_i + cR_j$ preserves the determinant at every step, so $\det A$ equals the product of the diagonal entries of the resulting triangular matrix.

---

### Problem Statement

**Exercise 13. Determinant by Elimination**

Compute the determinant

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

using elimination. Record the effect of every row operation used on the value of the determinant.

---

### Solution

**Step 1: Identify the pivot and plan the elimination**

The entry $a_{11} = 1$ serves as the first pivot. To create zeros below it in column 1, subtract suitable multiples of row 1 from rows 2 and 3.

The original matrix is:

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

**Step 2: Apply $R_2 \leftarrow R_2 - 2R_1$**

Compute the new second row: $(2 - 2,\; 5 - 4,\; 7 - 6) = (0, 1, 1)$.

$$
A_1 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

Effect on the determinant: this is an operation of the form $R_i \leftarrow R_i + cR_j$, so the determinant is unchanged. $\det A_1 = \det A$.

**Step 3: Apply $R_3 \leftarrow R_3 - R_1$**

Compute the new third row: $(1 - 1,\; 0 - 2,\; 2 - 3) = (0, -2, -1)$.

$$
A_2 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & -2 & -1 \\
\end{pmatrix}
$$

Effect on the determinant: same type of operation, so the determinant is unchanged. $\det A_2 = \det A$.

**Step 4: Apply $R_3 \leftarrow R_3 + 2R_2$**

Compute the new third row: $(0 + 0,\; -2 + 2,\; -1 + 2) = (0, 0, 1)$.

$$
A_3 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

Effect on the determinant: same type of operation, so the determinant is unchanged. $\det A_3 = \det A$.

**Step 5: Read off the determinant from the upper triangular matrix**

The matrix $A_3$ is upper triangular. Its determinant is the product of its diagonal entries:

$$
\det A_3 = 1 \cdot 1 \cdot 1 = 1
$$

Since every row operation preserved the determinant:

$$
\det A = \det A_1 = \det A_2 = \det A_3 = 1
$$

**Step 6: Summary of operations and their effects**

| Operation | Type | Effect on determinant |
|---|---|---|
| $R_2 \leftarrow R_2 - 2R_1$ | $R_i \leftarrow R_i + cR_j$ | Unchanged |
| $R_3 \leftarrow R_3 - R_1$ | $R_i \leftarrow R_i + cR_j$ | Unchanged |
| $R_3 \leftarrow R_3 + 2R_2$ | $R_i \leftarrow R_i + cR_j$ | Unchanged |

All three operations are of the type that does not change the determinant, so the determinant of the original matrix equals the determinant of the final upper triangular matrix.

---

### Final Answer

$$
\det A = \det
\begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 0 & 2 \\
\end{pmatrix}
= 1
$$

Every row operation used ($R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - R_1$, $R_3 \leftarrow R_3 + 2R_2$) is of the form $R_i \leftarrow R_i + cR_j$ and leaves the determinant unchanged.
