### Essential Formulas

**Effect of Elementary Row Operations on Determinants:**
Let $A \in \mathbb{R}^{n \times n}$ be a square matrix and $B$ be the matrix obtained after applying a single elementary row operation:

1. **Row replacement ($R_i \leftarrow R_i + cR_j$ for $i \neq j$):** Adding a scalar multiple of one row to another row leaves the determinant unchanged:

$$
\det B = \det A
$$

2. **Row interchange ($R_i \leftrightarrow R_j$ for $i \neq j$):** Swapping two distinct rows multiplies the determinant by $-1$:

$$
\det B = -\det A
$$

3. **Row scaling ($R_i \leftarrow cR_i$ for $c \neq 0$):** Multiplying a single row by a nonzero scalar $c$ multiplies the determinant by $c$:

$$
\det B = c \det A
$$

**Determinant of an Upper Triangular Matrix:**
If $U = (u_{ij})$ is an $n \times n$ upper triangular matrix ($u_{ij} = 0$ for all $i > j$), its determinant is the product of its main diagonal entries:

$$
\det U = u_{11} u_{22} \cdots u_{nn}
$$

---

### Problem Statement

**Exercise 5. Row Operations**

For

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 0 \\
-1 & 4 & 2 \\
\end{pmatrix}
$$

find $\det A$ by simplifying the matrix with row operations. At each step, indicate whether and how the determinant changes.

> **Why this exercise:** connects determinants with row operations and requires conscious tracking of every step.

---

### Solution

**Step 1: Eliminate the $(2, 1)$-entry using $R_2 \leftarrow R_2 - 2R_1$**

Use the pivot $a_{11} = 1$ to create a zero in the $(2, 1)$-position by subtracting $2$ times row $1$ from row $2$:

$$
R_2 - 2R_1 = (2, 1, 0) - 2(1, 2, 3) = (2 - 2, 1 - 4, 0 - 6) = (0, -3, -6)
$$

The resulting matrix is:

$$
A_1 = \begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
-1 & 4 & 2 \\
\end{pmatrix}
$$

* **Effect on determinant:** Because $R_2 \leftarrow R_2 - 2R_1$ is a row replacement operation, the value of the determinant does not change:

$$
\det A_1 = \det A
$$

**Step 2: Eliminate the $(3, 1)$-entry using $R_3 \leftarrow R_3 + R_1$**

Create a zero in the $(3, 1)$-position by adding row $1$ to row $3$:

$$
R_3 + R_1 = (-1, 4, 2) + (1, 2, 3) = (-1 + 1, 4 + 2, 2 + 3) = (0, 6, 5)
$$

The resulting matrix is:

$$
A_2 = \begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 6 & 5 \\
\end{pmatrix}
$$

* **Effect on determinant:** Because $R_3 \leftarrow R_3 + R_1$ is a row replacement operation, the value of the determinant remains unchanged:

$$
\det A_2 = \det A_1 = \det A
$$

**Step 3: Eliminate the $(3, 2)$-entry using $R_3 \leftarrow R_3 + 2R_2$**

Use the $(2, 2)$-entry $-3$ as the second pivot to create a zero in the $(3, 2)$-position by adding $2$ times row $2$ to row $3$:

$$
R_3 + 2R_2 = (0, 6, 5) + 2(0, -3, -6) = (0, 6 - 6, 5 - 12) = (0, 0, -7)
$$

The resulting matrix is upper triangular:

$$
U = \begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 0 & -7 \\
\end{pmatrix}
$$

* **Effect on determinant:** Because $R_3 \leftarrow R_3 + 2R_2$ is also a row replacement operation, the determinant again remains unchanged:

$$
\det U = \det A_2 = \det A
$$

**Step 4: Compute $\det U$ from its upper triangular form**

Since $U$ is upper triangular, its determinant equals the product of its main diagonal entries $u_{11} = 1$, $u_{22} = -3$, and $u_{33} = -7$:

$$
\begin{aligned}
\det A &= \det U \\
&= 1 \cdot (-3) \cdot (-7) \\
&= 21
\end{aligned}
$$

**Step 5: Verification**

* **Sarrus' rule check on $A$:**
  * Downward diagonal products:

$$
S_+ = 1 \cdot 1 \cdot 2 + 2 \cdot 0 \cdot (-1) + 3 \cdot 2 \cdot 4 = 2 + 0 + 24 = 26
$$

  * Upward diagonal products:

$$
S_- = (-1) \cdot 1 \cdot 3 + 4 \cdot 0 \cdot 1 + 2 \cdot 2 \cdot 2 = -3 + 0 + 8 = 5
$$

  * Subtracting gives $\det A = S_+ - S_- = 26 - 5 = 21$.

* **Cofactor expansion check along row $2$:**
  Since $a_{23} = 0$, expanding along row $2$ requires only two $2 \times 2$ minors:

$$
\begin{aligned}
\det A &= -2 \det \begin{pmatrix}
2 & 3 \\
4 & 2 \\
\end{pmatrix}
+ 1 \det \begin{pmatrix}
1 & 3 \\
-1 & 2 \\
\end{pmatrix}
- 0 \\
&= -2(2 \cdot 2 - 3 \cdot 4) + 1(1 \cdot 2 - 3 \cdot (-1)) \\
&= -2(-8) + 5 \\
&= 21
\end{aligned}
$$

Both independent calculations confirm $\det A = 21$.

---

### Final Answer

1. **Determinant of $A$:**

$$
\det A = 21
$$

2. **Summary of row operations and determinant tracking:**
   * $R_2 \leftarrow R_2 - 2R_1$: row replacement; determinant does not change ($\det A_1 = \det A$).
   * $R_3 \leftarrow R_3 + R_1$: row replacement; determinant does not change ($\det A_2 = \det A$).
   * $R_3 \leftarrow R_3 + 2R_2$: row replacement; determinant does not change ($\det U = \det A$).
   * Evaluating the resulting upper triangular matrix $U$ gives $\det A = 1 \cdot (-3) \cdot (-7) = 21$.
