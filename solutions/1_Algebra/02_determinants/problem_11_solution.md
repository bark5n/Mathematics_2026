### Essential Formulas

**Determinant-Preserving Row Operations (Row Replacements):**
For any square matrix $A \in \mathbb{R}^{n \times n}$, adding a scalar multiple of one row to a different row ($R_i \leftarrow R_i + cR_j$ with $i \neq j$) leaves the determinant unchanged:

$$\det B = \det A$$

By contrast, interchanging two rows ($R_i \leftrightarrow R_j$) multiplies the determinant by $-1$, and scaling a row by $c \neq 0$ ($R_i \leftarrow cR_i$) multiplies the determinant by $c$.

**Determinant of a Triangular Matrix:**
For an upper triangular matrix $U = (u_{ij})$ ($u_{ij} = 0$ for all $i > j$) or a lower triangular matrix, the determinant equals the product of its main diagonal entries:

$$\det U = u_{11} u_{22} \cdots u_{nn}$$

**Cofactor Expansion Along a Row or Column:**
Expanding along row $i$ (or column $j$) simplifies dramatically when that row or column contains zeros:

$$\det A = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} \det M_{ij}$$

where $M_{ij}$ is the $(n-1) \times (n-1)$ submatrix formed by deleting row $i$ and column $j$.

---

### Problem Statement

**Exercise 11. Shortening the Calculation with Row Operations**

Compute

$$\det \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 4 \\ 1 & 4 & 6 \\ \end{pmatrix}$$

by first performing row operations that create as many zeros as possible. State which operations do not change the determinant.

> **Why this exercise:** develops planning instead of mechanically repeating the same procedure.

---

### Solution

**Step 1: State which row operations do not change the determinant**

Among the three elementary row operations, **row replacement operations** of the form

$$R_i \leftarrow R_i + cR_j \qquad (i \neq j, \; c \in \mathbb{R})$$

do not change the value of the determinant. Every operation used below is a row replacement, so the determinant remains invariant at every step.

**Step 2: Create zeros in the first column below the $(1, 1)$-pivot**

Denote the matrix by $A$:

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 4 \\ 1 & 4 & 6 \\ \end{pmatrix}$$

Apply two row replacements using row $1$ to eliminate the entries below $a_{11} = 1$:

1. $R_2 \leftarrow R_2 - R_1$: $(1, 3, 4) - (1, 2, 3) = (0, 1, 1)$
2. $R_3 \leftarrow R_3 - R_1$: $(1, 4, 6) - (1, 2, 3) = (0, 2, 3)$

This produces $A_1$ with two zeros in column $1$ and $\det A_1 = \det A$:

$$A_1 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 2 & 3 \\ \end{pmatrix}$$

**Step 3: Create a zero in the $(3, 2)$-position to reach upper triangular form**

Apply the row replacement $R_3 \leftarrow R_3 - 2R_2$ to $A_1$:

$$R_3 - 2R_2 = (0, 2, 3) - 2(0, 1, 1) = (0, 0, 1)$$

This produces the upper triangular matrix $U$ with three zeros below the main diagonal and $\det U = \det A$:

$$U = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \\ \end{pmatrix}$$

**Step 4: Eliminate above the main diagonal to maximize the number of zeros**

Applying upward row replacements preserves the determinant and clears the remaining nonzero off-diagonal entries:

1. $R_1 \leftarrow R_1 - 2R_2$: $(1, 2, 3) - 2(0, 1, 1) = (1, 0, 1)$
2. $R_1 \leftarrow R_1 - R_3$: $(1, 0, 1) - (0, 0, 1) = (1, 0, 0)$
3. $R_2 \leftarrow R_2 - R_3$: $(0, 1, 1) - (0, 0, 1) = (0, 1, 0)$

These three row replacements reduce the matrix to the $3 \times 3$ identity matrix $I_3$, which has six zeros (the maximum possible for an invertible $3 \times 3$ matrix):

$$I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ \end{pmatrix}$$

**Step 5: Read off the determinant**

Because every step was a determinant-preserving row replacement, the determinant equals the product of the main diagonal entries of $U$ (and of $I_3$):

$$\begin{aligned} \det A &= \det U \\ &= \det I_3 \\ &= 1 \cdot 1 \cdot 1 \\ &= 1 \end{aligned}$$

**Step 6: Verification**

* **Cofactor expansion along column $1$ of
