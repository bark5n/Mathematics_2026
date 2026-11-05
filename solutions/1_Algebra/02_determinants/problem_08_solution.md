### Essential Formulas

**Determinant of a Product:**
For square matrices $A$ and $B$ of the same size:

$$
\det(AB) = \det A \cdot \det B
$$

**Determinant of an Inverse:**
If $A$ is invertible, then:

$$
\det(A^{-1}) = \frac{1}{\det A}
$$

**Commutativity of Scalar Multiplication:**
Since determinants are real numbers, $\det A \cdot \det B = \det B \cdot \det A$, even though $AB \neq BA$ in general.

---

### Problem Statement

**Exercise 8. Determinant of a Product**

Let $A, B$ be square matrices such that $\det A = 3$ and $\det B = -5$. Compute $\det(AB)$, $\det(BA)$ and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB \neq BA$.

---

### Solution

**Step 1: Compute $\det(AB)$**

Apply the product property directly:

$$
\det(AB) = \det A \cdot \det B = (3)(-5) = -15
$$

**Step 2: Compute $\det(BA)$**

Apply the same property with the factors in the opposite order:

$$
\det(BA) = \det B \cdot \det A = (-5)(3) = -15
$$

**Step 3: Explain why $\det(AB) = \det(BA)$**

Although matrix multiplication is not commutative ($AB \neq BA$ in general), the determinant maps each matrix to a real number. The product property gives:

$$
\det(AB) = \det A \cdot \det B = \det B \cdot \det A = \det(BA)
$$

The equality holds because real number multiplication is commutative. The determinant "forgets" the order of the factors.

**Step 4: Check that $A^{-1}$ exists**

Since $\det A = 3 \neq 0$, the matrix $A$ is invertible, so $A^{-1}$ exists and the expression $A^{-1}B$ is well-defined.

**Step 5: Compute $\det(A^{-1}B)$**

First find the determinant of the inverse:

$$
\det(A^{-1}) = \frac{1}{\det A} = \frac{1}{3}
$$

Then apply the product property:

$$
\begin{aligned}
\det(A^{-1}B) &= \det(A^{-1}) \cdot \det B \\
&= \frac{1}{3} \cdot (-5) \\
&= -\frac{5}{3}
\end{aligned}
$$

---

### Final Answer

$$
\det(AB) = -15, \qquad \det(BA) = -15, \qquad \det(A^{-1}B) = -\frac{5}{3}
$$

The equality $\det(AB) = \det(BA)$ follows from the commutativity of real number multiplication, not from commutativity of the matrices themselves.
