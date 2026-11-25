### Essential Formulas

**Symmetry Properties on Symmetric Intervals $[-a, a]$:**
* If $f(-x) = -f(x)$ (**odd function**), then:
  $$\int_{-a}^{a} f(x) \, dx = 0$$
* If $f(-x) = f(x)$ (**even function**), then:
  $$\int_{-a}^{a} f(x) \, dx = 2 \int_0^a f(x) \, dx$$

---

### Problem Statement

**Problem 12. Symmetry, Sign, and Absolute Value**

Compare

$$\int_{-2}^{2} x \, dx$$

and

$$\int_{-2}^{2} \vert{}x\vert{} \, dx.$$

Before calculating, predict the results from symmetry and a sketch, then carry out the calculation and explain the difference.

> **Why this problem:** it teaches how to use symmetry and geometry before applying a computational procedure.

---

### Solution

**Step 1: Sketch both functions and predict the integrals from symmetry**

```text
  (a) Odd Function: f(x) = x              (b) Even Function: g(x) = |x|

            y ^         * (2, 2)                    y ^
              |       . |                 (-2, 2) *   |   * (2, 2)
              |     . ' |  + Area = 2              '. | .'
              |   . '   |                    Area=2  '|'  Area=2
  ------*-----+---------+------> x        ------------+----------> x
     (-2, 0) .| (0, 0)  2                -2         (0, 0)         2
    - |   . ' |
Area=2* '     |
   (-2, -2)   |
```

* **Prediction for $\int_{-2}^{2} x \, dx$:** The function $f(x) = x$ is **odd** ($f(-x) = -x = -f(x)$). On $[-2, 2]$, the negative triangle on $[-2, 0]$ (area $2$ below the $x$-axis) and the positive triangle on $[0, 2]$ (area $2$ above the $x$-axis) are congruent with opposite signs, so they cancel completely: predicted value is **$0$**.
* **Prediction for $\int_{-2}^{2} |x| \, dx$:** The function $g(x) = |x|$ is **even** ($g(-x) = |-x| = |x| = g(x)$). Reflecting the negative triangle above the $x$-axis gives two identical positive triangles of base $2$ and height $2$ (each of area $\frac{1}{2}(2)(2) = 2$), so they add together: predicted value is **$2 + 2 = 4$**.

**Step 2: Carry out the exact calculations**

1. **First integral ($\int_{-2}^{2} x \, dx$):**
   $$
   \int_{-2}^{2} x \, dx = \left[ \frac{x^2}{2} \right]_{-2}^{2} = \frac{2^2}{2} - \frac{(-2)^2}{2} = 2 - 2 = 0
   $$

2. **Second integral ($\int_{-2}^{2} |x| \, dx$):**
   Split at $x = 0$ where $|x|$ changes formula ($|x| = -x$ for $x < 0$ and $|x| = x$ for $x \ge 0$):
   $$
   \begin{aligned}
   \int_{-2}^{2} |x| \, dx
   &= \int_{-2}^{0} (-x) \, dx + \int_0^2 x \, dx \\
   &= \left[ -\frac{x^2}{2} \right]_{-2}^{0} + \left[ \frac{x^2}{2} \right]_0^2 \\
   &= \left(0 - (-2)\right) + (2 - 0) \\
   &= 2 + 2 = 4
   \end{aligned}
   $$

**Step 3: Explain the difference**

Both calculations confirm the geometric predictions ($0$ vs. $4$). The definite integral $\int_{-2}^{2} x \, dx$ measures **net signed accumulation**, where the negative values on $[-2, 0]$ cancel the positive values on $[0, 2]$. Applying the absolute value $|x|$ converts all negative outputs on $[-2, 0]$ into positive heights, turning the integral into **total unsigned geometric area** so both halves reinforce each other rather than cancel.

---

### Final Answer

1. **Predictions:** $\int_{-2}^{2} x \, dx = 0$ (odd symmetry cancellation) and $\int_{-2}^{2} |x| \, dx = 4$ (even symmetry addition of two triangles of area $2$).
2. **Calculated values:** $\int_{-2}^{2} x \, dx = 0$ and $\int_{-2}^{2} |x| \, dx = 4$.
3. **Explanation:** $\int_{-2}^{2} x \, dx$ computes signed net accumulation with cancellation, whereas $\int_{-2}^{2} |x| \, dx$ measures total positive geometric area.
