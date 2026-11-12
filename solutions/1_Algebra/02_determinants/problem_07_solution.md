### Essential Formulas

**Scalar Multiple of a Matrix:**
If $A \in \mathbb{R}^{n \times n}$ is an $n \times n$ matrix and $c \in \mathbb{R}$ is a scalar, multiplying $A$ by $c$ scales every one of its $n$ rows by $c$, which multiplies the determinant by $c^n$:

$$
\det(cA) = c^n \det A
$$

**Determinant of the Transpose:**
For any square matrix $A \in \mathbb{R}^{n \times n}$, transposing $A$ leaves its determinant unchanged:

$$
\det(A^T) = \det A
$$

**Multiplicative Property (Determinant of a Product and Power):**
For any two $n \times n$ matrices $A, B \in \mathbb{R}^{n \times n}$ and any positive integer $k \ge 1$:

$$
\det(AB) = \det A \cdot \det B,
\qquad
\det(A^k) = (\det A)^k
$$

---

### Problem Statement

**Exercise 7. Using Properties Instead of Recomputing**

Suppose that for a $3\times3$ matrix, $\det A=-4$. Compute

$$
\det(2A),
\qquad
\det(A^T),
\qquad
\det(A^2),
\qquad
\det(-A).
$$

Justify each answer using the appropriate property.

> **Why this exercise:** teaches how to use determinant properties instead of repeating a full calculation.

---

### Solution

**Step 1: Compute $\det(2A)$**

Because $A$ is a $3 \times 3$ matrix ($n = 3$), multiplying $A$ by the scalar $c = 2$ multiplies each of its $3$ rows by $2$. Applying the scalar multiplication property $\det(cA) = c^n \det A$ with $c = 2$ and $n = 3$:

$$
\begin{aligned}
\det(2A) &= 2^3 \det A \\
&= 8 \cdot (-4) \\
&= -32
\end{aligned}
$$

**Step 2: Compute $\det(A^T)$**

By the transpose property of determinants, a square matrix and its transpose always have the exact same determinant:

$$
\begin{aligned}
\det(A^T) &= \det A \\
&= -4
\end{aligned}
$$

**Step 3: Compute $\det(A^2)$**

Using the multiplicative property $\det(AB) = \det A \cdot \det B$ with $B = A$, the determinant of a matrix power equals the power of the determinant:

$$
\begin{aligned}
\det(A^2) &= \det(AA) \\
&= (\det A)^2 \\
&= (-4)^2 \\
&= 16
\end{aligned}
$$

**Step 4: Compute $\det(-A)$**

Write $-A = (-1)A$ and apply the scalar multiplication property $\det(cA) = c^n \det A$ with $c = -1$ and $n = 3$:

$$
\begin{aligned}
\det(-A) &= (-1)^3 \det A \\
&= (-1) \cdot (-4) \\
&= 4
\end{aligned}
$$

Because the dimension $n = 3$ is odd, negating all $3$ rows reverses the sign of the determinant three times, resulting in an overall sign change.

**Step 5: Verification**

Test all four properties on a concrete $3 \times 3$ diagonal matrix having $\det A = -4$, such as

$$
A = \begin{pmatrix}
-4 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

Computing each transformed matrix explicitly and taking the product of its diagonal entries gives:

* For $2A$:

$$
2A = \begin{pmatrix}
-8 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2 \\
\end{pmatrix},
\qquad
\det(2A) = (-8) \cdot 2 \cdot 2 = -32
$$

* For $A^T$:

$$
A^T = \begin{pmatrix}
-4 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix},
\qquad
\det(A^T) = (-4) \cdot 1 \cdot 1 = -4
$$

* For $A^2$:

$$
A^2 = \begin{pmatrix}
16 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix},
\qquad
\det(A^2) = 16 \cdot 1 \cdot 1 = 16
$$

* For $-A$:

$$
-A = \begin{pmatrix}
4 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & -1 \\
\end{pmatrix},
\qquad
\det(-A) = 4 \cdot (-1) \cdot (-1) = 4
$$

All four direct evaluations match the values derived from determinant properties.

---

### Final Answer

1. **Computed values:**

$$
\det(2A) = -32,
\qquad
\det(A^T) = -4,
\qquad
\det(A^2) = 16,
\qquad
\det(-A) = 4
$$

2. **Property justifications (for $n = 3$ and $\det A = -4$):**
   * $\det(2A) = 2^3 \det A = 8(-4) = -32$ by the scalar scaling property $\det(cA) = c^n \det A$.
   * $\det(A^T) = \det A = -4$ by the transpose invariance property $\det(A^T) = \det A$.
   * $\det(A^2) = (\det A)^2 = (-4)^2 = 16$ by the multiplicative property $\det(AB) = \det A \cdot \det B$.
   * $\det(-A) = (-1)^3 \det A = -(-4) = 4$ by the scalar scaling property with $c = -1$ and odd dimension $n = 3$.
