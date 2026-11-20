### Essential Formulas

**Intersection of a Line and a Plane:**
Given a line $L: P_0 + t v = (x_0 + t v_1, \, y_0 + t v_2, \, z_0 + t v_3)$ and a plane $\Pi: a x + b y + c z = d$, substitute the parametric coordinates of $L$ into the equation of $\Pi$:

$$a(x_0 + t v_1) + b(y_0 + t v_2) + c(z_0 + t v_3) = d$$

Solve for the parameter $t$, and substitute $t$ back into $L$ to obtain the intersection point.

---

### Problem Statement

**Exercise 8. Intersection of a Line and a Plane**

Find the point of intersection of the line

$$L: (1, 0, 2) + t(1, 2, -1)$$

with the plane

$$\Pi: x + y + z = 4.$$

Verify that the resulting point satisfies both the line equation and the plane equation.

> **Why this exercise:** reinforces substituting parametric line coordinates into a scalar plane equation to locate an intersection point.

---

### Solution

**Step 1: Write the parametric coordinates of the line**

From $L: (1, 0, 2) + t(1, 2, -1)$:

$$\begin{cases} x = 1 + t, \\ y = 2t, \\ z = 2 - t \end{cases} \qquad (t \in \mathbb{R})$$

**Step 2: Substitute into the plane equation and solve for $t$**

Substitute $x$, $y$, and $z$ into $x + y + z = 4$:

$$(1 + t) + (2t) + (2 - t) = 4$$

Combine like terms:

$$\begin{aligned} 3 + 2t &= 4 \\ 2t &= 1 \\ t &= \frac{1}{2} \end{aligned}$$

**Step 3: Compute the coordinates of the intersection point**

Substitute $t = \frac{1}{2}$ back into the parametric equations of $L$:

$$\begin{aligned} x &= 1 + \frac{1}{2} = \frac{3}{2} \\ y &= 2\left(\frac{1}{2}\right) = 1 \\ z &= 2 - \frac{1}{2} = \frac{3}{2} \end{aligned}$$

The point of intersection is $P = \left(\frac{3}{2}, 1, \frac{3}{2}\right)$.

**Step 4: Verify the intersection point**

1. **In the line equation:** At $t = \frac{1}{2}$, $(1, 0, 2) + \frac{1}{2}(1, 2, -1) = \left(\frac{3}{2}, 1, \frac{3}{2}\right)$.
2. **In the plane equation:**
   $$\frac{3}{2} + 1 + \frac{3}{2} = 3 + 1 = 4$$

Both equations are satisfied.

---

### Final Answer

1. **Parameter value:** $t = \frac{1}{2}$.
2. **Point of intersection:**
   $$P = \left(\frac{3}{2}, 1, \frac{3}{2}\right)$$
