### Essential Formulas

**Multiplicative Property of Determinants:**
For any square matrices $X, Y \in \mathbb{R}^{n \times n}$ of the same size, the determinant of a product equals the product of the determinants:

$$
\det(XY) = \det X \cdot \det Y
$$

By associativity, this extends to any finite product of $n \times n$ matrices; in particular, for three matrices $X, Y, Z \in \mathbb{R}^{n \times n}$:

$$
\det(XYZ) = \det X \cdot \det Y \cdot \det Z
$$

**Determinant of the Inverse Matrix:**
If $B \in \mathbb{R}^{n \times n}$ is invertible ($\det B \neq 0$), the identity $B^{-1}B = I_n$ gives $\det(B^{-1})\det B = 1$, so:

$$
\det(B^{-1}) = \frac{1}{\det B}
$$

**Determinant of the Transpose:**
For any square matrix $A \in \mathbb{R}^{n \times n}$, transposing leaves the determinant unchanged:

$$
\det(A^T) = \det A
$$

**Similarity Invariance of the Determinant:**
For any square matrix $M \in \mathbb{R}^{n \times n}$ and any invertible matrix $B \in \mathbb{R}^{n \times n}$, similar matrices share the same determinant:

$$
\det(B^{-1} M B) = \det M
$$

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

**Step 1: Apply the determinant properties in order**

Start with $\det(B^{-1} A^T B)$ and apply the properties sequentially:

1. **Multiplicative property ($\det(XYZ) = \det X \cdot \det Y \cdot \det Z$):**
   Since $B^{-1}$, $A^T$, and $B$ are all $2 \times 2$ matrices, break the determinant of the triple product into the product of three individual determinants:

$$
\det\left(B^{-1}A^TB\right) = \det(B^{-1}) \cdot \det(A^T) \cdot \det B
$$

2. **Inverse property ($\det(B^{-1}) = \frac{1}{\det B}$) and transpose property ($\det(A^T) = \det A$):**
   Because $B$ is invertible ($\det B = 3 \neq 0$), replace $\det(B^{-1})$ with $\frac{1}{\det B}$, and replace $\det(A^T)$ with $\det A$:

$$
\det\left(B^{-1}A^TB\right) = \frac{1}{\det B} \cdot \det A \cdot \det B
$$

**Step 2: Explain why the factors involving $B$ cancel**

In general, $B^{-1} A^T B \neq A^T$ at the matrix level because matrix multiplication is noncommutative ($B^{-1}$ and $B$ are separated by $A^T$ and cannot be moved next to each other).

However, once the multiplicative property is applied, $\frac{1}{\det B}$, $\det A$, and $\det B$ are ordinary real numbers rather than matrices. Because multiplication of real numbers is both commutative and associative, the nonzero scalar factors $\frac{1}{\det B}$ and $\det B$ can be grouped together and cancel to $1$:

$$
\begin{aligned}
\frac{1}{\det B} \cdot \det A \cdot \det B &= \left(\frac{1}{\det B} \cdot \det B\right) \cdot \det A \\
&= 1 \cdot \det A \\
&= \det A
\end{aligned}
$$

Geometrically, $B$ and $B^{-1}$ represent a change of basis and its inverse transformation; any volume scaling by $|\det B|$ and orientation change caused by $B$ is undone by $B^{-1}$, leaving only the determinant of $A^T$ (which equals $\det A$).

**Step 3: Substitute the given numerical values**

Substitute $\det A = -2$ (and $\det B = 3$ to verify the cancellation explicitly):

$$
\begin{aligned}
\det\left(B^{-1}A^TB\right) &= \frac{1}{3} \cdot (-2) \cdot 3 \\
&= \left(\frac{1}{3} \cdot 3\right) \cdot (-2) \\
&= 1 \cdot (-2) \\
&= -2
\end{aligned}
$$

**Step 4: Verification**

Test the result using two concrete non-commuting $2 \times 2$ matrices with $\det A = -2$ and $\det B = 3$:

$$
A = \begin{pmatrix}
-2 & 1 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
3 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

* **Check individual determinants:**
  * $\det A = (-2) \cdot 1 - 1 \cdot 0 = -2$
  * $\det B = 3 \cdot 1 - 1 \cdot 0 = 3$

* **Form $A^T$ and $B^{-1}$:**

$$
A^T = \begin{pmatrix}
-2 & 0 \\
1 & 1 \\
\end{pmatrix},
\qquad
B^{-1} = \frac{1}{3}
\begin{pmatrix}
1 & -1 \\
0 & 3 \\
\end{pmatrix}
$$

* **Compute the matrix product $B^{-1} A^T B$ explicitly:**

$$
A^T B = \begin{pmatrix}
-2 & 0 \\
1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
3 & 1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
-6 & -2 \\
3 & 2 \\
\end{pmatrix}
$$

$$
B^{-1} A^T B = \frac{1}{3}
\begin{pmatrix}
1 & -1 \\
0 & 3 \\
\end{pmatrix}
\begin{pmatrix}
-6 & -2 \\
3 & 2 \\
\end{pmatrix}
= \frac{1}{3}
\begin{pmatrix}
-9 & -4 \\
9 & 6 \\
\end{pmatrix}
= \begin{pmatrix}
-3 & -\frac{4}{3} \\
3 & 2 \\
\end{pmatrix}
$$

* **Compute $\det(B^{-1} A^T B)$ directly from the entries:**

$$
\det\left(B^{-1} A^T B\right) = (-3) \cdot 2 - \left(-\frac{4}{3}\right) \cdot 3 = -6 - (-4) = -2
$$

Although $B^{-1} A^T B \neq A^T$, its determinant equals $-2$, confirming the result.

---

### Final Answer

1. **Computed determinant:**

$$
\det\left(B^{-1}A^TB\right) = -2
$$

2. **Properties used in order:**
   * **Multiplicative property:** $\det(B^{-1}A^TB) = \det(B^{-1}) \cdot \det(A^T) \cdot \det B$.
   * **Inverse property:** $\det(B^{-1}) = \frac{1}{\det B}$.
   * **Transpose property:** $\det(A^T) = \det A$.
3. **Why the $B$-factors cancel:** Although $B^{-1}$ and $B$ do not commute past $A^T$ as matrices, their determinants are nonzero real scalars ($\frac{1}{\det B} = \frac{1}{3}$ and $\det B = 3$). Because real-number multiplication is commutative and associative, $\frac{1}{\det B} \cdot \det B = 1$, leaving $\det(B^{-1}A^TB) = \det A = -2$.
