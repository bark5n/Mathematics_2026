**Result:**

The columns of $B$ are

$$
b_1=\begin{pmatrix}1\\-1\\3\end{pmatrix},\qquad
b_2=\begin{pmatrix}2\\0\\1\end{pmatrix}.
$$

Their images under $A$ are

$$
Ab_1=\begin{pmatrix}-1\\2\end{pmatrix},\qquad
Ab_2=\begin{pmatrix}2\\1\end{pmatrix}.
$$

Therefore,

$$
AB=
\begin{pmatrix}
-1 & 2 \\
2 & 1
\end{pmatrix}
=
\begin{pmatrix}Ab_1&Ab_2\end{pmatrix}.
$$

**Steps & Detailed Explanation:**

Write the matrices and the columns of $B$ explicitly:

$$
A=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&2\\-1&0\\3&1\end{pmatrix}
=\begin{pmatrix}b_1&b_2\end{pmatrix},
$$

where

$$
b_1=\begin{pmatrix}1\\-1\\3\end{pmatrix},\qquad
b_2=\begin{pmatrix}2\\0\\1\end{pmatrix}.
$$

1. Multiply $A$ by the first column:
	$$
	Ab_1=
	\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}
	\begin{pmatrix}1\\-1\\3\end{pmatrix}
	=\begin{pmatrix}1-2+0\\0-1+3\end{pmatrix}
	=\begin{pmatrix}-1\\2\end{pmatrix}.
	$$

2. Multiply $A$ by the second column:
	$$
	Ab_2=
	\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}
	\begin{pmatrix}2\\0\\1\end{pmatrix}
	=\begin{pmatrix}2+0+0\\0+0+1\end{pmatrix}
	=\begin{pmatrix}2\\1\end{pmatrix}.
	$$

3. To find $AB$, place these two resulting vectors side by side as its columns:
	$$
	AB=\begin{pmatrix}Ab_1&Ab_2\end{pmatrix}
	=\begin{pmatrix}-1&2\\2&1\end{pmatrix}.
	$$
	Direct multiplication confirms this result:
	$$
	\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}
	\begin{pmatrix}1&2\\-1&0\\3&1\end{pmatrix}
	=\begin{pmatrix}
	1-2+0 & 2+0+0 \\
	0-1+3 & 0+0+1
	\end{pmatrix}
	=\begin{pmatrix}-1&2\\2&1\end{pmatrix}.
	$$

The column rule follows directly from how matrix multiplication is defined. The $j$th column of $AB$ is obtained by multiplying $A$ by the $j$th column of $B$. Since the columns of $B$ are $b_1$ and $b_2$, the columns of $AB$ are exactly $Ab_1$ and $Ab_2$.
