### Essential Formulas

**Sarrus' Rule for a $3 \times 3$ Matrix:**
For a matrix

$$
A = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i \\
\end{pmatrix}
$$

the determinant is calculated by taking the sum of the products of the three downward diagonals minus the sum of the products of the three upward diagonals:

$$
\det A = aei + bfg + cdh - ceg - afh - bdi
$$

**Laplace Expansion (Cofactor Expansion):**
The determinant can also be computed along any row or column. Expanding along column $j$:

$$
\det A = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}
$$

where $M_{ij}$ is the minor determinant formed by deleting row $i$ and column $j$.

---

### Problem Statement

**Exercise 2. Determinant of a 3×3 Matrix**

For

$$
A=
\begin{pmatrix}
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

Write down the $3 \times 3$ matrix $A$:

$$
A =
\begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 4 \\
2 & 1 & 5 \\
\end{pmatrix}
$$

Augment the matrix by repeating the first two columns to the right:

$$
\begin{pmatrix}
1 & 2 & -1 & 1 & 2 \\
0 & 3 & 4 & 0 & 3 \\
2 & 1 & 5 & 2 & 1 \\
\end{pmatrix}
$$

Compute the three downward diagonal products:
1. First diagonal: $1 \cdot 3 \cdot 5 = 15$
2. Second diagonal: $2 \cdot 4 \cdot 2 = 16$
3. Third diagonal: $(-1) \cdot 0 \cdot 1 = 0$

Sum of downward products: $15 + 16 + 0 = 31$.

Compute the three upward diagonal products:
1. First upward diagonal: $2 \cdot 3 \cdot (-1) = -6$
2. Second upward diagonal: $1 \cdot 4 \cdot 1 = 4$
3. Third upward diagonal: $5 \cdot 0 \cdot 2 = 0$

Sum of upward products: $-6 + 4 + 0 = -2$.

Subtract the upward sum from the downward sum:

$$
\begin{aligned}
\det A &= (15 + 16 + 0) - (-6 + 4 + 0) \\
&= 31 - (-2) \\
&= 31 + 2 \\
&= 33
\end{aligned}
$$

**Step 2: Verification using Laplace expansion along column 1**

To verify the result using a determinant property, expand along the first column of $A$, which has an advantageous entry of $0$:

$$
c_1 = \begin{pmatrix}
1 \\
0 \\
2 \\
\end{pmatrix}
$$

Expanding along column 1:

$$
\begin{aligned}
\det A &= (-1)^{1+1} (1) \det \begin{pmatrix}
3 & 4 \\
1 & 5 \\
\end{pmatrix}
+ (-1)^{2+1} (0) \det \begin{pmatrix}
2 & -1 \\
1 & 5 \\
\end{pmatrix}
+ (-1)^{3+1} (2) \det \begin{pmatrix}
2 & -1 \\
3 & 4 \\
\end{pmatrix} \\
&= 1 \cdot (3 \cdot 5 - 4 \cdot 1) - 0 + 2 \cdot (2 \cdot 4 - (-1) \cdot 3) \\
&= 1 \cdot (15 - 4) + 2 \cdot (8 + 3) \\
&= 11 + 2(11) \\
&= 11 + 22 \\
&= 33
\end{aligned}
$$

Both methods yield $33$, confirming the result.

---

### Final Answer

$$
\det A = 33
$$
