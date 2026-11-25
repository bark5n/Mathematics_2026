### Essential Formulas

**Additivity of the Definite Integral Over Adjacent Intervals:**
If $a < c < b$, then:

$$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$$

---

### Problem Statement

**Problem 14. A Piecewise-Defined Function**

Let

$$f(x) = \begin{cases} x + 1, & -1 \le x < 1, \\ 2, & 1 \le x \le 3. \end{cases}$$

Sketch the graph, decide where to split the integral, compute

$$\int_{-1}^{3} f(x) \, dx$$

and verify the result geometrically.

> **Why this problem:** it requires understanding the definition of the function before carrying out the calculation.

---

### Solution

**Step 1: Sketch the graph of $f(x)$ on $[-1, 3]$**

* On $[-1, 1)$: $f(x) = x + 1$ is a line segment connecting $(-1, 0)$ to the open circle $(1, 2)$.
* On $[1, 3]$: $f(x) = 2$ is a horizontal line segment connecting the closed dot $(1, 2)$ to $(3, 2)$ (notice both branches meet continuously at $(1, 2)$).

```text
                      y ^
                        |
                   2.00 +         *-------------------* (3, 2)
                        |       . | (1, 2)            |
                        |     . ' |                   |
                   1.00 +   * (0,1)    Rectangle      |
                        | . '     |    Area = 4       |
                        |'Triangle|                   |
  ----------------------*---------+-------------------+-----> x
                     (-1, 0)      1                   3
```

**Step 2: Decide where to split the integral**

Because the formula defining $f(x)$ changes at $x = 1$, split the interval $[-1, 3]$ at **$x = 1$** into $[-1, 1]$ and $[1, 3]$:

$$\int_{-1}^{3} f(x) \, dx = \int_{-1}^{1} (x + 1) \, dx + \int_{1}^{3} 2 \, dx$$

*(Note: Because the single point $x = 1$ has zero width, changing the endpoint value at $x = 1$ does not affect the definite integral over $[-1, 1]$.)*

**Step 3: Compute $\int_{-1}^{3} f(x) \, dx$**

Evaluate each piece separately:

1. **First integral on $[-1, 1]$:**
   $$\begin{aligned} \int_{-1}^{1} (x + 1) \, dx &= \left[ \frac{x^2}{2} + x \right]_{-1}^{1} \\ &= \left(\frac{1}{2} + 1\right) - \left(\frac{1}{2} - 1\right) \\ &= \frac{3}{2} - \left(-\frac{1}{2}\right) \\ &= 2 \end{aligned}$$

2. **Second integral on $[1, 3]$:**
   $$\int_{1}^{3} 2 \, dx = \big[ 2x \big]_1^3 = 2(3) - 2(1) = 6 - 2 = 4$$

Add both contributions:

$$\int_{-1}^{3} f(x) \, dx = 2 + 4 = 6$$

**Step 4: Verify the result geometrically**

Since $f(x) \ge 0$ on $[-1, 3]$, the integral equals the total area under the graph, which decomposes into two elementary shapes:
* **Left region ($-1 \le x \le 1$):** A right triangle with base $b_1 = 1 - (-1) = 2$ and height $h_1 = 2$:
  $$A_{\mathrm{triangle}} = \frac{1}{2} \cdot 2 \cdot 2 = 2$$
* **Right region ($1 \le x \le 3$):** A rectangle with width $b_2 = 3 - 1 = 2$ and height $h_2 = 2$:
  $$A_{\mathrm{rectangle}} = 2 \cdot 2 = 4$$
* **Total geometric area:** $A_{\mathrm{total}} = 2 + 4 = 6$, matching the integral value $6$ identically.

---

### Final Answer

1. **Split point:** Split at $x = 1$, where the piecewise definition changes.
2. **Definite integral:** $\int_{-1}^{3} f(x) \, dx = 2 + 4 = 6$.
3. **Geometric verification:** Sum of a right triangle of area $\frac{1}{2}(2)(2) = 2$ and a rectangle of area $2 \times 2 = 4$, giving $6$.
