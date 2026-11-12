### Essential Formulas

**Associativity of Matrix Multiplication:**
Let $A \in \mathbb{R}^{m \times n}$, $B \in \mathbb{R}^{n \times p}$, and $C \in \mathbb{R}^{p \times q}$ be matrices with compatible inner dimensions. Matrix multiplication is associative:

$$(AB)C = A(BC)$$

Both groupings yield the exact same $m \times q$ matrix, allowing the triple product to be written unambiguously as $ABC$.

**Operation Count for Matrix Multiplication:**
Multiplying a matrix $X \in \mathbb{R}^{m \times n}$ by a matrix $Y \in \mathbb{R}^{n \times p}$ produces $mp$ entries, where each entry is the dot product of two vectors of length $n$:

* Number of scalar multiplications: $mnp$
* Number of scalar additions: $mp(n - 1)$
* Total scalar arithmetic operations: $mp(2n - 1)$

Although $(AB)C$ and $A(BC)$ produce identical matrices, different parenthesizations can require different numbers of intermediate arithmetic operations.

---

### Problem Statement

**Exercise 15. Associativity of Multiplication and Different Calculation Paths**

Given

$$A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \\ \end{pmatrix}, \quad C = \begin{pmatrix} 2 & 1 \\ 0 & -1 \\ \end{pmatrix}.$$

Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

> **Why this exercise:** reinforces associativity by comparing two mathematically equivalent calculation paths.

---

### Solution

**Step 1: Check dimensions and compute $(AB)C$**

The matrix dimensions are $A_{2 \times 3}$, $B_{3 \times 2}$, and $C_{2 \times 2}$.

1. **Compute $AB$ ($2 \times 3$ multiplied by $3 \times 2$):**
   The intermediate product $AB$ has size $2 \times 2$:

$$\begin{aligned} AB &= \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \\ \end{pmatrix} \\ &= \begin{pmatrix} 1 \cdot 1 + 2 \cdot 2 + 0 \cdot (-1) & 1 \cdot 0 + 2 \cdot 1 + 0 \cdot 3 \\ 0 \cdot 1 + 1 \cdot 2 + 1 \cdot (-1) & 0 \cdot 0 + 1 \cdot 1 + 1 \cdot 3 \\ \end{pmatrix} \\ &= \begin{pmatrix} 1 + 4 + 0 & 0 + 2 + 0 \\ 0 + 2 - 1 & 0 + 1 + 3 \\ \end{pmatrix} \\ &= \begin{pmatrix} 5 & 2 \\ 1 & 4 \\ \end{pmatrix} \end{aligned}$$

   * Operation count for $AB$: $2 \times 2 = 4$ entries, each using $3$ multiplications and $2$ additions, giving $12$ multiplications and $8$ additions ($20$ operations).

2. **Compute $(AB)C$ ($2 \times 2$ multiplied by $2 \times 2$):**
   Multiply $AB$ on the right by $C$:

$$\begin{aligned} (AB)C &= \begin{pmatrix} 5 & 2 \\ 1 & 4 \\ \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & -1 \\ \end{pmatrix} \\ &= \begin{pmatrix} 5 \cdot 2 + 2 \cdot 0 & 5 \cdot 1 + 2 \cdot (-1) \\ 1 \cdot 2 + 4 \cdot 0 & 1 \cdot 1 + 4 \cdot (-1) \\ \end{pmatrix} \\ &= \begin{pmatrix} 10 + 0 & 5 - 2 \\ 2 + 0 & 1 - 4 \\ \end{pmatrix} \\ &= \begin{pmatrix} 10 & 3 \\ 2 & -3 \\ \end{pmatrix} \end{aligned}$$

   * Operation count for $(AB)C$: $2 \times 2 = 4$ entries, each using $2$ multiplications and $1$ addition, giving $8$ multiplications and $4$ additions ($12$ operations).

* **Total operations for $(AB)C$:** $12 + 8 = 20$ multiplications and $8 + 4 = 12$ additions, for a total of $32$ arithmetic operations.

**Step 2: Compute $A(BC)$**

1. **Compute $BC$ ($3 \times 2$ multiplied by $2 \times 2$):**
   The intermediate product $BC$ has size $3 \times 2$:

$$\begin{aligned} BC &= \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \\ \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & -1 \\ \end{pmatrix} \\ &= \begin{pmatrix} 1 \cdot 2 + 0 \cdot 0 & 1 \cdot 1 + 0 \cdot (-1) \\ 2 \cdot 2 + 1 \cdot 0 & 2 \cdot 1 + 1 \cdot (-1) \\ (-1) \cdot 2 + 3 \cdot 0 & (-1) \cdot 1 + 3 \cdot (-1) \\ \end{pmatrix} \\ &= \begin{pmatrix} 2 + 0 & 1 + 0 \\ 4 + 0 & 2 - 1 \\ -2 + 0 & -1 - 3 \\ \end{pmatrix} \\ &= \begin{pmatrix} 2 & 1 \\ 4 & 1 \\ -2 & -4 \\ \end{pmatrix} \end{aligned}$$

   * Operation count
