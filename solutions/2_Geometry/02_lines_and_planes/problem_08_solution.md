### Essential Formulas

**Relative Position of Two Lines in Space:**
Given two lines $L_1: P_1 + t v_1$ and $L_2: P_2 + s v_2$:
1. **Parallel:** $v_1$ and $v_2$ are scalar multiples ($v_1 = k v_2$ for some $k \neq 0$). If $P_1$ also lies on $L_2$, the lines are identical; otherwise, they are strictly parallel.
2. **Intersecting:** $v_1$ and $v_2$ are not parallel, and the system $P_1 + t v_1 = P_2 + s v_2$ has a unique solution $(t, s)$.
3. **Skew:** $v_1$ and $v_2$ are not parallel, and the system $P_1 + t v_1 = P_2 + s v_2$ is inconsistent (no solution).

---

### Problem Statement

**Exercise 8. Relative Position of Two Lines**

Determine whether the lines

$$L_1: \begin{cases} x = 1 + t, \\ y = 2 - t, \\ z = 3 + 2t, \end{cases} \qquad L_2: \begin{cases} x = 3 + s, \\ y = 2s, \\ z = 1 + s \end{cases}$$

are parallel, intersect, or are skew. If they intersect, find the point of intersection.

> **Why this exercise:** builds a systematic decision procedure for comparing two lines in $\mathbb{R}^3$.

---

### Solution

**Step 1: Check if the direction vectors are parallel**

Extract the direction vectors from the parametric equations:

$$v_1 = (1, -1, 2), \qquad v_2 = (1, 2, 1)$$

Compare the ratios of corresponding components:

$$\frac{1}{1} = 1, \qquad \frac{-1}{2} = -\frac{1}{2}$$

Since $1 \neq -\frac{1}{2}$, $v_1$ is not a scalar multiple of $v_2$. Therefore, the lines are **not parallel**.

**Step 2: Set up the system of equations for intersection**

Equate the $x$, $y$, and $z$ coordinates of $L_1$ and $L_2$:

$$\begin{cases} 1 + t = 3 + s, \\ 2 - t = 2s, \\ 3 + 2t = 1 + s \end{cases}$$

**Step 3: Solve the first two equations for $t$ and $s$**

From the first equation, express $t$ in terms of $s$:

$$t = s + 2$$

Substitute $t = s + 2$ into the second equation:

$$2 - (s + 2) = 2s \implies -s = 2s \implies 3s = 0 \implies s = 0$$

Substitute $s = 0$ back into $t = s + 2$:

$$t = 0 + 2 = 2$$

**Step 4: Check consistency in the third equation**

Substitute $t = 2$ and $s = 0$ into the third equation ($3 + 2t = 1 + s$):
* **Left-hand side:** $3 + 2(2) = 3 + 4 = 7$
* **Right-hand side:** $1 + 0 = 1$

Since $7 \neq 1$, the third equation is not satisfied, meaning the system has **no solution**.

**Step 5: Conclude the relative position**

Because the lines are neither parallel nor intersecting, they are **skew lines**.

---

### Final Answer

1. **Relative position:** The lines $L_1$ and $L_2$ are **skew**.
2. **Intersection point:** None (the lines do not intersect).
