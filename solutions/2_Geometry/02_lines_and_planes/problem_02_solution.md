### Essential Formulas

**Parametric Equation of a Line in $\mathbb{R}^3$:**
A line $L$ passing through a given point $P_0 = (x_0, y_0, z_0)$ and parallel to a nonzero direction vector $v = (v_1, v_2, v_3)$ is described in parametric form by:

$$
(x, y, z) = P_0 + t v = (x_0 + t v_1, \, y_0 + t v_2, \, z_0 + t v_3), \qquad t \in \mathbb{R}
$$

**Condition for a Point to Lie on a Line:**
A point $P_1 = (x_1, y_1, z_1)$ lies on the line if and only if there exists a **single, unique real number** $t$ that satisfies the coordinate equations simultaneously:

$$
\begin{cases}
x_1 = x_0 + t v_1, \\
y_1 = y_0 + t v_2, \\
z_1 = z_0 + t v_3.
\end{cases}
$$

---

### Problem Statement

**Exercise 2. A Line in Space**

Given

$$
L:(x,y,z)=(2,-1,3)+t(1,2,-2).
$$

State a point on the line and its direction vector, check whether $P=(4,3,-1)$ lies on $L$, and find the point corresponding to $t=-1$.

> **Why this exercise:** reinforces the interpretation of parametric form as “point + direction.”

---

### Solution

**Step 1: State a point on the line and its direction vector**

From the given parametric equation $L:(x,y,z)=(2,-1,3)+t(1,2,-2)$:
* **A point on the line** (corresponding to $t = 0$) is:

$$
P_0 = (2, -1, 3)
$$

* **The direction vector** of the line is:

$$
v = (1, 2, -2)
$$

**Step 2: Check whether $P = (4, 3, -1)$ lies on $L$**

Substitute the coordinates of $P = (4, 3, -1)$ into the parametric equations of the line to check if a consistent parameter value $t$ exists:

$$
\begin{cases}
2 + t = 4 \\
-1 + 2t = 3 \\
3 - 2t = -1
\end{cases}
$$

Solve each equation for $t$:
1. From the first equation: $t = 4 - 2 = 2$.
2. From the second equation: $2t = 3 + 1 = 4 \implies t = 2$.
3. From the third equation: $-2t = -1 - 3 = -4 \implies t = 2$.

Because all three equations yield the **exact same unique parameter value** ($t = 2$), the point $P = (4, 3, -1)$ lies on the line $L$.

**Step 3: Find the point corresponding to $t = -1$**

Substitute $t = -1$ into the parametric equation of the line:

$$
\begin{aligned}
(x, y, z) &= (2, -1, 3) + (-1)(1, 2, -2) \\
&= (2 - 1, \, -1 - 2, \, 3 - (-2)) \\
&= (1, -3, 5)
\end{aligned}
$$

**Step 4: Verification**

* **Check for $P(4, 3, -1)$:** Evaluating the line at $t = 2$ gives $(2 + 2, \, -1 + 2(2), \, 3 - 2(2)) = (4, 3, -1)$, which matches $P$ identically.
* **Check for $t = -1$:** Substituting back into the coordinate equations confirms that the derived point $(1, -3, 5)$ satisfies the linear parameter path.

---

### Final Answer

1. **Point on the line:** $P_0 = (2, -1, 3)$; **Direction vector:** $v = (1, 2, -2)$.
2. **Membership check:** The point $P = (4, 3, -1)$ **lies on the line** $L$ (corresponding to parameter value $t = 2$).
3. **Point at $t = -1$:** $(1, -3, 5)$.
