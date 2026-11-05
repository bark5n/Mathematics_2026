### Essential Formulas

**Gaussian Elimination and the Determinant:**
Gaussian elimination transforms a matrix into an upper triangular form $U$ via elementary row operations. The determinant of the original matrix $A$ is tracked by recording the effect of each operation:

1. **Row Addition ($R_i \leftarrow R_i + c R_j$ with $i \neq j$):**

   $$
   \det A' = \det A
   $$

   The determinant is strictly unchanged.

2. **Row Swap ($R_i \leftrightarrow R_j$):**

   $$
   \det A' = -\det A \implies \det A = -\det A'
   $$

   Each row swap negates the determinant.

3. **Row Scaling ($R_i \leftarrow c R_i$ with $c \neq 0$):**

   $$
   \det A' = c \det A \implies \det A = \frac{1}{c} \det A'
   $$

**Determinant of an Upper Triangular Matrix:**
Once reduced to upper triangular form $U$, the determinant equals the product of the diagonal elements:

$$
\det U = u_{11} \cdot u_{22} \cdots u_{nn}
$$

---

### Problem Statement

**Exercise 13. Determinant by Elimination**

Compute the determinant

$$
A=
\begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

using elimination. Record the effect of every row operation used on the value of the determinant.

> **Why this exercise:** reinforces organizing a determinant calculation through row operations without introducing an unnecessary second procedure.

---

### Solution

The given matrix is:

$$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

**Step 1: Eliminate entries in the first column below the pivot $a_{11} = 1$**

* **Operation 1: $R_2 \leftarrow R_2 - 2R_1$**
  * *Effect on determinant:* Adding a multiple of row 1 to row 2 does not change the determinant ($\det A_1 = \det A$).
  * Calculation:

    $$
    R_2 = (2 - 2\cdot 1,\ 5 - 2\cdot 2,\ 7 - 2\cdot 3) = (0, 1, 1)
    $$

* **Operation 2: $R_3 \leftarrow R_3 - R_1$**
  * *Effect on determinant:* Adding a multiple of row 1 to row 3 does not change the determinant ($\det A_2 = \det A_1 = \det A$).
  * Calculation:

    $$
    R_3 = (1 - 1,\ 0 - 2,\ 2 - 3) = (0, -2, -1)
    $$

After these two operations, the matrix is:

$$
A_2 = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & -2 & -1 \\
\end{pmatrix}
$$

**Step 2: Eliminate the entry in the second column below the pivot $a_{22} = 1$**

* **Operation 3: $R_3 \leftarrow R_3 + 2R_2$**
  * *Effect on determinant:* Adding a multiple of row 2 to row 3 does not change the determinant ($\det A_3 = \det A_2 = \det A$).
  * Calculation:

    $$
    R_3 = (0 + 2\cdot 0,\ -2 + 2\cdot 1,\ -1 + 2\cdot 1) = (0, 0, 1)
    $$

The matrix is now in upper triangular form $U$:

$$
U = A_3 = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

**Step 3: Record cumulative effects and calculate the determinant**

Tracking each row operation:
1. $R_2 \leftarrow R_2 - 2R_1$: Multiplier on determinant is $1$.
2. $R_3 \leftarrow R_3 - R_1$: Multiplier on determinant is $1$.
3. $R_3 \leftarrow R_3 + 2R_2$: Multiplier on determinant is $1$.

Since all operations performed were row additions, the determinant remained invariant throughout the entire elimination:

$$
\det A = \det U
$$

Compute the determinant of the upper triangular matrix $U$ by taking the product of its main diagonal entries:

$$
\det U = u_{11} \cdot u_{22} \cdot u_{33} = (1) \cdot (1) \cdot (1) = 1
$$

Therefore:

$$
\det A = 1
$$

**Step 4: Verification using Sarrus' rule**

Compute the determinant directly on the original matrix $A$:

* Downward diagonal products:

  $$
  (1)(5)(2) + (2)(7)(1) + (3)(2)(0) = 10 + 14 + 0 = 24
  $$

* Upward diagonal products:

  $$
  (3)(5)(1) + (1)(7)(0) + (2)(2)(2) = 15 + 0 + 8 = 23
  $$

* Difference:

  $$
  \det A = 24 - 23 = 1
  $$

The calculation confirms $\det A = 1$.

---

### Final Answer

Record of row operations:
* $R_2 \leftarrow R_2 - 2R_1$: Determinant unchanged ($\times 1$)
* $R_3 \leftarrow R_3 - R_1$: Determinant unchanged ($\times 1$)
* $R_3 \leftarrow R_3 + 2R_2$: Determinant unchanged ($\times 1$)

Calculated determinant:

$$
\det \begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 7 \\
1 & 0 & 2 \\
\end{pmatrix}
= 1
$$