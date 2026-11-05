### Essential Formulas

**Sarrus' Rule for $3 \times 3$ Determinants:**
For any $3 \times 3$ matrix, the determinant can be evaluated by summing the products along the three primary downward diagonals and subtracting the products along the three upward (anti-) diagonals:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{pmatrix}
$$

$$
\det A = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}
$$

**Laplace (Cofactor) Expansion:**
The determinant can also be computed by expanding along any row $i$ or column $j$:

$$
\det A = \sum_{k=1}^n (-1)^{k+j} a_{kj} \det M_{kj}
$$

where $M_{kj}$ is the $(n-1) \times (n-1)$ submatrix obtained by deleting row $k$ and column $j$.

---

### Problem Statement

**Exercise 2. Determinant of a 3×3 Matrix**

For

$$
A = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 4 \\
2 & 1 & 5 \\
\end{pmatrix}
$$

compute $\det A$ using Sarrus' rule. Then perform one simple check using a chosen property of the determinant.

> **Why this exercise:** teaches a basic method for $3\times3$ matrices and builds the habit of checking the result without adding a second full solution.

---

### Solution

**Step 1: Compute $\det A$ using Sarrus' rule**

Write down the three positive diagonal products:

1. Main diagonal:

   $$
   (1) \cdot (3) \cdot (5) = 15
   $$

2. Second diagonal:

   $$
   (2) \cdot (4) \cdot (2) = 16
   $$

3. Third diagonal:

   $$
   (-1) \cdot (0) \cdot (1) = 0
   $$

Sum of the positive diagonal products:

$$
15 + 16 + 0 = 31
$$

Write down the three negative anti-diagonal products:

1. First anti-diagonal:

   $$
   (-1) \cdot (3) \cdot (2) = -6
   $$

2. Second anti-diagonal:

   $$
   (1) \cdot (4) \cdot (1) = 4
   $$

3. Third anti-diagonal:

   $$
   (2) \cdot (0) \cdot (5) = 0
   $$

Sum of the negative anti-diagonal products:

$$
(-6) + 4 + 0 = -2
$$

Subtract the anti-diagonal sum from the main diagonal sum:

$$
\det A = 31 - (-2) = 31 + 2 = 33
$$

**Step 2: Verification using cofactor expansion**

To verify the result simply without repeating the full computation, expand along the first column of $A$, which contains an advantageous zero ($a_{21} = 0$):

$$
\det A = a_{11} C_{11} + a_{21} C_{21} + a_{31} C_{31}
$$

$$
\det A = 1 \cdot \det \begin{pmatrix}
3 & 4 \\
1 & 5 \\
\end{pmatrix}
- 0 \cdot \det \begin{pmatrix}
2 & -1 \\
1 & 5 \\
\end{pmatrix}
+ 2 \cdot \det \begin{pmatrix}
2 & -1 \\
3 & 4 \\
\end{pmatrix}
$$

Evaluate each $2 \times 2$ minor:

$$
\det \begin{pmatrix}
3 & 4 \\
1 & 5 \\
\end{pmatrix}
= (3)(5) - (4)(1) = 15 - 4 = 11
$$

$$
\det \begin{pmatrix}
2 & -1 \\
3 & 4 \\
\end{pmatrix}
= (2)(4) - (-1)(3) = 8 + 3 = 11
$$

Substitute these values back into the expansion:

$$
\det A = 1 \cdot (11) + 2 \cdot (11) = 11 + 22 = 33
$$

Both methods yield $33$, confirming the calculation.

---

### Final Answer

$$
\det A = 33
$$