### Problem Statement

For $u=(1,2,-1)$ and $v=(2,-1,3)$ compute $u\cdot v$ and determine whether the vectors are perpendicular. Then find $a$ so that $w=(2,-1,a)$ is perpendicular to $u$, and check the result.

> **Why this exercise:** shows the dot product as both a test and a tool for constructing a perpendicularity condition.

---

### Solution

#### Essential Formulas

1. **Dot Product (Scalar Product) in $\mathbb{R}^3$:**
   For vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$:

   $$
   u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3
   $$

2. **Geometric Definition and Orthogonality Criterion:**
   The dot product is related to the angle $\theta$ between the vectors by:

   $$
   u \cdot v = \|u\| \|v\| \cos\theta
   $$

   Two non-zero vectors $u$ and $v$ are perpendicular (orthogonal, $u \perp v$) if and only if their dot product vanishes:

   $$
   u \perp v \iff u \cdot v = 0
   $$

   * If $u \cdot v > 0$: $\theta$ is acute ($0 \le \theta < \pi/2$).
   * If $u \cdot v = 0$: $\theta = \pi/2$ (right angle, perpendicular).
   * If $u \cdot v < 0$: $\theta$ is obtuse ($\pi/2 < \theta \le \pi$).

---

**Step 1: Compute the Dot Product $u \cdot v$**

Given $u = (1, 2, -1)$ and $v = (2, -1, 3)$:

$$
u \cdot v = (1)(2) + (2)(-1) + (-1)(3)
$$

Compute the products:

$$
(1)(2) = 2, \qquad (2)(-1) = -2, \qquad (-1)(3) = -3
$$

Sum the terms:

$$
u \cdot v = 2 - 2 - 3 = -3
$$

---

**Step 2: Determine Whether $u$ and $v$ Are Perpendicular**

According to the orthogonality criterion:

$$
u \perp v \iff u \cdot v = 0
$$

Since:

$$
u \cdot v = -3 \neq 0
$$

the vectors $u$ and $v$ are **not perpendicular**.
Furthermore, because $u \cdot v = -3 < 0$, the angle $\theta$ between them is obtuse ($\theta > 90^\circ$).

---

**Step 3: Find $a$ Such that $w = (2, -1, a)$ Is Perpendicular to $u$**

For $w$ to be perpendicular to $u$, their dot product must be equal to zero:

$$
w \cdot u = 0
$$

Compute $w \cdot u$ using $w = (2, -1, a)$ and $u = (1, 2, -1)$:

$$
w \cdot u = (2)(1) + (-1)(2) + (a)(-1) = 0
$$

Evaluate the arithmetic terms:

$$
2 - 2 - a = 0
$$

$$
0 - a = 0 \implies a = 0
$$

Thus, the required value of the parameter is $a = 0$.

---

**Step 4: Verification of Perpendicularity**

Substitute $a = 0$ into vector $w$:

$$
w = (2, \ -1, \ 0)
$$

Now compute the dot product $w \cdot u$:

$$
w \cdot u = (2)(1) + (-1)(2) + (0)(-1) = 2 - 2 + 0 = 0
$$

Because $w \cdot u = 0$, the vector $w = (2, -1, 0)$ is confirmed to be perpendicular to $u$.

---

### Final Answer

1. **Dot Product $u \cdot v$:**

   $$
   u \cdot v = -3
   $$

2. **Perpendicularity of $u$ and $v$:**
   The vectors $u$ and $v$ are **not perpendicular** because $u \cdot v = -3 \neq 0$.

3. **Value of Parameter $a$:**

   $$
   a = 0
   $$

   yielding the perpendicular vector $w = (2, -1, 0)$.

4. **Verification:**

   $$
   w \cdot u = (2)(1) + (-1)(2) + (0)(-1) = 0 \implies w \perp u
   $$