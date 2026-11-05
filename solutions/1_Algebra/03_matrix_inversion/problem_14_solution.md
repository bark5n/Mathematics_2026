### Essential Formulas

**Definition of Inverse Matrix:**
A square matrix $A$ is invertible if there exists a matrix $B$ such that:

$$
A B = B A = I
$$

When such a matrix $B$ exists, it is unique and denoted $A^{-1}$.

**Involution (Involutory Matrix):**
A matrix $A$ satisfying
$$
A^2 = I
$$
is called an involution (or involutory matrix). For every involutory matrix, $A^{-1} = A$.

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

**Step 1: Show that $A^2 = I \implies A^{-1} = A$**

By assumption, $A^2 = I$. Write out the square as a product of two matrices:

$$
A \cdot A = I
$$

By definition, the inverse $A^{-1}$ is the unique matrix satisfying:

$$
A \cdot A^{-1} = I \quad \mathrm{and} \quad A^{-1} \cdot A = I
$$

Comparing $A \cdot A = I$ directly with the definition shows that multiplying $A$ by $A$ yields the identity matrix $I$.
Since the matrix inverse is unique, it follows directly that:

$$
A^{-1} = A
$$

Alternatively, multiplying both sides of $A^2 = I$ by $A^{-1}$ from the left gives:

$$
A^{-1} (A^2) = A^{-1} I \implies (A^{-1} A) A = A^{-1} \implies I A = A^{-1} \implies A = A^{-1}
$$

**Step 2: Construct an example of a $2 \times 2$ matrix with $A^2 = I$ ($A \neq \pm I$)**

Geometrically, a reflection across the line $y = x$ or across one of the coordinate axes is its own inverse (reflecting twice returns any point to its starting position).

*Example: Reflection across the line $y = x$ (swapping $x$ and $y$):*

$$
A = \begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
$$

Notice that $A \neq I$ and $A \neq -I$.

*(Another valid example is a reflection across the $x$-axis: $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \\ \end{pmatrix}$.)*

**Step 3: Verify the example by multiplication**

Multiply $A$ by itself:

$$
\begin{aligned}
A^2 &= \begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
0(0) + 1(1) & 0(1) + 1(0) \\
1(0) + 0(1) & 1(1) + 0(0) \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I
\end{aligned}
$$

The product confirms $A^2 = I$, which proves that $A^{-1} = A$.

---

### Final Answer

1. Proof:
From $A^2 = I$, we have $A \cdot A = I$. By definition of the matrix inverse ($A A^{-1} = I$), $A$ acts as its own inverse, so $A^{-1} = A$.

2. Example matrix:

$$
A = \begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
$$

3. Verification:

$$
A^2 = \begin{pmatrix}
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
\end{pmatrix} = I
$$
