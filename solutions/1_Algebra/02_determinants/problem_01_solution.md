### Essential Formulas

**Determinant of a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix $A$, the determinant is given by the product of the main diagonal entries minus the product of the off-diagonal entries:

$$
\det A = \det \begin{pmatrix} a & b \\ c & d \\ \end{pmatrix} = ad - bc
$$

**Invertibility and Determinant:**
A square matrix $A$ is invertible (non-singular) if and only if its determinant is nonzero:

$$
\det A \neq 0 \iff \exists A^{-1}
$$

If $\det A = 0$, the matrix is singular and has no inverse.

---

### Problem Statement

**Exercise 1. Determinant of a 2×2 Matrix**

Compute

$$
\det
\begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix},\qquad \det
\begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}.
$$

Which matrix is invertible? Justify your answer.

> **Why this exercise:** introduces the simplest determinant calculation and immediately connects it with invertibility.

---

### Solution

**Step 1: Compute the determinant of the first matrix**

For the first matrix $A$:

$$
A = \begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix}

$$

Using the formula $\det A = ad - bc$:

$$

\begin{aligned}
\det A &= (3)(4) - (-2)(5) \\
&= 12 - (-10) \\
&= 12 + 10 \\
&= 22
\end{aligned}

$$

**Step 2: Compute the determinant of the second matrix**

For the second matrix $B$:

$$

B = \begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}

$$

Using the formula $\det B = ad - bc$:

$$

\begin{aligned}
\det B &= (1)(14) - (7)(2) \\
&= 14 - 14 \\
&= 0
\end{aligned}

$$

**Step 3: Determine invertibility and justify**

* For matrix $A$, $\det A = 22 \neq 0$. Therefore, matrix $A$ is invertible.
* For matrix $B$, $\det B = 0$. Therefore, matrix $B$ is not invertible (singular).

Notice also that the second row of $B$ is a scalar multiple of the first row: $R_2 = 2R_1$. Linearly dependent rows always produce a zero determinant.

---

### Final Answer

1. Determinant values:

$$

\det
\begin{pmatrix}
3 & -2 \\
5 & 4 \\
\end{pmatrix}
= 22

$$

$$

\det
\begin{pmatrix}
1 & 7 \\
2 & 14 \\
\end{pmatrix}
= 0

$$

2. Invertibility:
The first matrix is invertible because its determinant is nonzero ($\det \neq 0$). The second matrix is not invertible because its determinant is zero ($\det = 0$).
