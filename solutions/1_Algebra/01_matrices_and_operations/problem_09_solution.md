**Result:**

$$ RSx= \begin{pmatrix} -2 \\ 2 \end{pmatrix} ,\qquad SRx= \begin{pmatrix} -4 \\ 1 \end{pmatrix} . $$

The results are different, so the order of the scaling and rotation matters for this vector.

**Steps & Detailed Explanation:**

The vector is

$$ x= \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix} , $$

and the matrices are

$$ S= \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ \end{pmatrix} ,\qquad R= \begin{pmatrix} 0 & -1 \\ 1 & 0 \\ \end{pmatrix} . $$

For $RSx$, apply $S$ first because the rightmost matrix acts first:

$$ Sx= \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \\ \end{pmatrix} . $$

Then rotate the scaled vector counterclockwise by $90^\circ$:

$$ RSx=R(Sx)= \begin{pmatrix} 0 & -1 \\ 1 & 0 \\ \end{pmatrix} \begin{pmatrix} 2 \\ 2 \\ \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \\ \end{pmatrix} . $$

For $SRx$, rotate first:

$$ Rx= \begin{pmatrix} 0 & -1 \\ 1 & 0 \\ \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix} = \begin{pmatrix} -2 \\ 1 \\ \end{pmatrix} . $$

Next apply the scaling matrix. It doubles the first coordinate and leaves the second coordinate unchanged:

$$ SRx=S(Rx)= \begin{pmatrix} 2 & 0 \\ 0 & 1 \\ \end{pmatrix} \begin{pmatrix} -2 \\ 1 \\ \end{pmatrix} = \begin{pmatrix} -4 \\ 1 \\ \end{pmatrix} . $$

Geometrically, $S$ stretches horizontally while leaving vertical distances unchanged, whereas $R$ changes which direction is horizontal and which is vertical. If we stretch before rotating, the stretched horizontal component is rotated into the vertical direction. If we rotate first, the vector's horizontal component after rotation is the one that gets stretched. Thus these transformations do not commute: in general, $RS\ne SR$.
