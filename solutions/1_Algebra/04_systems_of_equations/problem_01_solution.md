### Essential Formulas

**Matrix Form of a Linear System:**
A system of $m$ linear equations in $n$ unknowns can be written compactly as:

$$
A x = b
$$

where:
* $A \in \mathbb{R}^{m \times n}$ is the **coefficient matrix**, containing the coefficients of the unknowns.
* $x \in \mathbb{R}^{n \times 1}$ is the **vector of unknowns** (column vector).
* $b \in \mathbb{R}^{m \times 1}$ is the **right-hand side vector** of constant terms.

**Row-by-Column Interpretation:**
Matrix-vector multiplication states that row $i$ of matrix $A$, denoted $r_i$, multiplied by the column vector $x$ produces entry $i$ of the vector $b$:

$$
r_i \cdot x = b_i
$$

Thus, row $i$ in matrix notation corresponds precisely to equation $i$ in the algebraic system.

---

### Problem Statement

**Exercise 1. From a System to a Matrix**

Write the system

$$
\begin{cases}
2x-y+z=4, \\
x+3y-2z=1, \\
3x+y+z=7.
\end{cases}
$$

in the form $Ax=b$.
Identify the coefficient matrix, the vector of unknowns, and the right-hand side vector. Explain how each row of the matrix corresponds to one equation.

> **Why this exercise:** teaches how to move between a system of equations and matrix notation.

---

### Solution

**Step 1: Identify the variables, coefficients, and constants**

The system has three unknowns: $x$, $y$, and $z$.
* Equation 1: $2x - 1y + 1z = 4$
  * Coefficients: $(2, -1, 1)$, Constant: $4$
* Equation 2: $1x + 3y - 2z = 1$
  * Coefficients: $(1, 3, -2)$, Constant: $1$
* Equation 3: $3x + 1y + 1z = 7$
  * Coefficients: $(3, 1, 1)$, Constant: $7$

**Step 2: Construct $A$, $x$, and $b$**

* The **coefficient matrix** $A$ is formed by aligning the coefficients of $x$, $y$, and $z$ into columns:

$$
A = \begin{pmatrix}
2 & -1 & 1 \\
1 & 3 & -2 \\
3 & 1 & 1 \\
\end{pmatrix}
$$

* The **vector of unknowns** $x$ is:

$$
x = \begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
$$

* The **right-hand side vector** $b$ is:

$$
b = \begin{pmatrix}
4 \\
1 \\
7 \\
\end{pmatrix}
$$

**Step 3: Write in matrix form $Ax = b$**

$$
\begin{pmatrix}
2 & -1 & 1 \\
1 & 3 & -2 \\
3 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= \begin{pmatrix}
4 \\
1 \\
7 \\
\end{pmatrix}
$$

**Step 4: Explain the row-equation correspondence**

Computing the matrix product $Ax$ by taking the dot product of each row of $A$ with the column vector $x$:
* Row 1:

$$
\begin{pmatrix}
2 & -1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= 2x - y + z
$$

 Setting this equal to the first entry of $b$ gives $2x - y + z = 4$ (Equation 1).
* Row 2:

$$
\begin{pmatrix}
1 & 3 & -2 \\
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= x + 3y - 2z
$$

 Setting this equal to the second entry of $b$ gives $x + 3y - 2z = 1$ (Equation 2).
* Row 3:

$$
\begin{pmatrix}
3 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= 3x + y + z
$$

 Setting this equal to the third entry of $b$ gives $3x + y + z = 7$ (Equation 3).

Every horizontal row in the coefficient matrix contains the weights for the linear combination of the unknowns in the corresponding equation.

---

### Final Answer

1. Matrix form $Ax = b$:

$$
\begin{pmatrix}
2 & -1 & 1 \\
1 & 3 & -2 \\
3 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
= \begin{pmatrix}
4 \\
1 \\
7 \\
\end{pmatrix}
$$

2. Identified components:
   * Coefficient matrix:

$$
A = \begin{pmatrix}
2 & -1 & 1 \\
1 & 3 & -2 \\
3 & 1 & 1 \\
\end{pmatrix}
$$

$
   * Unknown vector:

$$
x = \begin{pmatrix}
x \\
y \\
z \\
\end{pmatrix}
$$

$
   * Right-hand side vector:

$$
b = \begin{pmatrix}
4 \\
1 \\
7 \\
\end{pmatrix}
$$

$
