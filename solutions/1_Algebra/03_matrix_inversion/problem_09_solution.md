**Result:**

$$X = \begin{pmatrix} -1 & -7 \\ 2 & 4 \\ \end{pmatrix}$$

**Steps & Detailed Explanation:**

We need to solve the matrix equation $AX = B$. To isolate $X$, we must multiply both sides of the equation by $A^{-1}$. Since matrix multiplication is not commutative, the order matters. Because $A$ is on the left of $X$, we must multiply from the left:

$$\begin{aligned} A^{-1}(AX) &= A^{-1}B \\ (A^{-1}A)X &= A^{-1}B \\ IX &= A^{-1}B \\ X &= A^{-1}B \end{aligned}$$

First, find $A^{-1}$. The matrix is:

$$A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ \end{pmatrix}$$

The determinant is $\det A = (1)(1) - (2)(0) = 1$. The inverse is:

$$A^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -2 \\ 0 & 1 \\ \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \\ \end{pmatrix}$$

Now multiply $A^{-1}$ and $B$:

$$\begin{aligned} X &= \begin{pmatrix} 1 & -2 \\ 0 & 1 \\ \end{pmatrix} \begin{pmatrix} 3 & 1 \\ 2 & 4 \\ \end{pmatrix} \\ &= \begin{pmatrix} (1)(3) + (-2)(2) & (1)(1) + (-2)(4) \\ (0)(3) + (1)(2) & (0)(1) + (1)(4) \\ \end{pmatrix} \\ &= \begin{pmatrix} 3 - 4 & 1 - 8 \\ 0 + 2 & 0 + 4 \\ \end{pmatrix} \\ &= \begin{pmatrix} -1 & -7 \\ 2 & 4 \\ \end{pmatrix} \end{aligned}$$

Check the result by computing $AX$:

$$\begin{aligned} AX &= \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ \end{pmatrix} \begin{pmatrix} -1 & -7 \\ 2 & 4 \\ \end{pmatrix} \\ &= \begin{pmatrix} -1 + 4 & -7 + 8 \\ 0 + 2 & 0 + 4 \\ \end{pmatrix} \\ &= \begin{pmatrix} 3 & 1 \\ 2 & 4 \\ \end{pmatrix} = B \end{aligned}$$

The result matches matrix $B$, confirming the solution is correct.