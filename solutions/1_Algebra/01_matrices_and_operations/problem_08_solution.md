### Essential Formulas

**Elementary Row Operations:**
Given a matrix $A \in \mathbb{R}^{m \times n}$ with rows $R_1, R_2, \ldots, R_m$, the three elementary row operations are:

1. **Row replacement (row addition):** Add a scalar multiple $c \in \mathbb{R}$ of row $j$ to row $i$ ($i \neq j$):

$$
R_i \leftarrow R_i + cR_j
$$

2. **Row interchange (row swap):** Exchange row $i$ and row $j$:

$$
R_i \leftrightarrow R_j
$$

3. **Row scaling:** Multiply row $i$ by a nonzero scalar $c \neq 0$:

$$
R_i \leftarrow cR_i
$$

**Inverse Elementary Row Operations:**
Every elementary row operation is reversible by applying a single inverse elementary row operation of the same type:

* The inverse of $R_i \leftarrow R_i + cR_j$ ($i \neq j$) is:

$$
R_i \leftarrow R_i - cR_j
$$

* The inverse of $R_i \leftrightarrow R_j$ is the same interchange:

$$
R_i \leftrightarrow R_j
$$

* The inverse of $R_i \leftarrow cR_i$ ($c \neq 0$) is:

$$
R_i \leftarrow \frac{1}{c}R_i
$$

---

### Problem Statement

**Exercise 8. Row Operations and Their Reversibility**

For

$$
A = \begin{pmatrix}
1 & 2 & -1 \\
2 & 4 & 1 \\
-1 & 1 & 3 \\
\end{pmatrix}
$$

perform, in order:

1. $R_2 \leftarrow R_2 - 2R_1$,
2. $R_3 \leftarrow R_3 + R_1$,
3. interchange $R_2$ and $R_3$.

Write the matrix after each step. Then, for each of the three operations, state an operation that reverses it.

> **Why this exercise:** prepares for elimination by showing that row operations are controlled and reversible transformations of a matrix.

---

### Solution

**Step 1: Perform operation 1 ($R_2 \leftarrow R_2 - 2R_1$)**

Subtract $2$ times row $1$ from row $2$, leaving rows $1$ and $3$ unchanged:

$$
R_2 - 2R_1 = (2, 4, 1) - 2(1, 2, -1) = (2 - 2, 4 - 4, 1 - (-2)) = (0, 0, 3)
$$

The resulting matrix $A_1$ is:

$$
A_1 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix}
$$

**Step 2: Perform operation 2 ($R_3 \leftarrow R_3 + R_1$)**

Apply the second operation to $A_1$ by adding row $1$ to row $3$, leaving rows $1$ and $2$ unchanged:

$$
R_3 + R_1 = (-1, 1, 3) + (1, 2, -1) = (-1 + 1, 1 + 2, 3 + (-1)) = (0, 3, 2)
$$

The resulting matrix $A_2$ is:

$$
A_2 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix}
$$

**Step 3: Perform operation 3 (interchange $R_2$ and $R_3$)**

Exchange row $2$ and row $3$ of $A_2$, leaving row $1$ unchanged:

$$
A_3 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3 \\
\end{pmatrix}
$$

The resulting matrix $A_3$ is in upper triangular (row echelon) form.

**Step 4: State the inverse operation for each step**

Each elementary row operation is reversed by undoing its effect on the affected row(s):

1. **Reversing $R_2 \leftarrow R_2 - 2R_1$:** Add $2R_1$ back to $R_2$:

$$
R_2 \leftarrow R_2 + 2R_1
$$

2. **Reversing $R_3 \leftarrow R_3 + R_1$:** Subtract $R_1$ from $R_3$:

$$
R_3 \leftarrow R_3 - R_1
$$

3. **Reversing the interchange of $R_2$ and $R_3$:** Interchange $R_2$ and $R_3$ again:

$$
R_2 \leftrightarrow R_3
$$

**Step 5: Verification**

* **Reversal check:** Apply the three inverse operations to $A_3$ in reverse order (first $R_2 \leftrightarrow R_3$, then $R_3 \leftarrow R_3 - R_1$, then $R_2 \leftarrow R_2 + 2R_1$):
  * Applying $R_2 \leftrightarrow R_3$ to $A_3$ yields:

$$
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix}
= A_2
$$

  * Applying $R_3 \leftarrow R_3 - R_1$ to $A_2$ gives $(0, 3, 2) - (1, 2, -1) = (-1, 1, 3)$ in row $3$:

$$
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix}
= A_1
$$

  * Applying $R_2 \leftarrow R_2 + 2R_1$ to $A_1$ gives $(0, 0, 3) + 2(1, 2, -1) = (2, 4, 1)$ in row $2$:

$$
\begin{pmatrix}
1 & 2 & -1 \\
2 & 4 & 1 \\
-1 & 1 & 3 \\
\end{pmatrix}
= A
$$

* **Determinant invariant check:** Row replacements leave the determinant unchanged, while a single row interchange multiplies the determinant by $-1$. Since $A_3$ is upper triangular, $\det(A_3) = 1 \cdot 3 \cdot 3 = 9$, which implies $\det(A) = -9$. Expanding $\det(A)$ along row $1$ directly gives:

$$
\det(A) = 1(4 \cdot 3 - 1 \cdot 1) - 2(2 \cdot 3 - 1 \cdot (-1)) + (-1)(2 \cdot 1 - 4 \cdot (-1)) = 11 - 14 - 6 = -9
$$

Both checks confirm the intermediate matrices and inverse operations.

---

### Final Answer

1. Matrices after each sequential operation:

* After $R_2 \leftarrow R_2 - 2R_1$:

$$
A_1 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix}
$$

* After $R_3 \leftarrow R_3 + R_1$:

$$
A_2 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix}
$$

* After interchanging $R_2$ and $R_3$:

$$
A_3 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3 \\
\end{pmatrix}
$$

2. Operations that reverse each step:
   * Inverse of $R_2 \leftarrow R_2 - 2R_1$: $R_2 \leftarrow R_2 + 2R_1$
   * Inverse of $R_3 \leftarrow R_3 + R_1$: $R_3 \leftarrow R_3 - R_1$
   * Inverse of interchanging $R_2$ and $R_3$: interchange $R_2$ and $R_3$ ($R_2 \leftrightarrow R_3$)
