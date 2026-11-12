### Essential Formulas

**Multiplicative Property of Determinants:**
For any two square matrices $A, B \in \mathbb{R}^{n \times n}$ of the same size, the determinant of their product equals the product of their determinants:

$$\det(AB) = \det A \cdot \det B$$

**Determinant of the Inverse Matrix:**
A square matrix $A \in \mathbb{R}^{n \times n}$ is invertible if and only if $\det A \neq 0$. When $A^{-1}$ exists, the identity $A A^{-1} = I_n$ implies $(\det A)(\det A^{-1}) = \det I_n = 1$, giving:

$$\det(A^{-1}) = \frac{1}{\det A}$$

**Commutativity of Real Number Multiplication:**
Although matrix multiplication is generally noncommutative ($AB \neq BA$), determinants are real numbers, and real multiplication is commutative:

$$\det A \cdot \det B = \det B \cdot \det A$$

---

### Problem Statement

**Exercise 8. Determinant of a Product**

Let $A,B$ be square matrices such that $\det A=3$ and $\det B=-5$. Compute $\det(AB)$, $\det(BA)$ and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB\neq BA$.

> **Why this exercise:** organizes how determinants behave with respect to products and inverses.

---

### Solution

**Step 1: Compute $\det(AB)$ and $\det(BA)$**

Assuming $A$ and $B$ are square matrices of the same order $n$ so that the products $AB$ and $BA$ are defined, apply the multiplicative property $\det(XY) = \det X \cdot \det Y$:

* For $\det(AB)$:

$$\begin{aligned} \det(AB) &= \det A \cdot \det B \\ &= 3 \cdot (-5) \\ &= -15 \end{aligned}$$

* For $\det(BA)$:

$$\begin{aligned} \det(BA) &= \det B \cdot \det A \\ &= (-5) \cdot 3 \\ &= -15 \end{aligned}$$

**Step 2: Determine existence of $A^{-1}B$ and compute $\det(A^{-1}B)$**

Because $\det A = 3 \neq 0$, the matrix $A$ is invertible, so $A^{-1}$ exists and the product $A^{-1}B$ is well-defined. Using the inverse determinant formula $\det(A^{-1}) = \frac{1}{\det A}$ together with the multiplicative property gives:

$$\begin{aligned} \det(A^{-1}B) &= \det(A^{-1}) \cdot \det B \\ &= \frac{1}{\det A} \cdot \det B \\ &= \frac{1}{3} \cdot (-5) \\ &= -\frac{5}{3} \end{aligned}$$

**Step 3: Explain why $\det(AB) = \det(BA)$ even though usually $AB \neq BA$**

The matrices $AB$ and $BA$ are generally distinct matrices because matrix multiplication depends on the order in which rows and columns are paired. However, the determinant reduces each square matrix to a single real scalar, and the multiplicative rule turns matrix multiplication into ordinary multiplication of real numbers:

$$\det(AB) = \det A \cdot \det B = \det B \cdot \det A = \det(BA)$$

Because multiplication in $\mathbb{R}$ is commutative, swapping the order of the real numbers $3$ and $-5$ leaves the scalar product $-15$ unchanged. Geometrically, $\vert{}\det A\vert{}$ and $\vert{}\det B\vert{}$ measure volume scaling factors and their signs record orientation; composing two linear transformations scales signed volume by the product of their individual factors regardless of which transformation is applied first.

**Step 4: Verification**

Construct two concrete $2 \times 2$ matrices with $\det A = 3$ and $\det B = -5$ that do not commute, such as

$$A = \begin{pmatrix} 3 & 1 \\ 0 & 1 \\ \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 2 & -5 \\ \end{pmatrix}$$

Here $\det A = 3 \cdot 1 - 1 \cdot 0 = 3$ and $\det B = 1 \cdot (-5) - 0 \cdot 2 = -5$.

* **Check $AB$ and $BA$ directly:**

$$AB = \begin{pmatrix} 3 & 1 \\ 0 & 1 \\ \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & -5 \\ \end{pmatrix} = \begin{pmatrix} 5 & -5 \\ 2 & -5 \\ \end{pmatrix}, \qquad BA = \begin{pmatrix} 1 & 0 \\ 2 & -5 \\ \end{pmatrix} \begin{pmatrix} 3 & 1 \\ 0 & 1 \\ \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 6 & -3 \\ \end{pmatrix}$$

  Clearly $AB \neq BA$, yet their determinants are identical:

$$\det(AB) = 5 \cdot (-5) - (-5) \cdot 2 = -25 + 10 = -15$$

$$\det(BA) = 3 \cdot (-3) - 1 \cdot 6 = -9 - 6 = -15$$

* **Check $A^{-1}B$ directly:**
  The inverse of $A$ is

$$A^{-1} = \frac{1}{3} \begin{pmatrix} 1 & -1 \\ 0 & 3 \\ \end{pmatrix}$$

  Multiplying $A^{-1}$ by $B$ gives

$$A^{-1}B = \frac{1}{3} \begin{pmatrix} 1 & -1 \\ 0 & 3 \\ \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & -5 \\ \end{pmatrix} = \frac{1}{3} \begin{pmatrix} -1 & 5 \\ 6 & -15 \\ \end{pmatrix}$$

  Computing its determinant directly yields

$$\det(A^{-1}B) = \left(\frac{1}{3}\right)^2 \left((-1)(-15) - 5 \cdot 6\right) = \frac{1}{9}(15 - 30) = -\frac{15}{9} = -\frac{5}{3}$$

All three values match the results derived from determinant properties.

---

### Final Answer

1. **Computed determinants:**

$$\det(AB) = -15, \qquad \det(BA) = -15, \qquad \det(A^{-1}B) = -\frac{5}{3}$$

2. **Existence of $\det(A^{-1}B)$:** Because $\det A = 3 \neq 0$, $A^{-1}$ exists, so $\det(A^{-1}B) = (\det A)^{-1}\det B = -\frac{5}{3}$ is
