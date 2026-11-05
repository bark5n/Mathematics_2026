### Essential Formulas

**Row Operation — Adding a Multiple of One Row to Another:**
The operation $R_i \leftarrow R_i + cR_j$ (with $i \ne j$) does not change the value of the determinant:

$$
\det(A_{\mathrm{new}}) = \det(A_{\mathrm{orig}})
$$

**Invertibility Criterion:**
A square matrix $A$ is invertible if and only if $\det A \ne 0$. Equivalently, $A$ is not invertible if and only if $\det A = 0$.

**Cofactor Expansion Along a Row:**
For a $3 \times 3$ matrix, expanding the determinant along row $i$:

$$
\det A = \sum_{j=1}^{3} (-1)^{i+j}\, a_{ij}\, M_{ij}
$$

where $M_{ij}$ is the $(i,j)$-minor (the determinant of the $2 \times 2$ submatrix obtained by deleting row $i$ and column $j$).

---

### Problem Statement

**Exercise 12. A Parameter Revealed by a Row Operation**

For

$$
A(t) =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & t \\
0 & 1 & 1 \\
\end{pmatrix}
$$

find the values of $t$ for which the matrix is not invertible.

Before computing the determinant, perform the operation

$$
R_2 \leftarrow R_2 - 2R_1
$$

and use the resulting structure. At the end, explain what special thing happens to the rows for the value of the parameter you found.

---

### Solution

**Step 1: Perform the suggested row operation**

Apply $R_2 \leftarrow R_2 - 2R_1$. Compute each entry of the new second row:

$$
\begin{aligned}
&2 - 2(1) = 0, \\
&4 - 2(2) = 0, \\
&t - 2(3) = t - 6.
\end{aligned}
$$

The updated matrix is:

$$
A_1(t) =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & t - 6 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

Since the operation $R_2 \leftarrow R_2 - 2R_1$ is of the form $R_i \leftarrow R_i + cR_j$, the determinant is unchanged: $\det A_1(t) = \det A(t)$.

**Step 2: Compute the determinant by cofactor expansion along row 2**

Row 2 of $A_1(t)$ has two zeros, making expansion along this row efficient. The cofactor expansion along row 2 gives:

$$
\begin{aligned}
\det A_1(t) &= (-1)^{2+1}(0) \cdot M_{21} + (-1)^{2+2}(0) \cdot M_{22} + (-1)^{2+3}(t - 6) \cdot M_{23}
\end{aligned}
$$

The first two terms vanish because their entries are zero. Only the third term survives:

$$
\det A_1(t) = (-1)^{2+3}(t - 6) \cdot M_{23}
$$

where the minor $M_{23}$ is obtained by deleting row 2 and column 3:

$$
M_{23} = \det
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
= (1)(1) - (2)(0) = 1
$$

Therefore:

$$
\det A_1(t) = (-1)(t - 6)(1) = -(t - 6) = 6 - t
$$

**Step 3: Determine the values of $t$ that make the matrix non-invertible**

The matrix is not invertible when $\det A(t) = 0$:

$$
6 - t = 0 \implies t = 6
$$

**Step 4: Explain the row dependence at $t = 6$**

When $t = 6$, the original matrix becomes:

$$
A(6) =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

The second row $(2, 4, 6) = 2 \cdot (1, 2, 3)$ is exactly twice the first row. This means $R_2 = 2R_1$, so the rows are linearly dependent.

The row operation $R_2 \leftarrow R_2 - 2R_1$ produces the zero row $(0, 0, 0)$, which confirms the dependence. A matrix with a row of zeros has determinant zero and is therefore not invertible.

---

### Final Answer

The matrix $A(t)$ is not invertible when $t = 6$.

At $t = 6$, the second row is exactly twice the first row ($R_2 = 2R_1$), so the rows are linearly dependent and the determinant vanishes:

$$
\det A(t) = 6 - t
$$
