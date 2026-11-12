### Essential Formulas

**Matrix Multiplication Definition:**
For an $m \times p$ matrix $X$ and a $p \times n$ matrix $Y$, the product $XY$ is an $m \times n$ matrix whose $(i, j)$-entry is the dot product of the $i$-th row of $X$ and the $j$-th column of $Y$.

**Operation Count for Matrix Multiplication:**
Computing the product of an $m \times p$ matrix and a $p \times n$ matrix requires exactly $m \times n$ dot products. Each dot product of vectors of length $p$ requires $p$ scalar multiplications (and $p-1$ additions). Thus, the total number of scalar multiplications required is:

$$
\text{Number of multiplications} = m \cdot p \cdot n
$$

**Associativity of Matrix Multiplication:**
For any matrices $A, B, C$ with compatible dimensions (e.g., $A$ is $m \times p$, $B$ is $p \times q$, $C$ is $q \times n$), the order of grouping the multiplications does not change the final matrix result:

$$
(AB)C = A(BC)
$$

---

### Problem Statement

**Exercise 15. Associativity of Multiplication and Different Calculation Paths**

Given

$$
A=
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix},\quad B=
\begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix},\quad C=
\begin{pmatrix}
2 & 1 \\
0 & -1 \\
\end{pmatrix}.
$$

Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

> **Why this exercise:** reinforces associativity by comparing two mathematically equivalent calculation paths.

---

### Solution

**Step 1: Determine dimensions and set up paths**

* $A$ is $2 \times 3$.
* $B$ is $3 \times 2$.
* $C$ is $2 \times 2$.

Both paths $(AB)C$ and $A(BC)$ are valid and will produce a final $2 \times 2$ matrix.

**Step 2: Path 1 — Compute $(AB)C$**

First, compute $AB$ ($2 \times 3$ multiplied by $3 \times 2$ yields $2 \times 2$):

$$
\begin{aligned}
AB &=
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
1(1) + 2(2) + 0(-1) & 1(0) + 2(1) + 0(3) \\
0(1) + 1(2) + 1(-1) & 0(0) + 1(1) + 1(3) \\
\end{pmatrix} \\
&=
\begin{pmatrix}
1 + 4 + 0 & 0 + 2 + 0 \\
0 + 2 - 1 & 0 + 1 + 3 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
5 & 2 \\
1 & 4 \\
\end{pmatrix}
\end{aligned}
$$

Next, multiply $(AB)$ by $C$ ($2 \times 2$ multiplied by $2 \times 2$ yields $2 \times 2$):

$$
\begin{aligned}
(AB)C &=
\begin{pmatrix}
5 & 2 \\
1 & 4 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & -1 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
5(2) + 2(0) & 5(1) + 2(-1) \\
1(2) + 4(0) & 1(1) + 4(-1) \\
\end{pmatrix} \\
&=
\begin{pmatrix}
10 & 5 - 2 \\
2 & 1 - 4 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Path 2 — Compute $A(BC)$**

First, compute $BC$ ($3 \times 2$ multiplied by $2 \times 2$ yields $3 \times 2$):

$$
\begin{aligned}
BC &=
\begin{pmatrix}
1 & 0 \\
2 & 1 \\
-1 & 3 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & -1 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
1(2) + 0(0) & 1(1) + 0(-1) \\
2(2) + 1(0) & 2(1) + 1(-1) \\
-1(2) + 3(0) & -1(1) + 3(-1) \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2 & 1 \\
4 & 2 - 1 \\
-2 & -1 - 3 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2 & 1 \\
4 & 1 \\
-2 & -4 \\
\end{pmatrix}
\end{aligned}
$$

Next, multiply $A$ by $(BC)$ ($2 \times 3$ multiplied by $3 \times 2$ yields $2 \times 2$):

$$
\begin{aligned}
A(BC) &=
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
4 & 1 \\
-2 & -4 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
1(2) + 2(4) + 0(-2) & 1(1) + 2(1) + 0(-4) \\
0(2) + 1(4) + 1(-2) & 0(1) + 1(1) + 1(-4) \\
\end{pmatrix} \\
&=
\begin{pmatrix}
2 + 8 + 0 & 1 + 2 + 0 \\
0 + 4 - 2 & 0 + 1 - 4 \\
\end{pmatrix} \\
&=
\begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}
\end{aligned}
$$

**Step 4: Compare results, operation counts, and explain associativity**

* **Result comparison:** Both $(AB)C$ and $A(BC)$ yield the exact same final $2 \times 2$ matrix, confirming $(AB)C = A(BC)$.
* **Operation count comparison (counting scalar multiplications):**
  * **Path $(AB)C$:**
    1. Computing $AB$ ($2 \times 3$ by $3 \times 2$) requires $2 \cdot 3 \cdot 2 = 12$ multiplications.
    2. Computing $(AB)C$ ($2 \times 2$ by $2 \times 2$) requires $2 \cdot 2 \cdot 2 = 8$ multiplications.
    **Total for $(AB)C$:** $12 + 8 = \mathbf{20}$ multiplications.
  * **Path $A(BC)$:**
    1. Computing $BC$ ($3 \times 2$ by $2 \times 2$) requires $3 \cdot 2 \cdot 2 = 12$ multiplications.
    2. Computing $A(BC)$ ($2 \times 3$ by $3 \times 2$) requires $2 \cdot 3 \cdot 2 = 12$ multiplications.
    **Total for $A(BC)$:** $12 + 12 = \mathbf{24}$ multiplications.
* **Explanation of associativity:** Associativity of matrix multiplication means that while the **final result is guaranteed to be mathematically identical** regardless of grouping (as verified by the identical $10, 3, 2, -3$ entries), the **computational cost** (number of intermediate arithmetic operations) can differ significantly depending on the path chosen. Here, computing $(AB)$ first is structurally more efficient (by $4$ multiplications) because it collapses the wide inner dimensions early, creating smaller intermediate matrices.

---

### Final Answer

1. **Both calculation paths yield the same final matrix:**

$$
(AB)C = A(BC) =
\begin{pmatrix}
10 & 3 \\
2 & -3 \\
\end{pmatrix}
$$

2. **Operation counts:**
   * Path $(AB)C$ requires $12 + 8 = \mathbf{20}$ scalar multiplications.
   * Path $A(BC)$ requires $12 + 12 = \mathbf{24}$ scalar multiplications.
3. **What associativity means here:** Associativity guarantees that grouping $(AB)$ or $(BC)$ first has absolutely no effect on the final numerical result. However, it shows that the chosen order changes the sizes of intermediate matrices, making the first path ($20$ operations) computationally cheaper than the second ($24$ operations) without altering the outcome[cite: 3, 4].
