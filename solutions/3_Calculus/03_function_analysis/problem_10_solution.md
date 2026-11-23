### Essential Formulas

**First and Second Derivatives of $f(x) = \frac{x}{x^2 + 1}$:**

$$f'(x) = \frac{1 - x^2}{(x^2 + 1)^2}, \qquad f''(x) = \frac{2x(x^2 - 3)}{(x^2 + 1)^3}$$

---

### Problem Statement

**Problem 10. Complete Function Analysis**

Perform a complete analysis of

$$f(x) = \frac{x}{x^2 + 1}.$$

Include the domain, symmetry, zeros, limits, monotonicity, extrema, and convexity. Finally, produce a sketch based only on this information.

> **Why this problem:** it combines all the basic elements of function analysis into one organized process.

---

### Solution

**1. Domain**

Since $x^2 + 1 \ge 1 > 0$ for all real numbers, the denominator never vanishes:

$$D_f = \mathbb{R} = (-\infty, +\infty)$$

**2. Symmetry**

Evaluate $f(-x)$:

$$f(-x) = \frac{-x}{(-x)^2 + 1} = -\frac{x}{x^2 + 1} = -f(x)$$

Thus $f$ is an **odd function**, so its graph is symmetric with respect to the origin $(0, 0)$.

**3. Zeros and Sign**

Set $f(x) = 0$:

$$\frac{x}{x^2 + 1} = 0 \implies x = 0$$

The unique zero is $x = 0$ (passing through $(0, 0)$). Because $x^2 + 1 > 0$, $f(x) < 0$ for $x < 0$ and $f(x) > 0$ for $x > 0$.

**4. Limits and Asymptotes**

* **Vertical asymptotes:** None, since $f$ is continuous on all of $\mathbb{R}$.
* **Horizontal asymptote as $x \to \pm \infty$:** Divide numerator and denominator by $x^2$:
  $$\lim_{x \to \pm \infty} \frac{x}{x^2 + 1} = \lim_{x \to \pm \infty} \frac{\frac{1}{x}}{1 + \frac{1}{x^2}} = \frac{0}{1 + 0} = 0$$
  Hence $y = 0$ (the $x$-axis) is a **horizontal asymptote** on both sides (approached from above as $x \to +\infty$ and from below as $x \to -\infty$).

**5. Monotonicity and Extrema**

Differentiate using the quotient rule:

$$f'(x) = \frac{1 \cdot (x^2 + 1) - x \cdot (2x)}{(x^2 + 1)^2} = \frac{1 - x^2}{(x^2 + 1)^2} = \frac{(1 - x)(1 + x)}{(x^2 + 1)^2}$$

Setting $f'(x) = 0$ gives critical points $x = -1$ and $x = 1$. Since $(x^2 + 1)^2 > 0$:
* **On $(-\infty, -1)$:** $1 - x^2 < 0 \implies f'(x) < 0$ (**strictly decreasing**).
* **On $(-1, 1)$:** $1 - x^2 > 0 \implies f'(x) > 0$ (**strictly increasing**).
* **On $(1, +\infty)$:** $1 - x^2 < 0 \implies f'(x) < 0$ (**strictly decreasing**).

Evaluate $f$ at the critical points:
* At $x = -1$: $f(-1) = \frac{-1}{2} = -\frac{1}{2}$ (**local and global minimum** at $\left(-1, -\frac{1}{2}\right)$).
* At $x = 1$: $f(1) = \frac{1}{2}$ (**local and global maximum** at $\left(1, \frac{1}{2}\right)$).

**6. Convexity, Concavity, and Inflection Points**

Differentiate $f'(x) = (1 - x^2)(x^2 + 1)^{-2}$:

$$\begin{aligned} f''(x) &= \frac{(-2x)(x^2 + 1)^2 - (1 - x^2) \cdot 2(x^2 + 1)(2x)}{(x^2 + 1)^4} \\ &= \frac{-2x(x^2 + 1) - 4x(1 - x^2)}{(x^2 + 1)^3} \\ &= \frac{-2x^3 - 2x - 4x + 4x^3}{(x^2 + 1)^3} \\ &= \frac{2x^3 - 6x}{(x^2 + 1)^3} \\ &= \frac{2x(x - \sqrt{3})(x + \sqrt{3})}{(x^2 + 1)^3} \end{aligned}$$

Setting $f''(x) = 0$ gives candidates $x = -\sqrt{3}$, $x = 0$, and $x = \sqrt{3}$. Since $(x^2 + 1)^3 > 0$:
* **On $(-\infty, -\sqrt{3})$:** $f''(x) < 0$ (**concave / concave down**).
* **On $(-\sqrt{3}, 0)$:** $f''(x) > 0$ (**convex / concave up**).
* **On $(0, \sqrt{3})$:** $f''(x) < 0$ (**concave / concave down**).
* **On $(\sqrt{3}, +\infty)$:** $f''(x) > 0$ (**convex / concave up**).

Because $f''(x)$ changes sign across all three points, there are three **inflection points**:

$$\left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right), \qquad (0, 0), \qquad \left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)$$

**7. Labelled Sketch Based on the Analysis**

```text
                        y ^
                          |      * Global Max (1, 1/2)
                          |    . ' .
                          |  . '     * Inflection (sqrt(3), sqrt(3)/4)
      y = 0 (Asymptote)   |. '         ' . _ _ _ _ _ _ -> y -> 0+
  ------------------------*-----------------------------> x
    _ _ _ _ _ . '        .| (0, 0) Inflection
  y -> 0-    * Inflection |
           .' (-sqrt(3),  |
          *    -sqrt(3)/4)|
     Global Min (-1, -1/2)|
```

---

### Final Answer

1. **Domain and symmetry:** $D_f = \mathbb{R}$; odd function ($f(-x) = -f(x)$).
2. **Zeros and asymptotes:** Unique zero at $(0, 0)$; no vertical asymptotes; horizontal asymptote $y = 0$ as $x \to \pm \infty$.
3. **Monotonicity and extrema:** Decreasing on $(-\infty, -1)$ and $(1, +\infty)$, increasing on $(-1, 1)$; global minimum $\left(-1, -\frac{1}{2}\right)$ and global maximum $\left(1, \frac{1}{2}\right)$.
4. **Convexity and inflection points:** Concave on $(-\infty, -\sqrt{3}) \cup (0, \sqrt{3})$, convex on $(-\sqrt{3}, 0) \cup (\sqrt{3}, +\infty)$; inflection points at $\left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right)$, $(0, 0)$, and $\left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)$.
