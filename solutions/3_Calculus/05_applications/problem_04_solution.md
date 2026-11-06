### Essential Formulas

1. **Area Between Two Curves:**
   If $f(x) \ge g(x)$ for all $x \in [a, b]$, the area of the region bounded between $y = f(x)$ and $y = g(x)$ from $x = a$ to $x = b$ is:

   $$
   A = \int_a^b (f(x) - g(x)) \, dx = \int_a^b (y_{\mathrm{top}} - y_{\mathrm{bottom}}) \, dx
   $$

2. **Intersection of Curves:**
   The limits of integration $a$ and $b$ are determined by solving:

   $$
   f(x) = g(x) \iff f(x) - g(x) = 0
   $$

3. **Power Rule of Integration:**

   $$
   \int_a^b x^n \, dx = \left[ \frac{x^{n+1}}{n+1} \right]_a^b
   $$

---

### Problem Statement

Find the area of the region bounded by the graphs

$$
y=x
$$

and

$$
y=x^2.
$$

First find the intersection points and justify which function is greater on the relevant interval.

> **Why this problem:** it teaches that before integrating, one must first determine the geometry of the region and the correct order of the functions.

---

### Solution

**Step 1: Find the intersection points**

Set the two functions equal to each other to locate the bounding endpoints:

$$
x^2 = x
$$

Rearrange into standard polynomial form:

$$
x^2 - x = 0 \iff x(x - 1) = 0
$$

The roots are:

$$
x_1 = 0, \qquad x_2 = 1
$$

Compute the corresponding $y$-coordinates:
* At $x = 0$: $y = 0 \implies (0, 0)$
* At $x = 1$: $y = 1 \implies (1, 1)$

The two curves enclose a finite region between the $x$-coordinates $a = 0$ and $b = 1$.

---

**Step 2: Justify which function is greater on the interval $(0, 1)$**

Consider the vertical difference $d(x) = x - x^2$:

$$
d(x) = x(1 - x)
$$

For any $x$ in the open interval $(0, 1)$:
* $x > 0$
* $1 - x > 0$

The product of two positive numbers is strictly positive:

$$
x(1 - x) > 0 \implies x > x^2 \quad \forall x \in (0, 1)
$$

*Numerical Test Point:* At $x = \frac{1}{2}$:

$$
y_{\mathrm{line}} = \frac{1}{2} = 0.5, \qquad y_{\mathrm{parabola}} = \left(\frac{1}{2}\right)^2 = \frac{1}{4} = 0.25
$$

Since $0.5 > 0.25$, the straight line $y = x$ lies strictly above the parabola $y = x^2$ throughout the interior of the interval:

$$
y_{\mathrm{top}} = x, \qquad y_{\mathrm{bottom}} = x^2
$$

---

**Step 3: Set up and evaluate the area integral**

Integrate the difference $(y_{\mathrm{top}} - y_{\mathrm{bottom}})$ from $x = 0$ to $x = 1$:

$$
A = \int_0^1 (x - x^2) \, dx
$$

Find the antiderivative:

$$
A = \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1
$$

Substitute the limits:

$$
A = \left(\frac{1^2}{2} - \frac{1^3}{3}\right) - \left(\frac{0^2}{2} - \frac{0^3}{3}\right) = \frac{1}{2} - \frac{1}{3}
$$

Find a common denominator:

$$
A = \frac{3 - 2}{6} = \frac{1}{6}
$$

---

### Final Answer

1. **Intersection Points:**

   $$
   (0, 0), \qquad (1, 1)
   $$

2. **Function Ordering on $(0, 1)$:**
   The linear function $y = x$ is strictly greater than the parabola $y = x^2$ because $x - x^2 = x(1 - x) > 0$ for all $x \in (0, 1)$.

3. **Area of the Region:**

   $$
   A = \int_0^1 (x - x^2) \, dx = \frac{1}{6}
   $$