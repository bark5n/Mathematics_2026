### Essential Formulas

**Orthogonal Projection of a Point onto a Plane:**
Given a point $P$ and a plane $\Pi$ with normal vector $n$ passing through a point on the plane, the orthogonal projection $P'$ of $P$ onto the plane is found by constructing a line through $P$ parallel to $n$, finding its intersection $P'$ with the plane, and using the parameter $t$:

$$
P' = P + t n, \quad \text{where } t = \frac{d - n \cdot P}{n \cdot n}
$$

**Reflection of a Point Across a Plane:**
If $P'$ is the orthogonal projection of $P$ onto the plane, then the reflection $P''$ of $P$ across the plane is symmetric with respect to $P'$:

$$
P'' = 2P' - P
$$

---

### Problem Statement

**Exercise 10. Projection of a Point onto a Plane**

Find the orthogonal projection of $P=(2,1,3)$ onto the plane $x+y+z=3$, and then find the reflection of $P$ across this plane. Check that the midpoint of the segment joining the point and its reflection lies on the plane[cite: 13].

> **Why this exercise:** combines the normal, intersection, and distance into the construction of a projection and reflection[cite: 13].

---

### Solution

**Step 1: Find the normal vector of the plane**

From the general equation of the plane $\Pi: 1x + 1y + 1z = 3$, read off the normal vector:

$$
n = (1, 1, 1)
$$

**Step 2: Construct the line through $P$ parallel to the normal vector**

The line passing through $P = (2, 1, 3)$ with direction vector equal to $n = (1, 1, 1)$ has the parametric form:

$$
(x, y, z) = (2 + t, \, 1 + t, \, 3 + t)
$$

**Step 3: Find the parameter $t$ and the projection point $P'$**

Substitute the parametric coordinates into the plane equation $x + y + z = 3$:

$$
(2 + t) + (1 + t) + (3 + t) = 3
$$

Simplify and solve for $t$:

$$
\begin{aligned}
6 + 3t &= 3 \\
3t &= -3 \\
t &= -1
\end{aligned}
$$

Substitute $t = -1$ back into the line's parametric equations to obtain the projection point $P'$:

$$
P' = (2 + (-1), \, 1 + (-1), \, 3 + (-1)) = (1, 0, 2)
$$

**Step 4: Find the reflection point $P''$**

Using the reflection formula where $P'$ is the midpoint between $P$ and $P''$:

$$
P'' = 2P' - P = 2(1, 0, 2) - (2, 1, 3)
$$

$$
\begin{aligned}
P'' &= (2, 0, 4) - (2, 1, 3) \\
&= (0, -1, 1)
\end{aligned}
$$

**Step 5: Check that the midpoint of the segment joining $P$ and $P''$ lies on the plane**

The midpoint of the segment joining $P = (2, 1, 3)$ and its reflection $P'' = (0, -1, 1)$ is:

$$
\mathrm{Midpoint} = \frac{P + P''}{2} = \frac{(2, 1, 3) + (0, -1, 1)}{2} = \frac{(2, 0, 4)}{2} = (1, 0, 2) = P'
$$

Substitute this midpoint into the plane equation $x + y + z = 3$:

$$
1 + 0 + 2 = 3 \quad (\text{True})
$$

The midpoint lies on the plane identically[cite: 13].

---

### Final Answer

1. **Orthogonal projection ($P'$):** 

$$
(1, 0, 2)
$$

2. **Reflection ($P''$):** 

$$
(0, -1, 1)
$$

3. **Verification:** The midpoint of the segment joining $P$ and its reflection is $(1, 0, 2)$, which satisfies the plane equation $1 + 0 + 2 = 3[cite: 13, 14]$.
