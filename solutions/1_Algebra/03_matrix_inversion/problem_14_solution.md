### Essential Formulas

**Definition of the Inverse Matrix:**
Let $A \in \mathbb{R}^{n \times n}$ be a square matrix. A square matrix $B \in \mathbb{R}^{n \times n}$ is the **inverse** of $A$, denoted $B = A^{-1}$, if and only if:

$$
AB = I_n \qquad \mathrm{and} \qquad BA = I_n
$$

where $I_n$ is the $n \times n$ identity matrix.

**Uniqueness of the Inverse:**
If a square matrix $A \in \mathbb{R}^{n \times n}$ has an inverse, that inverse is unique: if both $B$ and $C$ satisfy $AB = BA = I_n$ and $AC = CA = I_n$, then $B = B I_n = B(AC) = (BA)C = I_n C = C$.

**Involutory Matrices:**
A square matrix $A \in \mathbb{R}^{n \times n}$ satisfying $A^2 = I_n$ is called an **involutory matrix**. Geometrically, such transformations (such as reflections) undo themselves when applied a second time.

---

### Problem Statement

**Exercise 14. A Matrix That Is Its Own Inverse**

Assume that a square matrix $A$ satisfies

$$
A^2=I.
$$

Show that

$$
A^{-1}=A.
$$

Then give an example of a $2\times2$ matrix different from $I$ and $-I$ that satisfies this condition, and verify it by multiplication.

> **Why this exercise:** requires using the definition of the inverse in a short argument and constructing an example independently, without introducing a new topic.

---

### Solution

**Step 1: Show that $A^{-1} = A$ using the definition of the inverse**

By definition of matrix powers, $A^2$ means the product $A \cdot A$. Rewriting the given hypothesis $A^2 = I$ in product form gives:

$$
A \cdot A = I
$$

Recall that a matrix $B$ is the inverse of $A$ ($B = A^{-1}$) if and only if both $AB = I$ and $BA = I$ hold. Setting $B = A$, both conditions become the single verified equation $A \cdot A = I$:

$$
AB = A \cdot A = I \qquad \mathrm{and} \qquad BA = A \cdot A = I
$$

Because the inverse of a square matrix is unique whenever it exists, $A$ is invertible and its inverse must equal $A$ itself:

$$
A^{-1} = A
$$

*(Note: Taking determinants of $A^2 = I$ also confirms invertibility, since $(\det A)^2 = \det(A^2) = \det I = 1$ implies $\det A = \pm 1 \neq 0$.)*

**Step 2: Construct an example of a $2 \times 2$ matrix different from $I_2$ and $-I_2$**

To find a $2 \times 2$ matrix $A \neq \pm I_2$ with $A^2 = I_2$, consider the reflection across the horizontal $x_1$-axis, which leaves the first coordinate unchanged and negates the second coordinate:

$$
A = \begin{pmatrix}
1 & 0 \\
0 & -1 \\
\end{pmatrix}
$$

Clearly $A \neq I_2$ and $A \neq -I_2$, because its two diagonal entries have opposite signs ($1$ and $-1$).

**Step 3: Verify the example by multiplication**

Compute $A^2 = A \cdot A$ directly:

$$
\begin{aligned}
A^2 &= \begin{pmatrix}
1 & 0 \\
0 & -1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & -1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 1 + 0 \cdot 0 & 1 \cdot 0 + 0 \cdot (-1) \\
0 \cdot 1 + (-1) \cdot 0 & 0 \cdot 0 + (-1) \cdot (-1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I_2
\end{aligned}
$$

Since $A^2 = I_2$, the matrix $A$ satisfies the condition and is its own inverse ($A^{-1} = A$).

**Step 4: Verification**

* **Check using the explicit $2 \times 2$ inverse formula:**
  Here $\det A = 1 \cdot (-1) - 0 \cdot 0 = -1 \neq 0$, so

$$
A^{-1} = \frac{1}{-1}
\begin{pmatrix}
-1 & 0 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & -1 \\
\end{pmatrix}
= A
$$

* **Alternative non-diagonal example (reflection across the line $x_2 = x_1$):**
  The permutation matrix

$$
P = \begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
$$

  is also distinct from $I_2$ and $-I_2$, and satisfies

$$
P^2 = \begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I_2
$$

  so $P^{-1} = P$ as well.

---

### Final Answer

1. **Proof that $A^{-1} = A$:** Writing $A^2 = I$ as $A \cdot A = I$ shows that $B = A$ satisfies both $AB = I$ and $BA = I$; by uniqueness of the inverse, $A^{-1} = A$.
2. **Example of a $2 \times 2$ matrix ($A \neq I_2, -I_2$):**

$$
A = \begin{pmatrix}
1 & 0 \\
0 & -1 \\
\end{pmatrix}
$$

3. **Verification:** Multiplying $A$ by itself gives $A^2 = I_2$, confirming that $A^{-1} = A$.
