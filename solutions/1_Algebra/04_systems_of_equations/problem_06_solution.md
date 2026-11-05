### Essential Formulas

**Parametric Linear System Classification:**
For an augmented matrix $[A(a) \mid b]$ reduced by row operations:
* **Unique solution:** Occurs if and only if $\det A(a) \neq 0$ (full rank).
* **Infinitely many solutions:** Occurs if $\det A(a) = 0$ and the reduced augmented matrix has no contradiction row, leaving fewer pivot rows than variables.
* **No solution (inconsistent):** Occurs if row operations produce a row of the form:

$$
  \begin{pmatrix} 0 & 0 & \mid & c \end{pmatrix} \quad \mathrm{for}\  c \neq 0
$$

---

### Problem Statement

**Exercise 6. A System with a Parameter — Which Cases Actually Occur?**

Analyze, depending on the parameter $a$, the system

$$
\begin{cases}
x+y=2, \\
ax+ay=4.
\end{cases}
$$

Among the three possibilities — exactly one solution, infinitely many solutions, no solution — determine which actually occur and for which values of $a$. If one type cannot occur, explain why.

> **Why this exercise:** teaches how to analyze a parameter without assuming in advance that all theoretically possible cases must occur in a specific system.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid b]$**

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
a & a & \mid & 4 \\
\end{pmatrix}
$$

**Step 2: Apply row elimination**

Eliminate the leading term of the second row by performing $R_2 \leftarrow R_2 - a R_1$:

$$
\begin{aligned}
R_2 - a R_1 &= (a, a \mid 4) - a(1, 1 \mid 2) \\
&= (a, a \mid 4) - (a, a \mid 2a) \\
&= (0, 0 \mid 4 - 2a)
\end{aligned}
$$

The augmented matrix in row echelon form is:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 4 - 2a \\
\end{pmatrix}
$$

**Step 3: Analyze the second row based on parameter $a$**

The second row translates to the algebraic equation:

$$
0 \cdot x + 0 \cdot y = 4 - 2a \implies 0 = 4 - 2a
$$

* **Case 1: $4 - 2a = 0 \iff a = 2$**
  The second row becomes $(0 \quad 0 \mid 0)$, which represents the identity $0 = 0$.
  The system reduces to the single equation:

$$
  x + y = 2 \implies x = 2 - y
$$

  Variable $y$ is free ($y = t$), yielding **infinitely many solutions**:

$$
  \begin{pmatrix} x \\ y \\ \end{pmatrix} = \begin{pmatrix} 2 - t \\ t \\ \end{pmatrix}, \qquad t \in \mathbb{R}
$$

* **Case 2: $4 - 2a \neq 0 \iff a \neq 2$**
  The second row has zeros for both variable coefficients, but a nonzero right-hand side ($4 - 2a \neq 0$).
  This creates the contradiction $0 = 4 - 2a \neq 0$, meaning the system is inconsistent and has **no solution**.

**Step 4: Explain why "exactly one solution" can never occur**

For any $2 \times 2$ system to possess a unique solution, its coefficient matrix must have nonzero determinant ($\det A \neq 0$).
Here, the coefficient matrix is:

$$
A = \begin{pmatrix}
1 & 1 \\
a & a \\
\end{pmatrix}
$$

Compute its determinant:

$$
\det A = (1)(a) - (1)(a) = a - a = 0
$$

The determinant is identically zero for **all** values of $a \in \mathbb{R}$.
Because row 2 is always a scalar multiple of row 1 ($R_2 = a R_1$), the columns/rows of the coefficient matrix are always linearly dependent, and the rank of $A$ can never equal $2$. Consequently, the case of **exactly one solution can never occur**.

---

### Final Answer

1. Classification of cases:
   * **Exactly one solution:** **Never occurs** (for any $a$).
   * **Infinitely many solutions:** Occurs when **$a = 2$**.
   * **No solution:** Occurs when **$a \neq 2$**.

2. Explanation:
The determinant of the coefficient matrix $\det A = (1)(a) - (1)(a) = 0$ is zero for every value of $a$, so the coefficient matrix is never invertible and the lines are always parallel. Therefore, a unique intersection point can never exist.
