### Essential Formulas

**Definition of the Inverse Matrix:**
For a square matrix $A \in \mathbb{R}^{n \times n}$, a matrix $B \in \mathbb{R}^{n \times n}$ is called the inverse of $A$ (denoted $A^{-1}$) if and only if:

$$
A B = B A = I
$$

where $I$ is the $n \times n$ identity matrix.

**Identity Matrix for $n = 2$:**

$$
I = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

**Matrix Multiplication ($2 \times 2$):**

$$
\begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
\begin{pmatrix}
e & f \\
g & h \\
\end{pmatrix}
=
\begin{pmatrix}
ae + bg & af + bh \\
ce + dg & cf + dh \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 1. Definition of the Inverse**

For

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
$$

check, without using a formula, whether $B=A^{-1}$. Compute $AB$ and $BA$ and relate the result to the definition of the inverse.

> **Why this exercise:** starts from the definition of the inverse through multiplication before any formulas or computational methods are introduced.

---

### Solution

**Step 1: Compute the matrix product $AB$**

Multiply row by column:

$$
\begin{aligned}
AB &= \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2(1) + 1(-1) & 2(-1) + 1(2) \\
1(1) + 1(-1) & 1(-1) + 1(2) \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 - 1 & -2 + 2 \\
1 - 1 & -1 + 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I
\end{aligned}
$$

**Step 2: Compute the matrix product $BA$**

Multiply in reverse order:

$$
\begin{aligned}
BA &= \begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1(2) + (-1)(1) & 1(1) + (-1)(1) \\
(-1)(2) + 2(1) & (-1)(1) + 2(1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 - 1 & 1 - 1 \\
-2 + 2 & -1 + 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I
\end{aligned}
$$

**Step 3: Relate the result to the definition of the inverse**

By definition, a matrix $B$ is the inverse of $A$ if and only if both products satisfy $AB = I$ and $BA = I$.
Since both calculations yield the $2 \times 2$ identity matrix:

$$
AB = BA = I
$$

the matrix $B$ satisfies the definition of the inverse. Therefore, $B = A^{-1}$.

---

### Final Answer

1. Matrix products:

$$
AB = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} = I, \qquad
BA = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} = I
$$

2. Conclusion:
Since $AB = BA = I$, by definition $B$ is the inverse of $A$, so $B = A^{-1}$.
