### Essential Formulas

**Quotient Rule with Natural Logarithm:**

$$
\left(\frac{\ln x}{x}\right)' = \frac{\frac{1}{x} \cdot x - (\ln x) \cdot 1}{x^2} = \frac{1 - \ln x}{x^2} \qquad (x > 0)
$$

**Logarithmic Growth Dominance:**

$$
\lim_{x \to +\infty} \frac{\ln x}{x} = 0
$$

---

### Problem Statement

**Problem 13. A Logarithm and an Asymptote**

Perform a complete analysis of

$$
f(x) = \frac{\ln x}{x}, \qquad x > 0.
$$

Find the maximum and the behavior at the ends of the domain. Explain which information is necessary for a correct sketch.

> **Why this problem:** it combines the domain, limits, and derivative in a less obvious example.

---

### Solution

**1. Domain, Zeros, and Sign**

* **Domain:** $D_f = (0, +\infty)$ (given, since $\ln x$ requires $x > 0$ and the denominator $x \neq 0$).
* **Zero:** $\frac{\ln x}{x} = 0 \iff \ln x = 0 \iff x = 1$. The unique $x$-intercept is $(1, 0)$.
* **Sign:** Since $x > 0$ on $D_f$, $f(x) < 0$ on $(0, 1)$ and $f(x) > 0$ on $(1, +\infty)$.

**2. Behavior at the Ends of the Domain (Limits and Asymptotes)**

* **Left endpoint ($x \to 0^+$):** As $x \to 0^+$, $\ln x \to -\infty$ and $\frac{1}{x} \to +\infty$, so their product diverges without bound:
  $$
  \lim_{x \to 0^+} \frac{\ln x}{x} = -\infty
  $$
  Thus $x = 0$ (the negative $y$-axis) is a **vertical asymptote**.

* **Right endpoint ($x \to +\infty$):** Substituting $x = e^t$ (as $t \to +\infty$) gives $\frac{\ln(e^t)}{e^t} = \frac{t}{e^t} \to 0$ (by Problem 5):
  $$
  \lim_{x \to +\infty} \frac{\ln x}{x} = 0
  $$
  Because $f(x) > 0$ for $x > 1$, $y = 0$ (the positive $x$-axis) is a **horizontal asymptote** approached from above.

**3. Monotonicity and Maximum**

Differentiate $f(x) = \frac{\ln x}{x}$ using the quotient rule:

$$
f'(x) = \frac{\frac{1}{x} \cdot x - (\ln x) \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}
$$

Set $f'(x) = 0$:

$$
1 - \ln x = 0 \implies \ln x = 1 \implies x = e \approx 2.718
$$

Since $x^2 > 0$ for all $x > 0$:
* **On $(0, e)$:** $\ln x < 1 \implies f'(x) > 0$ (**strictly increasing**).
* **On $(e, +\infty)$:** $\ln x > 1 \implies f'(x) < 0$ (**strictly decreasing**).

Therefore, $f$ attains its **unique global (and local) maximum** at $x = e$:

$$
f(e) = \frac{\ln e}{e} = \frac{1}{e} \approx 0.3679
$$

The maximum point is $\left(e, \frac{1}{e}\right)$.

**4. Inflection Point (Curvature)**

Differentiating $f'(x) = (1 - \ln x)x^{-2}$ gives:

$$
f''(x) = \frac{\left(-\frac{1}{x}\right) x^2 - (1 - \ln x)(2x)}{x^4} = \frac{-x - 2x + 2x\ln x}{x^4} = \frac{2\ln x - 3}{x^3}
$$

Setting $f''(x) = 0$ gives $\ln x = \frac{3}{2} \implies x = e^{3/2} \approx 4.48$, where $f$ changes from concave ($0 < x < e^{3/2}$) to convex ($x > e^{3/2}$), yielding an inflection point at $\left(e^{3/2}, \, \frac{3}{2e^{3/2}}\right)$.

**5. Information Necessary for a Correct Sketch**

To sketch $y = \frac{\ln x}{x}$ accurately without distorting its proportions, five essential pieces of information are needed:
1. **Domain boundary ($x > 0$) and vertical asymptote ($x = 0$):** Shows that the graph exists only in the right half-plane and plunges vertically to $-\infty$ near the $y$-axis.
2. **Unique $x$-intercept at $(1, 0)$:** Marks the exact transition from negative values ($0 < x < 1$) to positive values ($x > 1$).
3. **Global maximum at $\left(e, \frac{1}{e}\right) \approx (2.72, 0.37)$:** Fixes the peak height and location where the curve turns downward.
4. **Horizontal asymptote $y = 0$ as $x \to +\infty$:** Ensures the right tail decays gradually toward the positive $x$-axis from above without crossing it again.
5. **Inflection point at $\left(e^{3/2}, \frac{3}{2e^{3/2}}\right) \approx (4.48, 0.33)$:** Explains why the curve bends downward over the peak and then bends upward to flatten smoothly along $y = 0$.

---

### Final Answer

1. **Maximum:** Global maximum of $\frac{1}{e}$ at $x = e$, i.e., $\left(e, \frac{1}{e}\right)$.
2. **End behavior:** $\lim_{x \to 0^+} f(x) = -\infty$ (vertical asymptote $x = 0$) and $\lim_{x \to +\infty} f(x) = 0^+$ (horizontal asymptote $y = 0$).
3. **Key sketch data:** Domain $(0, +\infty)$, vertical asymptote $x = 0$, zero at $(1, 0)$, global peak at $\left(e, \frac{1}{e}\right)$, inflection at $\left(e^{3/2}, \frac{3}{2e^{3/2}}\right)$, and horizontal asymptote $y = 0$.
