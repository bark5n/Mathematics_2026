### Essential Formulas

**Effects of Elementary Row Operations on the Determinant:**
Let $A$ be a square matrix.

1. **Row Addition ($R_i \leftarrow R_i + c R_j$ with $i \neq j$):**
   Adding a scalar multiple of one row to another row does not change the determinant:

   $$
   \det A' = \det A
   $$

2. **Row Swap ($R_i \leftrightarrow R_j$):**
   Exchanging two rows reverses the sign of the determinant:

   $$
   \det A' = -\det A
   $$

3. **Scalar Multiplication ($R_i \leftarrow c R_i$):**
   Multiplying a row by a non-zero scalar $c$ scales the determinant by $c$:

   $$
   \det A' = c \cdot \det A \implies \det A = \frac{1}{c} \det A'
   $$

**Determinant of an Upper Triangular Matrix:**
When a matrix is brought to upper triangular form $U$, its determinant is the product of its diagonal entries:

$$
\det U = u_{11} \cdot u_{22} \cdots u_{nn}
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

**Step 1: Eliminate entries in the first column below the pivot**

The initial matrix is:

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 0 \\
-1 & 4 & 2 \\
\end{pmatrix}
$$

* **Operation 1: $R_2 \leftarrow R_2 - 2R_1$**
  * *Effect on determinant:* Adding a multiple of row 1 to row 2 does not change the determinant ($\det A_1 = \det A$).
  * Computation:

    $$
    R_2 = (2 - 2\cdot 1,\ 1 - 2\cdot 2,\ 0 - 2\cdot 3) = (0, -3, -6)
    $$

* **Operation 2: $R_3 \leftarrow R_3 + R_1$**
  * *Effect on determinant:* Adding row 1 to row 3 does not change the determinant ($\det A_2 = \det A_1 = \det A$).
  * Computation:

    $$
    R_3 = (-1 + 1,\ 4 + 2,\ 2 + 3) = (0, 6, 5)
    $$

The matrix becomes:

$$
A_2 = \begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 6 & 5 \\
\end{pmatrix}
$$

At this stage, $\det A = \det A_2$.

**Step 2: Eliminate the entry in the second column below the pivot**

* **Operation 3: $R_3 \leftarrow R_3 + 2R_2$**
  * *Effect on determinant:* Adding $2$ times row 2 to row 3 does not change the determinant ($\det A_3 = \det A_2 = \det A$).
  * Computation:

    $$
    R_3 = (0 + 2\cdot 0,\ 6 + 2(-3),\ 5 + 2(-6)) = (0, 0, -7)
    $$

The matrix is now in upper triangular form:

$$
A_3 = \begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 0 & -7 \\
\end{pmatrix}
$$

**Step 3: Compute the determinant of the upper triangular matrix**

Because all operations used were of the form $R_i \leftarrow R_i + c R_j$, the determinant remained strictly invariant across every step:

$$
\det A = \det A_3
$$

Since $A_3$ is upper triangular, its determinant is the product of the main diagonal elements:

$$
\det A_3 = (1) \cdot (-3) \cdot (-7) = 21
$$

Therefore:

$$
\det A = 21
$$

**Step 4: Verification using Sarrus' rule**

Compute $\det A$ directly from the original matrix using Sarrus' rule:

Downward diagonal products:

$$
(1)(1)(2) + (2)(0)(-1) + (3)(2)(4) = 2 + 0 + 24 = 26
$$

Upward diagonal products:

$$
(3)(1)(-1) + (1)(0)(4) + (2)(2)(2) = -3 + 0 + 8 = 5
$$

Subtract upward sum from downward sum:

$$
\det A = 26 - 5 = 21
$$

Both methods yield $21$, confirming the result and the tracking of row operations.

---

### Final Answer

$$
\det A = 21
$$