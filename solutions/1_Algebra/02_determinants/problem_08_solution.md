**Result:**

$$
\det(AB) = -15, \qquad \det(BA) = -15, \qquad \det(A^{-1}B) = -\frac{5}{3}
$$

**Steps & Detailed Explanation:**

The determinant of a matrix product is equal to the product of their separate determinants: $\det(XY) = \det X \det Y$.

For $AB$:

$$
\det(AB) = \det A \det B = (3)(-5) = -15
$$

For $BA$:

$$
\det(BA) = \det B \det A = (-5)(3) = -15
$$

The determinant evaluates to real numbers. Since real number multiplication is commutative, $\det(AB) = \det(BA)$ is always true for square matrices, even though matrix multiplication itself is generally not commutative ($AB \ne BA$).

For the expression with the inverse, recall that $\det(A^{-1}) = \frac{1}{\det A}$. Thus:

$$
\begin{aligned}
\det(A^{-1}B) &= \det(A^{-1}) \det(B) \\
&= \frac{1}{\det A} \det B \\
&= \frac{1}{3} (-5) \\
&= -\frac{5}{3}
\end{aligned}
$$