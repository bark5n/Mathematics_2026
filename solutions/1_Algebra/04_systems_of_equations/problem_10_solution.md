### Essential Formulas

**Point-Incidence Condition for a Polynomial Graph:**
The graph of a quadratic polynomial $p(x) = ax^2 + bx + c$ passes through a point $(x_i, y_i) \in \mathbb{R}^2$ if and only if $p(x_i) = y_i$, which yields a linear equation in the unknown coefficients $(a, b, c)$:

$$
x_i^2 a + x_i b + 1 \cdot c = y_i
$$

**Vandermonde Linear System for Three Distinct Points:**
Given three points $(x_1, y_1)$, $(x_2, y_2)$, and $(x_3, y_3)$ with distinct $x$-coordinates ($x_1, x_2, x_3$ pairwise distinct), finding $p(x) = ax^2 + bx + c$ reduces to solving the $3 \times 3$ linear system:

$$
\begin{pmatrix}
x_1^2 & x_1 & 1 \\
x_2^2 & x_2 & 1 \\
x_3^2 & x_3 & 1 \\
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
c \\
\end{pmatrix}
=
\begin{pmatrix}
y_1 \\
y_2 \\
y_3 \\
\end{pmatrix}
$$

**Gaussian Elimination and Back-Substitution:**
Forming the augmented matrix $[A \mid y]$ and reducing it to upper triangular (row echelon) form via elementary row operations allows $c$, $b$, and $a$ to be determined uniquely from bottom to top.

---

### Problem Statement

**Exercise 10. A Polynomial Through Three Points**

Find a polynomial $p(x)=ax^2+bx+c$ whose graph passes through $(0,1)$, $(1,3)$, and $(2,9)$. Reduce the problem to a system of equations and check the result by substituting all three points.

> **Why this exercise:** shows that finding unknown coefficients can be reduced to solving a linear system.

---

### Solution

**Step 1: Translate the three point conditions into a system of linear equations**

For the graph of $p(x) = ax^2 + bx + c$ to pass through each given point $(x_i, y_i)$, the condition $p(x_i) = y_i$ must hold:

1. **Passing through $(0, 1)$ ($p(0) = 1$):**

$$
a(0)^2 + b(0) + c = 1 \implies 0a + 0b + c = 1
$$

2. **Passing through $(1, 3)$ ($p(1) = 3$):**

$$
a(1)^2 + b(1) + c = 3 \implies a + b + c = 3
$$

3. **Passing through $(2, 9)$ ($p(2) = 9$):**

$$
a(2)^2 + b(2) + c = 9 \implies 4a + 2b + c = 9
$$

Ordering the unknowns as $(a, b, c)$, we obtain the $3 \times 3$ linear system:

$$
\begin{cases}
0a + 0b + c = 1, \\
a + b + c = 3, \\
4a + 2b + c = 9.
\end{cases}
$$

**Step 2: Solve the system using Gaussian elimination**

Write the augmented matrix $[A \mid y]$ corresponding to the unknowns $(a, b, c)$:

$$
\begin{pmatrix}
0 & 0 & 1 & \mid & 1 \\
1 & 1 & 1 & \mid & 3 \\
4 & 2 & 1 & \mid & 9 \\
\end{pmatrix}
$$

1. **Swap rows $1$ and $2$ ($R_1 \leftrightarrow R_2$) to place a leading $1$ in position $(1, 1)$:**

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 3 \\
0 & 0 & 1 & \mid & 1 \\
4 & 2 & 1 & \mid & 9 \\
\end{pmatrix}
$$

2. **Eliminate the $(3, 1)$-entry using $R_3 \leftarrow R_3 - 4R_1$:**

$$
(4, 2, 1 \mid 9) - 4(1, 1, 1 \mid 3) = (4 - 4, 2 - 4, 1 - 4 \mid 9 - 12) = (0, -2, -3 \mid -3)
$$

   The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 3 \\
0 & 0 & 1 & \mid & 1 \\
0 & -2 & -3 & \mid & -3 \\
\end{pmatrix}
$$

3. **Swap rows $2$ and $3$ ($R_2 \leftrightarrow R_3$) to obtain upper triangular (row echelon) form:**

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 3 \\
0 & -2 & -3 & \mid & -3 \\
0 & 0 & 1 & \mid & 1 \\
\end{pmatrix}
$$

**Step 3: Find the coefficients $c$, $b$, and $a$ via back-substitution**

Solve from the bottom row upward:

1. **From row 3:**

$$
c = 1
$$

2. **From row 2 (substituting $c = 1$):**

$$
-2b - 3c = -3 \implies -2b - 3(1) = -3 \implies -2b = 0 \implies b = 0
$$

3. **From row 1 (substituting $b = 0$ and $c = 1$):**

$$
a + b + c = 3 \implies a + 0 + 1 = 3 \implies a = 2
$$

Substituting $a = 2$, $b = 0$, and $c = 1$ into $p(x) = ax^2 + bx + c$ gives the polynomial:

$$
p(x) = 2x^2 + 1
$$

**Step 4: Check the result by substituting all three points**

Evaluate $p(x) = 2x^2 + 1$ at $x = 0$, $x = 1$, and $x = 2$:

* **Point $(0, 1)$:**

$$
p(0) = 2(0)^2 + 1 = 0 + 1 = 1 \qquad (\mathrm{matches}\ y_1 = 1)
$$

* **Point $(1, 3)$:**

$$
p(1) = 2(1)^2 + 1 = 2(1) + 1 = 3 \qquad (\mathrm{matches}\ y_2 = 3)
$$

* **Point $(2, 9)$:**

$$
p(2) = 2(2)^2 + 1 = 2(4) + 1 = 9 \qquad (\mathrm{matches}\ y_3 = 9)
$$

All three points lie on the graph of $p(x) = 2x^2 + 1$.

**Step 5: Verification**

* **Finite-difference consistency check:**
  For the equally spaced inputs $x = 0, 1, 2$ ($\Delta x = 1$), the output values are $1, 3, 9$. The first differences are $3 - 1 = 2$ and $9 - 3 = 6$, and the constant second difference is $\Delta^2 y = 6 - 2 = 4$. For any quadratic $ax^2 + bx + c$ with step $\Delta x = 1$, $\Delta^2 y = 2a$, so $2a = 4 \implies a = 2$, independently confirming the leading coefficient.

---

### Final Answer

1. **Reduced linear system for the coefficients $(a, b, c)$:**

$$
\begin{cases}
c = 1, \\
a + b + c = 3, \\
4a + 2b + c = 9
\end{cases}
\qquad \Longrightarrow \qquad
\begin{pmatrix}
a \\
b \\
c \\
\end{pmatrix}
=
\begin{pmatrix}
2 \\
0 \\
1 \\
\end{pmatrix}
$$

2. **Polynomial passing through $(0, 1)$, $(1, 3)$, and $(2, 9)$:**

$$
p(x) = 2x^2 + 1
$$

3. **Verification:** $p(0) = 1$, $p(1) = 3$, and $p(2) = 9$, confirming that all three points lie on the graph of $p(x)$.
