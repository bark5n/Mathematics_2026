### Essential Formulas

**Determinant Criterion for Unique Solutions of $Ax = b$:**
Let $A \in \mathbb{R}^{n \times n}$ be a square coefficient matrix and $b \in \mathbb{R}^n$ be any right-hand side vector. The linear system $Ax = b$ has a unique solution $x = A^{-1}b$ for every $b \in \mathbb{R}^n$ if and only if $A$ is invertible, which is equivalent to:

$$
\det A \neq 0
$$

**Behavior of a Square System When $\det A = 0$:**
When $\det A = 0$, the matrix $A$ is singular (not invertible), and the linear system $Ax = b$ never has a unique solution. Instead, depending on whether $b$ lies in the column space of $A$:

* **Infinitely many solutions:** Occurs when the augmented matrix $\begin{pmatrix} A & \mid & b \\ \end{pmatrix}$ is consistent (no contradictory row of the form $\begin{pmatrix} 0 & \cdots & 0 & \mid & c \\ \end{pmatrix}$ with $c \neq 0$).
* **No solution (inconsistent):** Occurs when row reduction produces a row $\begin{pmatrix} 0 & \cdots & 0 & \mid & c \\ \end{pmatrix}$ with $c \neq 0$.

---

### Problem Statement

**Exercise 14. A System of Equations and the Determinant**

Consider the system $Ax = b$, where

$$
A = \begin{pmatrix}
1 & 2 \\
k & 4 \\
\end{pmatrix}.
$$

For which values of $k$ does the system have exactly one solution for every $b$? For the remaining value, give an example of a right-hand side $b$ for which the system has infinitely many solutions, and an example for which it has no solution.

> **Why this exercise:** connects the determinant with uniqueness of solutions and requires distinguishing the exceptional cases.

---

### Solution

**Step 1: Compute $\det A$ and determine when the system has a unique solution**

Compute the determinant of the $2 \times 2$ coefficient matrix $A$:

$$
\begin{aligned}
\det A &= \det \begin{pmatrix}
1 & 2 \\
k & 4 \\
\end{pmatrix} \\
&= 1 \cdot 4 - 2 \cdot k \\
&= 4 - 2k
\end{aligned}
$$

The system $Ax = b$ has a unique solution for every $b \in \mathbb{R}^2$ if and only if $A$ is invertible, that is, $\det A \neq 0$:

$$
4 - 2k \neq 0 \iff 2k \neq 4 \iff k \neq 2
$$

Therefore, for every real number $k \neq 2$, the matrix $A$ is invertible and $Ax = b$ has the unique solution $x = A^{-1}b$ for any $b \in \mathbb{R}^2$.

**Step 2: Analyze the remaining value $k = 2$**

For the single remaining parameter value $k = 2$, $\det A = 0$ and the matrix $A$ becomes:

$$
A = \begin{pmatrix}
1 & 2 \\
2 & 4 \\
\end{pmatrix}
$$

Write out the system $Ax = b$ for $x = (x_1, x_2)^T$ and $b = (b_1, b_2)^T$:

$$
\begin{cases}
x_1 + 2x_2 = b_1, \\
2x_1 + 4x_2 = b_2.
\end{cases}
$$

Form the augmented matrix and perform the row replacement $R_2 \leftarrow R_2 - 2R_1$:

$$
\begin{pmatrix}
1 & 2 & \mid & b_1 \\
2 & 4 & \mid & b_2 \\
\end{pmatrix}
\longrightarrow
\begin{pmatrix}
1 & 2 & \mid & b_1 \\
0 & 0 & \mid & b_2 - 2b_1 \\
\end{pmatrix}
$$

The second equation simplifies to $0 = b_2 - 2b_1$, which splits the behavior at $k = 2$ into two mutually exclusive cases:

