### Essential Formulas

1. **Average Value of a Continuous Function:**
   The average (mean) value of a continuous function $f(x)$ over an interval $[a, b]$ is defined as:

   $$
   f_{\mathrm{avg}} = \frac{1}{b - a} \int_a^b f(x) \, dx
   $$

2. **Mean Value Theorem for Definite Integrals:**
   If $f$ is continuous on $[a, b]$, there exists at least one point $c \in [a, b]$ such that:

   $$
   f(c) = f_{\mathrm{avg}} = \frac{1}{b - a} \int_a^b f(x) \, dx
   $$

   or equivalently:

   $$
   \int_a^b f(x) \, dx = f(c)(b - a)
   $$

---

### Problem Statement

Compute the average value of the function

$$
f(x)=x^2
$$

on the interval $[0,3]$.

Find a point $c\in[0,3]$ for which $f(c)$ is equal to this average value, and interpret the result geometrically.

> **Why this problem:** it gives the integral the interpretation of an average value and connects the numerical result with a level of the function on the graph.

---

### Solution

**Step 1: Compute the average value $f_{\mathrm{avg}}$**

The interval is $[a, b] = [0, 3]$, so the length of the interval is:

$$
b - a = 3 - 0 = 3
$$

Compute the definite integral of $f(x) = x^2$ over $[0, 3]$:

$$
\int_0^3 x^2 \, dx = \left[ \frac{x^3}{3} \right]_0^3 = \frac{3^3}{3} - 0 = \frac{27}{3} = 9
$$

Compute the average value using the formula:

$$
f_{\mathrm{avg}} = \frac{1}{b - a} \int_a^b f(x) \, dx = \frac{1}{3} \cdot 9 = 3
$$

The average value of $f(x) = x^2$ on $[0, 3]$ is $3$.

---

**Step 2: Find the point $c \in [0, 3]$ where $f(c) = f_{\mathrm{avg}}$**

Set the function value at $c$ equal to the average value $3$:

$$
f(c) = 3 \iff c^2 = 3
$$

Taking the square root gives two algebraic solutions:

$$
c = \pm\sqrt{3}
$$

Because the interval is $[0, 3]$, discard the negative root $-\sqrt{3} < 0$. The unique point belonging to the interval is:

$$
c = \sqrt{3} \approx 1.73205
$$

Since $0 \le \sqrt{3} \le 3$, this point satisfies the Mean Value Theorem for Integrals.

---

**Step 3: Geometric interpretation**

1. **Equal Area Rectangle:**
   The area under the parabola $y = x^2$ from $x = 0$ to $x = 3$ is:

   $$
   A = \int_0^3 x^2 \, dx = 9
   $$

   Consider a rectangle constructed on the same base $[0, 3]$ (width $= 3$) with a constant horizontal height equal to $f_{\mathrm{avg}} = 3$.
   The area of this rectangle is:

   $$
   A_{\mathrm{rect}} = 3 \times 3 = 9
   $$

   The area under the curved parabola is identical to the area of the rectangle of height $f_{\mathrm{avg}}$.

2. **Level of Balance:**
   The point $c = \sqrt{3}$ is the horizontal coordinate where the parabola intersects the horizontal line $y = 3$.
   * To the left of $c$ (on $[0, \sqrt{3}]$), the curve lies below the horizontal line $y = 3$, creating a deficit.
   * To the right of $c$ (on $[\sqrt{3}, 3]$), the curve rises above the line $y = 3$, creating a surplus.
   The surplus area above the line $y = 3$ on $[\sqrt{3}, 3]$ fits into the deficit area below the line on $[0, \sqrt{3}]$. The average value $f_{\mathrm{avg}} = 3$ represents the level water line if the area under the curve were liquid leveled out flat.

---

### Final Answer

1. **Average Value:**

   $$
   f_{\mathrm{avg}} = \frac{1}{3}\int_0^3 x^2\,dx = 3
   $$

2. **Point $c$:**

   $$
   c = \sqrt{3} \approx 1.732
   $$

3. **Geometric Interpretation:**
   The area under the parabolic curve on $[0, 3]$ ($A = 9$) equals the area of a rectangle of width $3$ and constant height $f_{\mathrm{avg}} = 3$. The point $c = \sqrt{3}$ is where the curve reaches this balancing height.