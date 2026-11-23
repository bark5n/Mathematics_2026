### Essential Formulas

**First Derivative Test for Monotonicity and Local Extrema:**
* If $f'(x) > 0$ on an open interval $I$, then $f$ is strictly increasing on $I$.
* If $f'(x) < 0$ on an open interval $I$, then $f$ is strictly decreasing on $I$.
* At a critical point $c$ where $f'(c) = 0$: if $f'$ changes sign from $+$ to $-$, $f(c)$ is a local maximum; if $f'$ changes sign from $-$ to $+$, $f(c)$ is a local minimum.

---

### Problem Statement

**Problem 1. A Cubic Polynomial**

Analyze the monotonicity and extrema of

$$f(x) = x^3 - 3x^2 + 2.$$

Sketch the graph based on the results and mark the critical points.

> **Why this problem:** it teaches how to use the first derivative to describe the shape of a polynomial.

---

### Solution

**Step 1: Compute the first derivative and find the critical points**

Differentiate $f(x) = x^3 - 3x^2 + 2$:

$$f'(x) = 3x^2 - 6x = 3x(x - 2)$$

Set $f'(x) = 0$ to find the critical points:

$$3x(x - 2) = 0 \implies x_1 = 0, \qquad x_2 = 2$$

**Step 2: Determine the sign of $f'(x)$ and intervals of monotonicity**

Analyze the sign of $f'(x) = 3x(x - 2)$ on the intervals separated by $0$ and $2$:

| Interval | Sign of $3x$ | Sign of $(x - 2)$ | Sign of $f'(x)$ | Monotonicity of $f$ |
| :--- | :--- | :--- | :--- | :--- |
| $(-\infty, 0)$ | $-$ | $-$ | $+$ | Strictly increasing |
| $(0, 2)$ | $+$ | $-$ | $-$ | Strictly decreasing |
| $(2, +\infty)$ | $+$ | $+$ | $+$ | Strictly increasing |

**Step 3: Classify the local extrema and compute their values**

* **At $x = 0$:** $f'(x)$ changes sign from $+$ to $-$, so $f$ has a **local maximum** at:
  $$f(0) = 0^3 - 3(0)^2 + 2 = 2 \implies (0, 2)$$

* **At $x = 2$:** $f'(x)$ changes sign from $-$ to $+$, so $f$ has a **local minimum** at:
  $$f(2) = 2^3 - 3(2)^2 + 2 = 8 - 12 + 2 = -2 \implies (2, -2)$$

*(Additional helpful points: $f(1) = 1 - 3 + 2 = 0$, $f(-1) = -1 - 3 + 2 = -2$, $f(3) = 27 - 27 + 2 = 2$.)*

**Step 4: Labelled Sketch of the Graph**

```text
                      y ^
                        |
          Local Max     |                 . (3, 2)
            (0, 2) *    |               . '
                 .' '.  |             . '
               .'     '.|  (1, 0)   . '
  ------------*---------+---*-----*----------------> x
          (-0.73, 0)    |    '. .'   (2.73, 0)
                        |      * Local Min
                        |     (2, -2)
```

---

### Final Answer

1. **Monotonicity:** Strictly increasing on $(-\infty, 0)$ and $(2, +\infty)$; strictly decreasing on $(0, 2)$.
2. **Local extrema:** Local maximum at $(0, 2)$ and local minimum at $(2, -2)$.
