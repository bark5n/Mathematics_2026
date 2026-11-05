### Essential Formulas

**Effect of Elementary Row Operations on the Determinant:**
1. **Row Addition / Elimination ($R_i \leftarrow R_i + c R_j$ with $i \neq j$):**
   Adding a scalar multiple of one row to another does **not** change the determinant:
   $$
   \det(A_{\mathrm{new}}) = \det(A_{\mathrm{old}})
   $$
2. **Row Swap ($R_i \leftrightarrow R_j$):**
   Swapping two rows multiplies the determinant by $-1$:
   $$
   \det(A_{\mathrm{new}}) = -\det(A_{\mathrm{old}})
   $$
3. **Row Scaling ($R_i \leftarrow c R_i$):**
   Multiplying a row by a nonzero scalar $c$ scales the determinant by $c$:
   $$
   \det(A_{\mathrm{new}}) = c \cdot \det(A_{\mathrm{old}})
   $$

**Triangular Determinant Formula:**
Once transformed into upper triangular form $U$, the determinant is:
$$
\det U = u_{11} u_{22} \cdots u_{nn}
$$

---

### Problem Statement

**Exercise 5. Row Operations**

For

$$
A=
\begin{pmatrix}
1 & 2 & 3 \\
2 & 1 & 0 \\
-1 & 4 & 2 \\
\end{pmatrix}
$$

find $\det A$ by simplifying the matrix with row operations. At each step, indicate whether and how the determinant changes.

> **Why this exercise:** connects determinants with row operations and requires conscious tracking of every step.

---

### Solution

**Step 1: Eliminate the entry in row 2, column 1**

Perform the row operation:
$$
R_2 \leftarrow R_2 - 2R_1
$$

*Effect on determinant:* Adding a scalar multiple of one row to another preserves the determinant ($\det A_1 = \det A$).

Compute the new row 2:
$$
(2, 1, 0) - 2(1, 2, 3) = (2 - 2, 1 - 4, 0 - 6) = (0, -3, -6)
$$

The resulting matrix is:

$$
A_1 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
-1 & 4 & 2 \\
\end{pmatrix}
$$

**Step 2: Eliminate the entry in row 3, column 1**

Perform the row operation:
$$
R_3 \leftarrow R_3 + R_1
$$

*Effect on determinant:* Preserves the determinant ($\det A_2 = \det A_1 = \det A$).

Compute the new row 3:
$$
(-1, 4, 2) + (1, 2, 3) = (-1 + 1, 4 + 2, 2 + 3) = (0, 6, 5)
$$

The resulting matrix is:

$$
A_2 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 6 & 5 \\
\end{pmatrix}
$$

**Step 3: Eliminate the entry in row 3, column 2 to achieve upper triangular form**

Perform the row operation:
$$
R_3 \leftarrow R_3 + 2R_2
$$

*Effect on determinant:* Preserves the determinant ($\det A_3 = \det A_2 = \det A$).

Compute the new row 3:
$$
(0, 6, 5) + 2(0, -3, -6) = (0 + 0, 6 - 6, 5 - 12) = (0, 0, -7)
$$

The resulting upper triangular matrix is:

$$
A_3 =
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 0 & -7 \\
\end{pmatrix}
$$

**Step 4: Compute the determinant of the upper triangular matrix**

Since every operation used was of the type $R_i \leftarrow R_i + c R_j$, the determinant is completely unchanged:
$$
\det A = \det A_3
$$

For the upper triangular matrix $A_3$, the determinant is the product of its diagonal elements:

$$
\begin{aligned}
\det A &= 1 \cdot (-3) \cdot (-7) \\
&= 21
\end{aligned}
$$

---

### Final Answer

$$
\det A = 21
$$
