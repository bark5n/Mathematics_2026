### Essential Formulas

**Plane Through Three Non-Collinear Points:**
Given three non-collinear points $A$, $B$, and $C$ in $\mathbb{R}^3$, two direction vectors lying in the plane are:

$$
u = \overrightarrow{AB} = B - A, \qquad v = \overrightarrow{AC} = C - A
$$

A normal vector $n$ perpendicular to the plane is computed via the cross product:

$$
n = u \times v = (a, b, c)
$$

Using $n = (a, b, c)$ and point $A = (x_1, y_1, z_1)$, the scalar equation of the plane is:

$$
a(x - x_1) + b(y - y_1) + c(z - z_1) = 0
$$

---

### Problem Statement

**Exercise 4. Plane Through Three Points**

Find the equation of the plane passing through the points

$$
A = (1, 0, 0), \qquad B = (0, 1, 0), \qquad C = (0, 0, 1),
$$

using two in-plane vectors and a cross product. Verify that all three given points satisfy the resulting plane equation.

> **Why this exercise:** connects three non-collinear points in space with in-plane vectors and the cross product to construct a plane normal.

---

### Solution

**Step 1: Construct two in-plane vectors**

Using $A = (1, 0, 0)$ as the initial point, compute the vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$:

$$
u = \overrightarrow{AB} = B - A = (0 - 1, \, 1 - 0, \, 0 - 0) = (-1, 1, 0)
$$

$$
v = \overrightarrow{AC} = C - A = (0 - 1, \, 0 - 0, \, 1 - 0) = (-1, 0, 1)
$$

**Step 2: Compute a normal vector via the cross product**

Take the cross product $n = u \times v$:

$$
\begin{aligned}
n &= (-1, 1, 0) \times (-1, 0, 1) \\
  &= \big((1)(1) - (0)(0), \, (0)(-1) - (-1)(1), \, (-1)(0) - (1)(-1)\big) \\
  &= (1 - 0, \, 0 + 1, \, 0 + 1) \\
  &= (1, 1, 1)
\end{aligned}
$$

**Step 3: Write the equation of the plane**

Substitute the normal vector $n = (1, 1, 1)$ and point $A = (1, 0, 0)$ into the point-normal equation:

$$
1(x - 1) + 1(y - 0) + 1(z - 0) = 0
$$

Simplify the expression:

$$
x - 1 + y + z = 0 \implies x + y + z = 1
$$

**Step 4: Verify that all three points satisfy the equation**

1. **Point $A = (1, 0, 0)$:** $1 + 0 + 0 = 1$.
2. **Point $B = (0, 1, 0)$:** $0 + 1 + 0 = 1$.
3. **Point $C = (0, 0, 1)$:** $0 + 0 + 1 = 1$.

All three points satisfy $x + y + z = 1$.

---

### Final Answer

1. **In-plane vectors:** $u = (-1, 1, 0)$ and $v = (-1, 0, 1)$.
2. **Normal vector:** $n = u \times v = (1, 1, 1)$.
3. **Equation of the plane:**
   $$
   x + y + z = 1
   $$
