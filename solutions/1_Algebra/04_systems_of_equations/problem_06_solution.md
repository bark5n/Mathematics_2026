### Essential Formulas

**Trichotomy of Solution Cases for a Linear System $Ax = b$:**
Every system of linear equations over $\mathbb{R}$ falls into exactly one of three mutually exclusive cases, determined from the row echelon form $[U \mid c]$ of its augmented matrix $[A \mid b]$ (where $n$ is the number of unknowns and $r = \mathrm{rank}(A)$ is the number of pivots):

1. **No solution (inconsistent):** A contradictory row $(0 \ 0 \ \cdots \ 0 \mid d)$ with $d \neq 0$ appears ($\mathrm{rank}(A) < \mathrm{rank}([A \mid b])$).
2. **Infinitely many solutions (consistent, underdetermined):** No contradictory row appears and $r < n$ (leaving $n - r \ge 1$ free variables).
3. **Exactly one solution (consistent, uniquely determined):** No contradictory row appears and $r = n$ (for a $2 \times 2$ system, this occurs if and only if $\det A \neq 0$).

**Determinant of a $2 \times 2$ Coefficient Matrix:**
For a $2 \times 2$ matrix

$$
A = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{pmatrix}
$$

its determinant is $\det A = a_{11}a_{22} - a_{12}a_{21}$. If $\det A = 0$ identically, the system can never have a unique solution.

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

**Step 1: Set up the augmented matrix and perform Gaussian elimination**

Write the augmented matrix $[A \mid b]$ of the system:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
a & a & \mid & 4 \\
\end{pmatrix}
$$

Apply the elementary row operation $R_2 \leftarrow R_2 - a R_1$ (which is valid for every $a \in \mathbb{R}$ because it does not divide by $a$):

* Left side: $(a, a) - a(1, 1) = (a - a, a - a) = (0, 0)$
* Right side: $4 - a(2) = 4 - 2a$

The augmented matrix reduces to row echelon form:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 4 - 2a \\
\end{pmatrix}
$$

This corresponds to the equivalent system:

$$
\begin{cases}
x + y = 2, \\
0x + 0y = 4 - 2a.
\end{cases}
$$

**Step 2: Determine which cases occur and for which values of $a$**

Whether the second equation $0 = 4 - 2a$ is satisfied depends on whether $4 - 2a$ vanishes:

1. **Case 1: $a = 2$ ($4 - 2a = 0$) $\implies$ Infinitely many solutions**
   Substituting $a = 2$ into the reduced augmented matrix gives:

$$
\begin{pmatrix}
1 & 1 & \mid & 2 \\
0 & 0 & \mid & 0 \\
\end{pmatrix}
$$

   There is no contradictory row ($\mathrm{rank}(A) = \mathrm{rank}([A \mid b]) = 1$), and there is $r = 1$ pivot column (column $1$, corresponding to $x$) among $n = 2$ variables. Thus $n - r = 2 - 1 = 1$ variable is free: setting $y = t$ ($t \in \mathbb{R}$) gives $x = 2 - t$. The system has **infinitely many solutions**:

$$
\begin{cases}
x = 2 - t, \\
y = t,
\end{cases}
\qquad t \in \mathbb{R}
$$

   *(Geometrically, when $a = 2$, the second equation $2x + 2y = 4$ is just twice the first equation $x + y = 2$, so both equations describe the exact same line.)*

2. **Case 2: $a \neq 2$ ($4 - 2a \neq 0$) $\implies$ No solution**
   Whenever $a \neq 2$, the quantity $4 - 2a$ is nonzero. The second row $(0, 0 \mid 4 - 2a)$ has all zeros on the coefficient side and a nonzero constant on the right ($\mathrm{rank}(A) = 1 < 2 = \mathrm{rank}([A \mid b])$), yielding the impossible equation:

$$
0x + 0y = 4 - 2a \neq 0
$$

   Therefore, for all $a \in \mathbb{R} \setminus \{2\}$, the system is inconsistent and has **no solution**.
   *(Specifically, for $a = 0$ the second equation becomes $0 = 4$, while for $a \neq 0, 2$ dividing by $a$ gives $x + y = \frac{4}{a} \neq 2$, which represents a line strictly parallel to $x + y = 2$.)*

**Step 3: Explain why “exactly one solution” cannot occur**

The case of **exactly one solution** never occurs for any value of $a \in \mathbb{R}$, for three equivalent reasons:

* **Rank / pivot count:** In the coefficient matrix

$$
A = \begin{pmatrix}
1 & 1 \\
a & a \\
\end{pmatrix}
$$

  the second row is always a scalar multiple of the first ($R_2 = a R_1$) and the two columns are identical. Hence $\mathrm{rank}(A) = 1 < 2$ for every $a \in \mathbb{R}$; the system can never have $2$ pivots, which is necessary for a unique solution in $2$ unknowns.
* **Vanishing determinant:** For every $a \in \mathbb{R}$,

$$
\det A = \det \begin{pmatrix}
1 & 1 \\
a & a \\
\end{pmatrix}
= 1 \cdot a - 1 \cdot a = 0
$$

  Because $\det A = 0$ identically, $A$ is never invertible and $Ax = b$ cannot have a unique solution.
* **Algebraic coupling of the equations:** Any $(x, y)$ satisfying $x + y = 2$ automatically forces $ax + ay = a(x + y) = 2a$. Thus the second equation either contradicts the first ($2a \neq 4$) or repeats it without adding any independent constraint ($2a = 4$), never pinning down a single point.

**Step 4: Verification**

* **Check at $a = 2$ (infinitely many solutions):**
  * Choosing $t = 0$ gives $(x, y) = (2, 0)$: $2 + 0 = 2$ and $2(2) + 2(0) = 4$.
  * Choosing $t = 3$ gives $(x, y) = (-1, 3)$: $-1 + 3 = 2$ and $2(-1) + 2(3) = 4$.
* **Check at $a = 3$ ($a \neq 2$, no solution):**
  * The system becomes $x + y = 2$ and $3x + 3y = 4$. Multiplying the first by $3$ gives $3x + 3y = 6 \neq 4$, a contradiction.
* **Check at $a = 0$ ($a \neq 2$, no solution):**
  * The system becomes $x + y = 2$ and $0 = 4$, an immediate contradiction.

---

### Final Answer

1. **Cases that actually occur:**
   * **Infinitely many solutions:** Occurs **only when $a = 2$**, giving the solution family $(x, y) = (2 - t, t)$ for $t \in \mathbb{R}$.
   * **No solution (inconsistent):** Occurs **for all $a \neq 2$** ($a \in \mathbb{R} \setminus \{2\}$).
2. **Case that cannot occur and why:** **Exactly one solution** cannot occur for any $a \in \mathbb{R}$, because the rows of the coefficient matrix are always proportional ($R_2 = a R_1$), so $\det A = a - a = 0$ and $\mathrm{rank}(A) = 1 < 2$ for every value of $a$.
