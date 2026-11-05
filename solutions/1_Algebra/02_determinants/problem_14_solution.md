### Essential Formulas

**Determinant of a $2 \times 2$ Matrix:**

$$
\det \begin{pmatrix} a & b \\ c & d \\ \end{pmatrix} = ad - bc
$$

**Cramer's Rule / Invertibility Criterion for $Ax = b$:**
A linear system $Ax = b$ with a square matrix $A$ has a unique solution for every vector $b$ if and only if $A$ is invertible, which is equivalent to:

$$
\det A \neq 0
$$

When $\det A = 0$:
* If the augmented matrix $[A \mid b]$ has the same rank as $A$, the system is consistent and has infinitely many solutions.
* If the augmented matrix has a rank strictly greater than $\mathrm{rank}(A)$ (producing a row of the form $(0 \quad 0 \mid c)$ with $c \neq 0$), the system is inconsistent and has no solution.

---

### Problem Statement

**Exercise 14. A System of Equations and the Determinant**

Consider the system $Ax=b$, where

$$
A=
\begin{pmatrix}
1 & 2 \\
k & 4 \\
\end{pmatrix}.
$$

For which values of $k$ does the system have exactly one solution for every $b$? For the remaining value, give an example of a right-hand side $b$ for which the system has infinitely many solutions, and an example for which it has no solution.

> **Why this exercise:** connects the determinant with uniqueness of solutions and requires distinguishing the exceptional cases.

---

### Solution

**Step 1: Compute $\det A$ in terms of the parameter $k$**

Using the $2 \times 2$ determinant formula:

$$
\begin{aligned}
\det A &= (1)(4) - (2)(k) \\
&= 4 - 2k
\end{aligned}
$$

**Step 2: Determine when the system has a unique solution for every $b$**

The system $Ax = b$ has a unique solution for every right-hand side $b$ if and only if $A$ is invertible ($\det A \neq 0$):

$$
4 - 2k \neq 0 \iff 2k \neq 4 \iff k \neq 2
$$

Therefore, for all $k \neq 2$, the system has exactly one solution for any vector $b$.

**Step 3: Analyze the exceptional value $k = 2$**

Substitute $k = 2$ into the matrix $A$:

$$
A =
\begin{pmatrix}
1 & 2 \\
2 & 4 \\
\end{pmatrix}
$$

The system $Ax = b$ with $b = \begin{pmatrix} b_1 \\ b_2 \\ \end{pmatrix}$ corresponds to:

$$
\begin{cases}
x + 2y = b_1, \\
2x + 4y = b_2.
\end{cases}
$$

Notice that the left-hand side of the second equation is $2(x + 2y) = 2 \cdot (\mathrm{LHS}(E_1))$.

* **Infinitely many solutions:**
  For the system to be consistent, the right-hand sides must satisfy the same proportionality: $b_2 = 2b_1$.
  Let $b_1 = 1$, which requires $b_2 = 2$.
  Then:

$$
b = \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix}
$$

  The augmented matrix is:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 \\
2 & 4 & \mid & 2 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow R_2 - 2R_1}
\begin{pmatrix}
1 & 2 & \mid & 1 \\
0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

  The second equation is $0 = 0$, leaving $x = 1 - 2y$ with $y$ as a free parameter, giving infinitely many solutions.

* **No solution:**
  For the system to be inconsistent, choose a right-hand side where $b_2 \neq 2b_1$.
  Let $b_1 = 1$ and $b_2 = 3$.
  Then:

$$
b = \begin{pmatrix} 1 \\ 3 \\ \end{pmatrix}
$$

  The augmented matrix is:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 \\
2 & 4 & \mid & 3 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow R_2 - 2R_1}
\begin{pmatrix}
1 & 2 & \mid & 1 \\
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

  The second row yields the contradiction $0x + 0y = 1$, which is impossible ($0 = 1$). Thus the system has no solution.

---

### Final Answer

1. Value of $k$ for unique solution for every $b$:

$$
k \neq 2
$$

2. For $k = 2$:
   * **Infinitely many solutions example:**

$$
b = \begin{pmatrix} 1 \\ 2 \\ \end{pmatrix}
$$

   * **No solution example:**

$$
b = \begin{pmatrix} 1 \\ 3 \\ \end{pmatrix}
$$
