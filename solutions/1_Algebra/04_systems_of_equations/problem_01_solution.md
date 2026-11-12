### Essential Formulas

**Matrix Form of a Linear System:**
A system of $m$ linear equations in $n$ unknowns can be written as a single matrix equation:

$$Ax = b$$

where:
* $A$ is the $m \times n$ **coefficient matrix** containing the weights of the variables.
* $x$ is the $n \times 1$ column **vector of unknowns**.
* $b$ is the $m \times 1$ column **right-hand side vector** of constants.

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

**Step 1: Identify the components for the matrix equation $Ax = b$**

Read the coefficients of the variables $x, y, z$ from the left side of each equation to form the coefficient matrix $A$. Group the variables into the column vector $x$, and take the constants from the right side of the equals signs to form the vector $b$.

1. **Coefficient matrix $A$:**

$$A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \\ \end{pmatrix}$$

2. **Vector of unknowns $x$:**

$$x = \begin{pmatrix} x \\ y \\ z \\ \end{pmatrix}$$

3. **Right-hand side vector $b$:**

$$b = \begin{pmatrix} 4 \\ 1 \\ 7 \\ \end{pmatrix}$$

**Step 2: Write the system in the form $Ax = b$**

Combining the identified components, the matrix equation is:

$$\begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \\ \end{pmatrix} \begin{pmatrix} x \\ y \\ z \\ \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \\ \end{pmatrix}$$

**Step 3: Explain the row-to-equation correspondence**

By the definition of matrix multiplication, multiplying the $i$-th row of matrix $A$ by the column vector $x$ produces the left-hand side of the $i$-th equation in the original system. For example, multiplying the first row of $A$ by the vector of unknowns gives the dot product:

$$\begin{pmatrix} 2 & -1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 2x + (-1)y + 1z = 2x - y + z$$

Equating this result to the first entry of the vector $b$ gives $2x - y + z = 4$, which perfectly recovers the first equation of the system. Thus, each row of the augmented matrix acts as a direct placeholder for the coefficients and constant of one specific equation.

---

### Final Answer

1. **The system in $Ax = b$ form:**

$$\begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \\ \end{pmatrix} \begin{pmatrix} x \\ y \\ z \\ \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \\ \end{pmatrix}$$

2. **Identified parts:**
   * **Coefficient matrix:** $A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix}$
   * **Vector of unknowns:** $x = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$
   * **Right-hand side:** $b = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}$
3. **Row correspondence:** By the rules of matrix-vector multiplication, the dot product of the $i$-th row of $A$ and the vector $x$ produces the algebraic expression for the $i$-th equation, which is then equated to the $i$-th entry of $b$.
