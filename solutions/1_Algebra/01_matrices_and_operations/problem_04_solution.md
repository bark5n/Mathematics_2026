**Result:**

$$ AB= \begin{pmatrix} 8 & 2 \\ 3 & 1 \\ \end{pmatrix} ,\qquad BA= \begin{pmatrix} 2 & 4 \\ 3 & 7 \\ \end{pmatrix} . $$

Thus, $AB\ne BA$.

**Steps & Detailed Explanation:**

To find an entry of a matrix product, take the dot product of a row of the first matrix with a column of the second matrix. For $AB$,

$$ AB= \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 3 & 1 \\ \end{pmatrix} = \begin{pmatrix} 1\cdot2+2\cdot3 & 1\cdot0+2\cdot1 \\ 0\cdot2+1\cdot3 & 0\cdot0+1\cdot1 \\ \end{pmatrix} = \begin{pmatrix} 8 & 2 \\ 3 & 1 \\ \end{pmatrix} . $$

For $BA$, reverse the order of the factors and calculate again:

$$ BA= \begin{pmatrix} 2 & 0 \\ 3 & 1 \\ \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ \end{pmatrix} = \begin{pmatrix} 2\cdot1+0\cdot0 & 2\cdot2+0\cdot1 \\ 3\cdot1+1\cdot0 & 3\cdot2+1\cdot1 \\ \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 3 & 7 \\ \end{pmatrix} . $$

The results differ, for example in their top-left entries: $8\ne2$. Noncommutativity means matrix multiplication does not generally satisfy the commutative rule $AB=BA$. The order of the factors must be preserved; in applications, the two orders can represent different sequences of transformations.
