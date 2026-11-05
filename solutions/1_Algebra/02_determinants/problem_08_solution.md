### Essential Formulas

**Determinant of a Matrix Product:**
For any two square matrices $A$ and $B$ of the same size $n \times n$:

$$
\det(AB) = \det A \cdot \det B
$$

**Commutativity of the Determinant:**
Although matrix multiplication is generally non-commutative ($AB \neq BA$), determinants are scalars in $\mathbb{R}$. Because scalar multiplication is commutative:

$$
\det(AB) = \det A \cdot \det B = \det B \cdot \det A = \det(BA)
$$

**Determinant of an Inverse Matrix:**
Since $A A^{-1} = I$ and $\det I = 1$:

$$
\det(A A^{-1}) = \det A \cdot \det(A^{-1}) = 1
$$

Therefore, for any invertible matrix $A$ ($\det A \neq 0$):

$$
\det(A^{-1}) = \frac{1}{\det A}
$$

$$
\det(A^{-1}B) = \det(A^{-1}) \cdot \det B = \frac{\det B}{\det A}
$$

---

### Problem Statement

**Exercise 8. Determinant of a Product**

Let $A,B$ be square matrices such that $\det A=3$ and $\det B=-5$. Compute $\det(AB)$, $\det(BA)$ and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB\neq BA$.

> **Why this exercise:** organizes how determinants behave with respect to products and inverses.

---

### Solution

Given:

$$
\det A = 3, \qquad \det B = -5
$$

**Step 1: Compute $\det(AB)$**

Apply the product rule for determinants:

$$
\det(AB) = \det A \cdot \det B
$$

Substitute the given values:

$$
\det(AB) = 3 \cdot (-5) = -15
$$

**Step 2: Compute $\det(BA)$**

Apply the product rule in reverse order:

$$
\det(BA) = \det B \cdot \det A
$$

Substitute the given values:

$$
\det(BA) = (-5) \cdot 3 = -15
$$

**Step 3: Check existence and compute $\det(A^{-1}B)$**

* Existence of $A^{-1}$:
  A matrix is invertible if and only if its determinant is non-zero. Since $\det A = 3 \neq 0$, the inverse matrix $A^{-1}$ exists.

* Evaluate $\det(A^{-1})$:

  $$
  \det(A^{-1}) = \frac{1}{\det A} = \frac{1}{3}
  $$

* Evaluate $\det(A^{-1}B)$:
  Using the product rule:

  $$
  \det(A^{-1}B) = \det(A^{-1}) \cdot \det B = \frac{1}{3} \cdot (-5) = -\frac{5}{3}
  $$

**Step 4: Explain why $\det(AB) = \det(BA)$ even though $AB \neq BA$**

Matrix multiplication is an operation defined on matrices ($\mathbb{R}^{n \times n} \times \mathbb{R}^{n \times n} \to \mathbb{R}^{n \times n}$). In general:

$$
AB \neq BA
$$

because multiplying $A$ by $B$ forms linear combinations of the rows of $A$ and columns of $B$, whereas $BA$ forms combinations of the rows of $B$ and columns of $A$. These represent different linear maps.

However, the determinant function maps an entire matrix to a single scalar value in the field of real numbers ($\det: \mathbb{R}^{n \times n} \to \mathbb{R}$):

$$
\det(AB) = (\det A)(\det B)
$$

$$
\det(BA) = (\det B)(\det A)
$$

Because multiplication of real numbers is commutative ($x \cdot y = y \cdot x$ for all $x, y \in \mathbb{R}$):

$$
(\det A)(\det B) = (\det B)(\det A)
$$

Therefore, $\det(AB) = \det(BA) = -15$. Geometrically, both compositions scale $n$-dimensional volume by the same factor $(-15)$, even though the intermediate transformations orient space differently.

**Step 5: Verification using concrete diagonal matrices**

To verify with concrete matrices, let:

$$
A = \begin{pmatrix}
3 & 0 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
-5 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

Here $\det A = (3)(1) = 3$ and $\det B = (-5)(1) = -5$.

* Compute $AB$:

  $$
  AB = \begin{pmatrix}
  -15 & 0 \\
  0 & 1 \\
  \end{pmatrix}
  \implies \det(AB) = -15
  $$

* Compute $BA$:

  $$
  BA = \begin{pmatrix}
  -15 & 0 \\
  0 & 1 \\
  \end{pmatrix}
  \implies \det(BA) = -15
  $$

* Compute $A^{-1}B$:

  $$
  A^{-1} = \begin{pmatrix}
  \frac{1}{3} & 0 \\
  0 & 1 \\
  \end{pmatrix},
  \qquad
  A^{-1}B = \begin{pmatrix}
  -\frac{5}{3} & 0 \\
  0 & 1 \\
  \end{pmatrix}
  \implies \det(A^{-1}B) = -\frac{5}{3}
  $$

All direct evaluations match the property-based computations.

---

### Final Answer

Calculated determinants:

$$
\det(AB) = -15
$$

$$
\det(BA) = -15
$$

$$
\det(A^{-1}B) = -\frac{5}{3}
$$

Even though $AB \neq BA$, $\det(AB) = \det(BA)$ because the determinant maps matrices to real numbers, where scalar multiplication is commutative: $(\det A)(\det B) = (\det B)(\det A)$.