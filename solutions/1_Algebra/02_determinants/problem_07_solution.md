### Essential Formulas

**Scalar Multiplication of an $n \times n$ Matrix:**
Multiplying an $n \times n$ matrix $A$ by a scalar $c$ multiplies every single entry in all $n$ rows by $c$. Factoring $c$ out from each row yields:

$$
\det(cA) = c^n \det A
$$

**Transpose Property:**
Transposing a matrix interchanges its rows and columns without changing the value of the determinant:

$$
\det(A^T) = \det A
$$

**Multiplicative Property and Powers:**
The determinant of a product of two square matrices of the same size equals the product of their determinants:

$$
\det(AB) = \det A \cdot \det B
$$

Consequently, for any positive integer $k$:

$$
\det(A^k) = (\det A)^k
$$

**Negation of an $n \times n$ Matrix:**
Negating a matrix is equivalent to scalar multiplication by $c = -1$:

$$
\det(-A) = \det((-1)A) = (-1)^n \det A
$$

For an odd dimension $n$ (such as $n = 3$), $(-1)^n = -1$, reversing the sign. For an even dimension $n$, $(-1)^n = 1$, leaving the determinant unchanged.

---

### Problem Statement

**Exercise 7. Using Properties Instead of Recomputing**

Suppose that for a $3\times3$ matrix, $\det A=-4$. Compute

$$
\det(2A),\qquad \det(A^T),\qquad \det(A^2),\qquad \det(-A).
$$

Justify each answer using the appropriate property.

> **Why this exercise:** teaches how to use determinant properties instead of repeating a full calculation.

---

### Solution

Given that $A$ is a $3 \times 3$ matrix ($n = 3$) and:

$$
\det A = -4
$$

**Step 1: Compute $\det(2A)$**

Using the scalar multiplication property with scalar $c = 2$ and matrix dimension $n = 3$:

$$
\det(2A) = 2^3 \det A = 8 \det A
$$

Substitute $\det A = -4$:

$$
\det(2A) = 8 \cdot (-4) = -32
$$

*Justification:*
Multiplying the matrix by $2$ doubles every entry. Factoring out a factor of $2$ from each of the $3$ rows yields $2 \cdot 2 \cdot 2 = 2^3 = 8$.

**Step 2: Compute $\det(A^T)$**

Using the transpose property of determinants:

$$
\det(A^T) = \det A
$$

Substitute $\det A = -4$:

$$
\det(A^T) = -4
$$

*Justification:*
Transposing reflects entries across the main diagonal. Since row expansions and column expansions yield identical determinant formulas, transposition preserves the determinant.

**Step 3: Compute $\det(A^2)$**

Using the multiplicative property of determinants for $A^2 = A \cdot A$:

$$
\det(A^2) = \det(A \cdot A) = (\det A) \cdot (\det A) = (\det A)^2
$$

Substitute $\det A = -4$:

$$
\det(A^2) = (-4)^2 = 16
$$

*Justification:*
The determinant of a matrix product is the product of the individual determinants.

**Step 4: Compute $\det(-A)$**

Using the scalar property with $c = -1$ and dimension $n = 3$:

$$
\det(-A) = \det((-1)A) = (-1)^3 \det A = -1 \cdot \det A
$$

Substitute $\det A = -4$:

$$
\det(-A) = (-1) \cdot (-4) = 4
$$

*Justification:*
Negating the matrix multiplies each of the $3$ rows by $-1$. Factoring $-1$ out from each row produces $(-1)^3 = -1$.

**Step 5: Verification using a test diagonal matrix**

To verify these results with a concrete example, choose the diagonal $3 \times 3$ matrix:

$$
A = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & -4 \\
\end{pmatrix}
$$

The determinant is $\det A = (1)(1)(-4) = -4$.

Evaluate each transformed matrix directly:

* For $2A$:

  $$
  2A = \begin{pmatrix}
  2 & 0 & 0 \\
  0 & 2 & 0 \\
  0 & 0 & -8 \\
  \end{pmatrix}
  \implies \det(2A) = (2)(2)(-8) = -32
  $$

* For $A^T$:

  $$
  A^T = A \implies \det(A^T) = -4
  $$

* For $A^2$:

  $$
  A^2 = \begin{pmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 16 \\
  \end{pmatrix}
  \implies \det(A^2) = (1)(1)(16) = 16
  $$

* For $-A$:

  $$
  -A = \begin{pmatrix}
  -1 & 0 & 0 \\
  0 & -1 & 0 \\
  0 & 0 & 4 \\
  \end{pmatrix}
  \implies \det(-A) = (-1)(-1)(4) = 4
  $$

All values match the property-based derivations.

---

### Final Answer

Calculated determinants:

$$
\det(2A) = -32
$$

$$
\det(A^T) = -4
$$

$$
\det(A^2) = 16
$$

$$
\det(-A) = 4
$$