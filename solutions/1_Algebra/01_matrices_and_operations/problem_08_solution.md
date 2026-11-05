### Essential Formulas

**Elementary Row Operations:**
There are three basic types of elementary row operations that can be performed on a matrix:
1. **Row Addition:** Adding a multiple of one row to another row ($R_i \leftarrow R_i + k R_j$).
2. **Row Switching:** Interchanging two rows ($R_i \leftrightarrow R_j$).
3. **Row Multiplication:** Multiplying a row by a non-zero scalar ($R_i \leftarrow k R_i$).

**Reversibility (Inverse Operations):**
Every elementary row operation is reversible by another elementary row operation of the same type:
* The reverse of $R_i \leftarrow R_i + k R_j$ is $R_i \leftarrow R_i - k R_j$.
* The reverse of $R_i \leftrightarrow R_j$ is simply applying the same swap again: $R_i \leftrightarrow R_j$.
* The reverse of $R_i \leftarrow k R_i$ is $R_i \leftarrow \frac{1}{k} R_i$.

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
1. $R_2 \leftarrow R_2 - 2R_1$
2. $R_3 \leftarrow R_3 + R_1$
3. interchange $R_2$ and $R_3$

Write the matrix after each step. Then, for each of the three operations, state an operation that reverses it.

> **Why this exercise:** prepares for elimination by showing that row operations are controlled and reversible transformations of a matrix.

---

### Solution

**Step 1: Perform $R_2 \leftarrow R_2 - 2R_1$**

Multiply Row 1 by 2 to get $(2, 4, -2)$. Subtract this from Row 2 $(2, 4, 1)$:

$$
R_2 \leftarrow (2 - 2,\; 4 - 4,\; 1 - (-2)) = (0, 0, 3)
$$

The resulting matrix is:

$$
A_1 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix}
$$

**Step 2: Perform $R_3 \leftarrow R_3 + R_1$**

Add Row 1 $(1, 2, -1)$ to Row 3 $(-1, 1, 3)$:

$$
R_3 \leftarrow (-1 + 1,\; 1 + 2,\; 3 - 1) = (0, 3, 2)
$$

The resulting matrix is:

$$
A_2 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix}
$$

**Step 3: Interchange $R_2$ and $R_3$ ($R_2 \leftrightarrow R_3$)**

Swap the second and third rows of matrix $A_2$:

$$
A_3 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3 \\
\end{pmatrix}
$$

**Step 4: Reversing the operations**

Each elementary row operation is reversed by its corresponding inverse operation:

**Operation 1:** The operation $R_2 \leftarrow R_2 - 2R_1$ is reversed by:

$$
R_2 \leftarrow R_2 + 2R_1
$$

**Operation 2:** The operation $R_3 \leftarrow R_3 + R_1$ is reversed by:

$$
R_3 \leftarrow R_3 - R_1
$$

**Operation 3:** The operation $R_2 \leftrightarrow R_3$ is reversed by:

$$
R_2 \leftrightarrow R_3
$$

---

### Final Answer

Matrices after each step:

$$
A_1 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix},
\qquad
A_2 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix},
\qquad
A_3 = \begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3 \\
\end{pmatrix}
$$

Reverse operations:
1. $R_2 \leftarrow R_2 + 2R_1$
2. $R_3 \leftarrow R_3 - R_1$
3. $R_2 \leftrightarrow R_3$
