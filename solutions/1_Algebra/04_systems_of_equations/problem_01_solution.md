### Essential Formulas

**Matrix Form of a System of Linear Equations ($Ax = b$):**
A system of $m$ linear equations in $n$ unknowns $x_1, x_2, \ldots, x_n$:

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1, \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2, \\ \quad \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$

can be written compactly as a single matrix equation $Ax = b$, where:

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \\ \end{pmatrix}, \qquad x = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \\ \end{pmatrix}, \qquad b = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \\ \end{pmatrix}$$

* $A \in \mathbb{R}^{m \times n}$ is the **coefficient matrix**,
* $x \in \mathbb{R}^n$ is the **vector of unknowns**,
* $b \in \mathbb{R}^m$ is the **right-hand side vector**.

**Row-by-Column Multiplication Rule:**
The $i$-th entry of the matrix-vector product $Ax$ equals the dot product of the $i$-th row of $A$ with the column vector $x$:

$$(Ax)_i = a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n$$

---

### Problem Statement

**Exercise 1. From a System to a Matrix**

Write the system

$$\begin{cases} 2x-y+z=4, \\ x+3y-2z=1, \\ 3x+y+z=7. \end{cases}$$

in the form $Ax=b$.
Identify the coefficient matrix, the vector of unknowns, and the right-hand side vector. Explain how each row of the matrix corresponds to one equation.

> **Why this exercise:** teaches how to move between a system of equations and matrix notation.

---

### Solution

**Step 1: Align the variables and extract the coefficients and constants**

Write every equation with the variables in the consistent order $x$, $y$, $z$, making implicit coefficients of $1$ and $-1$ explicit:

$$\begin{cases} 2x + (-1)y + 1z = 4, \\ 1x + 3y + (-2)z = 1, \\ 3x + 1y + 1z = 7. \end{cases}$$

* From equation 1, the coefficients are $(2, -1, 1)$ and the right-hand side constant is $4$.
* From equation 2, the coefficients are $(1, 3, -2)$ and the right-hand side constant is $1$.
* From equation 3, the coefficients are $(3, 1, 1)$ and the right-hand side constant is $7$.

**Step 2: Identify $A$, $x$, and $b$, and write the system as $Ax = b$**

Arrange the coefficients into a $3 \times 3$ matrix $A$, the unknowns into a $3 \times 1$ column vector (denoting the vector of unknowns by $\mathbf{x}$ to distinguish it from the scalar variable $x$), and the constants into a $3 \times 1$ column vector $b$:

$$A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \\ \end{pmatrix}, \qquad \mathbf{x} = \begin{pmatrix} x \\ y \\ z \\ \end{pmatrix}, \qquad b = \begin{pmatrix} 4 \\ 1 \\ 7 \\ \end{pmatrix}$$

Writing the system in the matrix form $A\mathbf{x} = b$ gives:

$$\begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \\ \end{pmatrix} \begin{pmatrix} x \\ y \\ z \\ \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \\ \end{pmatrix}$$

**Step 3: Explain how each row of $A$ corresponds to one equation**

By the definition of matrix-vector multiplication, multiplying $A$ by $\mathbf{x}$ computes the dot product of each row of $A$ with the column vector $\mathbf{x} = (x, y, z)^T$, while vector equality equates corresponding entries on both sides:

* **Row 1 $\leftrightarrow$ Equation 1:** The first row $(2, -1, 1)$ contains the coefficients of $x$, $y$, and $z$ in the first equation. Multiplying Row 1 by $\mathbf{x}$ yields $2x - y + z$, and equating it to the first entry of $b$ ($4$) produces $2x - y + z = 4$.
* **Row 2 $\leftrightarrow$ Equation 2:** The second row $(1, 3, -2)$ contains the coefficients of $x$, $y$, and $z$ in the second equation. Multiplying Row 2 by $\mathbf{x}$ yields $x + 3y - 2z$, and equating it to the second entry of $b$ ($1$) produces $x + 3y - 2z = 1$.
* **Row 3 $\leftrightarrow$ Equation 3:** The third row $(3, 1, 1)$ contains the coefficients of $x$, $y$, and $z$ in the third equation. Multiplying Row 3 by $\mathbf{x}$ yields $3x + y + z$, and equating it to the third entry of $b$ ($7$) produces $3x + y + z = 7$.

*(Equivalently, the columns of $A$ group coefficients by variable: column 1 holds the coefficients of $x$, column 2
