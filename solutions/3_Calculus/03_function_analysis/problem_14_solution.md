### Essential Formulas

**Recovering Monotonicity and Extrema from $f'(x)$:**
* $f$ increases where $f'(x) > 0$ and decreases where $f'(x) < 0$.
* Local extrema occur where $f'(x)$ changes sign.
* Two functions with the same derivative on $\mathbb{R}$ differ by an additive constant: $g(x) = f(x) + C$.

---

### Problem Statement

**Problem 14. Reconstructing Information from the Derivative**

It is known that

$$f'(x) = (x - 1)(x + 2).$$

Determine the monotonicity and the locations of the extrema, and sketch a possible qualitative shape of the function. Then, for

$$g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x$$

verify that $g'(x) = (x - 1)(x + 2)$, and compare the specific graph with the earlier qualitative sketch.

> **Why this problem:** it teaches how to read the behavior of a function directly from its derivative.

---

### Solution

**Step 1: Determine monotonicity and locations of extrema from $f'(x) = (x - 1)(x + 2)$**

Find the zeros of $f'(x)$:

$$(x - 1)(x + 2) = 0 \implies x_1 = -2, \qquad x_2 = 1$$

Construct the sign chart for $f'(x) = (x - 1)(x + 2)$:

| Interval | Sign of $(x + 2)$ | Sign of $(x - 1)$ | Sign of $f'(x)$ | Behavior of $f$ |
| :--- | :--- | :--- | :--- | :--- |
| $(-\infty, -2)$ | $-$ | $-$ | $+$ | Strictly increasing |
| $(-2, 1)$ | $+$ | $-$ | $-$ | Strictly decreasing |
| $(1, +\infty)$ | $+$ | $+$ | $+$ | Strictly increasing |

* **Locations of extrema:**
  * At $x = -2$, $f'(x)$ changes sign from $+$ to $-$, so $f$ has a **local maximum at $x = -2$**.
  * At $x = 1$, $f'(x)$ changes sign from $-$ to $+$, so $f$ has a **local minimum at $x = 1$**.
* *(Note: Also $f''(x) = 2x + 1$, so $f$ has an inflection point at $x = -\frac{1}{2}$.)*

**Step 2: Sketch a qualitative shape of $f(x)$**

Because $f'(x)$ determines the slope at every $x$ but not the initial height $f(0)$, the qualitative shape is determined **up to an arbitrary vertical shift $+C$**:

```text
  (a) Qualitative Shape of f(x) (determined up to vertical shift +C)

              Local Max at x = -2
                    *
                  .' '.
                .'     '.
              .'         '.
            .'             '.             .'
          .'                 '.         .'
  -------+---------------------+-------*-------------> x
       x = -2                x = 1    Local Min at x = 1
```

**Step 3: Verify that $g'(x) = (x - 1)(x + 2)$ for $g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x$**

Differentiate $g(x)$ term by term:

$$\begin{aligned} g'(x) &= \frac{1}{3}(3x^2) + \frac{1}{2}(2x) - 2(1) \\ &= x^2 + x - 2 \\ &= (x - 1)(x + 2) \end{aligned}$$

Thus $g'(x)$ matches $f'(x)$ identically for all $x \in \mathbb{R}$.

**Step 4: Compute exact values for $g(x)$ and compare with the qualitative sketch**

Evaluate $g(x)$ at the critical points and origin:
* **Local maximum at $x = -2$:**
  $$g(-2) = \frac{(-2)^3}{3} + \frac{(-2)^2}{2} - 2(-2) = -\frac{8}{3} + 2 + 4 = \frac{10}{3} \approx 3.33 \implies \left(-2, \frac{10}{3}\right)$$
* **Origin ($x = 0$):**
  $$g(0) = 0 \implies (0, 0)$$
* **Local minimum at $x = 1$:**
  $$g(1) = \frac{1^3}{3} + \frac{1^2}{2} - 2(1) = \frac{1}{3} + \frac{1}{2} - 2 = -\frac{7}{6} \approx -1.17 \implies \left(1, -\frac{7}{6}\right)$$

**Comparison:** The specific graph $y = g(x)$ has the **exact same S-shaped cubic profile**, turning points ($x = -2$ and $x = 1$), and monotonicity intervals as the qualitative sketch in Step 2. The only difference is that choosing $g(x)$ fixes the integration constant ($C = 0$), anchoring the curve to pass through $(0, 0)$ with specific vertical heights $g(-2) = \frac{10}{3}$ and $g(1) = -\frac{7}{6}$.

---

### Final Answer

1. **Monotonicity and extrema from $f'(x)$:** Strictly increasing on $(-\infty, -2)$ and $(1, +\infty)$; strictly decreasing on $(-2, 1)$; local maximum at $x = -2$ and local minimum at $x = 1$.
2. **Verification for $g(x)$:** $g'(x) = x^2 + x - 2 = (x - 1)(x + 2)$.
3. **Comparison:** $g(x)$ reproduces the exact qualitative shape and turning-point locations of $f(x)$, with its vertical position fixed by $g(0) = 0$, local maximum $\left(-2, \frac{10}{3}\right)$, and local minimum $\left(1, -\frac{7}{6}\right)$.
