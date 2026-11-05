### Essential Formulas

**Determinant Properties:**
1. **Determinant of a Matrix Product:**
   For any square matrices $X, Y, Z$ of the same size:

$$
   \det(XYZ) = \det X \cdot \det Y \cdot \det Z
$$

2. **Determinant of an Inverse Matrix:**
   If $B$ is invertible ($\det B \neq 0$):

$$
   \det(B^{-1}) = \frac{1}{\det B}
$$

3. **Determinant of a Transpose:**
   For any square matrix $A$:

$$
   \det(A^T) = \det A
$$

4. **Multiplication of Real Numbers:**
   Because determinants are scalar values (real numbers), their scalar multiplication is commutative.

---

### Problem Statement

**Exercise 15. Combining Determinant Properties**

Let $A$ and $B$ be invertible $2\times2$ matrices with

$$
\det A=-2,\qquad \det B=3.
$$

Without finding the entries of the matrices, compute

$$
\det\left(B^{-1}A^TB\right).
$$

State the determinant properties you use in order and explain why the factors involving $B$ eventually cancel.

> **Why this exercise:** tests the transfer of several known properties into one short problem instead of checking a single property again with numbers.

---

### Solution

**Step 1: Apply the product property of determinants**

Using the property that the determinant of a matrix product is the product of their determinants:

$$
\det\left(B^{-1}A^TB\right) = \det(B^{-1}) \cdot \det(A^T) \cdot \det B
$$

**Step 2: Apply properties for the inverse and the transpose**

Next, evaluate the determinant of each factor using fundamental properties:
1. Inverse property:

$$
\det(B^{-1}) = \frac{1}{\det B}
$$

2. Transpose property:

$$
\det(A^T) = \det A
$$

Substitute these into the expression:

$$
\det\left(B^{-1}A^TB\right) = \left(\frac{1}{\det B}\right) \cdot (\det A) \cdot (\det B)
$$

**Step 3: Explain the cancellation of the factors involving $B$**

Determinant values are scalars (ordinary real numbers in $\mathbb{R}$). While matrix multiplication is non-commutative in general ($XY \neq YX$), the multiplication of real numbers is commutative:

$$
\left(\frac{1}{\det B}\right) \cdot (\det A) \cdot (\det B) = (\det A) \cdot \left(\frac{1}{\det B} \cdot \det B\right)
$$

Since $B$ is invertible, $\det B \neq 0$. Therefore:

$$
\frac{1}{\det B} \cdot \det B = 1
$$

The scalar factors $\det(B^{-1}) = \frac{1}{\det B}$ and $\det B$ cancel each other out, leaving:

$$
\det\left(B^{-1}A^TB\right) = \det A
$$

This reflects the general theorem that a similarity transformation (conjugation by an invertible matrix $B$) preserves the determinant of any matrix: $\det(B^{-1}MB) = \det M$.

**Step 4: Substitute the given numerical values**

Given $\det A = -2$ and $\det B = 3$:

$$
\begin{aligned}
\det\left(B^{-1}A^TB\right) &= \left(\frac{1}{3}\right) \cdot (-2) \cdot (3) \\
&= \left(\frac{1}{3} \cdot 3\right) \cdot (-2) \\
&= 1 \cdot (-2) \\
&= -2
\end{aligned}
$$

---

### Final Answer

$$
\det\left(B^{-1}A^TB\right) = -2
$$
