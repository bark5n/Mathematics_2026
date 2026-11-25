### Essential Formulas

**Fundamental Theorem of Calculus (Evaluation Rule):**
If $F'(x) = f(x)$ on $[a, b]$, then:

$$\int_a^b f(x) \, dx = F(b) - F(a)$$

**Geometric Area Between a Curve and the $x$-Axis:**

$$A = \int_a^b \vert{}f(x)\vert{} \, dx$$

---

### Problem Statement

**Problem 9. Definite Integral and Geometric Area**

Compute

$$\int_{-1}^{2} x \, dx.$$

Then separately compute the areas of the parts of the graph below and above the $x$-axis and explain the difference between the definite integral and geometric area.

> **Why this problem:** it clarifies the difference between signed accumulation and area.

---

### Solution

**Step 1: Compute the definite integral $\int_{-1}^{2} x \, dx$**

An antiderivative of $f(x) = x$ is $F(x) = \frac{x^2}{2}$. Evaluating from $-1$ to $2$:

$$\begin{aligned} \int_{-1}^{2} x \, dx &= \left[ \frac{x^2}{2} \right]_{-1}^{2} \\ &= \frac{2^2}{2} - \frac{(-1)^2}{2} \\ &= \frac{4}{2} - \frac{1}{2} \\ &= \frac{3}{2} = 1.5 \end{aligned}$$

**Step 2: Sketch the region and compute the geometric areas below and above the $x$-axis**

The line $y = x$ crosses the $x$-axis at $x = 0$, splitting $[-1, 2]$ into two triangles:

```text
                      y ^          * (2, 2)
                        |        . |
                        |      . ' |
                        |    . ' + |  Area A_2 = 2
                        |  . '     |
  --------------*-------+----------+--------> x
             (-1, 0)  .'| (0, 0)   2
              - |  . '  |
        Area    * '     |
       A_1=1/2 (-1,-1)  |
```

1. **Area below the $x$-axis on $[-1, 0]$ ($A_1$):**
   Here $x \le 0$, so the height is $\vert{}x\vert{} = -x$:
   $$A_1 = \int_{-1}^{0} \vert{}x\vert{} \, dx = \int_{-1}^{0} (-x) \, dx = \left[ -\frac{x^2}{2} \right]_{-1}^{0} = 0 - \left(-\frac{1}{2}\right) = \frac{1}{2}$$
   *(Geometrically, a right triangle with base $1$ and height $1$: $\frac{1}{2}(1)(1) = \frac{1}{2}$.)*

2. **Area above the $x$-axis on $[0, 2]$ ($A_2$):**
   Here $x \ge 0$, so $\vert{}x\vert{} = x$:
   $$A_2 = \int_{0}^{2} \vert{}x\vert{} \, dx = \int_{0}^{2} x \, dx = \left[ \frac{x^2}{2} \right]_{0}^{2} = \frac{4}{2} - 0 = 2$$
   *(Geometrically, a right triangle with base $2$ and height $2$: $\frac{1}{2}(2)(2) = 2$.)*

3. **Total geometric area ($A_{\mathrm{total}}$):**
   $$A_{\mathrm{total}} = A_1 + A_2 = \frac{1}{2} + 2 = \frac{5}{2} = 2.5$$

**Step 3: Explain the difference between the definite integral and geometric area**

* **Definite integral (net signed accumulation):** $\int_a^b f(x) \, dx$ weights regions above the $x$-axis positively ($+A_2$) and regions below the $x$-axis negatively ($-A_1$). Thus:
  $$\int_{-1}^{2} x \, dx = A_2 - A_1 = 2 - \frac{1}{2} = \frac{3}{2}$$
  Partial cancellation occurs between negative and positive contributions.
* **Geometric area (unsigned magnitude):** Area is always non-negative ($\int_a^b \vert{}f(x)\vert{} \, dx$), so both triangles add together without cancellation: $A_1 + A_2 = \frac{1}{2} + 2 = \frac{5}{2}$.

---

### Final Answer

1. **Definite integral:** $\int_{-1}^{2} x \, dx = \frac{3}{2}$.
2. **Individual and total areas:** Area below the $x$-axis is $A_1 = \frac{1}{2}$; area above the $x$-axis is $A_2 = 2$; total geometric area is $A_{\mathrm{total}} = \frac{5}{2}$.
3. **Difference:** The definite integral computes **net signed area** ($A_2 - A_1 = \frac{3}{2}$), whereas geometric area sums the absolute magnitudes ($A_1 + A_2 = \frac{5}{2}$).
