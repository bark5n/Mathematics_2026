**Result:**

The system has exactly one solution:

$$
x = 1, \qquad y = 2, \qquad z = 3
$$

**Steps & Detailed Explanation:**

Write the system as an augmented matrix $[A \mid b]$:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
2 & -1 & 1 & \mid & 3 \\
1 & 2 & -1 & \mid & 2 \\
\end{pmatrix}
$$

**Step 1:** Eliminate the first entry of the second row using $R_2 \leftarrow R_2 - 2R_1$.

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & -3 & -1 & \mid & -9 \\
1 & 2 & -1 & \mid & 2 \\
\end{pmatrix}
$$

**Step 2:** Eliminate the first entry of the third row using $R_3 \leftarrow R_3 - R_1$.

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & -3 & -1 & \mid & -9 \\
0 & 1 & -2 & \mid & -4 \\
\end{pmatrix}
$$

**Step 3:** Swap $R_2$ and $R_3$ to put a $1$ in the second pivot position, making calculations easier.

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & 1 & -2 & \mid & -4 \\
0 & -3 & -1 & \mid & -9 \\
\end{pmatrix}
$$

**Step 4:** Eliminate the second entry of the third row using $R_3 \leftarrow R_3 + 3R_2$.

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & 1 & -2 & \mid & -4 \\
0 & 0 & -7 & \mid & -21 \\
\end{pmatrix}
$$

Now perform back-substitution from the bottom up:
1. Third row: $-7z = -21 \implies z = 3$.
2. Second row: $y - 2z = -4 \implies y - 2(3) = -4 \implies y - 6 = -4 \implies y = 2$.
3. First row: $x + y + z = 6 \implies x + 2 + 3 = 6 \implies x = 1$.

**Consistency check:**
Substitute $(1, 2, 3)$ into the original equations:
1. $1 + 2 + 3 = 6$ (True)
2. $2(1) - 2 + 3 = 3$ (True)
3. $1 + 2(2) - 3 = 2$ (True)