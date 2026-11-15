### Essential Formulas

**Closest Point on a Plane (Orthogonal Projection):**
The point on a plane $\Pi$ closest to a given external point $P_0$ is its orthogonal projection onto the plane. This point can be found by constructing a line through $P_0$ parallel to the plane's normal vector $n = (a, b, c)$ and finding its intersection with the plane:

$$
P' = P_0 - \frac{ax_0 + by_0 + cz_0 - d}{a^2 + b^2 + c^2} n
$$

**Distance from a Point to a Plane:**
The shortest distance $D$ from a point $P_0 = (x_0, y_0, z_0)$ to a plane $ax + by + cz = d$ is given by:

$$
D = \frac{|ax_0 + by_0 + cz_0 - d|}{\sqrt{a^2 + b^2 + c^2}}
$$

**Perpendicularity Condition:**
A line segment joining an external point $P_0$ to its closest point $P'$ on a plane is perpendicular to the plane if and only if the vector $\overrightarrow{P_0P'}$ is parallel to the plane's normal vector $n$ (i.e., $\overrightarrow{P_0P'} = k n$ for some scalar $k$).

---

### Problem Statement

**Exercise 13. Closest Point on a Plane**

Find the point on the plane $x+2y+2z=4$ closest to $P=(3,0,0)$. Give the distance and check that the segment joining the two points is perpendicular to the plane.

> **Why this exercise:** combines projection, distance, and the normal direction in one problem.

---

### Solution

**Step 1: Identify the plane's normal vector and external point**

* From the plane equation $\Pi: 1x + 2y + 2z = 4$, the normal vector is:

$$
n = (1, 2, 2)
$$

* The given external point is $P = (3, 0, 0)$.

**Step 2: Construct the line through $P$ perpendicular to the plane**

The line passing through $P = (3, 0, 0)$ with direction vector equal to $n = (1, 2, 2)$ has the parametric equations:

$$
\begin{cases}
x = 3 + t \\
y = 2t \\
z = 2t
\end{cases}
$$

**Step 3: Find the parameter $t$ and the closest point $P'$**

Substitute the parametric coordinates into the plane equation $x + 2y + 2z = 4$:

$$
(3 + t) + 2(2t) + 2(2t) = 4
$$

Simplify and solve for $t$:

$$
\begin{aligned}
3 + t + 4t + 4t &= 4 \\
3 + 9t &= 4 \\
9t &= 1 \\
t &= \frac{1}{9}
\end{aligned}
$$

Substitute $t = \frac{1}{9}$ back into the parametric equations to find the closest point $P'$:

$$
P' = \left(3 + \frac{1}{9}, \, 2\left(\frac{1}{9}\right), \, 2\left(\frac{1}{9}\right)\right) = \left(\frac{28}{9}, \frac{2}{9}, \frac{2}{9}\right)
$$

**Step 4: Compute the distance between $P$ and $P'$**

Compute the distance $D$ using the distance formula or the norm of vector $\overrightarrow{PP'}$:

$$
\begin{aligned}
\overrightarrow{PP'} &= P' - P = \left(\frac{28}{9} - 3, \, \frac{2}{9} - 0, \, \frac{2}{9} - 0\right) \\
&= \left(\frac{1}{9}, \frac{2}{9}, \frac{2}{9}\right)
\end{aligned}
$$

Calculate its magnitude:

$$
\begin{aligned}
D &= \|\overrightarrow{PP'}\| = \sqrt{\left(\frac{1}{9}\right)^2 + \left(\frac{2}{9}\right)^2 + \left(\frac{2}{9}\right)^2} \\
&= \sqrt{\frac{1}{81} + \frac{4}{81} + \frac{4}{81}} \\
&= \sqrt{\frac{9}{81}} = \sqrt{\frac{1}{9}} = \frac{1}{3}
\end{aligned}
$$

*(Verification via the point-to-plane distance formula: $D = \frac{|1(3) + 2(0) + 2(0) - 4|}{\sqrt{1^2 + 2^2 + 2^2}} = \frac{|-1|}{\sqrt{9}} = \frac{1}{3}$.)*

**Step 5: Check that the segment joining the two points is perpendicular to the plane**

The displacement vector is $\overrightarrow{PP'} = \left(\frac{1}{9}, \frac{2}{9}, \frac{2}{9}\right) = \frac{1}{9}(1, 2, 2)$. 
Since $\overrightarrow{PP'} = \frac{1}{9} n$, the vector joining $P$ and $P'$ is a scalar multiple of the plane's normal vector $n = (1, 2, 2)$. This confirms that the segment is strictly perpendicular to the plane.

---

### Final Answer

1. **Closest point on the plane ($P'$):** 

$$
\left(\frac{28}{9}, \frac{2}{9}, \frac{2}{9}\right)
$$

2. **Distance:** 

$$
\frac{1}{3}
$$

3. **Perpendicularity check:** The vector $\overrightarrow{PP'} = \frac{1}{9}(1, 2, 2)$ is a scalar multiple of the normal vector $n = (1, 2, 2)$, proving the segment is perpendicular to the plane.
