**Result:**

Matrix $D$ is invertible. Matrix $E$ is not invertible.

$$D^{-1} = \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \\ \end{pmatrix}$$

**Steps & Detailed Explanation:**

For a diagonal matrix, the determinant is the product of its diagonal entries. 
For $D$, the determinant is $(2)(-3)(5) = -30$, which is nonzero, so $D$ is invertible. 
For $E$, the determinant is $(2)(0)(5) = 0$ due to the zero on the main diagonal, making it noninvertible.

The inverse of an invertible diagonal matrix is simply a diagonal matrix where each diagonal entry is the reciprocal of the original diagonal entry:

$$D^{-1} = \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \\ \end{pmatrix}$$

Check the result by multiplying $DD^{-1}$:

$$\begin{aligned} DD^{-1} &= \begin{pmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 5 \\ \end{pmatrix} \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \\ \end{pmatrix} \\ &= \begin{pmatrix} (2)(\frac{1}{2}) & 0 & 0 \\ 0 & (-3)(-\frac{1}{3}) & 0 \\ 0 & 0 & (5)(\frac{1}{5}) \\ \end{pmatrix} \\ &= \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ \end{pmatrix} = I \end{aligned}$$

The product is the identity matrix, confirming the rule for diagonal matrices.