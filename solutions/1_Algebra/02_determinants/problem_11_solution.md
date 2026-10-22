**Result:**

$$
\det
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
= 1
$$

**Steps & Detailed Explanation:**

Instead of expanding immediately, use row operations of the type $R_i \leftarrow R_i + cR_j$ to introduce zeros. This specific operation leaves the determinant completely unchanged.

Start with the original matrix:

$$
A = 
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

**Step 1:** Subtract row 1 from row 2 ($R_2 \leftarrow R_2 - R_1$) to get a zero in the first column.

$$
A_1 = 
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

**Step 2:** Subtract row 1 from row 3 ($R_3 \leftarrow R_3 - R_1$).

$$
A_2 = 
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 2 & 3 \\
\end{pmatrix}
$$

**Step 3:** Subtract $2$ times row 2 from row 3 ($R_3 \leftarrow R_3 - 2R_2$) to make the matrix upper triangular.

$$
A_3 = 
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

Since none of these operations changed the determinant, $\det A = \det A_3$. The determinant of a triangular matrix is the product of its diagonal entries:

$$
\det A = 1 \cdot 1 \cdot 1 = 1
$$