### Essential Formulas

**Relative Positions of Two Lines in $\mathbb{R}^3$:**
Given two lines $L_1$ and $L_2$ with direction vectors $v_1$ and $v_2$ passing through points $P_1$ and $P_2$ respectively:
1. **Parallel:** The direction vectors are scalar multiples ($v_1 = k v_2$). If a point on $L_1$ also satisfies $L_2$, they are identical; otherwise, they are strictly parallel.
2. **Intersecting:** The lines are not parallel, and their parametric equations yield a unique, consistent intersection point $(x, y, z)$.
3. **Skew:** The lines are neither parallel nor intersecting (they do not lie in the same plane).

**Checking for Intersection:**
Equating the coordinates of $L_1$ and $L_2$ produces a system of three linear equations in two parameters ($t$ and $s$). If a unique solution $(t, s)$ satisfies all three equations simultaneously, the lines intersect. If no solution exists, they are either parallel or skew.

---

### Problem Statement

**Exercise 5. Relative Position of Two Lines**

Analyze the position of

$$
L_1:(x,y,z)=(1,1,0)+t(1,2,1),
$$

$$
L_2:(x,y,z)=(2,0,1)+s(0,1,-1).
$$

If they intersect, give the intersection point. If not, determine whether they are parallel or skew. Justify the classification.

> **Why this exercise:** teaches how to distinguish qualitatively different relationships between lines in space.

---

### Solution

**Step 1: Identify direction vectors and check for parallelism**

From the parametric descriptions, extract the direction vectors:
* For $L_1$: $v_1 = (1, 2, 1)$
* For $L_2$: $v_2 = (0, 1, -1)$

Check if $v_1$ is a scalar multiple of $v_2$:

$$
(1, 2, 1) = k(0, 1, -1) \implies 1 = k \cdot 0 \implies \text{No solution}
$$

Because no such scalar $k$ exists, the direction vectors are not proportional. Therefore, the lines **are not parallel**. They either intersect or are skew.

**Step 2: Set up the coordinate equations to test for intersection**

Equate the corresponding $x, y,$ and $z$ components of $L_1$ and $L_2$:

$$
\begin{cases}
1 + t = 2 \\
1 + 2t = s \\
t = 1 - s
\end{cases}
$$

**Step 3: Solve the system for parameters $t$ and $s$**

1. From the first equation, directly solve for $t$:

$$
t = 2 - 1 = 1
$$

2. Substitute $t = 1$ into the second equation to find $s$:

$$
1 + 2(1) = s \implies s = 3
$$

3. Check consistency by substituting $t = 1$ and $s = 3$ into the third equation:

$$
1 = 1 - (3) \implies 1 = -2 \quad (\text{Contradiction})
$$

Because the third equation yields an inconsistent result ($1 \neq -2$), the system of equations has **no solution**.

**Step 4: Classify the relative position**

Since the lines are not parallel and fail to intersect, they do not share any common points in space. Therefore, lines $L_1$ and $L_2$ are **skew lines**.

**Step 5: Verification**

* **Direction test:** Non-collinear direction vectors $v_1 = (1, 2, 1)$ and $v_2 = (0, 1, -1)$ confirm they are not parallel.
* **Scalar triple product check for coplanarity:** 
  The vector connecting the base points $P_1 = (1, 1, 0)$ and $P_2 = (2, 0, 1)$ is $P_2 - P_1 = (1, -1, 1)$. The determinant formed by $(P_2 - P_1, v_1, v_2)$ is:

$$
\det
\begin{pmatrix}
1 & -1 & 1 \\
1 & 2 & 1 \\
0 & 1 & -1 \\
\end{pmatrix}
= 1(-2 - 1) - (-1)(-1 - 0) + 1(1 - 0) = -3 - 1 + 1 = -3 \neq 0
$$

  Because the scalar triple product is nonzero, the lines do not lie in the same plane, confirming mathematically that they are skew.

---

### Final Answer

1. **Classification:** The lines $L_1$ and $L_2$ are **skew lines** (they are neither parallel nor do they intersect).
2. **Justification:** The direction vectors are not proportional (ruling out parallelism), and equating the coordinate components leads to a contradiction ($1 = -2$), proving there is no intersection point[cite: 16].
