### Essential Formulas

**Scalar Multiple Property:**
For an $n \times n$ matrix $A$ and a scalar $c$:

$$
\det(cA) = c^n \det A
$$

**Transpose Property:**

$$
\det(A^T) = \det A
$$

**Product (Power) Property:**

$$
\det(A^k) = (\det A)^k
$$

In particular, $\det(A^2) = (\det A)^2$.

---

### Problem Statement

**Exercise 7. Using Properties Instead of Recomputing**

Suppose that for a $3 \times 3$ matrix, $\det A = -4$. Compute

$$
\det(2A),\qquad \det(A^T),\qquad \det(A^2),\qquad \det(-A).
$$

Justify each answer using the appropriate property.

---

### Solution

**Step 1: Compute $\det(2A)$**

Multiplying every entry of an $n \times n$ matrix by a scalar $c$ is equivalent to multiplying each of the $n$ rows by $c$. Each such row multiplication scales the determinant by $c$, so the total factor is $c^n$.

Since $A$ is $3 \times 3$ and $c = 2$:

$$
\det(2A) = 2^3 \det A = 8 \cdot (-4) = -32
$$

**Step 2: Compute $\det(A^T)$**

Transposing a matrix does not change its determinant. This holds for every square matrix:

$$
\det(A^T) = \det A = -4
$$

**Step 3: Compute $\det(A^2)$**

The determinant of a product equals the product of the determinants. Applying this to $A^2 = A \cdot A$:

$$
\det(A^2) = \det(A \cdot A) = \det A \cdot \det A = (\det A)^2 = (-4)^2 = 16
$$

**Step 4: Compute $\det(-A)$**

Negating a matrix is scalar multiplication by $c = -1$. Applying the scalar multiple property with $n = 3$:

$$
\det(-A) = (-1)^3 \det A = (-1)(-4) = 4
$$

Note that for odd-dimensional matrices, negation flips the sign of the determinant.

---

### Final Answer

$$
\det(2A) = -32, \qquad \det(A^T) = -4, \qquad \det(A^2) = 16, \qquad \det(-A) = 4
$$
