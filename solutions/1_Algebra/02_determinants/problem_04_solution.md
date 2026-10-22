**Result:**

$$
\det
\begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}
= -42
$$

**Steps & Detailed Explanation:**

For any upper or lower triangular matrix, the determinant is simply the product of the entries on its main diagonal. 

$$
\begin{aligned}
\det
\begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}
&= 2 \cdot (-3) \cdot 7 \\
&= -42
\end{aligned}
$$

This rule works because if you compute the determinant by expanding along the first column (which is mostly zeros), you only multiply the top-left entry by the determinant of the smaller triangular matrix. This pattern continues strictly down the diagonal, with all off-diagonal contributions being eliminated by multiplication with zero.