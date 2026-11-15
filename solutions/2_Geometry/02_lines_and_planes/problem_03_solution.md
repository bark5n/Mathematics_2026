### Essential Formulas

**Plane Equation from a Point and a Normal Vector:**
A plane $\Pi$ passing through a given point $P_0 = (x_0, y_0, z_0)$ and having a nonzero normal vector $n = (a, b, c)$ is defined by the point-normal equation:

$$
a(x - x_0) + b(y - y_0) + c(z - z_0) = 0
$$

Expanding this expression yields the general Cartesian equation of the plane:

$$
ax + by + cz = d
$$

where $d = ax_0 + by_0 + cz_0 = n \cdot P_0$.

**Geometric Role of the Normal Vector:**
The components $(a, b, c)$ of the normal vector $n$ form the coefficients of $x, y$, and $z$ in the general equation of the plane. Geometrically, $n$ is orthogonal (perpendicular) to every vector lying entirely within the plane.

---

### Problem Statement

**Exercise 3. Plane Through a Point with a Given Normal Vector**

Find the equation of the plane through $P=(1,-2,3)$ and perpendicular to $n=(2,1,-1)$. Check the result by substituting the point $P$ and explain the role of the normal vector.

> **Why this exercise:** shows the basic construction of a plane from a point and a normal vector.

---

### Solution

**Step 1: Set up the point-normal equation**

Given the point $P = (x_0, y_0, z_0) = (1, -2, 3)$ and the normal vector $n = (a, b, c) = (2, 1, -1)$, substitute these values into the point-normal equation:

$$
2(x - 1) + 1(y - (-2)) + (-1)(z - 3) = 0
$$

**Step 2: Simplify the equation into general form**

Distribute the coefficients and combine like terms:

$$
\begin{aligned}
2(x - 1) + 1(y + 2) - 1(z - 3) &= 0 \\
2x - 2 + y + 2 - z + 3 &= 0 \\
2x + y - z + 3 &= 0 \\
2x + y - z &= -3
\end{aligned}
$$

**Step 3: Check the result by substituting the point $P = (1, -2, 3)$**

Substitute $x = 1$, $y = -2$, and $z = 3$ into the left-hand side of the derived equation:

$$
2(1) + (-2) - (3) = 2 - 2 - 3 = -3
$$

The result matches the right-hand side constant $(-3)$ identically, confirming that point $P$ lies on the plane.

**Step 4: Explain the role of the normal vector**

* **Coefficients of the variables:** The coordinates of the normal vector $n = (2, 1, -1)$ directly dictate the coefficients $a=2, b=1, c=-1$ of $x, y,$ and $z$ in the plane equation. Any plane parallel to this one shares the exact same normal vector and differs only by the constant term $d$.
* **Orthogonality:** Geometrically, $n$ points directly "out of" the plane at a $90^\circ$ angle to every directional vector connecting $P$ to any other arbitrary point $X(x, y, z)$ residing on the plane (i.e., vector $\overrightarrow{PX} \cdot n = 0$).

---

### Abstract Summary & Final Answer

1. **Equation of the plane:**

$$
2x + y - z = -3 \quad (\text{or } 2x + y - z + 3 = 0)
$$

2. **Point verification:** Substituting $P(1, -2, 3)$ satisfies $2(1) + (-2) - (3) = -3$.
3. **Role of the normal vector:** $n = (2, 1, -1)$ determines the orientation of the plane by providing the orthogonal coefficients for the general Cartesian equation.
