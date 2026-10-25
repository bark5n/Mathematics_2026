**Result:**

The system in the form $Ax = b$ is:

$$
\left( \begin{array}{ccc}
2 & -1 & 1 \cr
1 & 3 & -2 \cr
3 & 1 & 1
\end{array} \right)
\left( \begin{array}{c}
x \cr
y \cr
z
\end{array} \right)
=
\left( \begin{array}{c}
4 \cr
1 \cr
7
\end{array} \right)
$$

**Steps & Detailed Explanation:**

A linear system can be represented by the matrix equation $Ax = b$, where:
- $A$ is the coefficient matrix, containing the numbers multiplying the variables.
- $x$ is the column vector of unknowns.
- $b$ is the column vector of the right-hand side constants.

Extracting these from the given system:

The coefficient matrix $A$ is formed by aligning the coefficients of $x$, $y$, and $z$ in columns:

$$
A = 
\left( \begin{array}{ccc}
2 & -1 & 1 \cr
1 & 3 & -2 \cr
3 & 1 & 1
\end{array} \right)
$$

The vector of unknowns $x$ and the right-hand side vector $b$ are:

$$
x = 
\left( \begin{array}{c}
x \cr
y \cr
z
\end{array} \right), 
\qquad 
b = 
\left( \begin{array}{c}
4 \cr
1 \cr
7
\end{array} \right)
$$

When you multiply the matrix $A$ by the vector $x$ using the standard row-by-column matrix multiplication, the first row of $A$ multiplies the column $x$ to give $2x - y + z$. This must equal the first entry of $b$, which is $4$. Thus, each horizontal row in the matrix multiplication reproduces exactly one equation from the original system.