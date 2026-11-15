### Essential Formulas

**Constructing a Plane from a Line and an External Point:**
Given a line $L$ passing through a point $P_0$ with direction vector $v$, and an external point $P$ not on $L$:
1. A second vector lying in the plane can be formed by connecting $P_0$ to $P$: 

$$
w = P - P_0
$$

2. The normal vector $n$ to the plane is obtained by taking the cross product of the direction vector and the in-plane vector:

$$
n = v \times w
$$

3. The equation of the plane is then determined using the normal vector $n$ and either point ($P_0$ or $P$).

---

### Problem Statement

**Exercise 11. Plane Containing a Line and a Point**

Find the equation of the plane containing

$$
(x,y,z)=(1,0,2)+t(1,1,-1)
$$

and the point $P=(0,2,1)$. Check that both the entire line and the point lie in the plane you obtain[cite: 12].

> **Why this exercise:** requires independently constructing two linearly independent directions in the plane[cite: 12].

---

### Solution

**Step 1: Extract a point and a direction vector from the line**

From the given parametric line equation $(x, y, z) = (1, 0, 2) + t(1, 1, -1)$[cite: 12]:
* **A point on the line:** $P_0 = (1, 0, 2)$
* **The direction vector of the line:** $v = (1, 1, -1)$

**Step 2: Construct a second vector lying in the plane**

Let $P = (0, 2, 1)$ be the given external point[cite: 12]. Compute the vector $w$ from $P_0$ to $P$:

$$
\begin{aligned}
w &= P - P_0 = (0 - 1, \, 2 - 0, \, 1 - 2) \\
&= (-1, 2, -1)
\end{aligned}
$$

Both vectors $v = (1, 1, -1)$ and $w = (-1, 2, -1)$ lie entirely within the desired plane and are linearly independent.

**Step 3: Compute the normal vector of the plane using the cross product**

Calculate the cross product $n = v \times w$ to find a normal vector orthogonal to both in-plane vectors:

$$
\begin{aligned}
n &= v \times w = (1, 1, -1) \times (-1, 2, -1) \\
&= \bigl(1(-1) - (-1)(2), \, (-1)(-1) - 1(-1), \, 1(2) - 1(-1)\bigr) \\
&= (-1 + 2, \, 1 + 1, \, 2 + 1) \\
&= (1, 2, 3)
\end{aligned}
$$

**Step 4: Write the equation of the plane**

Using the normal vector $n = (1, 2, 3)$ and the point $P_0 = (1, 0, 2)$ in the point-normal equation form:

$$
1(x - 1) + 2(y - 0) + 3(z - 2) = 0
$$

Expand and simplify to obtain the general Cartesian equation:

$$
\begin{aligned}
x - 1 + 2y + 3z - 6 &= 0 \\
x + 2y + 3z - 7 &= 0 \\
x + 2y + 3z &= 7
\end{aligned}
$$

**Step 5: Check that both the entire line and the point lie in the plane**

1. **Check the external point $P = (0, 2, 1)$:**

$$
0 + 2(2) + 3(1) = 0 + 4 + 3 = 7 \quad (\text{True})
$$

2. **Check the entire line $(x, y, z) = (1 + t, \, t, \, 2 - t)$:**

Substitute the parametric coordinates of the line into the plane equation:

$$
(1 + t) + 2(t) + 3(2 - t) = 7
$$

Simplify the expression:

$$
1 + t + 2t + 6 - 3t = 7 \implies 7 = 7 \quad (\text{True for all } t \in \mathbb{R})
$$

Since the identity holds for any real parameter $t$, every point on the line lies within the plane.

---

### Final Answer

1. **Equation of the plane:** 

$$
x + 2y + 3z = 7
$$

2. **Verification:** The given point $P(0, 2, 1)$ satisfies the equation, and substituting the parametric line expression yields $7 = 7$ identically for all $t[cite: 12, 13]$.
