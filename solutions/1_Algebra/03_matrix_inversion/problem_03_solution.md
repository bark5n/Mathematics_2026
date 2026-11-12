### Essential Formulas

**Determinant Criterion for Noninvertibility:**
A square matrix $A \in \mathbb{R}^{n \times n}$ is **not invertible** (singular) if and only if its determinant is zero:

$$
\det A = 0
$$

In particular, for a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \\ \end{pmatrix}$, $A^{-1}$ fails to exist if and only if $\det A = ad - bc = 0$.

**Row Dependence and Rank Criterion for Noninvertibility:**
An $n \times n$ matrix $A$ is not invertible if and only if its rows are linearly dependent (equivalently, $\mathrm{rank}(A) < n$). For a $2 \times 2$ matrix, its rows $R_1$ and $R_2$ are linearly dependent if and only if one row is a scalar multiple of the other ($R_1 = c R_2$ or $R_2 = c R_1$ for some $c \in \mathbb{R}$), in which case $A$ cannot be row-reduced to the $2 \times 2$ identity matrix $I_2$.

**Null-Space Obstruction to Invertibility:**
If there exists a nonzero vector $x \neq 0$ such that $Ax = 0$, then $A$ cannot have an inverse $A^{-1}$, because multiplying $Ax = 0$ on the left by $A^{-1}$ would force $x = A^{-1}0 = 0$.

---

### Problem Statement

**Exercise 3. When Does the Inverse Not Exist?**

For

$$
A = \begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
$$

explain in two ways why $A^{-1}$ does not exist: using the determinant and using dependence between the rows.

> **Why this exercise:** connects two signs of noninvertibility instead of treating them as unrelated facts.

---

### Solution

**Step 1: Way 1 — Explain noninvertibility using the determinant**

Compute the determinant of $A$ using the $2 \times 2$ formula $\det A = ad - bc$ with $a = 2$, $b = 4$, $c = 1$, and $d = 2$:

$$
\begin{aligned}
\det A &= \det \begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix} \\
&= 2 \cdot 2 - 4 \cdot 1 \\
&= 4 - 4 \\
&= 0
\end{aligned}
$$

Because $\det A = 0$, the matrix $A$ is singular and $A^{-1}$ does not exist. Specifically:

* **Multiplicative determinant contradiction:** If an inverse matrix $A^{-1}$ existed, then $A A^{-1} = I_2$ would imply

$$
(\det A)(\det A^{-1}) = \det I_2 \implies 0 \cdot \det(A^{-1}) = 1
$$

  which has no real solution.
* **Breakdown of the $2 \times 2$ inverse formula:** The explicit inverse formula $A^{-1} = \frac{1}{\det A}\begin{pmatrix} d & -b \\ -c & a \\ \end{pmatrix}$ would require dividing by $\det A = 0$, which is undefined.

**Step 2: Way 2 — Explain noninvertibility using linear dependence between the rows**

Label the two rows of $A$ as $R_1 = (2, 4)$ and $R_2 = (1, 2)$. Comparing corresponding entries shows that the first row is twice the second row:

$$
R_1 = 2R_2 \qquad \left(\mathrm{equivalently,} \quad R_1 - 2R_2 = (0, 0)\right)
$$

Because $R_1$ and $R_2$ are proportional, the rows of $A$ are **linearly dependent**, which prevents $A$ from being invertible for two equivalent structural reasons:

* **Failure of Gauss–Jordan reduction to $I_2$:** Applying the elementary row operation $R_1 \leftarrow R_1 - 2R_2$ produces an entire row of zeros:

$$
\begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
\longrightarrow
\begin{pmatrix}
0 & 0 \\
1 & 2 \\
\end{pmatrix}
$$

  No further elementary row operations can restore two pivot positions, so $A$ has $\mathrm{rank}(A) = 1 < 2$ and cannot be reduced to $I_2$.
* **Nontrivial solutions to $Ax = 0$:** Because the first equation $2x_1 + 4x_2 = 0$ is simply twice the second equation $x_1 + 2x_2 = 0$, the homogeneous system $Ax = 0$ reduces to the single condition $x_1 = -2x_2$. Choosing $x_2 = -1$ gives the nonzero vector $x = (2, -1)^T \neq 0$ satisfying $Ax = 0$. Since $A$ maps both $(2, -1)^T$ and $(0, 0)^T$ to $0$, the transformation $x \mapsto Ax$ is not one-to-one and cannot be inverted.

**Step 3: Verification**

* **Direct algebraic proof that no $2 \times 2$ matrix $B$ satisfies $AB = I_2$:**
  Suppose there existed a matrix

$$
B = \begin{pmatrix}
p & q \\
r & s \\
\end{pmatrix}
$$

  such that $AB = I_2$. Multiplying out $AB$ yields:

$$
\begin{aligned}
AB &= \begin{pmatrix}
2 & 4 \\
1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
p & q \\
r & s \\
\end{pmatrix} \\
&= \begin{pmatrix}
2p + 4r & 2q + 4s \\
p + 2r & q + 2s \\
\end{pmatrix}
\end{aligned}
$$

  Equating the first column of $AB$ to the first column of $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ \end{pmatrix}$ requires both:

$$
\begin{cases}
2p + 4r = 1, \\
p + 2r = 0.
\end{cases}
$$

  Substituting $p + 2r = 0$ into the first equation gives $2(p + 2r) = 2(0) = 0 = 1$, a contradiction. Thus no right inverse (and hence no inverse $A^{-1}$) exists.

* **Null-space vector check:**

$$
A\begin{pmatrix}
2 \\
-1 \\
\end{pmatrix}
= \begin{pmatrix}
2 \cdot 2 + 4 \cdot (-1) \\
1 \cdot 2 + 2 \cdot (-1) \\
\end{pmatrix}
= \begin{pmatrix}
4 - 4 \\
2 - 2 \\
\end{pmatrix}
= \begin{pmatrix}
0 \\
0 \\
\end{pmatrix}
$$

---

### Final Answer

1. **Using the determinant:** $\det A = 2 \cdot 2 - 4 \cdot 1 = 0$. A square matrix is invertible if and only if its determinant is nonzero, so $\det A = 0$ proves that $A^{-1}$ does not exist.
2. **Using row dependence:** The first row is twice the second row ($R_1 = 2R_2$), so the rows are linearly dependent and $\mathrm{rank}(A) = 1 < 2$. Consequently, $A$ row-reduces to a matrix with a zero row (never to $I_2$) and maps nonzero vectors such as $(2, -1)^T$ to $0$, making inversion impossible.
