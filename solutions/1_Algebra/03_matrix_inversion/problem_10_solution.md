### Essential Formulas

**Determinant and Inverse of a Diagonal Matrix:**
For an $n \times n$ diagonal matrix

$$
D = \begin{pmatrix}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_n \\
\end{pmatrix}
$$

the determinant is the product of the diagonal entries:

$$
\det D = d_1 \cdot d_2 \cdots d_n = \prod_{i=1}^{n} d_i
$$

**Invertibility Condition for Diagonal Matrices:**
$D$ is invertible if and only if **all** diagonal entries are nonzero ($d_i \neq 0$ for all $i = 1, \dots, n$).
If invertible, its inverse is obtained by simply taking the reciprocal of each diagonal entry:

$$
D^{-1} = \begin{pmatrix}
\frac{1}{d_1} & 0 & \cdots & 0 \\
0 & \frac{1}{d_2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \frac{1}{d_n} \\
\end{pmatrix}
$$

If any diagonal entry is zero, $\det D = 0$, and no inverse exists.

---

### Problem Statement

**Exercise 10. Inverse of a Diagonal Matrix**

Given

$$
D=
\begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix},\qquad E=
\begin{pmatrix}
2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}.
$$

Without using Gauss–Jordan elimination, decide which matrix is invertible. For the invertible matrix, give the inverse and check the result by multiplication.

> **Why this exercise:** teaches how to recognize invertibility and the inverse without using a full procedure when the matrix structure gives the answer immediately.

---

### Solution

**Step 1: Determine invertibility using the diagonal structure**

* **For matrix $D$:**
  The diagonal entries are $2$, $-3$, and $5$. None of them are zero:

$$
\det D = (2)(-3)(5) = -30 \neq 0
$$

  Because its determinant is nonzero, matrix $D$ is invertible.

* **For matrix $E$:**
  The entry in row 2, column 2 is $e_{22} = 0$:

$$
\det E = (2)(0)(5) = 0
$$

  Because its determinant is zero (and row 2 consists entirely of zeros), matrix $E$ is singular and not invertible.

**Step 2: State the inverse $D^{-1}$**

For a diagonal matrix, each diagonal element $d_i$ operates independently on the $i$-th coordinate axis. Inverting each scalar factor:
* First diagonal entry: $\frac{1}{2}$
* Second diagonal entry: $\frac{1}{-3} = -\frac{1}{3}$
* Third diagonal entry: $\frac{1}{5}$

Therefore:

$$
D^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
$$

**Step 3: Check by multiplication**

Compute the matrix product $D D^{-1}$:

$$
\begin{aligned}
D D^{-1} &= \begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}
\begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix} \\
&= \begin{pmatrix}
2\left(\frac{1}{2}\right) + 0 + 0 & 0 + 0 + 0 & 0 + 0 + 0 \\
0 + 0 + 0 & (-3)\left(-\frac{1}{3}\right) + 0 + 0 & 0 + 0 + 0 \\
0 + 0 + 0 & 0 + 0 + 0 & 5\left(\frac{1}{5}\right) + 0 + 0 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix} \\
&= I_3
\end{aligned}
$$

The product equals the $3 \times 3$ identity matrix $I_3$, confirming the result.

---

### Final Answer

1. Invertibility:
Matrix $D$ is invertible ($\det D = -30 \neq 0$). Matrix $E$ is not invertible ($\det E = 0$ due to a zero on the diagonal).

2. Inverse of $D$:

$$
D^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\
0 & -\frac{1}{3} & 0 \\
0 & 0 & \frac{1}{5} \\
\end{pmatrix}
$$
