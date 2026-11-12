### Essential Formulas

**Invalid Row Operations in Parametric Systems:**
When analyzing a system of equations with a parameter (e.g., $t$), one must avoid dividing a row by an expression containing $t$ (such as $t - 1$) unless one explicitly analyzes the case where that expression equals zero.

If an elimination step produces a row of the form:

$$
(0 \ \cdots \ 0 \mid d)
$$

where the left side evaluates to $0$ and the right side is a nonzero constant $d \neq 0$, the system is **inconsistent** (no solution) for that parameter value.

---

### Problem Statement

**Exercise 11. A Parameter in a System of Three Equations**

Analyze the number of solutions depending on $t$:

$$
\begin{cases}
x+y+z=1, \\
x+ty+z=2, \\
x+y+tz=3.
\end{cases}
$$

Use elimination and separately analyze the parameter values for which a standard calculation step ceases to be valid.

> **Why this exercise:** develops parametric analysis while still relying only on elimination.

---

### Solution

**Step 1: Set up the augmented matrix and perform initial elimination**

Write the augmented matrix for the system:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
1 & t & 1 & \mid & 2 \\
1 & 1 & t & \mid & 3 \\
\end{pmatrix}
$$

Use the $(1,1)$ entry as a pivot to eliminate the variables in the first column below it. Perform the row operations $R_2 \leftarrow R_2 - R_1$ and $R_3 \leftarrow R_3 - R_1$:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
0 & t-1 & 0 & \mid & 1 \\
0 & 0 & t-1 & \mid & 2 \\
\end{pmatrix}
$$

**Step 2: Identify the critical parameter value**

The matrix is now in row echelon form. The equations corresponding to the second and third rows are:

$$
\begin{aligned}
(t-1)y &= 1 \\
(t-1)z &= 2
\end{aligned}
$$

To solve for $y$ and $z$, we need to divide by $t-1$. This standard calculation step **ceases to be valid** when the denominator is zero, meaning when $t - 1 = 0 \implies t = 1$. We must split the analysis into two distinct cases.

**Step 3: Analyze Case 1 ($t = 1$)**

Substitute $t = 1$ directly into the row-reduced augmented matrix:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 1 \\
0 & 0 & 0 & \mid & 1 \\
0 & 0 & 0 & \mid & 2 \\
\end{pmatrix}
$$

The second row reads $0x + 0y + 0z = 1 \implies 0 = 1$.
The third row reads $0x + 0y + 0z = 2 \implies 0 = 2$.
These are blatant contradictions. Therefore, for $t = 1$, the system has **no solution**.

**Step 4: Analyze Case 2 ($t \neq 1$)**

If $t \neq 1$, then $t - 1 \neq 0$, and division by $t-1$ is mathematically valid. We can uniquely determine $y$ and $z$:

$$
\begin{aligned}
y &= \frac{1}{t-1} \\
z &= \frac{2}{t-1}
\end{aligned}
$$

Substitute $y$ and $z$ back into the first row's equation $x + y + z = 1$ to find $x$:

$$
\begin{aligned}
x + \frac{1}{t-1} + \frac{2}{t-1} &= 1 \\
x + \frac{3}{t-1} &= 1 \\
x &= 1 - \frac{3}{t-1} \\
x &= \frac{t-1-3}{t-1} \\
x &= \frac{t-4}{t-1}
\end{aligned}
$$

Because every variable is uniquely determined, the system has **exactly one solution** for any $t \neq 1$.

---

### Final Answer

Based on the elimination steps yielding $(t-1)y=1$ and $(t-1)z=2$, the division by $t-1$ requires splitting the parameter:

1. **For $t = 1$:** The division is invalid. The reduced matrix produces contradictory rows ($0=1$ and $0=2$), meaning the system has **no solution**.
2. **For $t \neq 1$:** The division by $t-1 \neq 0$ is valid, leading to **exactly one solution** (a unique point):

$$
x = \frac{t-4}{t-1}, \qquad y = \frac{1}{t-1}, \qquad z = \frac{2}{t-1}
$$
