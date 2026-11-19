### Essential Formulas

**Intersection of Two Planes (Line of Intersection):**
Given two non-parallel planes $\Pi_1: a_1 x + b_1 y + c_1 z = d_1$ and $\Pi_2: a_2 x + b_2 y + c_2 z = d_2$, their intersection is a straight line $L$.

1. **Direction vector:** The direction vector $v$ of the line $L$ is perpendicular to both plane normal vectors $n_1$ and $n_2$:

$$
v = n_1 \times n_2
$$

2. **Base point:** A point $P_0 = (x_0, y_0, z_0)$ on $L$ is found by setting one coordinate to a convenient value (e.g., $z = 0$) and solving the resulting $2 \times 2$ linear system.

---

### Problem Statement

**Exercise 9. Line of Intersection of Two Planes**

Find a parametric equation of the line of intersection of the planes

$$
x + y + z = 3, \qquad 2x - y + z = 2.
$$

Verify that your solution satisfies both plane equations for every value of the parameter.

> **Why this exercise:** connects a system of two linear equations in three variables with the parametric description of a line.

---

### Solution

**Step 1: Find the direction vector using the cross product**

Read the normal vectors from the two plane equations:

$$
n_1 = (1, 1, 1), \qquad n_2 = (2, -1, 1)
$$

Compute $v = n_1 \times n_2$:

$$
\begin{aligned}
v &= (1, 1, 1) \times (2, -1, 1) \\
  &= \big((1)(1) - (1)(-1), \, (1)(2) - (1)(1), \, (1)(-1) - (1)(2)\big) \\
  &= (1 + 1, \, 2 - 1, \, -1 - 2) \\
  &= (2, 1, -3)
\end{aligned}
$$

**Step 2: Find a specific point on the line**

Set $z = 0$ in both plane equations to obtain a system of two equations in $x$ and $y$:

$$
\begin{cases}
x + y = 3, \\
2x - y = 2
\end{cases}
$$

Add the two equations together to eliminate $y$:

$$
3x = 5 \implies x = \frac{5}{3}
$$

Substitute $x = \frac{5}{3}$ into $x + y = 3$:

$$
\frac{5}{3} + y = 3 \implies y = 3 - \frac{5}{3} = \frac{4}{3}
$$

Thus, a point on the line of intersection is $P_0 = \left(\frac{5}{3}, \frac{4}{3}, 0\right)$.

**Step 3: Write the parametric equation of the line**

Using $P_0 = \left(\frac{5}{3}, \frac{4}{3}, 0\right)$ and $v = (2, 1, -3)$:

$$
\begin{cases}
x = \frac{5}{3} + 2t, \\
y = \frac{4}{3} + t, \\
z = -3t
\end{cases}
\qquad (t \in \mathbb{R})
$$

**Step 4: Verify that the parametric solution satisfies both planes for all $t$**

1. **First plane ($x + y + z = 3$):**

$$
\left(\frac{5}{3} + 2t\right) + \left(\frac{4}{3} + t\right) + (-3t) = \frac{9}{3} + (2t + t - 3t) = 3 + 0 = 3
$$

2. **Second plane ($2x - y + z = 2$):**

$$
2\left(\frac{5}{3} + 2t\right) - \left(\frac{4}{3} + t\right) + (-3t) = \frac{10}{3} - \frac{4}{3} + (4t - t - 3t) = \frac{6}{3} + 0 = 2
$$

Both identities hold identically for every $t \in \mathbb{R}$.

---

### Final Answer

1. **Parametric equation of the line of intersection:**

$$
\begin{cases}
x = \frac{5}{3} + 2t, \\
y = \frac{4}{3} + t, \\
z = -3t
\end{cases}
\qquad (t \in \mathbb{R})
$$
