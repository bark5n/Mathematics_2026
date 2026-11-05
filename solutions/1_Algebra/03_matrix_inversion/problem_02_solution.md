### Essential Formulas

**Inverse Formula for a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix
$$
A = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$
with determinant $\det A = ad - bc \neq 0$, the inverse matrix is given by:

$$
A^{-1} = \frac{1}{\det A} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
= \frac{1}{ad - bc} \begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

**Verification Condition:**

$$
A A^{-1} = I
$$

---

### Problem Statement

**Exercise 2. Formula for a 2×2 Matrix**

Find the inverse of

$$
A=
\begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
$$

using the formula for a $2\times2$ matrix. At the end, check the result by computing one product with $A$.

> **Why this exercise:** teaches the simplest explicit formula for an inverse and requires verification using the definition.

---

### Solution

**Step 1: Compute the determinant of $A$**

Identify the matrix entries: $a = 3$, $b = 2$, $c = 5$, $d = 4$.

$$
\begin{aligned}
\det A &= ad - bc \\
&= (3)(4) - (2)(5) \\
&= 12 - 10 \\
&= 2
\end{aligned}
$$

Since $\det A = 2 \neq 0$, the matrix is invertible.

**Step 2: Apply the $2 \times 2$ inverse formula**

Swap the diagonal entries ($3$ and $4$), negate the off-diagonal entries ($2 \to -2$, $5 \to -5$), and multiply by $\frac{1}{\det A} = \frac{1}{2}$:

$$
\begin{aligned}
A^{-1} &= \frac{1}{2} \begin{pmatrix}
4 & -2 \\
-5 & 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{4}{2} & -\frac{2}{2} \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Verification by computing $A A^{-1}$**

Compute the product of $A$ and the calculated candidate $A^{-1}$:

$$
\begin{aligned}
A A^{-1} &= \begin{pmatrix}
3 & 2 \\
5 & 4 \\
\end{pmatrix}
\begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix} \\
&= \begin{pmatrix}
3(2) + 2\left(-\frac{5}{2}\right) & 3(-1) + 2\left(\frac{3}{2}\right) \\
5(2) + 4\left(-\frac{5}{2}\right) & 5(-1) + 4\left(\frac{3}{2}\right) \\
\end{pmatrix} \\
&= \begin{pmatrix}
6 - 5 & -3 + 3 \\
10 - 10 & -5 + 6 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I
\end{aligned}
$$

The product yields the identity matrix $I$, confirming that the inverse is correct.

---

### Final Answer

$$
A^{-1} = \begin{pmatrix}
2 & -1 \\
-\frac{5}{2} & \frac{3}{2} \\
\end{pmatrix}
$$
