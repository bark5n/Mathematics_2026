**Result & Choices:**

1. **System 1 (Triangular matrix):** Use Back-Substitution. 
   *Solution:* $y = 2, x = 2.5$.
2. **System 2 (Multiple $b_i$, known $A^{-1}$):** Multiply $x = A^{-1}b_i$.
3. **System 3 ($3 \times 3$, single solution, unknown $A^{-1}$):** Use Gaussian Elimination.

**Steps & Detailed Explanation:**

**Case 1:**
$$
\begin{cases}
2x - y = 3 \\
4y = 8
\end{cases}
$$
The coefficient matrix is already upper triangular. Applying full Gaussian elimination or finding an inverse would be redundant. We can simply use back-substitution immediately.
From the second equation, $4y = 8 \implies y = 2$.
Substitute into the first: $2x - 2 = 3 \implies 2x = 5 \implies x = 2.5$.

**Case 2:**
We have $Ax = b_i$ for three different right-hand sides, and $A^{-1}$ is already given. The most efficient choice is to use $x = A^{-1}b_i$. Since the inverse is known, computing a single matrix-vector multiplication is extremely fast. If we used Gaussian elimination, we would have to repeat the row operations for the left side three separate times (or form a large augmented matrix), which is unnecessary repeated labor.

**Case 3:**
We have a single $3 \times 3$ system and do not know the inverse. The best method is Gaussian elimination. Finding an inverse matrix from scratch just to solve a single system requires much more arithmetic (finding a matrix of cofactors or running full Gauss-Jordan to reach the identity matrix) than merely reducing the system to row echelon form and back-substituting.