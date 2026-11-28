### Essential Formulas

**Kinematics via Derivatives:**
Given position $s(t)$ as a function of time $t$:

$$
v(t) = s'(t), \qquad a(t) = v'(t) = s''(t)
$$

* If $v(t) > 0$, the point moves in the positive direction of the coordinate axis.
* If $v(t) < 0$, the point moves in the negative direction of the coordinate axis.
* If $v(t) = 0$, the point is instantaneously at rest (stopped).

---

### Problem Statement

**Problem 1. Motion — from Position to Velocity**

The position of a point is described by

$$
s(t) = t^3 - 6t^2 + 9t + 2, \qquad t \ge 0.
$$

1. Determine the velocity and acceleration.
2. Find the times at which the point stops.
3. Determine on which intervals the point moves in the positive direction of the axis and on which intervals it moves in the negative direction.

> **Why this problem:** it shows the derivative as a real rate of change and requires interpretation of the sign of the derivative in the context of motion.

---

### Solution

**1. Determine the velocity and acceleration**

Differentiate the position function $s(t) = t^3 - 6t^2 + 9t + 2$ once to obtain velocity $v(t)$:

$$
v(t) = s'(t) = 3t^2 - 12t + 9 = 3(t^2 - 4t + 3) = 3(t - 1)(t - 3)
$$

Differentiate velocity $v(t)$ to obtain acceleration $a(t)$:

$$
a(t) = v'(t) = 6t - 12 = 6(t - 2)
$$

**2. Find the times at which the point stops**

The point stops when $v(t) = 0$ for $t \ge 0$:

$$
3(t - 1)(t - 3) = 0 \implies t_1 = 1, \qquad t_2 = 3
$$

Both $t = 1$ and $t = 3$ lie in the domain $t \ge 0$, so the point stops at $t = 1$ and $t = 3$.

**3. Determine the intervals of positive and negative direction of motion**

Analyze the sign of $v(t) = 3(t - 1)(t - 3)$ on the subintervals of $[0, +\infty)$ separated by $t = 1$ and $t = 3$:

| Time Interval | Sign of $(t - 1)$ | Sign of $(t - 3)$ | Sign of $v(t)$ | Direction of Motion |
| :--- | :--- | :--- | :--- | :--- |
| $[0, 1)$ | $-$ | $-$ | $+$ | Positive direction |
| $(1, 3)$ | $+$ | $-$ | $-$ | Negative direction |
| $(3, +\infty)$ | $+$ | $+$ | $+$ | Positive direction |

*(Position milestones: starts at $s(0) = 2$, moves forward to $s(1) = 6$, reverses backward to $s(3) = 2$, and then moves forward indefinitely for $t > 3$.)*

---

### Final Answer

1. **Velocity and acceleration:** $v(t) = 3t^2 - 12t + 9$ and $a(t) = 6t - 12$.
2. **Stopping times:** $t = 1$ and $t = 3$.
3. **Direction of motion:** Moves in the positive direction on $[0, 1)$ and $(3, +\infty)$; moves in the negative direction on $(1, 3)$.
