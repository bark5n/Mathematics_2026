**Result:**

The unique solution is $x = 6$, $y = 4$.

**Steps & Detailed Explanation:**

The two conditions create a system of two linear equations:

$$
\begin{cases}
x + y = 10 \\
2x + 5y = 32
\end{cases}
$$

Write the augmented matrix:

$$
\begin{pmatrix}
1 & 1 & \mid & 10 \\
2 & 5 & \mid & 32 \\
\end{pmatrix}
$$

Eliminate the $x$-coefficient from the second row using $R_2 \leftarrow R_2 - 2R_1$:

$$
\begin{aligned}
R_2 &= (2, 5 \mid 32) - 2(1, 1 \mid 10) \\
&= (2, 5 \mid 32) - (2, 2 \mid 20) \\
&= (0, 3 \mid 12)
\end{aligned}
$$

The updated matrix is:

$$
\begin{pmatrix}
1 & 1 & \mid & 10 \\
0 & 3 & \mid & 12 \\
\end{pmatrix}
$$

Solve using back-substitution:
From the second row: $3y = 12 \implies y = 4$.
Substitute into the first row: $x + y = 10 \implies x + 4 = 10 \implies x = 6$.

Geometrically, each equation represents a straight line on a two-dimensional Cartesian plane. The first line is $y = -x + 10$ and the second is $y = -\frac{2}{5}x + \frac{32}{5}$. Because their slopes ($-1$ and $-0.4$) are different, the lines are not parallel. Two non-parallel lines in a plane must intersect at exactly one specific point. That intersection point is $(6, 4)$, which corresponds to the unique solution of the system.