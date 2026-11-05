### Essential Formulas

**Identity Matrix ($I$):**
The identity matrix $I$ is a square matrix with 1s on the main diagonal and 0s elsewhere. For a $2 \times 2$ matrix, it is:

$$
I = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

It acts as the neutral element (multiplicative identity) for matrix multiplication, meaning $AI = IA = A$ for any square matrix $A$.

**Zero Matrix ($0$):**
The zero matrix has 0s in all its entries. For a $2 \times 2$ matrix, it is:

$$
0 = \begin{pmatrix}
0 & 0 \\
0 & 0 \\
\end{pmatrix}
$$

It acts as the neutral element (additive identity) for matrix addition, meaning $A + 0 = A$.

**Matrix Powers:**
Successive powers of a square matrix $A$ are found by repeatedly multiplying the matrix by itself: $A^2 = A \cdot A$, $A^3 = A^2 \cdot A$, and in general $A^{n+1} = A^n \cdot A$.

---

### Problem Statement

**Exercise 7. Identity Matrix, Zero Matrix, and Powers**

For

$$
A = \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

compute

$$
AI,\qquad IA,\qquad A+0,\qquad A^2,\qquad A^3.
$$

Explain the roles of the matrices $I$ and $0$, and describe the pattern you observe in successive powers of $A$.

> **Why this exercise:** organizes the roles of neutral elements and reveals regularity in successive powers of a matrix.

---

### Solution

**Step 1: Compute $AI$ and $IA$**

Multiply matrix $A$ by the $2 \times 2$ identity matrix $I$:

$$
AI = \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
(2\cdot1 + 1\cdot0) & (2\cdot0 + 1\cdot1) \\
(0\cdot1 + 2\cdot0) & (0\cdot0 + 2\cdot1) \\
\end{pmatrix}
= \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

Similarly, multiply $I$ by $A$:

$$
IA = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
(1\cdot2 + 0\cdot0) & (1\cdot1 + 0\cdot2) \\
(0\cdot2 + 1\cdot0) & (0\cdot1 + 1\cdot2) \\
\end{pmatrix}
= \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

*Role of $I$:* The identity matrix acts like the number $1$ in standard algebra. Multiplying a matrix by $I$ from either side leaves the original matrix unchanged ($AI = IA = A$).

**Step 2: Compute $A + 0$**

Add the $2 \times 2$ zero matrix to $A$:

$$
A + 0 = \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
+ \begin{pmatrix}
0 & 0 \\
0 & 0 \\
\end{pmatrix}
= \begin{pmatrix}
2+0 & 1+0 \\
0+0 & 2+0 \\
\end{pmatrix}
= \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

*Role of $0$:* The zero matrix acts like the number $0$ in standard algebra. Adding it to another matrix does not alter the original matrix ($A + 0 = A$).

**Step 3: Compute $A^2$ and $A^3$**

To find $A^2$, multiply $A$ by itself:

$$
A^2 = A \cdot A = \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

Evaluating the matrix product:

$$
A^2 = \begin{pmatrix}
(2\cdot2 + 1\cdot0) & (2\cdot1 + 1\cdot2) \\
(0\cdot2 + 2\cdot0) & (0\cdot1 + 2\cdot2) \\
\end{pmatrix}
= \begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix}
$$

To find $A^3$, multiply $A^2$ by $A$:

$$
A^3 = A^2 \cdot A = \begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

Evaluating the product:

$$
A^3 = \begin{pmatrix}
(4\cdot2 + 4\cdot0) & (4\cdot1 + 4\cdot2) \\
(0\cdot2 + 4\cdot0) & (0\cdot1 + 4\cdot2) \\
\end{pmatrix}
= \begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}
$$

**Step 4: Describe the observed pattern**

Examine the successive powers of $A$:

$$
\begin{aligned}
A^1 &= \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}, \\
A^2 &= \begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix}
= \begin{pmatrix}
2^2 & 2 \cdot 2^1 \\
0 & 2^2 \\
\end{pmatrix}, \\
A^3 &= \begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}
= \begin{pmatrix}
2^3 & 3 \cdot 2^2 \\
0 & 2^3 \\
\end{pmatrix}
\end{aligned}
$$

*Pattern Observation:*
For any power $n$, the main diagonal elements are $2^n$, and the lower-left element remains $0$. The upper-right element is $n \cdot 2^{n-1}$. Thus, the general formula for successive powers of $A$ is:

$$
A^n = \begin{pmatrix}
2^n & n \cdot 2^{n-1} \\
0 & 2^n \\
\end{pmatrix}
$$

---

### Final Answer

$$
AI = IA = A = \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

$$
A + 0 = \begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}
$$

$$
A^2 = \begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix},
\qquad
A^3 = \begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}
$$

General formula:

$$
A^n = \begin{pmatrix}
2^n & n \cdot 2^{n-1} \\
0 & 2^n \\
\end{pmatrix}
$$
