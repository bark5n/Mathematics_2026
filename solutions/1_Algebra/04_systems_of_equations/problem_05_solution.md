**Result:**

The system has infinitely many solutions. In parametric form:

$$ \begin{cases} x = 1 + 5t \\ y = 1 - 2t \\ z = t \end{cases} $$

The number of free variables is $1$, which corresponds to the number of columns without a pivot in the coefficient matrix.

**Steps & Detailed Explanation:**

The given augmented matrix is already in row echelon form:

$$ \begin{pmatrix} 1 & 2 & -1 & 3 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} $$

Look at the columns representing the variables (the first three columns). The first column has a pivot in the first row. The second column has a pivot in the second row. The third column does not contain a leading non-zero entry in any row. 

Because column 3 lacks a pivot, the variable $z$ is free. Let $z = t$. The number of freely chosen variables is exactly the total number of variables minus the number of pivots (or non-zero equations). Here, $3$ variables $- 2$ pivots $= 1$ free variable.

Use back-substitution to express the pivot variables in terms of the free variable $t$:

From the second row:
$$ y + 2z = 1 \implies y + 2t = 1 \implies y = 1 - 2t $$

From the first row:
$$ x + 2y - z = 3 $$
Substitute $y = 1 - 2t$ and $z = t$ into the equation:
$$ \begin{aligned} x + 2(1 - 2t) - t &= 3 \\ x + 2 - 4t - t &= 3 \\ x + 2 - 5t &= 3 \\ x &= 1 + 5t \end{aligned} $$
