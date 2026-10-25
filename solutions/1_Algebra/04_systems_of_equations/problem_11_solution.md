**Result:**

- If $t \ne 1$, the system has exactly one solution.
- If $t = 1$, the system has no solution.

**Steps & Detailed Explanation:**

Write the augmented matrix for the system:

$$
\left( \begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
1 & t & 1 & 2 \\
1 & 1 & t & 3
\end{array} \right)
$$

**Step 1:** Eliminate entries in the first column below the pivot using $R_2 \leftarrow R_2 - R_1$ and $R_3 \leftarrow R_3 - R_1$.

$$
\left( \begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & t - 1 & 0 & 1 \\
0 & 0 & t - 1 & 2
\end{array} \right)
$$

The matrix is now in row echelon form. We analyze the parameter $t$ based on the diagonal entries.

**Case 1: $t = 1$**
If we substitute $t = 1$ into the reduced matrix, we get:

$$
\left( \begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 2
\end{array} \right)
$$

The second row reads $0x + 0y + 0z = 1 \implies 0 = 1$, which is a mathematical contradiction. Therefore, the system has no solution.

**Case 2: $t \ne 1$**
If $t - 1 \ne 0$, the system has pivots in every column corresponding to a variable (the determinant of the coefficient matrix is non-zero). This guarantees exactly one unique solution.