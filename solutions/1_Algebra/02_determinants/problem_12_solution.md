### Essential Formulas

**Determinant-Preserving Row Replacement:**
Adding a scalar multiple of one row to a different row ($R_i \leftarrow R_i + cR_j$ for $i \neq j$) leaves the determinant unchanged:

$$
\det B = \det A
$$

**Row Interchange and Upper Triangular Determinant:**
Swapping two distinct rows ($R_i \leftrightarrow R_j$) multiplies the determinant by $-1$. Once reduced to an upper triangular matrix $U = (u_{ij})$, the determinant equals the product of its main diagonal entries:

$$
\det U = u_{11} u_{22} \cdots u_{nn}
$$

**Noninvertibility and Row Dependence Criterion:**
A square matrix $A \in \mathbb{R}^{n \times n}$ is not invertible (singular) if and only if $\det A = 0$, which occurs if and only if its rows are linearly dependent (in particular, if one row becomes zero or proportional to another row).

---

### Problem Statement

**Exercise 12. A Parameter Revealed by a Row Operation**

For

$$
A(t) = \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & t \\
0 & 1 & 1 \\
\end{pmatrix}
$$

find the values of $t$ for which the matrix is not invertible.

Before computing the determinant, perform the operation

$$
R_2 \leftarrow R_2 - 2R_1
$$

and use the resulting structure. At the end, explain what special thing happens to the rows for the value of the parameter you found.

> **Why this exercise:** combines a parameter, row operations, and recognition of dependence in one short argument.

---

### Solution

**Step 1: Perform the row replacement $R_2 \leftarrow R_2 - 2R_1$**

Subtract $2$ times row $1$ from row $2$:

$$
R_2 - 2R_1 = (2, 4, t) - 2(1, 2, 3) = (2 - 2, 4 - 4, t - 6) = (0, 0, t - 6)
$$

Denote the resulting matrix by $B(t)$:

$$
B(t) = \begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & t - 6 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

Because $R_2 \leftarrow R_2 - 2R_1$ is a row replacement operation, it does not change the determinant:

$$
\det B(t) = \det A(t)
$$

**Step 2: Use the structure of $B(t)$ to compute $\det A(t)$**

In $B(t)$, rows $2$ and $3$ have zeros in column $1$. Interchanging row $2$ and row $3$ ($R_2 \leftrightarrow R_3$) yields an upper triangular matrix $U(t)$ while multiplying the determinant by $-1$:

$$
U(t) = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & t - 6 \\
\end{pmatrix}
$$

The determinant of the upper triangular matrix $U(t)$ is the product of its main diagonal entries $1$, $1$, and $t - 6$:

$$
\begin{aligned}
\det A(t) &= \det B(t) \\
&= -\det U(t) \\
&= -(1 \cdot 1 \cdot (t - 6)) \\
&= 6 - t
\end{aligned}
$$

**Step 3: Find the parameter value for which $A(t)$ is not invertible**

A square matrix $A(t)$ is not invertible if and only if $\det A(t) = 0$:

$$
6 - t = 0 \implies t = 6
$$

Thus, $t = 6$ is the unique value of $t$ for which $A(t)$ is not invertible.

**Step 4: Explain what happens to the rows when $t = 6$**

Substituting $t = 6$ into both $B(t)$ and the original matrix $A(t)$ reveals the exact structural dependence:

* In $B(6)$, the second row $(0, 0, t - 6)$ becomes $(0, 0, 0)$, an entire row of zeros:

$$
B(6) = \begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & 0 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

* In the original matrix $A(6)$, the second row $(2, 4, 6)$ becomes an exact scalar multiple of the first row $(1, 2, 3)$:

$$
A(6) = \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 1 \\
\end{pmatrix},
\qquad
R_2 = 2R_1
$$

Because $R_2 = 2R_1$, the first two rows are linearly dependent (proportional), reducing the rank of $A(6)$ from $3$ to $2$ and making the matrix singular.

**Step 5: Verification**

* **Sarrus' rule check on $A(t)$:**
  * Downward diagonal products:

$$
S_+ = 1 \cdot 4 \cdot 1 + 2 \cdot t \cdot 0 + 3 \cdot 2 \cdot 1 = 4 + 0 + 6 = 10
$$

  * Upward diagonal products:

$$
S_- = 0 \cdot 4 \cdot 3 + 1 \cdot t \cdot 1 + 1 \cdot 2 \cdot 2 = 0 + t + 4 = t + 4
$$

  * Subtracting gives $\det A(t) = S_+ - S_- = 10 - (t + 4) = 6 - t$, which equals $0$ if and only if $t = 6$.

* **Nontrivial null-space vector check at $t = 6$:**
  For $x = \begin{pmatrix} -1 \\ -1 \\ 1 \\ \end{pmatrix} \neq 0$,

$$
A(6)x = \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
-1 \\
-1 \\
1 \\
\end{pmatrix}
= \begin{pmatrix}
-1 - 2 + 3 \\
-2 - 4 + 6 \\
0 - 1 + 1 \\
\end{pmatrix}
= \begin{pmatrix}
0 \\
0 \\
0 \\
\end{pmatrix}
$$

  confirming that $A(6)$ maps a nonzero vector to $0$ and therefore has no inverse.

---

### Final Answer

1. **Matrix after $R_2 \leftarrow R_2 - 2R_1$:**

$$
B(t) = \begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & t - 6 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

2. **Parameter value for noninvertibility:** $\det A(t) = 6 - t = 0$ yields

$$
t = 6
$$

3. **Behavior of the rows at $t = 6$:** In $B(6)$, the second row becomes a zero row $(0, 0, 0)$. In the original matrix $A(6)$, the second row $(2, 4, 6)$ becomes twice the first row $(1, 2, 3)$ ($R_2 = 2R_1$), making the rows linearly dependent.
