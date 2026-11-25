### Essential Formulas

**Comparison / Monotonicity Property of Definite Integrals:**
If $m \le f(x) \le M$ for all $x \in [a, b]$ with $a \le b$, then:

$$
m(b - a) \le \int_a^b f(x) \, dx \le M(b - a)
$$

---

### Problem Statement

**Problem 10. Definite Integral and Checking the Result**

Before carrying out the exact calculation, estimate the possible range of values of the integral

$$
\int_0^2 (x^2 + 1) \, dx,
$$

using

$$
1 \le x^2 + 1 \le 5
$$

on $[0, 2]$. Only then compute the integral exactly, compare the result with the earlier estimate, and explain what type of computational error such a check can detect.

> **Why this problem:** it teaches how to predict the possible range of a result and check the calculation.

---

### Solution

**Step 1: Estimate the range of the integral before computing**

On the interval $[a, b] = [0, 2]$, the interval length is $b - a = 2 - 0 = 2$. Given that $1 \le x^2 + 1 \le 5$ for all $x \in [0, 2]$ (with lower bound $m = 1$ at $x = 0$ and upper bound $M = 5$ at $x = 2$), multiply the inequality by the interval length $2$:

$$
1 \cdot (2 - 0) \le \int_0^2 (x^2 + 1) \, dx \le 5 \cdot (2 - 0)
$$

$$
2 \le \int_0^2 (x^2 + 1) \, dx \le 10
$$

Geometrically, the area under $y = x^2 + 1$ over $[0, 2]$ is trapped between a lower rectangle of width $2$, height $1$ (area $2$) and an upper rectangle of width $2$, height $5$ (area $10$). Moreover, because $x^2 + 1$ is strictly increasing and not constant on $[0, 2]$, the exact value must lie strictly inside $(2, 10)$.

**Step 2: Compute the definite integral exactly**

Find an antiderivative $F(x) = \frac{x^3}{3} + x$ and evaluate from $0$ to $2$:

$$
\begin{aligned}
\int_0^2 (x^2 + 1) \, dx
&= \left[ \frac{x^3}{3} + x \right]_0^2 \\
&= \left(\frac{2^3}{3} + 2\right) - \left(\frac{0^3}{3} + 0\right) \\
&= \frac{8}{3} + 2 \\
&= \frac{14}{3} \approx 4.67
\end{aligned}
$$

**Step 3: Compare with the estimate and explain what errors this check detects**

* **Comparison:** Since $2 < \frac{14}{3} \approx 4.67 < 10$, the exact result lies comfortably inside the predicted range $[2, 10]$.
* **Types of computational errors detected by bounding checks:**
  1. **Sign errors:** Forgetting a minus sign or reversing limits of integration ($F(a) - F(b) = -\frac{14}{3}$) produces a negative result outside $[2, 10]$.
  2. **Wrong antiderivative powers or missing constants:** Multiplying instead of dividing by the new exponent (e.g., writing $3x^3 + x$, giving $26 > 10$) or dropping the $+1$ term (giving $\frac{8}{3}$, which is close, or forgetting to evaluate $+x$ at $x = 2$ when the lower bound is higher) often pushes the answer outside the allowable box $[m(b - a), M(b - a)]$.
  3. **Arithmetic or limit-substitution mistakes:** Substituting wrong endpoints or miscalculating fractions by an order of magnitude is immediately flagged whenever the computed number falls below $2$ or above $10$.

---

### Final Answer

1. **Estimated range:** $2 \le \int_0^2 (x^2 + 1) \, dx \le 10$.
2. **Exact value:** $\frac{14}{3} \approx 4.67$, which satisfies $2 < \frac{14}{3} < 10$.
3. **Errors detected:** Catches sign errors, reversed integration limits, wrong power-rule coefficients, and major arithmetic/substitution mistakes that push the result outside $[2, 10]$.
