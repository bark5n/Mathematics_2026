### Essential Formulas

**Plane Containing a Line and an External Point:**
Given a line $L: P_0 + t v$ and a point $P \notin L$, two non-parallel vectors lying in the plane $\Pi$ are:

$$v \qquad \mathrm{and} \qquad w = \overrightarrow{P_0 P} = P - P_0$$

A normal vector $n$ to the plane is given by the cross product:

$$n = v \times w = (a, b, c)$$

Using $n = (a, b, c)$ and $P_0 = (x_0, y_0, z_0)$, the plane equation is:

$$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$$

---

### Problem Statement

**Exercise 11. Plane Containing a Line and a Point**

Find the equation of the plane containing the line

$$L: P_0 + t v = (1, 0, 2) + t(1, 1, -1)$$

and the point $P = (0, 2, 1)$. Perform both checks to confirm that the entire line $L$ lies in the plane and that the point $P$ satisfies the plane equation.

> **Why this exercise:** combines a line direction vector with a displacement vector to construct a unique plane and verifies both containment conditions.

---

### Solution

**Step 1: Construct two direction vectors in the plane**

From the line $L$, take the base point $P_0 = (1, 0, 2)$ and direction vector $v = (1, 1, -1)$.
Form a second vector $w$ from $P_0 = (1, 0, 2)$ to $P = (0, 2, 1)$:

$$w = \overrightarrow{P_0 P} = P - P_0 = (0 - 1, \, 2 - 0, \, 1 - 2) = (-1, 2, -1)$$

Since $w$ is not a scalar multiple of $v$, $P$ does not lie on $L$, so a unique plane is determined.

**Step 2: Compute the normal vector via the cross product**

Compute $n = v \times w$:

$$\begin{aligned} n &= (1, 1, -1) \times (-1, 2, -1) \\ &= \big((1)(-1) - (-1)(2), \, (-1)(-1) - (1)(-1), \, (1)(2) - (1)(-1)\big) \\ &= (-1 + 2, \, 1 + 1, \, 2 + 1) \\ &= (1, 2, 3) \end{aligned}$$

**Step 3: Write the equation of the plane**

Substitute $n = (1, 2, 3)$ and $P_0 = (1, 0, 2)$ into the point-normal equation:

$$1(x - 1) + 2(y - 0) + 3(z - 2) = 0$$

Expand and simplify:

$$x - 1 + 2y + 3z - 6 = 0 \implies x + 2y + 3z = 7$$

**Step 4: Perform both containment checks**

1. **Check 1 (Point $P = (0, 2, 1)$ lies on the plane):**
   Substitute $(x, y, z) = (0, 2, 1)$ into $x + 2y + 3z$:
   $$0 + 2(2) + 3(1) = 0 + 4 + 3 = 7$$
   The point $P$ satisfies the plane equation.

2. **Check 2 (Every point of line $L$ lies on the plane):**
   Substitute the general parametric point $(x, y, z) = (1 + t, \, t, \, 2 - t)$ into $x + 2y + 3z$:
   $$(1 + t) + 2(t) + 3(2 - t) = 1 + t + 2t + 6 - 3t = 7 + 0t = 7$$
   The equation holds identically for every $t \in \mathbb{R}$, confirming that the entire line $L$ is contained in the plane.

---

### Final Answer

1. **Equation of the plane:**
   $$x + 2y + 3z = 7$$
2. **Verification:** Both $P = (0, 2, 1)$ and every point $(1 + t, t, 2 - t)$ on $L$ yield $x + 2y + 3z = 7$.
