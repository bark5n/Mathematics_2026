### Essential Formulas

**Polynomial Interpolation:**
A quadratic polynomial

$$
p(x) = a x^2 + b x + c
$$

passing through three points $(x_1, y_1)$, $(x_2, y_2)$, and $(x_3, y_3)$ requires that:

$$
p(x_i) = y_i \iff a x_i^2 + b x_i + c = y_i, \qquad i = 1, 2, 3
$$

This generates a system of three linear equations in the three unknown coefficients $a$, $b$, and $c$:

$$
\begin{pmatrix}
x_1^2 & x_1 & 1 \\
x_2^2 & x_2 & 1 \\
x_3^2 & x_3 & 1 \\
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
c \\
\end{pmatrix}
= \begin{pmatrix}
y_1 \\
y_2 \\
y_3 \\
\end{pmatrix}
$$

The coefficient matrix is a Vandermonde matrix, which is invertible as long as the $x$-coordinates are distinct.

---

### Problem Statement

**Exercise 10. A Polynomial Through Three Points**

Find a polynomial $p(x)=ax^2+bx+c$ whose graph passes through $(0,1)$, $(1,3)$, and $(2,9)$. Reduce the problem to a system of equations and check the result by substituting all three points.

> **Why this exercise:** shows that finding unknown coefficients can be reduced to solving a linear system.

---

### Solution

**Step 1: Set up the linear system from the points**

Substitute each given $(x, y)$ coordinate pair into $p(x) = ax^2 + bx + c$:

* Point 1: $(0, 1)$

$$
  p(0) = a(0)^2 + b(0) + c = 1 \implies c = 1
$$

* Point 2: $(1, 3)$

$$
  p(1) = a(1)^2 + b(1) + c = 3 \implies a + b + c = 3
$$

* Point 3: $(2, 9)$

$$
  p(2) = a(2)^2 + b(2) + c = 9 \implies 4a + 2b + c = 9
$$

In matrix form:

$$
\begin{pmatrix}
0 & 0 & 1 \\
1 & 1 & 1 \\
4 & 2 & 1 \\
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
c \\
\end{pmatrix}
= \begin{pmatrix}
1 \\
3 \\
9 \\
\end{pmatrix}
$$

**Step 2: Solve the system**

From the first equation, we immediately have $c = 1$.
Substitute $c = 1$ into the second and third equations:

$$
\begin{cases}
a + b + 1 = 3 \implies a + b = 2, \\
4a + 2b + 1 = 9 \implies 4a + 2b = 8.
\end{cases}
$$

Divide the second equation by $2$:

$$
2a + b = 4
$$

Subtract $a + b = 2$ from $2a + b = 4$:

$$
(2a + b) - (a + b) = 4 - 2 \implies a = 2
$$

Now substitute $a = 2$ back to find $b$:

$$
2 + b = 2 \implies b = 0
$$

Thus, the coefficients are:

$$
a = 2, \qquad b = 0, \qquad c = 1
$$

The interpolating polynomial is:

$$
p(x) = 2x^2 + 1
$$

**Step 3: Check consistency by substituting all three points**

1. For $x = 0$:

$$
   p(0) = 2(0)^2 + 1 = 0 + 1 = 1
$$

   Matches point $(0, 1)$.

2. For $x = 1$:

$$
   p(1) = 2(1)^2 + 1 = 2(1) + 1 = 3
$$

   Matches point $(1, 3)$.

3. For $x = 2$:

$$
   p(2) = 2(2)^2 + 1 = 2(4) + 1 = 8 + 1 = 9
$$

   Matches point $(2, 9)$.

All three points lie exactly on the graph of $p(x) = 2x^2 + 1$.

---

### Final Answer

1. Polynomial:

$$
p(x) = 2x^2 + 1
$$

2. Coefficients:

$$
a = 2, \qquad b = 0, \qquad c = 1
$$
