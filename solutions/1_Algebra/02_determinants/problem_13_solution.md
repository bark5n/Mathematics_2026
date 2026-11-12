### Essential Formulas

**Determinant via Gaussian Elimination:**
To compute $\det A$ for a square matrix $A \in \mathbb{R}^{n \times n}$, apply elementary row operations to reduce $A$ to an upper triangular (row echelon) matrix $U$ while tracking how each operation modifies the determinant:

1. **Row replacement ($R_i \leftarrow R_i + cR_j$ for $i \neq j$):** Leaves the determinant unchanged ($\det B = \det A$).
2. **Row interchange ($R_i \leftrightarrow R_j$ for $i \neq j$):** Multiplies the determinant by $-1$ ($\det B = -\det A$).
3. **Row scaling ($R_i \leftarrow cR_i$ for $c \neq 0$):** Multiplies the determinant by $c$ ($\det B = c \det A$).

**Determinant of an Upper Triangular Matrix:**
If $U = (u_{ij})$ is upper triangular ($u_{ij} = 0$ for all $i > j$), its determinant equals the product of its main diagonal (pivot) entries:

$$
\det U = u_{11} u_{22} \cdots u_{nn}
$$

If $r$ row interchanges and no row scalings are used to reduce $A$ to $U$, then:

$$
\det A = (-1)^r u_{11} u_{22} \cdots u_{nn}
$$

---

### Problem Statement

**Exercise 13. Determinant by Elimination**

Compute the determinant

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

using elimination. Record the effect of every row operation used on the value of the determinant.

> **Why this exercise:** reinforces organizing a determinant calculation through row operations without introducing an unnecessary second procedure.

---

### Solution

**Step 1: Eliminate the $(2, 1)$-entry below the first pivot**

Use the first pivot $a_{11} = 1$ and apply the row replacement $R_2 \leftarrow R_2 - 2R_1$:

$$
R_2 - 2R_1 = (2, 5, 7) - 2(1, 2, 3) = (2 - 2, 5 - 4, 7 - 6) = (0, 1, 1)
$$

This produces the matrix $A_1$:

$$
A_1 = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

* **Effect on the determinant:** $R_2 \leftarrow R_2 - 2R_1$ is a row replacement operation, so the determinant does not change:

$$
\det A_1 = \det A
$$

**Step 2: Eliminate the $(3, 1)$-entry below the first pivot**

Apply the row replacement $R_3 \leftarrow R_3 - R_1$ to $A_1$:

$$
R_3 - R_1 = (1, 0, 2) - (1, 2, 3) = (1 - 1, 0 - 2, 2 - 3) = (0, -2, -1)
$$

This produces the matrix $A_2$:

$$
A_2 = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & -2 & -1 \\
\end{pmatrix}
$$

* **Effect on the determinant:** $R_3 \leftarrow R_3 - R_1$ is a row replacement operation, so the determinant remains unchanged:

$$
\det A_2 = \det A_1 = \det A
$$

**Step 3: Eliminate the $(3, 2)$-entry below the second pivot**

Using the second pivot $1$ in position $(2, 2)$, apply the row replacement $R_3 \leftarrow R_3 + 2R_2$ to $A_2$:

$$
R_3 + 2R_2 = (0, -2, -1) + 2(0, 1, 1) = (0, -2 + 2, -1 + 2) = (0, 0, 1)
$$

This yields the upper triangular matrix $U$:

$$
U = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

* **Effect on the determinant:** $R_3 \leftarrow R_3 + 2R_2$ is also a row replacement operation, so the determinant again remains unchanged:

$$
\det U = \det A_2 = \det A
$$

**Step 4: Compute $\det A$ from the upper triangular matrix $U$**

Because every operation preserved the determinant and $U$ is upper triangular with diagonal entries $u_{11} = 1$, $u_{22} = 1$, and $u_{33} = 1$, multiply the main diagonal entries together:

$$
\begin{aligned}
\det A &= \det U \\
&= 1 \cdot 1 \cdot 1 \\
&= 1
\end{aligned}
$$

**Step 5: Verification**

* **Sarrus' rule check on $A$:**
  * Downward diagonal products:

$$
S_+ = 1 \cdot 5 \cdot 2 + 2 \cdot 7 \cdot 1 + 3 \cdot 2 \cdot 0 = 10 + 14 + 0 = 24
$$

  * Upward diagonal products:

$$
S_- = 1 \cdot 5 \cdot 3 + 0 \cdot 7 \cdot 1 + 2 \cdot 2 \cdot 2 = 15 + 0 + 8 = 23
$$

  * Difference: $\det A = S_+ - S_- = 24 - 23 = 1$.

* **Cofactor expansion check along row $3$:**
  Since $a_{32} = 0$, expanding along row $3$ uses only two $2 \times 2$ minors:

$$
\begin{aligned}
\det A &= 1 \det \begin{pmatrix}
2 & 3 \\
5 & 7 \\
\end{pmatrix}
- 0 + 2 \det \begin{pmatrix}
1 & 2 \\
2 & 5 \\
\end{pmatrix} \\
&= 1(2 \cdot 7 - 3 \cdot 5) + 2(1 \cdot 5 - 2 \cdot 2) \\
&= 1(14 - 15) + 2(5 - 4) \\
&= -1 + 2 \\
&= 1
\end{aligned}
$$

Both independent methods confirm $\det A = 1$.

---

### Final Answer

1. **Determinant of $A$:**

$$
\det A = 1
$$

2. **Record of elimination steps and their effect on the determinant:**
   * Step 1 ($R_2 \leftarrow R_2 - 2R_1$): row replacement; no change in determinant ($\det A_1 = \det A$).
   * Step 2 ($R_3 \leftarrow R_3 - R_1$): row replacement; no change in determinant ($\det A_2 = \det A$).
   * Step 3 ($R_3 \leftarrow R_3 + 2R_2$): row replacement; no change in determinant ($\det U = \det A$).
   * Step 4: $U$ is upper triangular with diagonal entries $1$, $1$, and $1$, giving $\det A = 1 \cdot 1 \cdot 1 = 1$.
