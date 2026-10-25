**Result:**

The parametric solution is:

$$
\begin{cases}
x = -t \\
y = t \\
z = t
\end{cases}
$$

The trivial solution $(0,0,0)$ always satisfies a homogeneous system because multiplying any coefficients by zero will always sum to zero, perfectly matching the zero right-hand side.

**Steps & Detailed Explanation:**

Write the augmented matrix for the homogeneous system:

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
2 & 4 & -2 & \mid & 0 \\
1 & -1 & 2 & \mid & 0 \\
\end{pmatrix}
$$

**Step 1:** $R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - R_1$

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
0 & -3 & 3 & \mid & 0 \\
\end{pmatrix}
$$

**Step 2:** Swap $R_2$ and $R_3$ to organize into echelon form, and divide the new $R_2$ by $-3$.

$$
\begin{pmatrix}
1 & 2 & -1 & \mid & 0 \\
0 & 1 & -1 & \mid & 0 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

Column 3 has no pivot, so $z$ is a free variable. Let $z = t$.
From the second row: $y - z = 0 \implies y = t$.
From the first row: $x + 2y - z = 0 \implies x + 2(t) - t = 0 \implies x + t = 0 \implies x = -t$.

A homogeneous system (where $b = 0$) guarantees that the origin $(0,0,0)$ is a solution because $A(0) = 0$ is a universal mathematical truth. The system's planes all pass through the origin. Therefore, a homogeneous system can never be inconsistent (it can never have "no solution"). It either has exactly one solution (the origin) or infinitely many (a line or plane passing through the origin).