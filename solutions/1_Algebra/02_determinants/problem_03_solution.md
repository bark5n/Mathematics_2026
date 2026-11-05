### Essential Formulas

**Row Swap Property of Determinants:**
If matrix $B$ is obtained from matrix $A$ by interchanging any two rows (or two columns), the sign of the determinant changes:

$$
\det B = -\det A
$$

**Cofactor Expansion along a Column:**
For a $3 \times 3$ matrix, expanding along column $1$:

$$
\det A = a_{11} C_{11} + a_{21} C_{21} + a_{31} C_{31}
$$

where $C_{ij} = (-1)^{i+j} M_{ij}$.

---

### Problem Statement

**Exercise 3. Swapping Two Rows**

For

$$
A=
\begin{pmatrix}
1 & 2 & 0 \\
0 & 3 & 1 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

compute $\det A$. Then form a matrix $B$ by swapping the first and second rows of $A$.

First predict $\det B$ using a determinant property, and then verify your prediction by calculation.

> **Why this exercise:** gives a second classical calculation with a $3\times3$ determinant while teaching the precise effect of a row swap on the sign of the determinant.

---

### Solution

**Step 1: Compute $\det A$**

Given

$$
A =
\begin{pmatrix}
1 & 2 & 0 \\
0 & 3 & 1 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

Expanding along the first column, which contains a zero at position $(2,1)$:

$$
\begin{aligned}
\det A &= 1 \cdot \det \begin{pmatrix}
3 & 1 \\
1 & 1 \\
\end{pmatrix}
- 0 \cdot \det \begin{pmatrix}
2 & 0 \\
1 & 1 \\
\end{pmatrix}
+ 2 \cdot \det \begin{pmatrix}
2 & 0 \\
3 & 1 \\
\end{pmatrix} \\
&= 1 \cdot (3 \cdot 1 - 1 \cdot 1) - 0 + 2 \cdot (2 \cdot 1 - 0 \cdot 3) \\
&= 1 \cdot (3 - 1) + 2 \cdot (2 - 0) \\
&= 2 + 4 \\
&= 6
\end{aligned}
$$

**Step 2: Form matrix $B$ and predict $\det B$**

Matrix $B$ is formed by swapping row 1 and row 2 of $A$:

$$
B =
\begin{pmatrix}
0 & 3 & 1 \\
1 & 2 & 0 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

*Prediction:*
Because interchanging two rows negates the determinant:

$$
\det B = -\det A = -6
$$

**Step 3: Verify the prediction by direct calculation of $\det B$**

Compute $\det B$ by expanding along its first column:

$$
\begin{aligned}
\det B &= 0 \cdot \det \begin{pmatrix}
2 & 0 \\
1 & 1 \\
\end{pmatrix}
- 1 \cdot \det \begin{pmatrix}
3 & 1 \\
1 & 1 \\
\end{pmatrix}
+ 2 \cdot \det \begin{pmatrix}
3 & 1 \\
2 & 0 \\
\end{pmatrix} \\
&= 0 - 1 \cdot (3 \cdot 1 - 1 \cdot 1) + 2 \cdot (3 \cdot 0 - 1 \cdot 2) \\
&= -1 \cdot (3 - 1) + 2 \cdot (0 - 2) \\
&= -1(2) + 2(-2) \\
&= -2 - 4 \\
&= -6
\end{aligned}
$$

The direct calculation yields $-6$, which matches the prediction $\det B = -\det A = -6$.

---

### Final Answer

1. Determinant of $A$:

$$
\det A = 6
$$

2. Prediction and verified value for $B$:

$$
\det B = -6
$$
