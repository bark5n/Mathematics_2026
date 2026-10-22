**Result:**

$$
\det A = 1
$$

**Steps & Detailed Explanation:**

We use Gaussian elimination to reduce the matrix to an upper triangular form. The operation $R_i \leftarrow R_i + cR_j$ does not change the value of the determinant.

$$
A = 
\begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

**Step 1:** Eliminate the first entry of the second row using $R_2 \leftarrow R_2 - 2R_1$. The determinant is unchanged.

$$
A_1 = 
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

**Step 2:** Eliminate the first entry of the third row using $R_3 \leftarrow R_3 - R_1$. The determinant is unchanged.

$$
A_2 = 
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & -2 & -1 \\
\end{pmatrix}
$$

**Step 3:** Eliminate the second entry of the third row using $R_3 \leftarrow R_3 + 2R_2$. The determinant is unchanged.

$$
A_3 = 
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

The matrix $A_3$ is upper triangular. Its determinant is the product of its diagonal entries:

$$
\det A_3 = (1)(1)(1) = 1
$$

Since all row operations used preserve the determinant exactly, $\det A = 1$.