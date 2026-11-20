### Essential Formulas

**Relative Position of a Line and a Plane:**
Let a line be parameterized as $L: P_0 + t v$ with base point $P_0$ and direction vector $v$, and let a plane be given by $\Pi: a x + b y + c z = d$ with normal vector $n = (a, b, c)$. The dot product $n \cdot v$ measures whether the line direction is perpendicular to the plane's normal vector (i.e., parallel to the plane):
1. **Unique Intersection Point:** $n \cdot v \neq 0$ (the line pierces the plane transversally).
2. **Strictly Parallel (No Common Points):** $n \cdot v = 0$ and $P_0 \notin \Pi$ ($n \cdot P_0 \neq d$).
3. **Line Contained in the Plane:** $n \cdot v = 0$ and $P_0 \in \Pi$ ($n \cdot P_0 = d$).

---

### Problem Statement

**Exercise 7. Classifying a Line Relative to a Plane**

Classify the line

$$
L: P_0 + t v = (1, 1, 0) + t(1, -1, 0)
$$

relative to the plane

$$
\Pi: x + y + z = 2,
$$

and explain the geometric meaning of the dot product $n \cdot v$ in this classification.

> **Why this exercise:** connects the algebraic dot product $n \cdot v$ with the geometric orientation between a line and a plane.

---

### Solution

**Step 1: Identify the line and plane vectors**

* **Line $L$:** Base point $P_0 = (1, 1, 0)$, direction vector $v = (1, -1, 0)$.
* **Plane $\Pi$:** Normal vector $n = (1, 1, 1)$, constant $d = 2$.

**Step 2: Compute and explain $n \cdot v$**

Compute the dot product between the plane normal $n$ and the line direction $v$:

$$
n \cdot v = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0
$$

**Geometric meaning of $n \cdot v$:**
The normal vector $n$ is perpendicular to every vector lying in the plane $\Pi$. Because $n \cdot v = 0$, the direction vector $v$ is orthogonal to $n$, which means the line $L$ runs **parallel to the plane $\Pi$** (either strictly parallel above/below it, or lying completely inside it).

**Step 3: Check whether the base point $P_0$ lies on the plane $\Pi$**

Substitute $P_0 = (1, 1, 0)$ into the left-hand side of $x + y + z = 2$:

$$
n \cdot P_0 = 1(1) + 1(1) + 1(0) = 2 = d
$$

Since $P_0 = (1, 1, 0)$ satisfies the plane equation $x + y + z = 2$, the point $P_0$ lies on $\Pi$.

**Step 4: Verify for an arbitrary parameter $t \in \mathbb{R}$**

For any point $(x, y, z) = (1 + t, 1 - t, 0)$ on $L$:

$$
(1 + t) + (1 - t) + 0 = 2
$$

Every point of $L$ satisfies the plane equation.

---

### Final Answer

1. **Classification:** The line $L$ is **contained in the plane** $\Pi$.
2. **Explanation of $n \cdot v$:** Since $n \cdot v = 0$, the direction vector $v$ is perpendicular to the plane's normal vector $n$, ensuring $L$ is parallel to $\Pi$; combined with $P_0 = (1, 1, 0) \in \Pi$, the entire line lies within the plane.
