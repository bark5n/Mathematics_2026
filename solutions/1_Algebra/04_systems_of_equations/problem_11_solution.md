**Result:**

- If $t \ne 1$ and $t \ne -2$, the system has exactly one solution.
- If $t = 1$, the system has no solution.
- If $t = -2$, the system has infinitely many solutions.

**Steps & Detailed Explanation:**

Write the augmented matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
1 & t & 1 & \mid & 2 \\
1 & 1 & t & \mid & 3 \\
\end{pmatrix}
$$

**Step 1:** Eliminate entries in the first column below the pivot using $R_2 \leftarrow R_2 - R_1$ and $R_3 \leftarrow R_3 - R_1$.

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
0 & t - 1 & 0 & \mid & 1 \\
0 & 0 & t - 1 & \mid & 2 \\
\end{pmatrix}
$$

The matrix is now in row echelon form (assuming $t - 1 \ne 0$). We analyze the parameter $t$ based on the diagonal entries.

**Case 1: $t - 1 \ne 0$ (so $t \ne 1$)**
The system has pivots in every column corresponding to a variable. This indicates a unique solution. However, we must ensure there isn't a contradiction. 
If $t \ne 1$, the second row gives $y = \frac{1}{t - 1}$ and the third row gives $z = \frac{2}{t - 1}$. A unique solution exists. 

Wait, the prompt asks to find where a standard calculation step ceases to be valid. The division by $t-1$ becomes invalid if $t=1$. Let's look closely at the matrix when $t=1$.

**Case 2: $t = 1$**
Substitute $t = 1$ into the reduced matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
0 & 0 & 0 & \mid & 1 \\
0 & 0 & 0 & \mid & 2 \\
\end{pmatrix}
$$

The second row reads $0 = 1$, which is a contradiction. The system has no solution.

Wait, are there any other critical values? Look at the determinant of the coefficient matrix to be sure. 
$$
\det A = (1)(t^2 - 1) - (1)(t - 1) + (1)(1 - t) = t^2 - 1 - t + 1 + 1 - t = t^2 - 2t + 1 = (t - 1)^2
$$
The only critical value is $t = 1$. The case $t = -2$ from my initial mental check does not apply to this specific matrix layout (it applies to a similar famous problem, but not this exact set of equations).

**Corrected Analysis:**
- If $t \ne 1$, the determinant is non-zero, so there is exactly one unique solution.
- If $t = 1$, the elimination yields $0 = 1$, proving there is no solution. There is no parameter value that yields infinitely many solutions for this specific right-hand side.