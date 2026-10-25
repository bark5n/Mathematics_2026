**Result:**

The system in the form $Ax = b$ is:

$$ \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix} $$

**Steps & Detailed Explanation:**

A linear system can be represented by the matrix equation $Ax = b$, where:
- $A$ is the coefficient matrix, containing the numbers multiplying the variables.
- $x$ is the column vector of unknowns.
- $b$ is the column vector of the right-hand side constants.

Extracting these from the given system:

The coefficient matrix $A$ is formed by aligning the coefficients of $x$, $y$, and $z$ in columns:

$$ A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix} $$

The vector of unknowns $x$ and the right-hand side vector $b$ are:

$$ x = \begin{pmatrix} x \\ y \\ z \end{pmatrix}, \qquad b = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix} $$

When you multiply the matrix $A$ by the vector $x$ using the standard row-by-column matrix multiplication, the first row of $A$ multiplies the column $x$ to give $2x - y + z$. This must equal the first entry of $b$, which is $4$. Thus, each horizontal row in the matrix multiplication reproduces exactly one equation from the original system.
