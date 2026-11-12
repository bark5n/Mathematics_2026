### Essential Formulas

**Upper and Lower Triangular Matrices:**
An $n \times n$ matrix $U = (u_{ij})$ is **upper triangular** if all entries below its main diagonal are zero ($u_{ij} = 0$ for all $i > j$). An $n \times n$ matrix $L = (l_{ij})$ is **lower triangular** if all entries above its main diagonal are zero ($l_{ij} = 0$ for all $i < j$).

**Determinant of a Triangular Matrix:**
For any $n \times n$ upper triangular, lower triangular, or diagonal matrix $T = (t_{ij})$, the determinant equals the product of its main diagonal entries:

$$
\det T = t_{11} t_{22} \cdots t_{nn} = \prod_{i=1}^{n} t_{ii}
$$

---

### Problem Statement

**Exercise 4. Triangular Matrix**

Without expanding the determinant, compute

$$
\det
\begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}.
$$

State the rule for an arbitrary triangular matrix and explain it using this example.

> **Why this exercise:** reinforces an important property of triangular matrices.

---

### Solution

**Step 1: Identify the triangular structure of the matrix**

Denote the given matrix by $A$:

$$
A = \begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}
$$

Every entry strictly below the main diagonal is zero ($a_{21} = 0$, $a_{31} = 0$, and $a_{32} = 0$). Therefore, $A$ is an **upper triangular matrix**.

**Step 2: Compute $\det A$ using the triangular matrix rule**

Read off the main diagonal entries of $A$:

$$
a_{11} = 2, \qquad a_{22} = -3, \qquad a_{33} = 7
$$

Multiply the main diagonal entries together:

$$
\begin{aligned}
\det A &= a_{11} a_{22} a_{33} \\
&= 2 \cdot (-3) \cdot 7 \\
&= -6 \cdot 7 \\
&= -42
\end{aligned}
$$

**Step 3: State the general rule and explain why it holds using this example**

* **General rule:** The determinant of any $n \times n$ triangular matrix (whether upper triangular, lower triangular, or diagonal) is the product of all entries on its main diagonal:

$$
\det T = t_{11} t_{22} \cdots t_{nn}
$$

* **Explanation using this example:** By definition, a $3 \times 3$ determinant is a signed sum of products formed by choosing one entry from each row and one entry from each column:
  1. In row $3$ of $A$, the entries in columns $1$ and $2$ are both $0$, so the only nonzero choice is $a_{33} = 7$ in column $3$.
  2. Moving to row $2$, column $3$ is already used and $a_{21} = 0$, leaving $a_{22} = -3$ in column $2$ as the only nonzero choice.
  3. Moving to row $1$, columns $2$ and $3$ are already used, forcing the choice of $a_{11} = 2$ in column $1$.

  Every other combination of entries from distinct rows and columns picks up at least one zero from below the main diagonal and contributes $0$ to the sum. Thus, only the main diagonal product $2 \cdot (-3) \cdot 7 = -42$ remains.

**Step 4: Verification**

* **Row-scaling and elimination check:** Scaling each row by the reciprocal of its diagonal entry ($R_1 \leftarrow \frac{1}{2}R_1$, $R_2 \leftarrow -\frac{1}{3}R_2$, $R_3 \leftarrow \frac{1}{7}R_3$) multiplies $\det A$ by $\frac{1}{2} \cdot \left(-\frac{1}{3}\right) \cdot \frac{1}{7} = -\frac{1}{42}$ and yields a unit upper triangular matrix:

$$
U_1 = \begin{pmatrix}
1 & 2 & \frac{1}{2} \\
0 & 1 & -\frac{5}{3} \\
0 & 0 & 1 \\
\end{pmatrix}
$$

  Applying row replacements upward ($R_2 \leftarrow R_2 + \frac{5}{3}R_3$, then $R_1 \leftarrow R_1 - \frac{1}{2}R_3$, then $R_1 \leftarrow R_1 - 2R_2$) preserves the determinant and reduces $U_1$ to the identity matrix $I_3$, which has $\det I_3 = 1$. Hence $-\frac{1}{42}\det A = 1$, confirming $\det A = -42$.
* **Invertibility consistency check:** A triangular matrix is invertible if and only if none of its diagonal entries are zero. Here $2 \neq 0$, $-3 \neq 0$, and $7 \neq 0$, consistent with $\det A = -42 \neq 0$.

---

### Final Answer

1. **Computed determinant:**

$$
\det \begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}
= 2 \cdot (-3) \cdot 7 = -42
$$

2. **General rule for an arbitrary triangular matrix:** For any $n \times n$ upper or lower triangular matrix $T = (t_{ij})$, the determinant is the product of its main diagonal entries: $\det T = t_{11} t_{22} \cdots t_{nn}$.
3. **Explanation:** Any selection of one entry per row and column other than the main diagonal must include at least one zero entry from the zero triangle below the diagonal, leaving only the product of the main diagonal entries $2$, $-3$, and $7$.
