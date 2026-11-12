### Essential Formulas

**Redundant Equations in a Linear System:**
An equation in a linear system $Ax = b$ is **redundant** if it is a linear combination of the remaining equations in the system. Removing a redundant equation does **not** change the solution set of the system, and during Gaussian elimination, a redundant equation reduces to a zero row $(0 \ 0 \ \cdots \ 0 \mid 0)$.

**Row Echelon Form and Free Variables:**
For a consistent system of linear equations in $n$ unknowns whose row echelon form has $r = \mathrm{rank}(A) = \mathrm{rank}([A \mid b])$ nonzero rows (pivots), there are $n - r$ free variables and $r$ independent equations needed to describe the solution set.

---

### Problem Statement

**Exercise 13. Does Every Equation Add New Information?**

Consider the system

$$x_1+x_2=10,\qquad x_2+x_3=8,\qquad x_1-x_3=2.$$

Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

> **Why this exercise:** teaches how to recognize redundant equations within a system.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid b]$ and apply Gaussian elimination**

Order the unknowns as $(x_1, x_2, x_3)$ and write the $3 \times 4$ augmented matrix of the system:

$$\begin{pmatrix} 1 & 1 & 0 & \mid & 10 \\ 0 & 1 & 1 & \mid & 8 \\ 1 & 0 & -1 & \mid & 2 \\ \end{pmatrix}$$

1. **Eliminate the $(3, 1)$-entry using $R_3 \leftarrow R_3 - R_1$:**

$$(1, 0, -1 \mid 2) - (1, 1, 0 \mid 10) = (0, -1, -1 \mid -8)$$

   The augmented matrix becomes:

$$\begin{pmatrix} 1 & 1 & 0 & \mid & 10 \\ 0 & 1 & 1 & \mid & 8 \\ 0 & -1 & -1 & \mid & -8 \\ \end{pmatrix}$$

2. **Eliminate the $(3, 2)$-entry using $R_3 \leftarrow R_3 + R_2$:**

$$(0, -1, -1 \mid -8) + (0, 1, 1 \mid 8) = (0, 0, 0 \mid 0)$$

   The augmented matrix reaches row echelon form:

$$\begin{pmatrix} 1 & 1 & 0 & \mid & 10 \\ 0 & 1 & 1 & \mid & 8 \\ 0 & 0 & 0 & \mid & 0 \\ \end{pmatrix}$$

3. **Eliminate the $(1, 2)$-entry using $R_1 \leftarrow R_1 - R_2$ to obtain reduced row echelon form (RREF):**

$$(1, 1, 0 \mid 10) - (0, 1, 1 \mid 8) = (1, 0, -1 \mid 2)$$

$$\begin{pmatrix} 1 & 0 & -1 & \mid & 2 \\ 0 & 1 & 1 & \mid & 8 \\ 0 & 0 & 0 & \mid & 0 \\ \end{pmatrix}$$

**Step 2: Write the complete solution set in parametric form**

There is no contradictory row ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 2$), and there are $r = 2$ pivot columns (column $1$ for $x_1$ and column $2$ for $x_2$) among $n = 3$ variables, leaving $n - r = 3 - 2 = 1$ free variable ($x_3$). Rewriting the two nonzero rows as equations gives:

$$\begin{cases} x_1 - x_3 = 2, \\ x_2 + x_3 = 8. \end{cases}$$

Assign an arbitrary real parameter $x_3 = t$ ($t \in \mathbb{R}$) and express $x_1$ and $x_2$ in terms of $t$:

$$\begin{cases} x_1 = 2 + t, \\ x_2 = 8 - t, \\ x_3 = t, \end{cases} \qquad t \in \mathbb{R}$$

Equivalently, in parametric vector form:

$$\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ \end{pmatrix} = \begin{pmatrix} 2 \\ 8 \\ 0 \\ \end{pmatrix} + t \begin{pmatrix} 1 \\ -1 \\ 1 \\ \end{pmatrix}, \qquad t \in \mathbb{R}$$

**Step 3: Check whether all three equations are independently necessary and show by calculation that one follows from the others**

* **Are all three equations independently necessary?**
  **No.** Because Gaussian elimination reduced the third row completely to $(0, 0, 0 \mid 0)$, the system contains only **$2$ independent equations** rather than $3$. Any one of the three equations is redundant and adds no new restriction to the solution set already determined by the other two.

* **Explicit algebraic calculation showing that Equation 3 follows from Equations 1 and 2:**
  Subtract Equation 2 ($x_2 + x_3 = 8$) from Equation 1 ($x_1 + x_2 = 10$):

$$
\begin{aligned}
(x_1 + x_2) - (x_2 + x_3) &= 10 - 8 \\
x_1 + (x_2 - x_2) - x_3 &= 2 \\
x_1
