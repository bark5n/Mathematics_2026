### Essential Formulas

**Associativity of Matrix Multiplication:**
For matrices $A, B, C$ with compatible dimensions, matrix multiplication is associative:

$$
(AB)C = A(BC)
$$

**Computational Cost of Matrix Multiplication:**
Multiplying an $m \times n$ matrix by an $n \times p$ matrix produces an $m \times p$ matrix. Calculating each entry requires $n$ scalar multiplications, resulting in a total of:

$$
m \cdot n \cdot p
$$

scalar multiplications.

---

### Problem Statement

**Exercise 15. Associativity of Multiplication and Different Calculation Paths**

Given

$$
A = \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix},
\qquad
C = \begin{pmatrix}
2 & 1 \\
0 & -1 \\
\end{pmatrix}
$$

Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

> **Why this exercise:** reinforces associativity by comparing two mathematically equivalent calculation paths.

---

### Solution

**Step 1: Compute Path 1: $(AB)C$**

First, compute the product $AB$. Multiplying the $2 \times 3$ matrix $A$ by the $3 \times 2$ matrix $B$ yields a $2 \times 2$ matrix:

$$
\begin{aligned}
AB &= \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot1 + 2\cdot2 + 0\cdot(-1)) & (1\cdot0 + 2\cdot1 + 0\cdot3) \\
(0\cdot1 + 1\cdot2 + 1\cdot(-1)) & (0\cdot0 + 1\cdot1 + 1\cdot3) \\
\end{pmatrix} \\
&= \begin{pmatrix}
5 & 2 \\
1 & 4 \\
\end{pmatrix}
\end{aligned}
$$

Multiplications for $AB$: $2 \times 3 \times 2 = 12$.

Next, multiply the result by $C$:

$$
\begin{aligned}
(AB)C &= \begin{pmatrix}
5 & 2 \\
1 & 4 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & -1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(5\cdot2 + 2\cdot0) & (5\cdot1 + 2\cdot(-1)) \\
(1\cdot2 + 4\cdot0) & (1\cdot1 + 4\cdot(-1)) \\
\end{pmatrix} \\
&= \begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}
\end{aligned}
$$

Multiplications for $(AB)C$: $2 \times 2 \times 2 = 8$.

Total multiplications for Path 1: $12 + 8 = 20$.

**Step 2: Compute Path 2: $A(BC)$**

First, compute the product $BC$. Multiplying the $3 \times 2$ matrix $B$ by the $2 \times 2$ matrix $C$ yields a $3 \times 2$ matrix:

$$
\begin{aligned}
BC &= \begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & -1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot2 + 0\cdot0) & (1\cdot1 + 0\cdot(-1)) \\
(2\cdot2 + 1\cdot0) & (2\cdot1 + 1\cdot(-1)) \\
(-1\cdot2 + 3\cdot0) & (-1\cdot1 + 3\cdot(-1)) \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 1 \\
4 & 1 \\
-2 & -4 \\
\end{pmatrix}
\end{aligned}
$$

Multiplications for $BC$: $3 \times 2 \times 2 = 12$.

Next, multiply $A$ by $BC$:

$$
\begin{aligned}
A(BC) &= \begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
4 & 1 \\
-2 & -4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(1\cdot2 + 2\cdot4 + 0\cdot(-2)) & (1\cdot1 + 2\cdot1 + 0\cdot(-4)) \\
(0\cdot2 + 1\cdot4 + 1\cdot(-2)) & (0\cdot1 + 1\cdot1 + 1\cdot(-4)) \\
\end{pmatrix} \\
&= \begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}
\end{aligned}
$$

Multiplications for $A(BC)$: $2 \times 3 \times 2 = 12$.

Total multiplications for Path 2: $12 + 12 = 24$.

**Step 3: Comparison and Explanation**

Both paths yield the identical $2 \times 2$ matrix:

$$
(AB)C = A(BC) = \begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}
$$

*Explanation:*
This verifies associativity of matrix multiplication: grouping factors differently does not affect the final mathematical result.

However, the computational cost differs between the two paths:
* Path 1, $(AB)C$, required **20** scalar multiplications.
* Path 2, $A(BC)$, required **24** scalar multiplications.

Associativity allows choosing the parenthesization that minimizes the total number of operations, which is the foundational principle of the matrix chain multiplication problem in algorithm design.

---

### Final Answer

Product matrix:

$$
(AB)C = A(BC) = \begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}
$$

Multiplication counts:
* Path 1: $(AB)C$ requires $12 + 8 = 20$ multiplications.
* Path 2: $A(BC)$ requires $12 + 12 = 24$ multiplications.
