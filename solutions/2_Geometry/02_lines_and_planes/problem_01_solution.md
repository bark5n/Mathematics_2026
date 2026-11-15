### Essential Formulas

**Direction Vector of a Line Through Two Points:**
Given two distinct points $A = (x_1, y_1)$ and $B = (x_2, y_2)$ in $\mathbb{R}^2$, the vector pointing from $A$ to $B$ serves as a direction vector $v$ for the line passing through them:

$$
v = B - A = (x_2 - x_1, \, y_2 - y_1)
$$

**Parametric Form of a Line:**
A line passing through a point $A = (x_0, y_0)$ with direction vector $v = (v_1, v_2)$ is given parametrically by:

$$
(x, y) = A + t v = (x_0 + t v_1, \, y_0 + t v_2), \qquad t \in \mathbb{R}
$$

**General Form and Normal Vector of a Line in $\mathbb{R}^2$:**
The general linear equation of a line is expressed as:

$$
ax + by = c
$$

where the vector $n = (a, b)$ is **normal (perpendicular)** to the line and satisfies $n \cdot v = 0$ with any direction vector $v = (v_1, v_2)$ of the line (i.e., $a v_1 + b v_2 = 0$).

---

### Problem Statement

**Exercise 1. Line Through Two Points**

Find the equation of the line through $A=(1,2)$ and $B=(4,-1)$ in parametric and general form. Identify a direction vector and an example of a normal vector. Check that both points satisfy the equation you obtain.

> **Why this exercise:** teaches how to move between equivalent descriptions of a line and connect them with the appropriate vectors.

---

### Solution

**Step 1: Identify a direction vector $v$**

Subtract the coordinates of point $A = (1, 2)$ from $B = (4, -1)$ to obtain a direction vector $v$:

$$
\begin{aligned}
v &= B - A = (4 - 1, \, -1 - 2) \\
&= (3, -3)
\end{aligned}
$$

We can simplify this direction vector by dividing by the common scalar factor $3$ to use the cleaner primitive direction vector:

$$
v = (1, -1)
$$

**Step 2: Write the parametric form of the line**

Using the point $A = (1, 2)$ as the initial position and $v = (1, -1)$ as the direction vector, the parametric equations are:

$$
\begin{cases}
x = 1 + t, \\
y = 2 - t,
\end{cases}
\qquad t \in \mathbb{R}
$$

or compactly in vector form:

$$
(x, y) = (1, 2) + t(1, -1)
$$

**Step 3: Find a normal vector $n$ and the general form of the line**

Let the normal vector be $n = (a, b)$. Since $n$ must be perpendicular to the direction vector $v = (1, -1)$, their dot product must be zero ($n \cdot v = 0$):

$$
(a, b) \cdot (1, -1) = a(1) + b(-1) = a - b = 0 \implies a = b
$$

Choosing $a = 1$ gives $b = 1$, yielding a simple normal vector:

$$
n = (1, 1)
$$

Using this normal vector $n = (1, 1)$ and the point $A = (1, 2)$ in the point-normal equation form $a(x - x_1) + b(y - y_1) = 0$:

$$
1(x - 1) + 1(y - 2) = 0
$$

Expanding and simplifying gives the general form:

$$
x + y = 3
$$

**Step 4: Check that both points satisfy the general equation**

1. **Check point $A = (1, 2)$:**

$$
1 + 2 = 3 \quad (\text{True})
$$

2. **Check point $B = (4, -1)$:**

$$
4 + (-1) = 3 \quad (\text{True})
$$

Both points satisfy the line equation identically.

**Step 5: Verification via slope-intercept form**

The slope $m$ of the line passing through $A(1, 2)$ and $B(4, -1)$ is:

$$
m = \frac{-1 - 2}{4 - 1} = \frac{-3}{3} = -1
$$

Using the point-slope form with point $A(1, 2)$:

$$
y - 2 = -1(x - 1) \implies y - 2 = -x + 1 \implies x + y = 3
$$

This matches the general form obtained in Step 3.

---

### Abstract Summary & Identified Vectors

1. **Direction vector:** $v = (1, -1)$ (or any nonzero scalar multiple such as $(3, -3)$).
2. **Normal vector:** $n = (1, 1)$ (or any nonzero scalar multiple such as $(2, 2)$).
3. **Parametric equation:** $(x, y) = (1, 2) + t(1, -1)$.
4. **General equation:** $x + y = 3$.
