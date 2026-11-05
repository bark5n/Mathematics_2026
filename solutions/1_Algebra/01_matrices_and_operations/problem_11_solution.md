### Essential Formulas

**Matrix Commutativity:**
In general, matrix multiplication is not commutative ($AB \neq BA$). Two square matrices $A$ and $B$ of the same size commute if and only if:

$$
AB = BA
$$

**Matrix Equality:**
Two matrices are equal if and only if they have the same dimensions and all their corresponding entries are identical.

---

### Problem Statement

**Exercise 11. When Do Matrices Commute?**

Given

$$
A = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

Find the conditions on $a,b,c,d$ under which $AB=BA$. Describe the general form of all such matrices $B$.

> **Why this exercise:** deepens the idea of noncommutativity by finding the conditions under which commutativity does hold.

---

### Solution

**Step 1: Compute the product $AB$**

Multiply matrix $A$ by matrix $B$:

$$
\begin{aligned}
AB &= \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot a + 1\cdot c) & (1\cdot b + 1\cdot d) \\
(0\cdot a + 1\cdot c) & (0\cdot b + 1\cdot d) \\
\end{pmatrix} \\
&= \begin{pmatrix}
a + c & b + d \\
c & d \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compute the product $BA$**

Multiply matrix $B$ by matrix $A$:

$$
\begin{aligned}
BA &= \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(a\cdot 1 + b\cdot 0) & (a\cdot 1 + b\cdot 1) \\
(c\cdot 1 + d\cdot 0) & (c\cdot 1 + d\cdot 1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
a & a + b \\
c & c + d \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Equate $AB$ and $BA$ to determine conditions**

For $A$ and $B$ to commute, $AB = BA$:

$$
\begin{pmatrix}
a + c & b + d \\
c & d \\
\end{pmatrix}
= \begin{pmatrix}
a & a + b \\
c & c + d \\
\end{pmatrix}
$$

Equating corresponding entries yields four equations:
1. Top-left: $a + c = a \implies c = 0$
2. Top-right: $b + d = a + b \implies d = a$
3. Bottom-left: $c = c$ (identity)
4. Bottom-right: $d = c + d$ (with $c=0$, $d = d$, identity)

Thus, the required conditions are $c = 0$ and $d = a$, with $a$ and $b$ being arbitrary real numbers.

**Step 4: Describe the general form of matrix $B$**

Substituting $c = 0$ and $d = a$ into $B$:

$$
B = \begin{pmatrix}
a & b \\
0 & a \\
\end{pmatrix}
$$

*Conclusion:*
Matrix $B$ commutes with $A$ if and only if $B$ is an upper triangular matrix whose diagonal entries are equal.

---

### Final Answer

Conditions:

$$
c = 0, \qquad d = a
$$

General form of matrix $B$:

$$
B = \begin{pmatrix}
a & b \\
0 & a \\
\end{pmatrix}
\qquad (a, b \in \mathbb{R})
$$
