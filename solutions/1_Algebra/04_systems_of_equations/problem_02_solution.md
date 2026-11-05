### Essential Formulas

**Gaussian Elimination and Augmented Matrix:**
A linear system $Ax = b$ can be solved using elementary row operations on the augmented matrix:

$$
[A \mid b] = \begin{pmatrix}
a_{11} & a_{12} & a_{13} & \mid & b_1 \\
a_{21} & a_{22} & a_{23} & \mid & b_2 \\
a_{31} & a_{32} & a_{33} & \mid & b_3 \\
\end{pmatrix}
$$

**Elementary Row Operations:**
1. $R_i \leftrightarrow R_j$ (Swap two rows)
2. $R_i \leftarrow c R_i$ ($c \neq 0$, scale a row)
3. $R_i \leftarrow R_i + c R_j$ ($i \neq j$, add a multiple of one row to another)

**Back-Substitution:**
Once reduced to upper triangular (row echelon) form, solve for the variables beginning from the bottom row and substituting upwards.

---

### Problem Statement

**Exercise 2. Gaussian Elimination — One Solution**

Solve using Gaussian elimination:

$$
\begin{cases}
x+y+z=6, \\
2x-y+z=3, \\
x+2y-z=2.
\end{cases}
$$

After solving, substitute the result into all equations and check consistency.

> **Why this exercise:** introduces the basic method for solving a system and builds the habit of checking the result.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid b]$**

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
2 & -1 & 1 & \mid & 3 \\
1 & 2 & -1 & \mid & 2 \\
\end{pmatrix}
$$

**Step 2: Eliminate $x$ from rows 2 and 3**

* Eliminate entry at $(2,1)$ using $R_2 \leftarrow R_2 - 2R_1$:
  $$
  (2, -1, 1 \mid 3) - 2(1, 1, 1 \mid 6) = (0, -3, -1 \mid -9)
  $$

* Eliminate entry at $(3,1)$ using $R_3 \leftarrow R_3 - R_1$:
  $$
  (1, 2, -1 \mid 2) - (1, 1, 1 \mid 6) = (0, 1, -2 \mid -4)
  $$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & -3 & -1 & \mid & -9 \\
0 & 1 & -2 & \mid & -4 \\
\end{pmatrix}
$$

**Step 3: Swap $R_2$ and $R_3$ for an easier pivot of $1$**

Perform $R_2 \leftrightarrow R_3$:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & 1 & -2 & \mid & -4 \\
0 & -3 & -1 & \mid & -9 \\
\end{pmatrix}
$$

**Step 4: Eliminate entry at $(3,2)$**

Perform $R_3 \leftarrow R_3 + 3R_2$:

$$
(0, -3, -1 \mid -9) + 3(0, 1, -2 \mid -4) = (0, 0, -7 \mid -21)
$$

The augmented matrix in row echelon form is:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & 1 & -2 & \mid & -4 \\
0 & 0 & -7 & \mid & -21 \\
\end{pmatrix}
$$

**Step 5: Back-substitution**

1. From row 3:
   $$
   -7z = -21 \implies z = \frac{-21}{-7} = 3
   $$

2. From row 2, substitute $z = 3$:
   $$
   y - 2z = -4 \implies y - 2(3) = -4 \implies y - 6 = -4 \implies y = 2
   $$

3. From row 1, substitute $y = 2$ and $z = 3$:
   $$
   x + y + z = 6 \implies x + 2 + 3 = 6 \implies x + 5 = 6 \implies x = 1
   $$

Thus, the unique solution is $(x, y, z) = (1, 2, 3)$.

**Step 6: Check consistency across all three original equations**

* Equation 1: $1 + 2 + 3 = 6$ (holds: $6 = 6$)
* Equation 2: $2(1) - 2 + 3 = 2 - 2 + 3 = 3$ (holds: $3 = 3$)
* Equation 3: $1 + 2(2) - 3 = 1 + 4 - 3 = 2$ (holds: $2 = 2$)

All three equations are satisfied.

---

### Final Answer

$$
x = 1, \qquad y = 2, \qquad z = 3
$$
