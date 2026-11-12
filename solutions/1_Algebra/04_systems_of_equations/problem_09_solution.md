### Essential Formulas

**Gaussian Elimination for a $2 \times 2$ Linear System:**
For a system of two linear equations in two unknowns $x, y$:

$$
\begin{cases}
a_{11}x + a_{12}y = b_1, \\
a_{21}x + a_{22}y = b_2
\end{cases}
$$

forming the augmented matrix $[A \mid b]$ and eliminating $x$ from the second equation via row replacement yields row echelon form, from which $y$ and $x$ are found by back-substitution.

**Geometric Interpretation of Two Linear Equations in $\mathbb{R}^2$:**
Each equation $ax + by = c$ with $(a, b) \neq (0, 0)$ defines a straight line in the Cartesian plane $\mathbb{R}^2$. When $b \neq 0$, its slope-intercept form is:

$$
y = -\frac{a}{b}x + \frac{c}{b}
$$

Two lines with **different slopes** ($m_1 \neq m_2$) are non-parallel and therefore intersect in **exactly one point**, which corresponds to the unique solution of the system (equivalently, $\det A = a_{11}a_{22} - a_{12}a_{21} \neq 0$).

---

### Problem Statement

**Exercise 9. A System from a Sum Condition**

Find numbers $x,y$ satisfying

$$
x+y=10,\qquad 2x+5y=32.
$$

Solve the system and explain geometrically why the solution is unique.

> **Why this exercise:** reinforces the transition from two linear conditions to the intersection point of two lines.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid b]$**

Write the two given linear conditions as a system and form its $2 \times 3$ augmented matrix:

$$
\begin{cases}
x + y = 10, \\
2x + 5y = 32
\end{cases}
\qquad \Longrightarrow \qquad
\begin{pmatrix}
1 & 1 & \mid & 10 \\
2 & 5 & \mid & 32 \\
\end{pmatrix}
$$

**Step 2: Perform Gaussian elimination and back-substitution**

1. **Eliminate $x$ in row 2 using $R_2 \leftarrow R_2 - 2R_1$:**
   * Left side: $(2, 5) - 2(1, 1) = (2 - 2, 5 - 2) = (0, 3)$
   * Right side: $32 - 2(10) = 32 - 20 = 12$

   The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 1 & \mid & 10 \\
0 & 3 & \mid & 12 \\
\end{pmatrix}
$$

2. **Solve by back-substitution:**
   * From row 2:

$$
3y = 12 \implies y = \frac{12}{3} = 4
$$

   * From row 1 (substituting $y = 4$):

$$
x + y = 10 \implies x + 4 = 10 \implies x = 6
$$

Thus, the numbers satisfying both conditions are $x = 6$ and $y = 4$.

**Step 3: Explain geometrically why the solution is unique**

In the two-dimensional Cartesian plane $\mathbb{R}^2$, each linear equation represents a straight line consisting of all points $(x, y)$ that satisfy that condition:

* **First equation ($L_1$):**

$$
x + y = 10 \iff y = -x + 10
$$

  This is a straight line with slope $m_1 = -1$ and $y$-intercept $(0, 10)$.

* **Second equation ($L_2$):**

$$
2x + 5y = 32 \iff y = -\frac{2}{5}x + \frac{32}{5}
$$

  This is a straight line with slope $m_2 = -\frac{2}{5}$ and $y$-intercept $(0, 6.4)$.

Because the two lines have **different slopes** ($m_1 = -1 \neq -\frac{2}{5} = m_2$), they are neither parallel nor coincident. In the Euclidean plane, any two non-parallel lines must cross at **exactly one point**. That single point of intersection $(6, 4)$ is the only point lying on both $L_1$ and $L_2$ simultaneously, which guarantees geometrically that the solution $(x, y) = (6, 4)$ is unique.

**Step 4: Verification**

* **Direct substitution into both conditions:**
  * Sum condition: $x + y = 6 + 4 = 10$ (matches RHS $= 10$).
  * Weighted sum condition: $2x + 5y = 2(6) + 5(4) = 12 + 20 = 32$ (matches RHS $= 32$).
* **Determinant check:**
  For the coefficient matrix

$$
A = \begin{pmatrix}
1 & 1 \\
2 & 5 \\
\end{pmatrix}
$$

  the determinant is $\det A = 1 \cdot 5 - 1 \cdot 2 = 3 \neq 0$, confirming algebraically that $A$ is invertible and the solution is unique.

---

### Final Answer

1. **Numbers $x, y$ satisfying the system:**

$$
x = 6, \qquad y = 4 \qquad \left(\mathrm{or}\quad \begin{pmatrix}
x \\
y \\
\end{pmatrix}
=
\begin{pmatrix}
6 \\
4 \\
\end{pmatrix}\right)
$$

2. **Geometric explanation for uniqueness:** Each equation defines a straight line in $\mathbb{R}^2$, namely $y = -x + 10$ (slope $m_1 = -1$) and $y = -\frac{2}{5}x + \frac{32}{5}$ (slope $m_2 = -\frac{2}{5}$). Because their slopes are unequal, the two lines are not parallel and therefore intersect at **one and only one point**, $(6, 4)$.
