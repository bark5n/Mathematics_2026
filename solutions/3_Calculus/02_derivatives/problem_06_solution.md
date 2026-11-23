### Essential Formulas

**Basic Trigonometric Derivatives:**

$$\frac{d}{dx}(\sin x) = \cos x, \qquad \frac{d}{dx}(\cos x) = -\sin x$$

**Product Rule:**

$$\big(u(x) v(x)\big)' = u'(x) v(x) + u(x) v'(x)$$

---

### Problem Statement

**Problem 6. Product Rule and Trigonometry**

For

$$f(x) = x \sin x + \cos x$$

compute the derivative and simplify the result. Then compute $f'(0)$ and interpret the direction of the tangent line at that point.

> **Why this problem:** it combines the product rule with trigonometric derivatives and geometric interpretation.

---

### Solution

**Step 1: Differentiate $f(x) = x \sin x + \cos x$ and simplify**

Apply the product rule to the first term $x \sin x$ (with $u(x) = x$ and $v(x) = \sin x$) and differentiate $\cos x$ in the second term:

$$\begin{aligned} f'(x) &= \frac{d}{dx}(x) \cdot \sin x + x \cdot \frac{d}{dx}(\sin x) + \frac{d}{dx}(\cos x) \\ &= 1 \cdot \sin x + x \cos x - \sin x \\ &= x \cos x \end{aligned}$$

The $\sin x$ and $-\sin x$ terms cancel, leaving $f'(x) = x \cos x$.

**Step 2: Compute $f'(0)$**

Substitute $x = 0$ into $f'(x) = x \cos x$:

$$f'(0) = 0 \cdot \cos(0) = 0 \cdot 1 = 0$$

**Step 3: Interpret the direction of the tangent line at $x = 0$**

Since $f(0) = 0 \cdot \sin(0) + \cos(0) = 1$, the point of tangency is $(0, 1)$. Because the derivative at this point is $f'(0) = 0$, the tangent line has slope $m = 0$. Geometrically, the tangent line is **horizontal** (parallel to the $x$-axis, with equation $y = 1$). Moreover, since $\cos x > 0$ near $0$, $f'(x) = x \cos x$ changes sign from negative (for $x < 0$) to positive (for $x > 0$), so $(0, 1)$ is a stationary point corresponding to a **local minimum** of $f(x)$.

---

### Final Answer

1. **Simplified derivative:** $f'(x) = x \cos x$.
2. **Value at $x = 0$:** $f'(0) = 0$.
3. **Tangent line direction:** The slope is $0$, so the tangent line at $(0, 1)$ is **horizontal** ($y = 1$), and $(0, 1)$ is a local minimum because $f'(x) = x \cos x$ changes from negative to positive across $x = 0$.
