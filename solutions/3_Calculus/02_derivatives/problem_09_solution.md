### Essential Formulas

**Chain Rule for the Natural Logarithm:**

$$\frac{d}{dx}\big(\ln(h(x))\big) = \frac{h'(x)}{h(x)} \qquad \big(h(x) > 0\big)$$

---

### Problem Statement

**Problem 9. A Logarithm and the Chain Rule**

For

$$f(x) = \ln(x^2 + 1)$$

compute the derivative. Then determine the sign of $f'(x)$ for $x < 0$, $x = 0$, and $x > 0$, and describe qualitatively how the function behaves around zero.

> **Why this problem:** it connects differentiation with sign analysis and the behavior of a function.

---

### Solution

**Step 1: Compute the derivative $f'(x)$**

Note that $x^2 + 1 \ge 1 > 0$ for all $x \in \mathbb{R}$, so $f(x)$ is defined and differentiable everywhere on $\mathbb{R}$. Apply the chain rule with outer function $\ln u$ and inner function $u = x^2 + 1$ ($u' = 2x$):

$$f'(x) = \frac{1}{x^2 + 1} \cdot \frac{d}{dx}(x^2 + 1) = \frac{2x}{x^2 + 1}$$

**Step 2: Analyze the sign of $f'(x)$**

Since the denominator $x^2 + 1$ is strictly positive ($x^2 + 1 \ge 1 > 0$) for all $x \in \mathbb{R}$, the sign of $f'(x) = \frac{2x}{x^2 + 1}$ is determined entirely by the numerator $2x$:
* **For $x < 0$:** $2x < 0 \implies f'(x) < 0$ (**negative**).
* **For $x = 0$:** $2(0) = 0 \implies f'(0) = 0$ (**zero**).
* **For $x > 0$:** $2x > 0 \implies f'(x) > 0$ (**positive**).

**Step 3: Describe qualitatively how $f(x)$ behaves around zero**

* Because $f'(x) < 0$ for $x < 0$, the function is **strictly decreasing** as $x$ approaches $0$ from the left.
* At $x = 0$, $f'(0) = 0$ and $f(0) = \ln(1) = 0$, so the graph has a horizontal tangent at the origin $(0, 0)$.
* Because $f'(x) > 0$ for $x > 0$, the function is **strictly increasing** for $x > 0$.
* Combining these observations (and noting $f(-x) = f(x)$, so $f$ is an even function), $f(x) = \ln(x^2 + 1)$ attains a **global minimum** of $0$ at $x = 0$, forming a smooth symmetric U-shaped valley around $(0, 0)$.

---

### Final Answer

1. **Derivative:**
   $$f'(x) = \frac{2x}{x^2 + 1}$$
2. **Sign of $f'(x)$:** Negative ($f'(x) < 0$) for $x < 0$, zero ($f'(0) = 0$) at $x = 0$, and positive ($f'(x) > 0$) for $x > 0$.
3. **Behavior around zero:** $f(x)$ decreases on $(-\infty, 0)$, reaches a smooth global minimum at $(0, 0)$ with horizontal tangent $y = 0$, and increases on $(0, +\infty)$.
