**Result:**

- **Exactly one solution:** Never occurs.
- **Infinitely many solutions:** Occurs when $a = 2$.
- **No solution:** Occurs when $a \ne 2$.

**Steps & Detailed Explanation:**

Write the system as an augmented matrix:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
a & a & \mid & 4 \\
\end{pmatrix}
$$

Perform Gaussian elimination to clear the first entry of the second row using $R_2 \leftarrow R_2 - aR_1$:

$$
\begin{aligned}
R_2 &= (a, a \mid 4) - a(1, 1 \mid 2) \\
&= (a, a \mid 4) - (a, a \mid 2a) \\
&= (0, 0 \mid 4 - 2a)
\end{aligned}
$$

The updated matrix is:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 4 - 2a \\
\end{pmatrix}
$$

Analyze the second row: $0x + 0y = 4 - 2a$.
1. If $4 - 2a = 0$ (which means $a = 2$), the equation becomes $0 = 0$. This is true for any $x$ and $y$ that satisfy the first equation. Thus, there are infinitely many solutions.
2. If $4 - 2a \ne 0$ (which means $a \ne 2$), the equation becomes $0 = \text{non-zero number}$, which is a contradiction. Thus, there is no solution.

The case of "exactly one solution" requires the coefficient matrix to be invertible. However, the determinant of the coefficient matrix is $(1)(a) - (1)(a) = 0$ for every possible value of $a$. Because the determinant is always zero, the rows are always linearly dependent, making a unique intersection point impossible.