### Essential Formulas

**Determinant of a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix

$$
M = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

its determinant is given by:

$$
\det M = ad - bc
$$

**Singular (Noninvertible) Matrix Criterion:**
A square matrix $M \in \mathbb{R}^{n \times n}$ is **not invertible** (singular) if and only if its determinant equals zero:

$$
\det M = 0
$$

Equivalently, $\det M = 0$ holds if and only if the rows (and columns) of $M$ are linearly dependent, in which case no matrix $M^{-1}$ exists such that $M M^{-1} = I_n$.

**Explicit $2 \times 2$ Inverse Formula:**
Whenever $\det M = ad - bc \neq 0$, the inverse of $M$ is:

$$
M^{-1} = \frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 6. Parameter and Invertibility**

For

$$
A(t) = \begin{pmatrix}
t & 1 \\
2 & t \\
\end{pmatrix}
$$

find all values of $t$ for which the matrix is not invertible. Explain how your answer is related to the determinant being zero.

> **Why this exercise:** shows how the determinant can be used to study a family of matrices depending on a parameter.

---

### Solution

**Step 1: Compute $\det A(t)$ as a function of $t$**

Apply the $2 \times 2$ determinant formula $\det M = ad - bc$ with $a = t$, $b = 1$, $c = 2$, and $d = t$:

$$
\begin{aligned}
\det A(t) &= \det \begin{pmatrix}
t & 1 \\
2 & t \\
\end{pmatrix} \\
&= t \cdot t - 1 \cdot 2 \\
&= t^2 - 2
\end{aligned}
$$

**Step 2: Solve $\det A(t) = 0$ to find the noninvertible parameter values**

Set the determinant equal to zero:

$$
t^2 - 2 = 0
$$

Solve for $t$:

$$
t^2 = 2 \implies t = \sqrt{2} \quad \mathrm{or} \quad t = -\sqrt{2}
$$

Thus, $A(t)$ is not invertible for $t = \sqrt{2}$ and $t = -\sqrt{2}$ (over $\mathbb{R}$).

**Step 3: Explain the connection to the determinant being zero**

A square matrix $A(t)$ fails to be invertible precisely when $\det A(t) = 0$ for two equivalent algebraic and structural reasons:

1. **Failure of the inverse formula:** For any $t \neq \pm\sqrt{2}$, $\det A(t) = t^2 - 2 \neq 0$, and the inverse matrix is explicitly

$$
A(t)^{-1} = \frac{1}{t^2 - 2}
\begin{pmatrix}
t & -1 \\
-2 & t \\
\end{pmatrix}
$$

   When $t = \pm\sqrt{2}$, the denominator $\det A(t) = t^2 - 2$ vanishes, so division by $\det A(t)$ is impossible and no inverse matrix exists.

2. **Linear dependence of rows and columns:** When $\det A(t) = 0$, the rows of $A(t)$ become scalar multiples of one another:
   * At $t = \sqrt{2}$, row $2$ is $\sqrt{2}$ times row $1$: $(2, \sqrt{2}) = \sqrt{2}(\sqrt{2}, 1)$.
   * At $t = -\sqrt{2}$, row $2$ is $-\sqrt{2}$ times row $1$: $(2, -\sqrt{2}) = -\sqrt{2}(-\sqrt{2}, 1)$.

   Because the rows are linearly dependent, $A(\pm\sqrt{2})$ has rank $1 < 2$ and maps nonzero vectors (such as $(1, -\sqrt{2})^T$ for $t = \sqrt{2}$) to the zero vector, making it impossible to recover inputs uniquely via an inverse matrix.

**Step 4: Verification**

* **Direct substitution at $t = \sqrt{2}$:**

$$
A(\sqrt{2}) = \begin{pmatrix}
\sqrt{2} & 1 \\
2 & \sqrt{2} \\
\end{pmatrix},
\qquad
\det A(\sqrt{2}) = (\sqrt{2})(\sqrt{2}) - 1 \cdot 2 = 2 - 2 = 0
$$

  Multiplying $A(\sqrt{2})$ by the nonzero vector $v_1 = \begin{pmatrix} 1 \\ -\sqrt{2} \\ \end{pmatrix}$ gives

$$
A(\sqrt{2}) v_1 = \begin{pmatrix}
\sqrt{2} & 1 \\
2 & \sqrt{2} \\
\end{pmatrix}
\begin{pmatrix}
1 \\
-\sqrt{2} \\
\end{pmatrix}
= \begin{pmatrix}
\sqrt{2} - \sqrt{2} \\
2 - 2 \\
\end{pmatrix}
= \begin{pmatrix}
0 \\
0 \\
\end{pmatrix}
$$

  confirming that $A(\sqrt{2})$ has a nontrivial null space and is not invertible.

* **Direct substitution at $t = -\sqrt{2}$:**

$$
A(-\sqrt{2}) = \begin{pmatrix}
-\sqrt{2} & 1 \\
2 & -\sqrt{2} \\
\end{pmatrix},
\qquad
\det A(-\sqrt{2}) = (-\sqrt{2})(-\sqrt{2}) - 1 \cdot 2 = 2 - 2 = 0
$$

  Multiplying $A(-\sqrt{2})$ by the nonzero vector $v_2 = \begin{pmatrix} 1 \\ \sqrt{2} \\ \end{pmatrix}$ gives

$$
A(-\sqrt{2}) v_2 = \begin{pmatrix}
-\sqrt{2} & 1 \\
2 & -\sqrt{2} \\
\end{pmatrix}
\begin{pmatrix}
1 \\
\sqrt{2} \\
\end{pmatrix}
= \begin{pmatrix}
-\sqrt{2} + \sqrt{2} \\
2 - 2 \\
\end{pmatrix}
= \begin{pmatrix}
0 \\
0 \\
\end{pmatrix}
$$

  confirming that $A(-\sqrt{2})$ is also not invertible.

---

### Final Answer

1. **Parameter values for which $A(t)$ is not invertible:**

$$
t = \sqrt{2} \qquad \mathrm{and} \qquad t = -\sqrt{2}
$$

2. **Connection to $\det A(t) = 0$:** A square matrix is invertible if and only if its determinant is nonzero. Setting $\det A(t) = t^2 - 2 = 0$ identifies the exact parameter values $t = \pm\sqrt{2}$ at which the rows of $A(t)$ become linearly dependent and the inverse $A(t)^{-1}$ fails to exist.
