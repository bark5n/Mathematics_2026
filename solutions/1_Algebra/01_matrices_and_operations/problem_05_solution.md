## Exercise 5. Matrix Times Vector

### Essential Formulas

**Matrix-Vector Product as Column Combination:**
If $A$ has columns $c_1, c_2, \ldots, c_n$ and $x = (x_1, x_2, \ldots, x_n)^T$, then:

$$
Ax = x_1 c_1 + x_2 c_2 + \cdots + x_n c_n
$$

### Problem Statement

Let

$$
A =
\begin{pmatrix}
2 & -1 \\
1 & 3 \\
\end{pmatrix},
\qquad
x =
\begin{pmatrix}
4 \\
2 \\
\end{pmatrix}
$$

Compute $Ax$. Then express $Ax$ as a linear combination of the columns of $A$, with coefficients coming from the vector $x$.

### Solution

**Step 1: Compute $Ax$ via dot products**

$$
Ax =
\begin{pmatrix}
2(4) + (-1)(2) \\
1(4) + 3(2) \\
\end{pmatrix}
=
\begin{pmatrix}
8 - 2 \\
4 + 6 \\
\end{pmatrix}
=
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
$$

**Step 2: Express as column combination**

Using the columns of $A$ and the entries of $x$:

$$
Ax =
4
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+
2
\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
=
\begin{pmatrix}
8 \\
4 \\
\end{pmatrix}
+
\begin{pmatrix}
-2 \\
6 \\
\end{pmatrix}
=
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
$$

### Final Answer

$$
Ax =
\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}
=
4
\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}
+
2
\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}
$$
