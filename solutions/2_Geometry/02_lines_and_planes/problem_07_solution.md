### Essential Formulas

**Relative Position of a Line and a Plane:**
Given a line $L: P_0 + tv$ with direction vector $v$, and a plane $\Pi$ with normal vector $n = (a, b, c)$, the relationship is determined by the dot product $n \cdot v$:
1. **Single Intersection Point:** If $n \cdot v \neq 0$, the line is not perpendicular to the normal, meaning it intersects the plane at exactly one point.
2. **Parallel or Contained:** If $n \cdot v = 0$, the line's direction is orthogonal to the plane's normal, so the line is either strictly parallel to the plane or lies entirely within it. To distinguish between these two cases, test whether a point on the line satisfies the plane equation.

---

### Problem Statement

**Exercise 7. A Line Relative to a Plane**

For

$$
L:(x,y,z)=(1,1,0)+t(1,-1,0),\qquad \Pi:x+y+z=2,
$$

determine whether the line intersects the plane at one point, is parallel to it, or lies in it. Explain the role of the dot product of the direction vector and the normal vector.

> **Why this exercise:** builds a universal test for the relative position of a line and a plane[cite: 15].

---

### Solution

**Step 1: Extract the direction vector of the line and the normal vector of the plane**

* From the parametric description of line $L$, the base point and direction vector are:

$$
P_0 = (1, 1, 0), \qquad v = (1, -1, 0)
$$

* From the general equation of the plane $\Pi: 1x + 1y + 1z = 2$, the normal vector is:

$$
n = (1, 1, 1)
$$

**Step 2: Compute the dot product of the direction vector and the normal vector**

Calculate $n \cdot v$:

$$
n \cdot v = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0
$$

Because $n \cdot v = 0$, the direction vector $v$ is orthogonal to the normal vector $n$. This implies that the line is perpendicular to the normal of the plane, meaning the line is either strictly parallel to the plane or lies entirely within it.

**Step 3: Test whether the line lies in the plane**

To determine which of the two cases applies, substitute a known point on the line (for example, $P_0 = (1, 1, 0)$ corresponding to $t = 0$) into the equation of the plane $\Pi$:

$$
1 + 1 + 0 = 2 \implies 2 = 2 \quad (\text{True})
$$

Because the point $P_0$ satisfies the plane equation, and the line is parallel to the plane (orthogonal to its normal), the entire line **lies in the plane**.

**Step 4: Explain the role of the dot product**

The dot product $n \cdot v$ measures the alignment between the line's direction vector $v$ and the plane's normal vector $n$:
* If $n \cdot v \neq 0$, the line pierces the plane at an angle, guaranteeing a unique intersection point.
* If $n \cdot v = 0$, the line runs perpendicular to the normal vector, forcing the line to be parallel to the plane's surface. A subsequent point substitution then distinguishes whether it floats above the plane (parallel) or rests directly inside it (contained).

---

### Final Answer

1. **Relative position:** The line **lies entirely within** the plane $\Pi$.
2. **Justification:** The dot product of the direction vector and the normal vector is zero ($n \cdot v = 0$), and a point on the line ($P_0 = (1, 1, 0)$) satisfies the plane equation[cite: 15].
