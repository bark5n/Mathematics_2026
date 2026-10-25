**Result:**

The system has infinitely many solutions. In parametric form:

$$
\begin{cases}
x = 1 - t \\
y = 1 \\
z = t
\end{cases}
$$

where $t$ is any real number. $z$ is the free variable.

**Steps & Detailed Explanation:**

Write the augmented matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
2 & 2 & 2 & \mid & 4 \\
1 & -1 & 1 & \mid & 0 \\
\end{pmatrix}
$$

**Step 1:** Eliminate the first column below the first pivot. 
$R_2 \leftarrow R_2 - 2R_1$ gives $(0, 0, 0 \mid 0)$.
$R_3 \leftarrow R_3 - R_1$ gives $(0, -2, 0 \mid -2)$.

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
0 & 0 & 0 & \mid & 0 \\
0 & -2 & 0 & \mid & -2 \\
\end{pmatrix}
$$

**Step 2:** Swap $R_2$ and $R_3$ to organize the matrix into row echelon form.

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 2 \\
0 & -2 & 0 & \mid & -2 \\
0 & 0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

The third column does not have a pivot, which means $z$ is a free variable. Let $z = t$.

Now solve for the pivot variables $y$ and $x$ using back-substitution:
1. Second row: $-2y = -2 \implies y = 1$.
2. First row: $x + y + z = 2 \implies x + 1 + t = 2 \implies x = 1 - t$.

**Check with a chosen parameter:**
Let $t = 2$. Then the solution is $(-1, 1, 2)$.
Substitute into the original system:
1. $-1 + 1 + 2 = 2$ (True)
2. $2(-1) + 2(1) + 2(2) = -2 + 2 + 4 = 4$ (True)
3. $-1 - 1 + 2 = 0$ (True)