### Essential Formulas

**Chain Rule for Function Composition:**
If $y = g(u)$ is differentiable at $u = h(x)$ and $u = h(x)$ is differentiable at $x$, then the composite function $f(x) = g(h(x))$ has derivative:

$$
f'(x) = g'\big(h(x)\big) \cdot h'(x)
$$

---

### Problem Statement

**Problem 5. The Chain Rule as Working Through Layers**

For

$$
f(x) = (3x^2 - 2x + 1)^5
$$

identify the inner and outer functions, compute their derivatives, and combine the result according to the chain rule. Explain the origin of the additional factor.

> **Why this problem:** it teaches how to recognize the structure of a composition instead of memorizing the rule as a meaningless pattern.

---

### Solution

**Step 1: Identify the outer and inner functions**

Decompose $f(x) = g(h(x))$ into two layers:
* **Outer function:** $g(u) = u^5$
* **Inner function:** $u = h(x) = 3x^2 - 2x + 1$

**Step 2: Compute the derivatives of both layers**

* **Derivative of the outer function with respect to $u$:**
  $$
  g'(u) = 5u^4
  $$
* **Derivative of the inner function with respect to $x$:**
  $$
  h'(x) = 6x - 2
  $$

**Step 3: Combine via the chain rule**

Multiply $g'(h(x))$ by $h'(x)$:

$$
\begin{aligned}
f'(x) &= g'\big(h(x)\big) \cdot h'(x) \\
      &= 5(3x^2 - 2x + 1)^4 \cdot (6x - 2) \\
      &= 10(3x - 1)(3x^2 - 2x + 1)^4
\end{aligned}
$$

**Step 4: Explain the origin of the additional factor $(6x - 2)$**

Differentiating $g(u) = u^5$ gives $5u^4$, which measures how fast the outer power $u^5$ changes **per unit change in $u$** ($\frac{dy}{du}$). However, $u = 3x^2 - 2x + 1$ is not equal to $x$; when $x$ changes by a small amount $\Delta x$, $u$ changes by approximately $\Delta u \approx h'(x)\,\Delta x = (6x - 2)\,\Delta x$. Multiplying by the inner derivative $h'(x) = 6x - 2$ ($\frac{du}{dx}$) converts the rate of change with respect to $u$ into the rate of change with respect to $x$ via $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$.

---

### Final Answer

1. **Layers and derivatives:** Outer function $g(u) = u^5$ with $g'(u) = 5u^4$; inner function $h(x) = 3x^2 - 2x + 1$ with $h'(x) = 6x - 2$.
2. **Combined derivative:**
   $$
   f'(x) = 5(3x^2 - 2x + 1)^4 (6x - 2) = 10(3x - 1)(3x^2 - 2x + 1)^4
   $$
3. **Origin of the extra factor:** The factor $6x - 2 = \frac{du}{dx}$ accounts for how fast the inner quantity $u$ itself varies with respect to $x$.
