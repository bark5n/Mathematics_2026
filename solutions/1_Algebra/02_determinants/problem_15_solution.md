**Result:**

$$
\det\left(B^{-1}A^TB\right) = -2
$$

**Steps & Detailed Explanation:**

We use three fundamental properties of determinants to evaluate the expression:

1. The determinant of a product is the product of the determinants: $\det(XYZ) = \det X \det Y \det Z$.
2. The determinant of an inverse is the reciprocal of the determinant: $\det(B^{-1}) = \frac{1}{\det B}$.
3. The determinant of a transpose is the determinant of the original matrix: $\det(A^T) = \det A$.

Apply the first property to split the expression:

$$
\det\left(B^{-1}A^TB\right) = \det(B^{-1}) \det(A^T) \det(B)
$$

Substitute the second and third properties into the equation:

$$
\det\left(B^{-1}A^TB\right) = \left( \frac{1}{\det B} \right) (\det A) (\det B)
$$

Since determinants of matrices evaluate to real numbers, their multiplication is commutative. The factors $\frac{1}{\det B}$ and $\det B$ cancel each other out:

$$
\begin{aligned}
\det\left(B^{-1}A^TB\right) &= \left( \frac{1}{3} \right) (-2) (3) \\
&= \left( \frac{1}{3} \right) (3) (-2) \\
&= (1)(-2) \\
&= -2
\end{aligned}
$$

The final result depends only on the determinant of $A$, illustrating that a similarity transformation $B^{-1}MB$ preserves the determinant of a matrix $M$.