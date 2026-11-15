### Essential Formulas

**Distance from a Point to a Line in $\mathbb{R}^2$:**
The shortest distance $d$ from a point $P_0 = (x_0, y_0)$ to a line given by the general equation $ax + by + c = 0$ is computed by:

$$
d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}
$$

**Distance from a Point to a Plane in $\mathbb{R}^3$:**
The shortest distance $D$ from a point $Q_0 = (x_0, y_0, z_0)$ to a plane given by the general equation $ax + by + cz + d = 0$ is computed by:

$$
D = \frac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}}
$$

**Geometric Connection with the Normal Direction:**
Both formulas stem from the same geometric principle: the shortest path from an external point to a line or plane always lies along the direction of the object's normal vector $n$. The numerator evaluates the residual of plugging the point into the object's equation, while the denominator divides by the magnitude of the normal vector to convert that residual into a true Euclidean length.

---

### Problem Statement

**Exercise 9. Distances**

Compute:

1. the distance from $P=(2,3)$ to the line $3x+4y-10=0$,
2. the distance from $Q=(2,-1,3)$ to the plane $2x-2y+z-4=0$.

Compare the two formulas and explain their common connection with the normal direction[cite: 15].

> **Why this exercise:** organizes two similar formulas through one geometric idea[cite: 15].

---

### Solution

**Step 1: Compute the distance from $P = (2, 3)$ to the line $3x + 4y - 10 = 0$**

Identify the coefficients from the line equation and the coordinates of the point:
* $a = 3, \, b = 4, \, c = -10$
* $x_0 = 2, \, y_0 = 3$

Substitute these values into the point-to-line distance formula:

$$
\begin{aligned}
d &= \frac{|3(2) + 4(3) - 10|}{\sqrt{3^2 + 4^2}} \\
&= \frac{|6 + 12 - 10|}{\sqrt{9 + 16}} \\
&= \frac{|18 - 10|}{\sqrt{25}} \\
&= \frac{8}{5} = 1.6
\end{aligned}
$$

**Step 2: Compute the distance from $Q = (2, -1, 3)$ to the plane $2x - 2y + z - 4 = 0$**

Identify the coefficients from the plane equation and the coordinates of the point:
* $a = 2, \, b = -2, \, c = 1, \, d = -4$
* $x_0 = 2, \, y_0 = -1, \, z_0 = 3$

Substitute these values into the point-to-plane distance formula:

$$
\begin{aligned}
D &= \frac{|2(2) + (-2)(-1) + 1(3) - 4|}{\sqrt{2^2 + (-2)^2 + 1^2}} \\
&= \frac{|4 + 2 + 3 - 4}{\sqrt{4 + 4 + 1}} \\
&= \frac{|5}{\sqrt{9}} \\
&= \frac{5}{3}
\end{aligned}
$$

**Step 3: Compare formulas and explain their common connection with the normal vector**

* **Structural comparison:** Both formulas share an identical mathematical layout. The numerator takes the absolute value of the object's linear expression evaluated at the given coordinates, measuring how much the point fails to satisfy the equation (the residual offset). The denominator divides by the Euclidean norm ($\|nundu\|$) of the object's normal vector ($n = (a, b)$ for the line in $\mathbb{R}^2$ and $n = (a, b, c)$ for the plane in $\mathbb{R}^3$).
* **Normal direction connection:** Geometrically, the shortest distance from any external point to a linear geometric object always runs parallel to its orthogonal normal vector. Projecting the displacement vector (connecting a point on the object to the external point) onto the unit normal vector yields these exact algebraic expressions.

---

### Final Answer

1. **Distance from $P(2,3)$ to the line:** 

$$
\frac{8}{5} \quad (\text{or } 1.6)
$$

2. **Distance from $Q(2,-1,3)$ to the plane:** 

$$
\frac{5}{3}
$$

3. **Comparison:** Both formulas divide the evaluated algebraic residual at the point by the length of the object's normal vector, reflecting the fundamental geometric principle that shortest distances are measured along normal lines[cite: 15, 16].
