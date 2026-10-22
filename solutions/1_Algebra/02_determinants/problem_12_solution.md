**Result:**

The matrix is not invertible when $t = 6$. At this value, the second row becomes a row of zeros.

**Steps & Detailed Explanation:**

The given matrix is:

$$
A(t) = 
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & t \\
0 & 1 & 1 \\
\end{pmatrix}
$$

Perform the suggested row operation, replacing the second row with itself minus twice the first row ($R_2 \leftarrow R_2 - 2R_1$). 

The new second row is $(2, 4, t) - 2(1, 2, 3) = (0, 0, t - 6)$. The updated matrix is:

$$
A_1(t) = 
\begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & t - 6 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

This operation does not change the determinant. A matrix is not invertible if its determinant is zero. Expanding the determinant of $A_1(t)$ along the second row gives:

$$
\det A_1(t) = -(t - 6) \det
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix}
= -(t - 6)(1)
$$

Set the determinant to zero to find when the matrix is not invertible:

$$
-(t - 6) = 0 \implies t = 6
$$

If $t = 6$, the operation $R_2 \leftarrow R_2 - 2R_1$ produces a row of entirely zeros. A row of zeros means the original rows were linearly dependent, confirming the matrix cannot be inverted.