### Essential Formulas

**Point-Normal Equation of a Plane:**
A plane passing through a point $P_0 = (x_0, y_0, z_0)$ with a nonzero normal vector $n = (a, b, c)$ is defined by the orthogonality condition $n \cdot \overrightarrow{P_0P} = 0$, which expands to:

$$
a(x - x_0) + b(y - y_0) + c(z - z_0) = 0
$$

or in general scalar form:

$$
ax + by + cz = d, \qquad \text{where } d = ax_0 + by_0 + cz_0
$$

---

### Problem Statement

**Exercise 5. Plane from a Point and a Normal Vector**

Find the equation of the plane passing through $P_0 = (2, -1, 4)$ with normal vector $n = (3, 1, -2)$. Determine whether the points $Q = (1, 0, 3)$ and $R = (0, 1, 2)$ lie on this plane.

> **Why this exercise:** builds direct fluency with the normal equation of a plane.

---

### Solution

**Step 1: Construct the equation of the plane**

Substitute the coordinates of $P_0 = (2, -1, 4)$ and the components of the normal vector $n = (3, 1, -2)$ into the point-normal formula:

$$
3(x - 2) + 1(y - (-1)) - 2(z - 4) = 0
$$

Expand and simplify:

$$
\begin{aligned}
3x - 6 + y + 1 - 2z + 8 &= 0 \\
3x + y - 2z + 3 &= 0 \\
3x + y - 2z &= -3
\end{aligned}
$$

**Step 2: Check whether point $Q = (1, 0, 3)$ lies on the plane**

Substitute $Q = (1, 0, 3)$ into the left-hand side of $3x + y - 2z = -3$:

$$
3(1) + 0 - 2(3) = 3 + 0 - 6 = -3
$$

Since $-3 = -3$, point $Q$ **lies on the plane**.

**Step 3: Check whether point $R = (0, 1, 2)$ lies on the plane**

Substitute $R = (0, 1, 2)$ into the left-hand side of $3x + y - 2z = -3$:

$$
3(0) + 1 - 2(2) = 0 + 1 - 4 = -3
$$

Since $-3 = -3$, point $R$ **also lies on the plane**.

---

### Final Answer

1. **Equation of the plane:**
   $$
   3x + y - 2z = -3
   $$
2. **Point membership:** Both $Q = (1, 0, 3)$ and $R = (0, 1, 2)$ satisfy the equation and therefore lie on the plane.
