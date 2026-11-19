### Essential Formulas

**Plane Through Three Non-Collinear Points:**
Given three non-collinear points $A$, $B$, and $C$ in space, two direction vectors lying on the plane are:

$$
u = \overrightarrow{AB} = B - A, \qquad v = \overrightarrow{AC} = C - A
$$

A normal vector $n$ perpendicular to the plane is obtained via the cross product:

$$
n = u \times v = (a, b, c)
$$

Using $n = (a, b, c)$ and point $A = (x_1, y_1, z_1)$, the plane equation is:

$$
a(x - x_1) + b(y - y_1) + c(z - z_1) = 0
$$

---

### Problem Statement

**Exercise 6. Plane Through Three Points**

Find the equation of the plane passing through the points

$$
A = (1, 0, 2), \qquad B = (2, 1, 1), \qquad C = (0, 2, 3).
$$

Check that all three points satisfy the obtained equation.

> **Why this exercise:** connects three points in space with the cross product and the normal vector of a plane.

---

### Solution

**Step 1: Construct two vectors in the plane**

Compute $\overrightarrow{AB}$ and $\overrightarrow{AC}$ using $A = (1, 0, 2)$ as the common reference point:

$$
u = \overrightarrow{AB} = (2 - 1, \, 1 - 0, \, 1 - 2) = (1, 1, -1)
$$

$$
v = \overrightarrow{AC} = (0 - 1, \, 2 - 0, \, 3 - 2) = (-1, 2, 1)
$$

**Step 2: Find a normal vector via the cross product**

Compute $n = u \times v$:

$$
\begin{aligned}
n &= (1, 1, -1) \times (-1, 2, 1) \\
  &= \big((1)(1) - (-1)(2), \, (-1)(-1) - (1)(1), \, (1)(2) - (1)(-1)\big) \\
  &= (1 + 2, \, 1 - 1, \, 2 + 1) \\
  &= (3, 0, 3)
\end{aligned}
$$

To simplify calculations, scale $n$ by $\frac{1}{3}$ to obtain a simpler normal vector $n_0 = (1, 0, 1)$.

**Step 3: Write the equation of the plane**

Substitute $n_0 = (1, 0, 1)$ and point $A = (1, 0, 2)$ into the point-normal equation:

$$
1(x - 1) + 0(y - 0) + 1(z - 2) = 0
$$

Simplify the expression:

$$
x - 1 + z - 2 = 0 \implies x + z = 3
$$

**Step 4: Verify that all three points satisfy the equation**

1. **Point $A = (1, 0, 2)$:**
   $$
   1 + 2 = 3
   $$
2. **Point $B = (2, 1, 1)$:**
   $$
   2 + 1 = 3
   $$
3. **Point $C = (0, 2, 3)$:**
   $$
   0 + 3 = 3
   $$

All three points satisfy the equation.

---

### Final Answer

1. **Equation of the plane:**

$$
x + z = 3
$$

2. **Verification:** Substituting $A(1,0,2)$, $B(2,1,1)$, and $C(0,2,3)$ into $x + z$ yields $3$ in every case.