* **Infinitely many solutions ($b_2 = 2b_1$):** Both equations reduce to the single equation $x_1 + 2x_2 = b_1$. Letting $x_2 = t \in \mathbb{R}$ be a free parameter gives $x_1 = b_1 - 2t$, yielding infinitely many solutions.
* **No solution ($b_2 \neq 2b_1$):** The second equation becomes $0 = b_2 - 2b_1 \neq 0$, which is impossible, so the system is inconsistent.

**Step 3: Construct concrete examples of $b$ for $k = 2$**

1. **Example with infinitely many solutions:**
   Choose $b_1 = 1$ and $b_2 = 2b_1 = 2$, so

$$
b = \begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
$$

   With this right-hand side, the system is

$$
\begin{cases}
x_1 + 2x_2 = 1, \\
2x_1 + 4x_2 = 2.
\end{cases}
$$

   The second equation is simply twice the first equation, so the solution set consists of all vectors

$$
x = \begin{pmatrix}
1 - 2t \\
t \\
\end{pmatrix},
\qquad
t \in \mathbb{R}
$$

   which contains infinitely many solutions.

2. **Example with no solution:**
   Choose $b_1 = 1$ and $b_2 = 3 \neq 2b_1$, so

$$
b = \begin{pmatrix}
1 \\
3 \\
\end{pmatrix}
$$

   With this right-hand side, the system is

$$
\begin{cases}
x_1 + 2x_2 = 1, \\
2x_1 + 4x_2 = 3.
\end{cases}
$$

   Multiplying the first equation by $2$ gives $2x_1 + 4x_2 = 2$, which contradicts $2x_1 + 4x_2 = 3$. Hence no solution exists.

**Step 4: Verification**

* **Check unique solution formula for $k \neq 2$:**
  When $k \neq 2$, $\det A = 4 - 2k \neq 0$ and

$$
A^{-1} = \frac{1}{4 - 2k}
\begin{pmatrix}
4 & -2 \\
-k & 1 \\
\end{pmatrix}
$$

  Multiplying $A$ by $x = A^{-1}b$ gives $A(A^{-1}b) = I_2 b = b$ for every $b \in \mathbb{R}^2$, confirming existence and uniqueness.

* **Check the infinitely-many-solutions example at $k = 2$:**
  Substituting $x = \begin{pmatrix} 1 - 2t \\ t \\ \end{pmatrix}$ into $Ax$ for $k = 2$ gives

$$
\begin{pmatrix}
1 & 2 \\
2 & 4 \\
\end{pmatrix}
\begin{pmatrix}
1 - 2t \\
t \\
\end{pmatrix}
= \begin{pmatrix}
(1 - 2t) + 2t \\
2(1 - 2t) + 4t \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
$$

  for every real value of $t$ (for instance, $t = 0$ gives $(1, 0)^T$ and $t = 1$ gives $(-1, 1)^T$).

* **Check the no-solution example at $k = 2$:**
  For any vector $(x_1, x_2)^T \in \mathbb{R}^2$, the second component of $Ax$ is $2x_1 + 4x_2 = 2(x_1 + 2x_2)$, which is always twice the first component. Since $3 \neq 2 \cdot 1$, the vector $(1, 3)^T$ cannot be written in the form $Ax$.

---

### Final Answer

1. **Values of $k$ for a unique solution:** The system $Ax = b$ has exactly one solution for every $b \in \mathbb{R}^2$ if and only if $\det A = 4 - 2k \neq 0$, that is, for all

$$
k \neq 2
$$

2. **Examples for the remaining value $k = 2$:**
   * **Infinitely many solutions:** Take

$$
b = \begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
$$

     which yields the infinite solution family $x = \begin{pmatrix} 1 - 2t \\ t \\ \end{pmatrix}$ ($t \in \mathbb{R}$).

   * **No solution:** Take

$$
b = \begin{pmatrix}
1 \\
3 \\
\end{pmatrix}
$$

     which produces the inconsistent equations $x_1 + 2x_2 = 1$ and $2x_1 + 4x_2 = 3$ ($2 = 3$, contradiction).
