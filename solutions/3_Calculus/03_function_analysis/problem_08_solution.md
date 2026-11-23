### Essential Formulas

**Second Derivative Test for Curvature and Inflection Points:**
* If $f''(x) > 0$ on an open interval $I$, then $f$ is **convex (concave up)** on $I$.
* If $f''(x) < 0$ on an open interval $I$, then $f$ is **concave (concave down)** on $I$.
* A point $\big(c, f(c)\big)$ is an **inflection point** if $f$ is continuous at $c$ and $f''(x)$ changes sign across $x = c$.

---

### Problem Statement

**Problem 8. The Second Derivative**

For

$$f(x) = x^4 - 4x^2$$

find the local extrema, intervals of convexity and concavity, and inflection points. Sketch the graph and mark all the identified features on it.

> **Why this problem:** it introduces the second derivative as a tool for describing the curvature of a graph.

---

### Solution

**Step 1: Compute $f'(x)$ and find the local extrema**

Differentiate $f(x) = x^4 - 4x^2$:

$$f'(x) = 4x^3 - 8x = 4x(x^2 - 2) = 4x(x - \sqrt{2})(x + \sqrt{2})$$

Setting $f'(x) = 0$ gives three critical points:

$$x_1 = -\sqrt{2}, \qquad x_2 = 0, \qquad x_3 = \sqrt{2}$$

Analyze the sign of $f'(x)$:
* On $(-\infty, -\sqrt{2})$: $f'(x) < 0$ (decreasing).
* On $(-\sqrt{2}, 0)$: $f'(x) > 0$ (increasing).
* On $(0, \sqrt{2})$: $f'(x) < 0$ (decreasing).
* On $(\sqrt{2}, +\infty)$: $f'(x) > 0$ (increasing).

Evaluate $f$ at the critical points:
* $f(-\sqrt{2}) = (-\sqrt{2})^4 - 4(-\sqrt{2})^2 = 4 - 8 = -4 \implies \big(-\sqrt{2}, -4\big)$ is a **local (and global) minimum**.
* $f(0) = 0^4 - 4(0)^2 = 0 \implies (0, 0)$ is a **local maximum**.
* $f(\sqrt{2}) = (\sqrt{2})^4 - 4(\sqrt{2})^2 = 4 - 8 = -4 \implies \big(\sqrt{2}, -4\big)$ is a **local (and global) minimum**.

*(Note also the zeros $x^2(x^2 - 4) = 0 \implies x = -2, 0, 2$.)*

**Step 2: Compute $f''(x)$ and find intervals of convexity, concavity, and inflection points**

Differentiate $f'(x) = 4x^3 - 8x$:

$$f''(x) = 12x^2 - 8 = 4(3x^2 - 2)$$

Set $f''(x) = 0$:

$$3x^2 - 2 = 0 \implies x^2 = \frac{2}{3} \implies x = \pm \sqrt{\frac{2}{3}} = \pm \frac{\sqrt{6}}{3} \approx \pm 0.816$$

Check the sign of $f''(x) = 12\left(x^2 - \frac{2}{3}\right)$:
* **On $\left(-\infty, -\sqrt{\frac{2}{3}}\right)$:** $x^2 > \frac{2}{3} \implies f''(x) > 0$, so $f$ is **convex (concave up)**.
* **On $\left(-\sqrt{\frac{2}{3}}, \sqrt{\frac{2}{3}}\right)$:** $x^2 < \frac{2}{3} \implies f''(x) < 0$, so $f$ is **concave (concave down)**.
* **On $\left(\sqrt{\frac{2}{3}}, +\infty\right)$:** $x^2 > \frac{2}{3} \implies f''(x) > 0$, so $f$ is **convex (concave up)**.

Because $f''(x)$ changes sign at both $x = -\sqrt{\frac{2}{3}}$ and $x = \sqrt{\frac{2}{3}}$, both are **inflection points** with $y$-coordinate:

$$f\left(\pm \sqrt{\frac{2}{3}}\right) = \left(\frac{2}{3}\right)^2 - 4\left(\frac{2}{3}\right) = \frac{4}{9} - \frac{8}{3} = -\frac{20}{9} \approx -2.22$$

Thus the inflection points are $\left(-\sqrt{\frac{2}{3}}, -\frac{20}{9}\right)$ and $\left(\sqrt{\frac{2}{3}}, -\frac{20}{9}\right)$.

**Step 3: Labelled Sketch of the Graph**

```text
                      y ^
                        |
          (-2, 0)       | Local Max      (2, 0)
  -----------*----------+----*-------------+-----------> x
              \         |  (0, 0)         /
               \        |                /
                *-------+---------------*  Inflection Points:
     Inflection  \      |              /   (-sqrt(2/3), -20/9) and
                  '.    |            .'    ( sqrt(2/3), -20/9)
                    ' . |        . '
                       '*-------*'
          Local Min (-sqrt(2),-4) and (sqrt(2),-4)
```

---

### Final Answer

1. **Local extrema:** Local (and global) minima at $\big(-\sqrt{2}, -4\big)$ and $\big(\sqrt{2}, -4\big)$; local maximum at $(0, 0)$.
2. **Convexity and concavity:** Convex (concave up) on $\left(-\infty, -\sqrt{\frac{2}{3}}\right)$ and $\left(\sqrt{\frac{2}{3}}, +\infty\right)$; concave (concave down) on $\left(-\sqrt{\frac{2}{3}}, \sqrt{\frac{2}{3}}\right)$.
3. **Inflection points:** $\left(-\sqrt{\frac{2}{3}}, -\frac{20}{9}\right)$ and $\left(\sqrt{\frac{2}{3}}, -\frac{20}{9}\right)$.
