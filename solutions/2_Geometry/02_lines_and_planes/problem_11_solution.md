### Essential Formulas

**Distance from a Point to a Plane:**
Given a point $P_0 = (x_0, y_0, z_0)$ and a plane $\Pi$ with general equation $ax + by + cz + d = 0$ (or $ax + by + cz = D$), the shortest perpendicular distance $d(P_0, \Pi)$ is:

$$
d(P_0, \Pi) = \frac{|a x_0 + b y_0 + c z_0 + d|}{\sqrt{a^2 + b^2 + c^2}} = \frac{|n \cdot P_0 - D|}{\|n\|}
$$

**Foot of the Perpendicular (Orthogonal Projection onto a Plane):**
The closest point $H$ on the plane $\Pi$ to $P_0$ lies along the line passing through $P_0$ in the direction of the normal vector $n = (a, b, c)$:

$$
H = P_0 + t_0 n, \qquad \text{where } t_0 = \frac{D - n \cdot P_0}{\|n\|^2}
$$

---

### Problem Statement

**Exercise 11. Distance from a Point to a Plane**

Compute the distance from the point $P_0 = (2, -1, 3)$ to the plane

$$
2x - y + 2z = 5.
$$

Then find the foot of the perpendicular dropped from $P_0$ onto the plane, and verify that the distance from $P_0$ to this point equals the distance computed earlier.

> **Why this exercise:** connects the distance formula with the geometric notion of orthogonal projection onto a plane.

---

### Solution

**Step 1: Compute the distance from $P_0$ to the plane**

Identify the normal vector $n = (2, -1, 2)$ and constant $D = 5$ (or $d = -5$ in $2x - y + 2z - 5 = 0$). Compute the magnitude of $n$:

$$
\|n\| = \sqrt{2^2 + (-1)^2 + 2^2} = \sqrt{4 + 1 + 4} = \sqrt{9} = 3
$$

Substitute $P_0 = (2, -1, 3)$ into the distance formula:

$$
d(P_0, \Pi) = \frac{|2(2) - (-1) + 2(3) - 5|}{3} = \frac{|4 + 1 + 6 - 5|}{3} = \frac{|6|}{3} = 2
$$

**Step 2: Set up the perpendicular line through $P_0$**

The line through $P_0 = (2, -1, 3)$ parallel to the normal vector $n = (2, -1, 2)$ has parametric equations:

$$
\begin{cases}
x = 2 + 2t, \\
y = -1 - t, \\
z = 3 + 2t
\end{cases}
\qquad (t \in \mathbb{R})
$$

**Step 3: Find the foot of the perpendicular $H$**

Substitute the parametric expressions into the plane equation $2x - y + 2z = 5$:

$$
\begin{aligned}
2(2 + 2t) - (-1 - t) + 2(3 + 2t) &= 5 \\
4 + 4t + 1 + t + 6 + 4t &= 5 \\
11 + 9t &= 5 \\
9t &= -6 \\
t &= -\frac{2}{3}
\end{aligned}
$$

Substitute $t = -\frac{2}{3}$ back into the parametric equations to find $H$:

$$
\begin{aligned}
x &= 2 + 2\left(-\frac{2}{3}\right) = 2 - \frac{4}{3} = \frac{2}{3} \\
y &= -1 - \left(-\frac{2}{3}\right) = -1 + \frac{2}{3} = -\frac{1}{3} \\
z &= 3 + 2\left(-\frac{2}{3}\right) = 3 - \frac{4}{3} = \frac{5}{3}
\end{aligned}
$$

Thus, the foot of the perpendicular is $H = \left(\frac{2}{3}, -\frac{1}{3}, \frac{5}{3}\right)$.

**Step 4: Verify the Euclidean distance between $P_0$ and $H$**

Compute the distance $\|P_0 - H\|$:

$$
\begin{aligned}
\|P_0 - H\| &= \sqrt{\left(2 - \frac{2}{3}\right)^2 + \left(-1 - \left(-\frac{1}{3}\right)\right)^2 + \left(3 - \frac{5}{3}\right)^2} \\
&= \sqrt{\left(\frac{4}{3}\right)^2 + \left(-\frac{2}{3}\right)^2 + \left(\frac{4}{3}\right)^2} \\
&= \sqrt{\frac{16}{9} + \frac{4}{9} + \frac{16}{9}} \\
&= \sqrt{\frac{36}{9}} = \sqrt{4} = 2
\end{aligned}
$$

This matches the distance $d(P_0, \Pi) = 2$ computed in Step 1.

---

### Final Answer

1. **Distance from $P_0$ to the plane:** $2$.
2. **Foot of the perpendicular:** $H = \left(\frac{2}{3}, -\frac{1}{3}, \frac{5}{3}\right)$.
