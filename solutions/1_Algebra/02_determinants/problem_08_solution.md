### Essential Formulas

**Determinant of a Product (Multiplicativity):**
For any two square matrices $A$ and $B$ of the same size, the determinant of their product is the product of their determinants:

$$
\det(AB) = \det(A)\det(B)
$$

**Determinant of an Inverse:**
If $A$ is an invertible matrix (meaning $\det A \neq 0$), the determinant of its inverse is the reciprocal of its determinant:

$$
\det(A^{-1}) = \frac{1}{\det A}
$$

---

### Problem Statement

**Exercise 8. Determinant of a Product**

Let $A,B$ be square matrices such that $\det A=3$ and $\det B=-5$. Compute $\det(AB)$, $\det(BA)$ and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB\neq BA$.

> **Why this exercise:** organizes how determinants behave with respect to products and inverses.

---

### Solution

**Step 1: Compute $\det(AB)$ and $\det(BA)$**

Using the multiplicative property of determinants, we can separate the products:

$$
\begin{aligned}
\det(AB) &= \det(A)\det(B) \\
&= 3 \cdot (-5) \\
&= -15
\end{aligned}
$$

Similarly, for the reverse product:

$$
\begin{aligned}
\det(BA) &= \det(B)\det(A) \\
&= (-5) \cdot 3 \\
&= -15
\end{aligned}
$$

**Step 2: Check for the existence of $A^{-1}$ and compute $\det(A^{-1}B)$**

Because $\det A = 3 \neq 0$, the matrix $A$ is invertible, so the inverse matrix $A^{-1}$ exists. We can apply the determinant properties for products and inverses:

$$
\begin{aligned}
\det(A^{-1}B) &= \det(A^{-1})\det(B) \\
&= \left(\frac{1}{\det A}\right) \det(B) \\
&= \left(\frac{1}{3}\right) (-5) \\
&= -\frac{5}{3}
\end{aligned}
$$

**Step 3: Explain why $\det(AB) = \det(BA)$ despite $AB \neq BA$**

Matrix multiplication is generally non-commutative ($AB \neq BA$), meaning the resulting matrices have entirely different entries. However, the determinant is a function that maps a matrix to a single real number (a scalar).

Because the determinant of a product splits into the product of determinants ($\det(AB) = \det(A)\det(B)$) and multiplication of real numbers *is* commutative ($xy = yx$ for any $x, y \in \mathbb{R}$), we strictly have:

$$
\det(A)\det(B) = \det(B)\det(A)
$$

Therefore, the scalar values of the determinants must be exactly equal, even if the underlying matrices $AB$ and $BA$ are completely different.

---

### Final Answer

1. **Computed determinants:**

$$
\det(AB) = -15, \qquad \det(BA) = -15, \qquad \det(A^{-1}B) = -\frac{5}{3}
$$

2. **Explanation of equality:** Even though the matrices $AB$ and $BA$ are usually not equal, their determinants are just scalar numbers. Because the determinant of a product is the product of the determinants ($\det(AB) = \det(A)\det(B)$), and scalar multiplication is commutative, the two values must be identical[cite: 5, 6].
