### Essential Formulas

1. **Kinematics: Velocity and Acceleration as Derivatives:**
   For a position function $s(t)$:
   * **Instantaneous Velocity:**

     $$
     v(t) = s'(t) = \frac{ds}{dt}
     $$

   * **Instantaneous Acceleration:**

     $$
     a(t) = v'(t) = s''(t) = \frac{d^2s}{dt^2}
     $$

2. **Direction of Motion:**
   * The particle is moving in the **positive direction** when $v(t) > 0$.
   * The particle is moving in the **negative direction** when $v(t) < 0$.
   * The particle is **instantaneously at rest (stops)** when $v(t) = 0$.

---

### Problem Statement

The position of a point is described by

$$
s(t)=t^3-6t^2+9t+2,\qquad t\ge0.
$$

1. Determine the velocity and acceleration.
2. Find the times at which the point stops.
3. Determine on which intervals the point moves in the positive direction of the axis and on which intervals it moves in the negative direction.

> **Why this problem:** it shows the derivative as a real rate of change and requires interpretation of the sign of the derivative in the context of motion.

---

### Solution

**Step 1: Determine the velocity and acceleration**

1. Differentiate the position function $s(t)$ with respect to time $t$ to find the velocity:

   $$
   v(t) = s'(t) = \frac{d}{dt}[t^3 - 6t^2 + 9t + 2]
   $$

   Apply the power rule:

   $$
   v(t) = 3t^2 - 12t + 9
   $$

   Factor out the constant $3$:

   $$
   v(t) = 3(t^2 - 4t + 3) = 3(t - 1)(t - 3)
   $$

2. Differentiate the velocity function $v(t)$ with respect to time $t$ to find the acceleration:

   $$
   a(t) = v'(t) = \frac{d}{dt}[3t^2 - 12t + 9]
   $$

   $$
   a(t) = 6t - 12 = 6(t - 2)
   $$

---

**Step 2: Find the times at which the point stops**

The point comes to an instantaneous stop when its velocity is zero:

$$
v(t) = 0 \iff 3(t - 1)(t - 3) = 0
$$

The roots are:

$$
t_1 = 1, \qquad t_2 = 3
$$

Since both values satisfy $t \ge 0$, the particle stops at times $t = 1$ and $t = 3$.

---

**Step 3: Determine the direction of motion on intervals**

The stopping times $t = 1$ and $t = 3$ partition the domain $[0, \infty)$ into three intervals:
1. **Interval $[0, 1)$:**
   Test at $t = 0$:

   $$
   v(0) = 3(0 - 1)(0 - 3) = 3(-1)(-3) = 9 > 0
   $$

   Because $v(t) > 0$, the point moves in the **positive direction** on $[0, 1)$.

2. **Interval $(1, 3)$:**
   Test at $t = 2$:

   $$
   v(2) = 3(2 - 1)(2 - 3) = 3(1)(-1) = -3 < 0
   $$

   Because $v(t) < 0$, the point moves in the **negative direction** on $(1, 3)$.

3. **Interval $(3, \infty)$:**
   Test at $t = 4$:

   $$
   v(4) = 3(4 - 1)(4 - 3) = 3(3)(1) = 9 > 0
   $$

   Because $v(t) > 0$, the point moves in the **positive direction** on $(3, \infty)$.

---

### Final Answer

1. **Velocity and Acceleration:**

   $$
   v(t) = 3t^2 - 12t + 9 = 3(t - 1)(t - 3)
   $$

   $$
   a(t) = 6t - 12 = 6(t - 2)
   $$

2. **Times at Which the Point Stops:**

   $$
   t = 1, \qquad t = 3
   $$

3. **Intervals and Direction of Motion:**
   * **Positive direction:** on $[0, 1)$ and on $(3, \infty)$ (where $v(t) > 0$)
   * **Negative direction:** on $(1, 3)$ (where $v(t) < 0$)