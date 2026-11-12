### Essential Formulas

**Direction Vectors Lying in a Plane Determined by Three Points:**
Given three non-collinear points $A, B, C \in \mathbb{R}^3$, subtracting the position of $A$ from $B$ and $C$ produces two non-parallel vectors lying entirely in the plane containing $A, B, C$:

$$
u = \overrightarrow{AB} = B - A, \qquad v = \overrightarrow{AC} = C - A
$$

**Normal Vector to a Plane via the Cross Product:**
For two non-parallel vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ lying in a plane, their cross product $n = u \times v$ (or any nonzero scalar multiple thereof) is perpendicular to both $u$ and $v$, and hence **normal (perpendicular) to the entire plane**:

$$
n = u \times v = (u_2 v_3 - u_3 v_2, \; u_3 v_1 - u_1 v_3, \; u_1 v_2 - u_2 v_1)
$$

**Orthogonality Verification Criterion:**
A nonzero vector $n$ is perpendicular to both $u$ and $v$ if and only if:

$$
n \cdot u = 0 \qquad \mathrm{and} \qquad n \cdot v = 0
$$

---

### Problem Statement

**Exercise 12. A Normal Vector to a Plane**

Given $A=(1,0,2)$, $B=(2,1,0)$, and $C=(0,3,1)$. Construct two vectors lying in the plane, find a vector perpendicular to both, and check the perpendicularity using dot products.

> **Why this exercise:** creates a direct bridge from vectors to the description of a plane.

---

### Solution

**Step 1: Construct two vectors lying in the plane**

Using $A = (1, 0, 2)$ as the common reference point, construct the displacement vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ joining $A$ to $B = (2, 1, 0)$ and $C = (0, 3, 1)$:

$$
\begin{aligned}
u &= \overrightarrow{AB} = B - A = (2 - 1, \, 1 - 0, \, 0 - 2) = (1, 1, -2), \\
v &= \overrightarrow{AC} = C - A = (0 - 1, \, 3 - 0, \, 1 - 2) = (-1, 3, -1).
\end{aligned}
$$

Because $u = (1, 1, -2)$ and $v = (-1, 3, -1)$ are not scalar multiples of one another, the points $A, B, C$ are non-collinear and uniquely define a plane in $\mathbb{R}^3$, with both $u$ and $v$ lying inside that plane.

**Step 2: Find a vector $n$ perpendicular to both $u$ and $v$**

Compute the cross product $n = u \times v$ using $u = (1, 1, -2)$ and $v = (-1, 3, -1)$:

$$
\begin{aligned}
n &= u \times v = (1, 1, -2) \times (-1, 3, -1) \\
&= \bigl(1 \cdot (-1) - (-2) \cdot 3, \; (-2) \cdot (-1) - 1 \cdot (-1), \; 1 \cdot 3 - 1 \cdot (-1)\bigr) \\
&= (-1 + 6, \; 2 + 1, \; 3 + 1) \\
&= (5, 3, 4)
\end{aligned}
$$

Thus, $n = (5, 3, 4)$ is a normal vector perpendicular to both $u$ and $v$ (and therefore perpendicular to every vector in the plane through $A, B, C$).

**Step 3: Check perpendicularity using dot products**

Compute the dot product of $n = (5, 3, 4)$ with $u = (1, 1, -2)$ and with $v = (-1, 3, -1)$:

1. **Dot product with $u = \overrightarrow{AB}$:**

$$
\begin{aligned}
n \cdot u &= (5, 3, 4) \cdot (1, 1, -2) \\
&= 5 \cdot 1 + 3 \cdot 1 + 4 \cdot (-2) \\
&= 5 + 3 - 8 \\
&= 0
\end{aligned}
$$

2. **Dot product with $v = \overrightarrow{AC}$:**

$$
\begin{aligned}
n \cdot v &= (5, 3, 4) \cdot (-1, 3, -1) \\
&= 5 \cdot (-1) + 3 \cdot 3 + 4 \cdot (-1) \\
&= -5 + 9 - 4 \\
&= 0
\end{aligned}
$$

Since $n = (5, 3, 4) \neq \mathbf{0}$ and both $n \cdot u = 0$ and $n \cdot v = 0$, $n$ is confirmed to be perpendicular to both vectors in the plane.

**Step 4: Verification**

* **Check against the third edge vector $\overrightarrow{BC}$ in the plane:**
  Constructing $\overrightarrow{BC} = C - B = (0 - 2, \, 3 - 1, \, 1 - 0) = (-2, 2, 1)$ (which also lies in the plane since $\overrightarrow{BC} = \overrightarrow{AC} - \overrightarrow{AB}$) and taking its dot product with $n = (5, 3, 4)$ gives:

$$
n \cdot \overrightarrow{BC} = (5, 3, 4) \cdot (-2, 2, 1) = -10 + 6 + 4 = 0
$$

* **Plane equation consistency check:**
  Using normal vector $n = (5, 3, 4)$ and point $A = (1, 0, 2)$ yields the scalar plane equation $5(x - 1) + 3(y - 0) + 4(z - 2) = 0 \iff 5x + 3y + 4z = 13$. Evaluating $5x + 3y + 4z$ at all three given points gives:
  * At $A = (1, 0, 2)$: $5(1) + 3(0) + 4(2) = 5 + 0 + 8 = 13$.
  * At $B = (2, 1, 0)$: $5(2) + 3(1) + 4(0) = 10 + 3 + 0 = 13$.
  * At $C = (0, 3, 1)$: $5(0) + 3(3) + 4(1) = 0 + 9 + 4 = 13$.
  All three points satisfy the exact same plane equation, independently confirming the normal vector $n = (5, 3, 4)$.

---

### Final Answer

1. **Two vectors lying in the plane:**

$$
\overrightarrow{AB} = (1, 1, -2), \qquad \overrightarrow{AC} = (-1, 3, -1)
$$

2. **Normal vector perpendicular to both:**

$$
n = \overrightarrow{AB} \times \overrightarrow{AC} = (5, 3, 4)
$$

3. **Perpendicularity verification via dot products:**

$$
n \cdot \overrightarrow{AB} = 5(1) + 3(1) + 4(-2) = 0, \qquad n \cdot \overrightarrow{AC} = 5(-1) + 3(3) + 4(-1) = 0
$$

   confirming that $n = (5, 3, 4)$ is perpendicular to both vectors and normal to the plane through $A, B, C$.
