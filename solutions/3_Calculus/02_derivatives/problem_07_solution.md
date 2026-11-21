### Essential Formulas

**Chain Rule for Trigonometric Compositions:**

$$
\frac{d}{dx}\big(\sin(h(x))\big) = \cos\big(h(x)\big) \cdot h'(x)
$$

---

### Problem Statement

**Problem 7. A Trigonometric Composition**

For

$$
f(x) = \sin(x^2 + 1)
$$

compute the derivative. Explicitly identify the outer function, the inner function, and the derivative of the inner function. Finally, determine the sign of $f'(0)$.

> **Why this problem:** it reinforces the chain rule in a different type of composition.

---

### Solution

**Step 1: Identify the outer function, inner function, and inner derivative**

Decompose $f(x) = g(h(x))$:
* **Outer function:** $g(u) = \sin u$, whose derivative is $g'(u) = \cos u$.
* **Inner function:** $u = h(x) = x^2 + 1$.
* **Derivative of the inner function:** $h'(x) = 2x$.

**Step 2: Apply the chain rule to compute $f'(x)$**

Combine $g'(h(x))$ and $h'(x)$:

$$
\begin{aligned}
f'(x) &= g'\big(h(x)\big) \cdot h'(x) \\
      &= \cos(x^2 + 1) \cdot 2x \\
      &= 2x \cos(x^2 + 1)
\end{aligned}
$$

**Step 3: Compute $f'(0)$ and determine its sign**

Substitute $x = 0$ into $f'(x)$:

$$
f'(0) = 2(0) \cos(0^2 + 1) = 0 \cdot \cos(1) = 0
$$

Because $f'(0) = 0$, the derivative at $x = 0$ is **zero** (neither positive nor negative; $x = 0$ is a critical point where the tangent line is horizontal).

---

### Final Answer

1. **Layers:** Outer function $g(u) = \sin u$, inner function $h(x) = x^2 + 1$, inner derivative $h'(x) = 2x$.
2. **Derivative:** $f'(x) = 2x \cos(x^2 + 1)$.
3. **Sign of $f'(0)$:** $f'(0) = 0$, so it is **zero** (neither positive nor negative).
