**Result:**

The system has exactly one solution for every $b$ when $k \ne 2$. 

For $k = 2$:
- Infinite solutions occur if $b = (1, 2)^T$.
- No solution occurs if $b = (1, 3)^T$.

**Steps & Detailed Explanation:**

The system $Ax = b$ has exactly one solution for every right-hand side $b$ if and only if the matrix $A$ is invertible. This requires $\det A \ne 0$.

Compute the determinant:

$$
\begin{aligned}
\det A &= \det
\begin{pmatrix}
1 & 2 \\
k & 4 \\
\end{pmatrix} \\
&= (1)(4) - (2)(k) \\
&= 4 - 2k
\end{aligned}
$$

Set this to be non-zero:

$$
4 - 2k \ne 0 \implies k \ne 2
$$

When $k = 2$, the determinant is zero, meaning the matrix is not invertible and the rows are dependent. The system becomes:

$$
\begin{cases}
x + 2y = b_1, \\
2x + 4y = b_2.
\end{cases}
$$

The left side of the second equation is exactly twice the left side of the first equation.

To have infinitely many solutions, the right side must follow the exact same multiple. Let $b_1 = 1$, then $b_2$ must be $2$. Thus, $b = (1, 2)^T$ yields infinitely many solutions because the equations are identical: $x + 2y = 1$.

To have no solution, choose a right side that contradicts the multiple. Let $b_1 = 1$ and $b_2 = 3$. The system then states $x + 2y = 1$ and $2(x + 2y) = 3$, which simplifies to $2 = 3$, an impossibility. Thus, $b = (1, 3)^T$ yields no solution.