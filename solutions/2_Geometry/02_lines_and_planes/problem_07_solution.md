### Essential Formulas

**Intersection of a Line and a Plane:**
Given a line in parametric form:

$$
\begin{cases}
x = x_0 + t v_1, \\
y = y_0 + t v_2, \\
z = z_0 + t v_3
\end{cases}
$$

and a plane $ax + by + cz = d$, substitute the parametric expressions for $x$, $y$, and $z$ into the plane equation:

$$
a(x_0 + t v_1) + b(y_0 + t v_2) + c(z_0 + t v_3) = d
$$

Solve this linear equation for the parameter $t$, then substitute $t$ back into the line equations to obtain the intersection coordinates.

---

### Problem Statement

**Exercise 7. Intersection of a Line and a Plane**

Find the point of intersection of the line

$$
\begin{cases}
x = 1 + 2t, \\
y = -1 + t, \\
z = 3 - t
\end{cases}
$$

with the plane $2x - y + z = 7$. Check that the obtained point satisfies both the equations of the line and the equation of the plane.

> **Why this exercise:** teaches the standard algebraic method for intersecting a line with a plane.

---

### Solution

**Step 1: Substitute the parametric equations into the plane equation**

Replace $x$, $y$, and $z$ in $2x - y + z = 7$ with the expressions from the line:

$$
2(1 + 2t) - (-1 + t) + (3 - t) = 7
$$

**Step 2: Solve for the parameter $t$**

Expand and combine like terms:

$$
\begin{aligned}
2 + 4t + 1 - t + 3 - t &= 7 \\
6 + 2t &= 7 \\
2t &= 1 \\
t &= \frac{1}{2}
\end{aligned}
$$

**Step 3: Find the coordinates of the intersection point**

Substitute $t = \frac{1}{2}$ back into the parametric equations of the line:

$$
\begin{aligned}
x &= 1 + 2\left(\frac{1}{2}\right) = 1 + 1 = 2 \\
y &= -1 + \frac{1}{2} = -\frac{1}{2} \\
z &= 3 - \frac{1}{2} = \frac{5}{2}
\end{aligned}
$$

The intersection point is $P = \left(2, -\frac{1}{2}, \frac{5}{2}\right)$.

**Step 4: Verify the intersection point**

1. **Check in the line equations:** At $t = \frac{1}{2}$, the parametric equations produce $\left(2, -\frac{1}{2}, \frac{5}{2}\right)$ directly.
2. **Check in the plane equation:** Substitute $P = \left(2, -\frac{1}{2}, \frac{5}{2}\right)$ into $2x - y + z$:

$$
2(2) - \left(-\frac{1}{2}\right) + \frac{5}{2} = 4 + \frac{1}{2} + \frac{5}{2} = 4 + 3 = 7
$$

Both conditions hold.

---

### Final Answer

1. **Intersection point:**

$$
P = \left(2, -\frac{1}{2}, \frac{5}{2}\right)
$$

2. **Parameter value:** $t = \frac{1}{2}$.
