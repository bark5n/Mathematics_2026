### Essential Formulas

**Multiplicative Property of Determinants:**
The determinant of a product of square matrices equals the product of their individual determinants:

$$
\det(XYZ) = \det X \cdot \det Y \cdot \det Z
$$

**Determinant of an Inverse Matrix:**
For any invertible matrix $B$ ($\det B \neq 0$):

$$
\det(B^{-1}) = \frac{1}{\det B}
$$

**Determinant of a Transpose:**
Transposing a matrix does not change its determinant:

$$
\det(A^T) = \det A
$$

**Determinant Invariance under Similarity Transformations:**
A matrix of the form $P^{-1} M P$ is similar to $M$. Because scalar multiplication in $\mathbb{R}$ is commutative:

$$
\det(P^{-1} M P) = \det(P^{-1}) \cdot \det M \cdot \det P = \frac{1}{\det P} \cdot \det P \cdot \det M = \det M
$$

Thus, conjugating a matrix by an invertible matrix preserves its determinant.

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

Given that $A$ and $B$ are invertible $2 \times 2$ matrices with:

$$
\det A = -2, \qquad \det B = 3
$$

**Step 1: State and apply determinant properties in sequential order**

1. **Property 1: Multiplicative Property of Determinants**
   Apply the product rule to split the three-factor product into scalar determinants:

   $$
   \det(B^{-1} A^T B) = \det(B^{-1}) \cdot \det(A^T) \cdot \det B
   $$

2. **Property 2: Determinant of an Inverse Matrix**
   Since $B$ is invertible and $\det B = 3 \neq 0$:

   $$
   \det(B^{-1}) = \frac{1}{\det B} = \frac{1}{3}
   $$

3. **Property 3: Determinant of a Transposed Matrix**
   Transposition preserves determinant values:

   $$
   \det(A^T) = \det A = -2
   $$

**Step 2: Evaluate the expression and explain the cancellation of $B$**

Substitute the individual determinants back into the expansion:

$$
\det(B^{-1} A^T B) = \left(\frac{1}{\det B}\right) \cdot (\det A^T) \cdot (\det B)
$$

Substitute $\det A^T = \det A$:

$$
\det(B^{-1} A^T B) = \frac{1}{\det B} \cdot \det A \cdot \det B
$$

Because determinants are real numbers, scalar multiplication is commutative and associative:

$$
\det(B^{-1} A^T B) = \left( \frac{1}{\det B} \cdot \det B \right) \cdot \det A = 1 \cdot \det A = \det A
$$

Substitute the numerical value $\det A = -2$:

$$
\det(B^{-1} A^T B) = \frac{1}{3} \cdot (-2) \cdot 3 = -2
$$

*Why factors involving $B$ cancel:*
* **Algebraic Explanation:** The determinant operation maps matrices to scalars. In scalar multiplication, $\det(B^{-1}) = (\det B)^{-1}$. Multiplying any non-zero real number by its multiplicative inverse yields $1$: $(\det B)^{-1} \cdot \det B = 1$.
* **Geometric Explanation:** The matrix $B^{-1} A^T B$ represents a similarity transformation of $A^T$. The matrix $B$ transforms coordinates into a new basis (scaling volume by a factor of $\det B = 3$), the matrix $A^T$ acts on that space (scaling volume by $\det A = -2$), and $B^{-1}$ transforms back to the original basis (scaling volume by $\det(B^{-1}) = 1/3$). The net volume scaling factor introduced by changing bases and returning is $3 \cdot \frac{1}{3} = 1$, so the factors of $B$ completely cancel out.

**Step 3: Verification using test matrices**

Select concrete invertible matrices satisfying $\det A = -2$ and $\det B = 3$:

$$
A = \begin{pmatrix}
-2 & 0 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
1 & 0 \\
0 & 3 \\
\end{pmatrix}
$$

Find $A^T$ and $B^{-1}$:

$$
A^T = \begin{pmatrix}
-2 & 0 \\
0 & 1 \\
\end{pmatrix},
\qquad
B^{-1} = \begin{pmatrix}
1 & 0 \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

Compute the product $A^T B$:

$$
A^T B = \begin{pmatrix}
-2 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 3 \\
\end{pmatrix}
= \begin{pmatrix}
-2 & 0 \\
0 & 3 \\
\end{pmatrix}
$$

Multiply on the left by $B^{-1}$:

$$
B^{-1} A^T B = \begin{pmatrix}
1 & 0 \\
0 & \frac{1}{3} \\
\end{pmatrix}
\begin{pmatrix}
-2 & 0 \\
0 & 3 \\
\end{pmatrix}
= \begin{pmatrix}
-2 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

Calculate the determinant of the resulting matrix:

$$
\det(B^{-1} A^T B) = (-2)(1) - (0)(0) = -2
$$

The direct matrix computation confirms the result $-2$.

---

### Final Answer

Properties used in order:
1. Multiplicative property: $\det(B^{-1}A^TB) = \det(B^{-1}) \cdot \det(A^T) \cdot \det B$
2. Inverse property: $\det(B^{-1}) = \frac{1}{\det B}$
3. Transpose property: $\det(A^T) = \det A$
4. Scalar cancellation: $\frac{1}{\det B} \cdot \det B = 1$

Calculated determinant:

$$
\det\left(B^{-1}A^TB\right) = -2
$$
