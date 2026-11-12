## Exercise 2. Addition and Scalar Multiplication

### Essential Formulas

**Matrix Addition and Subtraction:**
For matrices of the same size $m \times n$:

$$
A \pm B =
\begin{pmatrix}
a_{11} \pm b_{11} & \cdots & a_{1n} \pm b_{1n} \\
\vdots & \ddots & \vdots \\
a_{m1} \pm b_{m1} & \cdots & a_{mn} \pm b_{mn} \\
\end{pmatrix}
$$

**Scalar Multiplication:**

$$
cA =
\begin{pmatrix}
ca_{11} & \cdots & ca_{1n} \\
\vdots & \ddots & \vdots \\
ca_{m1} & \cdots & ca_{mn} \\
\end{pmatrix}
$$

### Problem Statement

For

$$
A =
\begin{pmatrix}
1 & 2 \\
-1 & 3 \\
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
4 & -2 \\
0 & 5 \\
\end{pmatrix}
$$

compute $A+B$, $A-B$, and $3A-2B$. Explain why matrix addition is possible only for matrices of the same size.

### Solution

**Step 1: Compute $A+B$**

$$
A + B =
\begin{pmatrix}
1+4 & 2+(-2) \\
-1+0 & 3+5 \\
\end{pmatrix}
=
\begin{pmatrix}
5 & 0 \\
-1 & 8 \\
\end{pmatrix}
$$

**Step 2: Compute $A-B$**

$$
A - B =
\begin{pmatrix}
1-4 & 2-(-2) \\
-1-0 & 3-5 \\
\end{pmatrix}
=
\begin{pmatrix}
-3 & 4 \\
-1 & -2 \\
\end{pmatrix}
$$

**Step 3: Compute $3A-2B$**

$$
3A - 2B =
\begin{pmatrix}
3(1)-2(4) & 3(2)-2(-2) \\
3(-1)-2(0) & 3(3)-2(5) \\
\end{pmatrix}
=
\begin{pmatrix}
-5 & 10 \\
-3 & -1 \\
\end{pmatrix}
$$

**Step 4: Explanation**

Matrix addition operates entry by entry, pairing each $a_{ij}$ with $b_{ij}$. If two matrices have different dimensions, some entries will have no corresponding partner to add to, leaving the operation undefined.

### Final Answer

$$
A+B =
\begin{pmatrix}
5 & 0 \\
-1 & 8 \\
\end{pmatrix},
\qquad
A-B =
\begin{pmatrix}
-3 & 4 \\
-1 & -2 \\
\end{pmatrix},
\qquad
3A-2B =
\begin{pmatrix}
-5 & 10 \\
-3 & -1 \\
\end{pmatrix}
$$
