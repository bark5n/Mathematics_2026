### Essential Formulas

**Determinant of a Parameter-Dependent $2 \times 2$ Matrix:**
For a matrix

$$
A(t) = \begin{pmatrix}
a(t) & b(t) \\
c(t) & d(t) \\
\end{pmatrix}
$$

the determinant is:

$$
\det A(t) = a(t)d(t) - b(t)c(t)
$$

**Invertibility and Inverse Formula:**
The matrix $A(t)$ is invertible if and only if $\det A(t) \neq 0$.
When invertible, its inverse is given by:

$$
A(t)^{-1} = \frac{1}{\det A(t)} \begin{pmatrix}
d(t) & -b(t) \\
-c(t) & a(t) \\
\end{pmatrix}
$$

---

### Problem Statement

**Exercise 11. Parameter and Invertibility**

For

$$
A(t)=
\begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
$$

find all $t$ for which the matrix is invertible, and then give a formula for $A(t)^{-1}$. Explain what happens to this formula at the excluded values.

> **Why this exercise:** combines a parameter, determinant, and an explicit inverse formula in one problem.

---

### Solution

**Step 1: Compute $\det A(t)$**

Given

$$
A(t) = \begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
$$

Compute the determinant:

$$
\begin{aligned}
\det A(t) &= (1)(1) - (t)(t) \\
&= 1 - t^2
\end{aligned}
$$

**Step 2: Determine values of $t$ for which $A(t)$ is invertible**

The matrix $A(t)$ is invertible if and only if $\det A(t) \neq 0$:

$$
1 - t^2 \neq 0 \iff t^2 \neq 1 \iff t \neq 1 \quad \mathrm{and} \quad t \neq -1
$$

In set notation, $A(t)$ is invertible for all $t \in \mathbb{R} \setminus \{-1, 1\}$.

**Step 3: Construct the formula for $A(t)^{-1}$**

For $t \neq \pm 1$, use the $2 \times 2$ matrix inverse formula:

$$
\begin{aligned}
A(t)^{-1} &= \frac{1}{\det A(t)} \begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix} \\
&= \frac{1}{1 - t^2} \begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{1 - t^2} & -\frac{t}{1 - t^2} \\
-\frac{t}{1 - t^2} & \frac{1}{1 - t^2} \\
\end{pmatrix}
\end{aligned}
$$

**Step 4: Explain what happens at the excluded values**

* At $t = 1$ and $t = -1$, the determinant becomes zero ($1 - (\pm 1)^2 = 0$). In the inverse formula, this causes a division by zero:

$$
  \frac{1}{0}
$$

  which is undefined, so the formula breaks down and no inverse exists.
* **Structural breakdown at $t = 1$:**

$$
  A(1) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ \end{pmatrix}
$$

  Here $R_2 = R_1$, so the rows are identical and linearly dependent.
* **Structural breakdown at $t = -1$:**

$$
  A(-1) = \begin{pmatrix} 1 & -1 \\ -1 & 1 \\ \end{pmatrix}
$$

  Here $R_2 = -R_1$, so the rows are exact opposites and linearly dependent.
* In both cases, the transformation squashes the 2-dimensional plane onto a 1-dimensional line, so information is destroyed and the mapping cannot be inverted.

---

### Final Answer

1. Range of invertibility:

$$
t \in \mathbb{R} \setminus \{-1, 1\} \quad (t \neq 1 \quad \mathrm{and} \quad t \neq -1)
$$

2. Formula for the inverse:

$$
A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix}
$$

3. Excluded values:
At $t = \pm 1$, $\det A(t) = 0$, leading to division by zero in the formula. The rows become linearly dependent ($R_1 = \pm R_2$), meaning the matrix is singular and has no inverse.
