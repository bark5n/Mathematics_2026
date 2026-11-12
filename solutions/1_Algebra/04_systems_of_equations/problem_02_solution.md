### Essential Formulas

**Gaussian Elimination on an Augmented Matrix $[A \mid b]$:**
To solve a system of linear equations $Ax = b$, form the augmented matrix $[A \mid b]$ and apply elementary row operations—which preserve the solution set of the system—until the coefficient block reaches row echelon (upper triangular) form $[U \mid c]$:

1. **Row interchange ($R_i \leftrightarrow R_j$):** Swaps two equations.
2. **Nonzero row scaling ($R_i \leftarrow k R_i$, $k \neq 0$):** Multiplies an equation by a nonzero constant.
3. **Row replacement ($R_i \leftarrow R_i + k R_j$, $i \neq j$):** Adds a multiple of one equation to another to eliminate a variable below a pivot.

**Back-Substitution:**
Once the augmented matrix is in row echelon form $[U \mid c]$ with nonzero pivots in every column, solve for the unknowns sequentially from the bottom row upward.

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

**Step 1: Write the augmented matrix $[A \mid b]$**

Record the coefficients of $x$, $y$, $z$ and the right-hand side constants in a $3 \times 4$ augmented matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
2 & -1 & 1 & \mid & 3 \\
1 & 2 & -1 & \mid & 2 \\
\end{pmatrix}
$$

**Step 2: Forward elimination — eliminate $x$ below the $(1, 1)$-pivot**

Using the leading $1$ in position $(1, 1)$ as the first pivot, eliminate the entries below it in column $1$:

1. **$R_2 \leftarrow R_2 - 2R_1$:**

$$
(2, -1, 1 \mid 3) - 2(1, 1, 1 \mid 6) = (2 - 2, -1 - 2, 1 - 2 \mid 3 - 12) = (0, -3, -1 \mid -9)
$$

2. **$R_3 \leftarrow R_3 - R_1$:**

$$
(1, 2, -1 \mid 2) - (1, 1, 1 \mid 6) = (1 - 1, 2 - 1, -1 - 1 \mid 2 - 6) = (0, 1, -2 \mid -4)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & -3 & -1 & \mid & -9 \\
0 & 1 & -2 & \mid & -4 \\
\end{pmatrix}
$$

**Step 3: Forward elimination — swap rows and eliminate $y$ below the second pivot**

Interchange rows $2$ and $3$ ($R_2 \leftrightarrow R_3$) to bring the unit entry $1$ into the $(2, 2)$-pivot position and avoid fractions:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & 1 & -2 & \mid & -4 \\
0 & -3 & -1 & \mid & -9 \\
\end{pmatrix}
$$

Now eliminate the $(3, 2)$-entry using $R_3 \leftarrow R_3 + 3R_2$:

$$
(0, -3, -1 \mid -9) + 3(0, 1, -2 \mid -4) = (0, -3 + 3, -1 - 6 \mid -9 - 12) = (0, 0, -7 \mid -21)
$$

This produces the upper triangular (row echelon) augmented matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & 1 & -2 & \mid & -4 \\
0 & 0 & -7 & \mid & -21 \\
\end{pmatrix}
$$

**Step 4: Solve for $z$, $y$, and $x$ via back-substitution**

Translate the row echelon matrix back into equations and solve from bottom to top:

1. **From row 3:**

$$
-7z = -21 \implies z = \frac{-21}{-7} = 3
$$

2. **From row 2 (substituting $z = 3$):**

$$
y - 2z = -4 \implies y - 2(3) = -4 \implies y - 6 = -4 \implies y = 2
$$

3. **From row 1 (substituting $y = 2$ and $z = 3$):**

$$
x + y + z = 6 \implies x + 2 + 3 = 6 \implies x + 5 = 6 \implies x = 1
$$

Thus, the system has the unique solution $(x, y, z) = (1, 2, 3)$.

**Step 5: Substitute $(x, y, z) = (1, 2, 3)$ into all equations to check consistency**

Evaluate the left-hand side of each original equation at $x = 1$, $y = 2$, and $z = 3$:

* **Equation 1:**

$$
x + y + z = 1 + 2 + 3 = 6 \qquad (\mathrm{matches\ RHS} = 6)
$$

* **Equation 2:**

$$
2x - y + z = 2(1) - 2 + 3 = 2 - 2 + 3 = 3 \qquad (\mathrm{matches\ RHS} = 3)
$$

* **Equation 3:**

$$
x + 2y - z = 1 + 2(2) - 3 = 1 + 4 - 3 = 2 \qquad (\mathrm{matches\ RHS} = 2)
$$

All three equations are satisfied identically, confirming that the system is consistent and $(1, 2, 3)$ is its unique solution.

---

### Final Answer

1. **Unique solution:**

$$
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
=
\begin{pmatrix}
1 \\
2 \\
3 \\
\end{pmatrix}
\qquad
(x = 1, \quad y = 2, \quad z = 3)
$$

2. **Consistency check:** Substituting $(x, y, z) = (1, 2, 3)$ into the three equations yields $1 + 2 + 3 = 6$, $2(1) - 2 + 3 = 3$, and $1 + 2(2) - 3 = 2$, verifying that all equations hold.
