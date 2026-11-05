### Essential Formulas

**Determinant of a Parameter-Dependent $2 \times 2$ Matrix:**
For a matrix whose entries depend on a scalar parameter $t$:

$$
\det \begin{pmatrix}
a(t) & b(t) \\
c(t) & d(t) \\
\end{pmatrix}
= a(t)d(t) - b(t)c(t)
$$

**Invertibility and Singularity Condition:**
A square matrix $A(t)$ is **not invertible** (singular) if and only if its determinant is zero:

$$
\det A(t) = 0
$$

When $\det A(t) = 0$:
1. The matrix does not have full rank.
2. The rows (and columns) are linearly dependent (parallel vectors in $\mathbb{R}^2$).
3. The inverse formula $A^{-1} = \frac{1}{\det A} \mathrm{adj}(A)$ is undefined due to division by zero.

Conversely, $A(t)$ is invertible if and only if $\det A(t) \neq 0$.

---

### Problem Statement

**Exercise 6. Parameter and Invertibility**

For

$$
A(t) = \begin{pmatrix}
t & 1 \\
2 & t \\
\end{pmatrix}
$$

find all values of $t$ for which the matrix is not invertible. Explain how your answer is related to the determinant being zero.

> **Why this exercise:** shows how the determinant can be used to study a family of matrices depending on a parameter.

---

### Solution

**Step 1: Compute the determinant of $A(t)$**

Using the $2 \times 2$ determinant formula:

$$
\det A(t) = (t)(t) - (1)(2) = t^2 - 2
$$

**Step 2: Find the parameter values where the matrix is not invertible**

A square matrix fails to be invertible precisely when its determinant is zero:

$$
\det A(t) = 0
$$

Substitute the expression for $\det A(t)$:

$$
t^2 - 2 = 0
$$

Solve for $t$:

$$
t^2 = 2 \implies t = \sqrt{2} \quad \mathrm{or} \quad t = -\sqrt{2}
$$

Thus, there are two values of $t$ for which $A(t)$ is not invertible: $t = \pm\sqrt{2}$.

**Step 3: Explain the connection to the determinant being zero**

The invertibility of a matrix is directly governed by its determinant:

1. **Algebraic Inverse:**
   The explicit formula for the inverse of a $2 \times 2$ matrix is:

   $$
   A(t)^{-1} = \frac{1}{t^2 - 2}
   \begin{pmatrix}
   t & -1 \\
   -2 & t \\
   \end{pmatrix}
   $$

   When $t = \pm\sqrt{2}$, the denominator $t^2 - 2$ equals zero. Since division by zero is undefined, no inverse matrix exists.

2. **Linear Dependence of Rows:**
   The vanishing of the determinant signifies that the rows of $A(t)$ become linearly dependent:

   * For $t = \sqrt{2}$:

     $$
     R_1 = (\sqrt{2}, 1), \qquad R_2 = (2, \sqrt{2}) = \sqrt{2} \cdot (\sqrt{2}, 1) = \sqrt{2} R_1
     $$

   * For $t = -\sqrt{2}$:

     $$
     R_1 = (-\sqrt{2}, 1), \qquad R_2 = (2, -\sqrt{2}) = -\sqrt{2} \cdot (-\sqrt{2}, 1) = -\sqrt{2} R_1
     $$

   In both cases, row 2 is a direct scalar multiple of row 1, collapsing the area spanned by the row vectors to zero.

**Step 4: Verification**

* Evaluate the determinant at $t = \sqrt{2}$:

  $$
  \det A(\sqrt{2}) = (\sqrt{2})^2 - 2 = 2 - 2 = 0
  $$

* Evaluate the determinant at $t = -\sqrt{2}$:

  $$
  \det A(-\sqrt{2}) = (-\sqrt{2})^2 - 2 = 2 - 2 = 0
  $$

* For any other real value $t \neq \pm\sqrt{2}$, $t^2 - 2 \neq 0$, meaning $\det A(t) \neq 0$ and $A(t)$ is invertible.

---

### Final Answer

Values of $t$ for which $A(t)$ is not invertible:

$$
t = \sqrt{2}, \qquad t = -\sqrt{2}
$$

A matrix is not invertible if and only if $\det A(t) = 0$, which occurs when the rows become linearly dependent and division by zero prevents the existence of $A(t)^{-1}$.