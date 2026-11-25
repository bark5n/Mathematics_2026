### Essential Formulas

**Fundamental Theorem of Calculus (Part 1 — Derivative of an Integral Function):**
If $f$ is continuous on an interval $I$ and $a \in I$, then the accumulation function

$$
F(x) = \int_a^x f(t) \, dt
$$

is differentiable on $I$ and satisfies:

$$
F'(x) = f(x)
$$

---

### Problem Statement

**Problem 13. An Integral Depending on the Upper Limit**

Let

$$
F(x) = \int_0^x (t^2 + 1) \, dt.
$$

Determine $F(x)$, compute $F'(x)$, and compare the result with the integrand. Explain in your own words why the height of the function describes the local rate of increase of the accumulated area.

> **Why this problem:** it connects differentiation and integration through the idea of accumulation.

---

### Solution

**Step 1: Determine $F(x)$ explicitly by evaluating the definite integral**

An antiderivative of $f(t) = t^2 + 1$ is $\frac{t^3}{3} + t$. Evaluating from $0$ to $x$:

$$
\begin{aligned}
F(x) &= \int_0^x (t^2 + 1) \, dt \\
     &= \left[ \frac{t^3}{3} + t \right]_0^x \\
     &= \left(\frac{x^3}{3} + x\right) - \left(\frac{0^3}{3} + 0\right) \\
     &= \frac{x^3}{3} + x
\end{aligned}
$$

**Step 2: Compute $F'(x)$ and compare with the integrand**

Differentiate $F(x) = \frac{x^3}{3} + x$ with respect to $x$:

$$
F'(x) = \frac{1}{3}(3x^2) + 1 = x^2 + 1
$$

**Comparison:** $F'(x) = x^2 + 1$ is **identical** to the integrand $f(t) = t^2 + 1$ evaluated at the upper limit $t = x$.

**Step 3: Explain why the height of the function describes the local rate of increase of accumulated area**

For $x > 0$, $F(x)$ represents the area under the curve $y = t^2 + 1$ from $t = 0$ to $t = x$. When the right boundary advances from $x$ to $x + \Delta x$ (with a tiny width $\Delta x > 0$), a thin vertical strip of area $\Delta F = F(x + \Delta x) - F(x)$ is added on the right. Because $f(t) = t^2 + 1$ is continuous, this thin strip is nearly a rectangle of base $\Delta x$ and height $f(x) = x^2 + 1$, so:

$$
\Delta F \approx f(x) \, \Delta x \implies \frac{\Delta F}{\Delta x} \approx f(x)
$$

Passing to the limit $\Delta x \to 0$, the instantaneous rate at which accumulated area grows per unit increase in $x$ equals the current height $f(x)$ of the curve at the moving right edge: the taller the curve at $x$, the faster new area accumulates.

---

### Final Answer

1. **Explicit function:** $F(x) = \frac{x^3}{3} + x$.
2. **Derivative:** $F'(x) = x^2 + 1$, matching the integrand $t^2 + 1$ at $t = x$.
3. **Geometric explanation:** Advancing the upper limit by a small $\Delta x$ adds a narrow strip of width $\Delta x$ and height $f(x)$, so $\frac{\Delta F}{\Delta x} \approx f(x)$; thus the curve's height $f(x)$ is the instantaneous rate of area accumulation.
