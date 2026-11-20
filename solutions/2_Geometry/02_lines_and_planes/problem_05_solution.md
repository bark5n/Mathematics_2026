### Essential Formulas

**Classification of Two Lines in Space:**
Given two lines $L_1: P_1 + t v_1$ and $L_2: P_2 + s v_2$ in $\mathbb{R}^3$:
1. **Parallel or Coincident:** $v_1$ and $v_2$ are scalar multiples ($v_1 = k v_2$ for some $k \neq 0$). If $P_1 \in L_2$, they coincide; otherwise they are strictly parallel.
2. **Intersecting:** $v_1$ and $v_2$ are not parallel, and the vector equation $P_1 + t v_1 = P_2 + s v_2$ yields a unique solution $(t, s)$.
3. **Skew:** $v_1$ and $v_2$ are not parallel, and $P_1 + t v_1 = P_2 + s v_2$ has no solution (the system is inconsistent).

---

### Problem Statement

**Exercise 5. Classifying Two Lines in Space**

Classify the relative position of the two lines

$$L_1: P_1 + t v_1 = (1, 1, 0) + t(1, 2, 1), \qquad L_2: P_2 + s v_2 = (2, 0, 1) + s(0, 1, -1),$$

determining whether they are parallel, coincident, intersecting, or skew. If they intersect, find the point of intersection.

> **Why this exercise:** establishes a systematic procedure for testing parallelism and solving parameter equations to classify lines in $\mathbb{R}^3$.

---

### Solution

**Step 1: Check whether the direction vectors are parallel**

Identify the direction vectors of $L_1$ and $L_2$:

$$v_1 = (1, 2, 1), \qquad v_2 = (0, 1, -1)$$

Because the first component of $v_2$ is $0$ while the first component of $v_1$ is $1$, there is no scalar $k$ such that $v_1 = k v_2$. Thus, the lines are **not parallel** (and not coincident).

**Step 2: Set up the coordinate system for intersection**

Equate the parametric coordinates of $L_1$ and $L_2$:

$$\begin{cases} 1 + t = 2 + 0s, \\ 1 + 2t = 0 + s, \\ 0 + t = 1 - s \end{cases}$$

**Step 3: Solve the first two equations for $t$ and $s$**

From the first equation:

$$1 + t = 2 \implies t = 1$$

Substitute $t = 1$ into the second equation:

$$1 + 2(1) = s \implies s = 3$$

**Step 4: Test consistency in the third equation**

Substitute $t = 1$ and $s = 3$ into the third equation ($t = 1 - s$):
* **Left-hand side:** $t = 1$
* **Right-hand side:** $1 - s = 1 - 3 = -2$

Since $1 \neq -2$, the third equation fails and the system is inconsistent.

**Step 5: Conclude the classification**

Since $L_1$ and $L_2$ are neither parallel nor intersecting, they are **skew lines**.

---

### Final Answer

1. **Classification:** The lines $L_1$ and $L_2$ are **skew**.
2. **Intersection:** None (the parameter system is inconsistent because $1 \neq -2$).
