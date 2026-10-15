**Result:**

- $A$ has size $2 \times 3$, and $B$ has size $3 \times 2$.
- $a_{12} = -1$, $a_{23} = 5$, $b_{21} = -2$, and $b_{32} = 4$.
- The second row of $A$ is $(0, 4, 5)$.
- The first column of $B$ is $(1, -2, 4)^T$.

**Steps & Detailed Explanation:**

The size of a matrix is written as (number of rows) $\times$ (number of columns). Matrix $A$ has two rows and three columns, so its size is $2 \times 3$. Matrix $B$ has three rows and two columns, so its size is $3 \times 2$.

For an entry $a_{ij}$, the first index $i$ identifies the row and the second index $j$ identifies the column. Reading the requested positions gives

$$
a_{12} = -1, \qquad a_{23} = 5.
$$

Applying the same row-then-column convention to $B$ gives

$$
b_{21} = -2, \qquad b_{32} = 4.
$$

The second row of $A$ consists of all entries in its second horizontal row, in order:

$$
(0, 4, 5).
$$

The first column of $B$ consists of the first entry from each row, read from top to bottom:

$$
\begin{pmatrix}
1 \\
-2 \\
4 \\
\end{pmatrix}
$$

This distinction between row and column is reflected in their vector notation: rows are naturally written horizontally, while columns are written vertically.