**Result:**

The matrix is not invertible for $t = \sqrt{2}$ and $t = -\sqrt{2}$.

**Steps & Detailed Explanation:**

A matrix is not invertible if and only if its determinant is zero. First, find the determinant of $A(t)$:

$$
\begin{aligned}
\det A(t) &= \det
\begin{pmatrix}
t & 1 \\
2 & t \\
\end{pmatrix} \\
&= (t)(t) - (1)(2) \\
&= t^2 - 2
\end{aligned}
$$

Set the determinant equal to zero to find the values for which the matrix cannot be inverted:

$$
t^2 - 2 = 0
$$

Solving for $t$ yields:

$$
t^2 = 2 \implies t = \pm\sqrt{2}
$$

For these specific values of $t$, the determinant evaluates to zero, meaning the rows of the matrix become linearly dependent and the matrix is singular.