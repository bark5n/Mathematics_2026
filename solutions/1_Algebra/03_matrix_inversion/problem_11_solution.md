**Result:**

The matrix is invertible for all real numbers $t$ except $t = 1$ and $t = -1$.

$$A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix} 1 & -t \\ -t & 1 \\ \end{pmatrix}$$

**Steps & Detailed Explanation:**

A $2 \times 2$ matrix is invertible if and only if its determinant is nonzero. Compute the determinant of $A(t)$:

$$\det A(t) = (1)(1) - (t)(t) = 1 - t^2$$

Set the determinant to zero to find the excluded values:

$$1 - t^2 = 0 \implies t^2 = 1 \implies t = \pm 1$$

Thus, the matrix is invertible for any $t \notin \{-1, 1\}$.

Using the standard formula for the inverse of a $2 \times 2$ matrix, swap the main diagonal entries, flip the signs of the