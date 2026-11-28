### Essential Formulas

**Area Between Two Curves:**
If $f(x) \ge g(x)$ on $[a, b]$, the area of the region bounded between $y = f(x)$ and $y = g(x)$ from $x = a$ to $x = b$ is:

$$A = \int_a^b \big(f(x) - g(x)\big) \, dx$$

---

### Problem Statement

**Problem 4. Area Between Curves**

Find the area of the region bounded by the graphs

$$y = x$$

and

$$y = x^2.$$

First find the intersection points and justify which function is greater on the relevant interval.

> **Why this problem:** it teaches that before integrating, one must first determine the geometry of the region and the correct order of the functions.

---

### Solution

**Step 1: Find the intersection points**

Set the two expressions equal to each other:

$$x^2 = x \implies x^2 - x = 0 \implies x(x - 1) = 0$$

This yields two intersection points:
* At $x = 0$: $y = 0 \implies (0, 0)$
* At $x = 1$: $y = 1 \implies (1, 1)$

Thus the bounded region lies over the interval $[0, 1]$.

**Step 2: Justify which function is greater on $[0, 1]$**

For every $x \in (0, 1)$, we have $0 < x < 1$. Multiplying the inequality $x < 1$ by the positive number $x > 0$ gives:

$$x^2 < x \qquad \mathrm{for\ all}\ x \in (0, 1)$$

Equivalently, $x - x^2 = x(1 - x) > 0$ on $(0, 1)$ because both factors $x$ and $1 - x$ are strictly positive. Therefore, the line $y = x$ forms the **upper boundary** and the parabola $y = x^2$ forms the **lower boundary** throughout $[0, 1]$.

```text
                      y ^
                        |        * (1, 1)
                        |      .'|
                        |    .' /  Upper: y = x
                        |  .'  /
                        |.' _ '    Lower: y = x^2
  ----------------------*--------+--------> x
                     (0, 0)      1
```

**Step 3: Compute the area by integration**

Integrate the vertical height $(x - x^2)$ from $x = 0$ to $x = 1$:

$$
\begin{aligned}
A &= \int_0^1 (x - x^2) \, dx \\
  &= \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1 \\
  &= \left(\frac{1^2}{2} - \frac{1^3}{3}\right) - (0 - 0) \\
  &= \frac{1}{2} - \frac{1}{3} \\
  &= \frac{1}{6}
\end{aligned}
$$

---

### Final Answer

1. **Intersection points:** $(0, 0)$ and $(1, 1)$, giving interval $[0, 1]$.
2. **Order of functions:** $x \ge x^2$ on $[0, 1]$ because $x - x^2 = x(1 - x) \ge 0$.
3. **Bounded area:** $A = \frac{1}{6}$.
