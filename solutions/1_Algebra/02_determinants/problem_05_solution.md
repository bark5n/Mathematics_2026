**Result:**

$$
\det A = 21
$$

**Steps & Detailed Explanation:**

We simplify the matrix using row operations that add a multiple of one row to another. This specific type of row operation does not change the determinant.

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 0 \\
-1 & 4 & 2 \\
\end{pmatrix}
$$

**Step 1:** Replace $R_2$ with $R_2 - 2R_1$. The determinant is unchanged.

$$
A_1 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
-1 & 4 & 2 \\
\end{pmatrix}
$$

**Step 2:** Replace $R_3$ with $R_3 + R_1$. The determinant is unchanged.

$$
A_2 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 6 & 5 \\
\end{pmatrix}
$$

**Step 3:** Replace $R_3$ with $R_3 + 2R_2$ to make the matrix upper triangular. The determinant is unchanged.

$$
A_3 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 0 & -7 \\
\end{pmatrix}
$$

Since the determinant was preserved at each step, $\det A = \det A_3$. Because $A_3$ is a triangular matrix, its determinant is the product of its main diagonal:

$$
\det A = 1 \cdot (-3) \cdot (-7) = 21
$$