### Essential Formulas

**Edge Vectors from Three Points:**
Given three non-collinear points $A, B, C \in \mathbb{R}^3$, two vectors lying entirely within the plane passing through them are given by:

$$
\overrightarrow{AB} = B - A, \qquad \overrightarrow{AC} = C - A
$$

**Normal Vector via Cross Product:**
The cross product of $\overrightarrow{AB}$ and $\overrightarrow{AC}$ produces a vector orthogonal to both, which serves as the normal vector $n$ to the plane:

$$
n = \overrightarrow{AB} \times \overrightarrow{AC}
$$

---

### Problem Statement

**Exercise 4. Plane Through Three Points**

Find the equation of the plane through

$$
A=(1,0,0),\quad B=(0,1,0),\quad C=(0,0,1).
$$

First construct two vectors lying in the plane, and then use the cross product. Check the resulting equation on all three points[cite: 16].

> **Why this exercise:** connects earlier vector tools with constructing the equation of a plane[cite: 16].

---

### Solution

**Step 1: Construct two vectors lying in the plane**

Using point $A = (1, 0, 0)$ as the common reference vertex, construct the edge vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ to points $B = (0, 1, 0)$ and $C = (0, 0, 1)$:

$$
\begin{aligned}
\overrightarrow{AB} &= B - A = (0 - 1, \, 1 - 0, \, 0 - 0) = (-1, 1, 0), \\
\overrightarrow{AC} &= C - A = (0 - 1, \, 0 - 0, \, 1 - 0) = (-1, 0, 1).
\end{aligned}
$$

**Step 2: Find the normal vector $n$ using the cross product**

Compute the cross product $n = \overrightarrow{AB} \times \overrightarrow{AC}$ to find a vector perpendicular to both vectors (and thus normal to the plane):

$$
\begin{aligned}
n &= \overrightarrow{AB} \times \overrightarrow{AC} = (-1, 1, 0) \times (-1, 0, 1) \\
&= \bigl(1 \cdot 1 - 0 \cdot 0, \, 0 \cdot (-1) - (-1) \cdot 1, \, (-1) \cdot 0 - 1 \cdot (-1)\bigr) \\
&= (1 - 0, \, 0 + 1, \, 0 + 1) \\
&= (1, 1, 1)
\end{aligned}
$$

**Step 3: Write the equation of the plane**

Using the normal vector $n = (1, 1, 1)$ and point $A = (1, 0, 0)$ in the point-normal equation form:

$$
1(x - 1) + 1(y - 0) + 1(z - 0) = 0
$$

Expanding and simplifying gives the general equation of the plane:

$$
x + y + z = 1
$$

**Step 4: Check the resulting equation on all three points**

1. **Check point $A = (1, 0, 0)$:**

$$
1 + 0 + 0 = 1 \quad (\text{True})
$$

2. **Check point $B = (0, 1, 0)$:**

$$
0 + 1 + 0 = 1 \quad (\text{True})
$$

3. **Check point $C = (0, 0, 1)$:**

$$
0 + 0 + 1 = 1 \quad (\text{True})
$$

All three points satisfy the plane equation identically[cite: 16].

---

### Final Answer

1. **Two in-plane vectors:**

$$
\overrightarrow{AB} = (-1, 1, 0), \qquad \overrightarrow{AC} = (-1, 0, 1)
$$

2. **Normal vector:**

$$
n = \overrightarrow{AB} \times \overrightarrow{AC} = (1, 1, 1)
$$

3. **Equation of the plane:**

$$
x + y + z = 1
$$

   (Verified by substituting points $A, B,$ and $C$, all of which satisfy the equation)[cite: 16].
