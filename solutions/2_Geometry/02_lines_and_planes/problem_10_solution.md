### Essential Formulas

**Orthogonal Projection of a Point onto a Plane:**
Given a point $P$ and a plane $\Pi: n \cdot x = d$ with normal vector $n$, the perpendicular line through $P$ is $L(t) = P + t n$. Substituting into the plane equation determines the parameter $t_0$ for the foot of the perpendicular (orthogonal projection) $H$:

$$
t_0 = \frac{d - n \cdot P}{\|n\|^2}, \qquad H = P + t_0 n
$$

**Reflection of a Point Across a Plane:**
Since $H$ is the midpoint of the segment joining $P$ and its reflection $P'$, the reflected point $P'$ satisfies:

$$
H = \frac{P + P'}{2} \implies P' = 2H - P = P + 2 t_0 n
$$

---

### Problem Statement

**Exercise 10. Orthogonal Projection and Reflection Across a Plane**

Find the orthogonal projection $H$ and the reflection $P'$ of the point $P = (2, 1, 3)$ across the plane

$$
\Pi: x + y + z = 3.
$$

Verify your answer using a midpoint check confirming that the midpoint of $PP'$ lies on the plane $\Pi$.

> **Why this exercise:** connects perpendicular projection onto a plane with reflection symmetry and midpoint verification.

---

### Solution

**Step 1: Identify the normal vector and perpendicular line through $P$**

From the plane $\Pi: x + y + z = 3$, the normal vector is $n = (1, 1, 1)$ and $d = 3$.
The line through $P = (2, 1, 3)$ in the direction of $n = (1, 1, 1)$ has parametric equations:

$$
\begin{cases}
x = 2 + t, \\
y = 1 + t, \\
z = 3 + t
\end{cases}
\qquad (t \in \mathbb{R})
$$

**Step 2: Find the orthogonal projection $H$**

Substitute the parametric coordinates into $x + y + z = 3$:

$$
\begin{aligned}
(2 + t) + (1 + t) + (3 + t) &= 3 \\
6 + 3t &= 3 \\
3t &= -3 \\
t_0 &= -1
\end{aligned}
$$

Substitute $t_0 = -1$ back into the line equations to get the orthogonal projection $H$:

$$
H = (2 - 1, \, 1 - 1, \, 3 - 1) = (1, 0, 2)
$$

**Step 3: Find the reflection $P'$ across the plane**

Since $H$ is the midpoint of $P$ and $P'$ (corresponding to $t = 2 t_0 = -2$):

$$
P' = 2H - P = 2(1, 0, 2) - (2, 1, 3) = (2 - 2, \, 0 - 1, \, 4 - 3) = (0, -1, 1)
$$

**Step 4: Perform the midpoint check**

Compute the midpoint $M$ of the segment connecting $P = (2, 1, 3)$ and $P' = (0, -1, 1)$:

$$
M = \frac{P + P'}{2} = \left(\frac{2 + 0}{2}, \, \frac{1 + (-1)}{2}, \, \frac{3 + 1}{2}\right) = (1, 0, 2) = H
$$

Substitute $M = (1, 0, 2)$ into the plane equation $x + y + z = 3$:

$$
1 + 0 + 2 = 3
$$

The midpoint coincides with $H$ and lies directly on $\Pi$. Additionally, the vector $\overrightarrow{PP'} = (-2, -2, -2) = -2n$ is parallel to the normal vector $n$, confirming orthogonality.

---

### Final Answer

1. **Orthogonal projection:** $H = (1, 0, 2)$.
2. **Reflection across the plane:** $P' = (0, -1, 1)$.
3. **Midpoint check:** The midpoint $\frac{P + P'}{2} = (1, 0, 2)$ satisfies $1 + 0 + 2 = 3$, confirming it lies on $\Pi$.
