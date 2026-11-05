### Essential Formulas

**Row Operation Invariance (Type III Row Operations):**
Adding any scalar multiple of one row to another row does not alter the value of the determinant:

$$
R_i \leftarrow R_i + c R_j \quad (i \neq j) \implies \det A' = \det A
$$

By strategically selecting $c$, this operation can be used systematically to introduce zeros into targeted positions, reducing the matrix to an upper triangular form without requiring sign adjustments or scalar division corrections.

**Determinant of an Upper Triangular Matrix:**
Once all entries below the main diagonal are reduced to zeros ($a_{ij} = 0$ for $i > j$), the determinant is simply the product of the diagonal elements:

$$
\det U = u_{11} \cdot u_{22} \cdots u_{nn}
$$

---

### Problem Statement

**Exercise 11. Shortening the Calculation with Row Operations**

Compute

$$
\det
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

by first performing row operations that create as many zeros as possible. State which operations do not change the determinant.

> **Why this exercise:** develops planning instead of mechanically repeating the same procedure.

---

### Solution

Let the given matrix be:

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

**Step 1: Create zeros in the first column**

Notice that the first column contains $1$ in every row. Using the pivot $a_{11} = 1$, eliminate the entries in row 2 and row 3:

* **Operation 1: $R_2 \leftarrow R_2 - R_1$**
  * *Effect on determinant:* Does not change the determinant ($\det A_1 = \det A$).
  * Calculation:

    $$
    R_2 = (1 - 1,\ 3 - 2,\ 4 - 3) = (0, 1, 1)
    $$

* **Operation 2: $R_3 \leftarrow R_3 - R_1$**
  * *Effect on determinant:* Does not change the determinant ($\det A_2 = \det A_1 = \det A$).
  * Calculation:

    $$
    R_3 = (1 - 1,\ 4 - 2,\ 6 - 3) = (0, 2, 3)
    $$

The matrix becomes:

$$
A_2 = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 2 & 3 \\
\end{pmatrix}
$$

**Step 2: Create a zero in the second column below the pivot**

Now use the pivot $a_{22} = 1$ in row 2 to eliminate the entry below it in row 3:

* **Operation 3: $R_3 \leftarrow R_3 - 2R_2$**
  * *Effect on determinant:* Does not change the determinant ($\det A_3 = \det A_2 = \det A$).
  * Calculation:

    $$
    R_3 = (0 - 2\cdot 0,\ 2 - 2\cdot 1,\ 3 - 2\cdot 1) = (0, 0, 1)
    $$

The matrix is now in upper triangular form:

$$
A_3 = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

**Step 3: State the operations and compute the determinant**

* **Operations that do not change the determinant:**
  All three operations performed:
  1. $R_2 \leftarrow R_2 - R_1$
  2. $R_3 \leftarrow R_3 - R_1$
  3. $R_3 \leftarrow R_3 - 2R_2$

  are elementary row operations of the form $R_i \leftarrow R_i + c R_j$ with $i \neq j$. None of these operations change the value of the determinant.

* **Compute $\det A_3$:**
  Because $A_3$ is upper triangular, its determinant is the product of its diagonal entries:

  $$
  \det A = \det A_3 = (1) \cdot (1) \cdot (1) = 1
  $$

**Step 4: Verification using Sarrus' rule**

Compute the determinant directly on the original matrix $A$:

* Downward diagonal products:

  $$
  (1)(3)(6) + (2)(4)(1) + (3)(1)(4) = 18 + 8 + 12 = 38
  $$

* Upward diagonal products:

  $$
  (3)(3)(1) + (1)(4)(4) + (2)(1)(6) = 9 + 16 + 12 = 37
  $$

* Difference:

  $$
  \det A = 38 - 37 = 1
  $$

The direct calculation verifies the result $\det A = 1$.

---

### Final Answer

Operations that do not change the determinant:

$$
R_2 \leftarrow R_2 - R_1, \qquad R_3 \leftarrow R_3 - R_1, \qquad R_3 \leftarrow R_3 - 2R_2
$$

All operations of the form $R_i \leftarrow R_i + c R_j$ ($i \neq j$) preserve the determinant.

Calculated determinant:

$$
\det \begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
= 1
$$