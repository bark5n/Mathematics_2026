### Essential Formulas

**Determinant of a Triangular Matrix:**
A square matrix is called **upper triangular** if all entries below the main diagonal are zero ($a_{ij} = 0$ for $i > j$), and **lower triangular** if all entries above the main diagonal are zero ($a_{ij} = 0$ for $i < j$).

For any triangular (or diagonal) matrix $T \in \mathbb{R}^{n \times n}$, the determinant is simply the product of its diagonal entries:

$$
\det T = \prod_{i=1}^n t_{ii} = t_{11} \cdot t_{22} \cdots t_{nn}
$$

**Reason by Successive Cofactor Expansion:**
Expanding along the first column of an upper triangular matrix isolates the diagonal entry $t_{11}$ multiplied by another triangular matrix of dimension $(n-1) \times (n-1)$, repeatedly until only the product of the diagonal elements remains.

---

### Problem Statement

**Exercise 4. Triangular Matrix**

Without expanding the determinant, compute

$$
\det
\begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}.
$$

State the rule for an arbitrary triangular matrix and explain it using this example.

> **Why this exercise:** reinforces an important property of triangular matrices.

---

### Solution

**Step 1: Identify the matrix structure and diagonal entries**

Let

$$
T = \begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}
$$

All entries strictly below the main diagonal are zero ($t_{21} = 0, t_{31} = 0, t_{32} = 0$). Therefore, $T$ is an **upper triangular matrix**.

The entries along the main diagonal are:

$$
t_{11} = 2, \qquad t_{22} = -3, \qquad t_{33} = 7
$$

**Step 2: Compute the determinant using the diagonal rule**

Using the property for triangular matrices, multiply the diagonal entries directly:

$$
\det T = t_{11} \cdot t_{22} \cdot t_{33} = 2 \cdot (-3) \cdot 7 = -42
$$

**Step 3: State the general rule and explanation**

* **General Rule:**
  For any $n \times n$ upper triangular, lower triangular, or diagonal matrix $A$, the determinant equals the product of its diagonal entries:

  $$
  \det A = a_{11} a_{22} \cdots a_{nn}
  $$

* **Explanation using this example:**
  Consider Laplace expansion along the first column of $T$:

  $$
  \det T = 2 \cdot \det \begin{pmatrix}
  -3 & 5 \\
  0 & 7 \\
  \end{pmatrix}
  - 0 \cdot \det \begin{pmatrix}
  4 & 1 \\
  0 & 7 \\
  \end{pmatrix}
  + 0 \cdot \det \begin{pmatrix}
  4 & 1 \\
  -3 & 5 \\
  \end{pmatrix}
  $$

  The second and third terms vanish completely due to the zero entries in the first column:

  $$
  \det T = 2 \cdot \det \begin{pmatrix}
  -3 & 5 \\
  0 & 7 \\
  \end{pmatrix}
  $$

  Expanding the remaining $2 \times 2$ matrix:

  $$
  \det \begin{pmatrix}
  -3 & 5 \\
  0 & 7 \\
  \end{pmatrix}
  = (-3)(7) - (5)(0) = (-3)(7)
  $$

  Combining these steps:

  $$
  \det T = 2 \cdot (-3) \cdot 7 = -42
  $$

  Because all off-diagonal products in the expansion are multiplied by zeros, only the single product of the diagonal elements survives.

**Step 4: Verification**

To verify using Sarrus' rule:
* Downward diagonals:

  $$
  (2)(-3)(7) + (4)(5)(0) + (1)(0)(0) = -42 + 0 + 0 = -42
  $$

* Upward diagonals:

  $$
  (1)(-3)(0) + (2)(5)(0) + (4)(0)(7) = 0 + 0 + 0 = 0
  $$

* Subtracting:

  $$
  \det T = -42 - 0 = -42
  $$

The calculation confirms the diagonal product result.

---

### Final Answer

General rule for any triangular matrix $A$:

$$
\det A = a_{11} a_{22} \cdots a_{nn}
$$

Calculated determinant:

$$
\det \begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}
= -42
$$