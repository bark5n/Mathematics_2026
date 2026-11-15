### Essential Formulas

**Relative Position of a Line and a Plane:**
Given a line $L: P_0 + tv$ with direction vector $v$, and a plane $\Pi$ with normal vector $n = (a, b, c)$:
1. **Intersection:** If the dot product of the direction vector and the normal vector is nonzero ($n \cdot v \neq 0$), the line intersects the plane at a unique point.
2. **Parallelism:** If $n \cdot v = 0$, the line's direction is orthogonal to the plane's normal vector. If the starting point $P_0$ satisfies the plane equation, the line lies in the plane; otherwise, it is strictly parallel to the plane.

---

### Problem Statement

**Exercise 14. Contrast: Intersection and Parallelism**

From the point $P=(0,0,1)$, two lines are drawn with direction vectors

$$
v_1=(2,1,-1),\qquad v_2=(2,1,0).
$$

For each line, analyze its position relative to the plane $z=0$.

For the line that intersects the plane, find the intersection point. For the other line, explain how you can recognize parallelism without solving an equation.

> **Why this exercise:** compares two very similar data sets that lead to different outcomes and forces recognition of the geometric condition before calculation.

---

### Solution

**Step 1: Identify the plane's normal vector**

The given plane is $\Pi: z = 0$ (the $xy$-plane). Its normal vector is:

$$
n = (0, 0, 1)
$$

**Step 2: Analyze Line $L_1$ with direction vector $v_1 = (2, 1, -1)$**

1. **Parametric equation of $L_1$:** Passing through $P = (0, 0, 1)$ with direction $v_1$:

$$
(x, y, z) = (0, 0, 1) + t(2, 1, -1) = (2t, t, 1 - t)
$$

2. **Test intersection with the plane $z = 0$:**
Substitute the $z$-coordinate into the plane equation:

$$
1 - t = 0 \implies t = 1
$$

3. **Find the intersection point:**
Substitute $t = 1$ back into the parametric equations:

$$
(x, y, z) = (2(1), 1, 1 - 1) = (2, 1, 0)
$$

Line $L_1$ intersects the plane at the point $(2, 1, 0)$.

**Step 3: Analyze Line $L_2$ with direction vector $v_2 = (2, 1, 0)$**

1. **Parametric equation of $L_2$:** Passing through $P = (0, 0, 1)$ with direction $v_2$:

$$
(x, y, z) = (0, 0, 1) + s(2, 1, 0) = (2s, s, 1)
$$

2. **Recognize parallelism without solving an equation:**
Compute the dot product of the direction vector $v_2$ and the normal vector $n$:

$$
n \cdot v_2 = (0)(2) + (0)(1) + (1)(0) = 0
$$

Because $n \cdot v_2 = 0$, the direction vector $v_2$ is orthogonal to the plane's normal vector $n$, meaning the line is parallel to the plane. Furthermore, the starting point $P = (0, 0, 1)$ does not satisfy the plane equation ($1 \neq 0$), confirming that the line does not lie in the plane but is strictly parallel to it. This can be recognized instantly from the zero dot product and constant $z$-coordinate ($z = 1$ for all points on $L_2$) without needing to solve an explicit system of equations.

---

### Final Answer

1. **Line $L_1$:** Intersects the plane $z = 0$ at the point **$(2, 1, 0)$** (at parameter $t = 1$).
2. **Line $L_2$:** Is **strictly parallel** to the plane $z = 0$.
3. **Recognition of parallelism:** Parallelism is recognized immediately without solving an equation by observing that the dot product of the direction vector $v_2 = (2, 1, 0)$ and the normal vector $n = (0, 0, 1)$ is zero ($n \cdot v_2 = 0$), and the constant $z$-coordinate ($z = 1$) never matches the plane level $z = 0$.
