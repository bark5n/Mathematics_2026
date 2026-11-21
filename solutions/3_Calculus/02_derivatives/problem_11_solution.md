### Essential Formulas

**Limit Definition of the Derivative:**

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

**Algebraic Expansion of a Square:**

$$(x + h)^2 = x^2 + 2xh + h^2$$

---

### Problem Statement

**Problem 11. Derivative from the Definition**

Using only

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h},$$

find the derivative of $f(x) = x^2$. Compare the result with the power rule and indicate where the limit is used in the calculation.

> **Why this problem:** it shows the origin of the power rule and the direct connection between the derivative and a limit.

---

### Solution

**Step 1: Form the difference quotient for $f(x) = x^2$**

For $h \neq 0$, compute $f(x + h) - f(x)$:

$$\begin{aligned} \frac{f(x + h) - f(x)}{h} &= \frac{(x + h)^2 - x^2}{h} \\ &= \frac{x^2 + 2xh + h^2 - x^2}{h} \\ &= \frac{2xh + h^2}{h} \end{aligned}$$

**Step 2: Simplify the difference quotient by canceling $h \neq 0$**

Factor $h$ out of the numerator and cancel with the denominator (valid because in the limit $h \to 0$, we only consider $h \neq 0$):

$$\frac{h(2x + h)}{h} = 2x + h \qquad (h \neq 0)$$

**Step 3: Take the limit as $h \to 0$**

Now apply the limit operation to the simplified expression $2x + h$:

$$f'(x) = \lim_{h \to 0} (2x + h) = 2x + 0 = 2x$$

**Step 4: Compare with the power rule and indicate where the limit is used**

* **Comparison with the power rule:** Applying the power rule $\frac{d}{dx}(x^n) = n x^{n-1}$ with $n = 2$ gives $2 x^{2 - 1} = 2x$, which matches the result derived from first principles.
* **Where the limit is used:**
  1. **Before taking the limit:** The condition $h \to 0$ implies $h \neq 0$, which justifies dividing numerator and denominator by $h$ to eliminate the $\frac{0}{0}$ indeterminate form in $\frac{2xh + h^2}{h}$.
  2. **At the final step:** The limit $\lim_{h \to 0} (2x + h) = 2x$ removes the residual secant-slope error term $+h$, turning the average rate of change over $[x, x + h]$ into the exact instantaneous rate of change at $x$.

---

### Final Answer

1. **Derivative from definition:** $f'(x) = 2x$ (identical to the power rule $2x^{2-1} = 2x$).
2. **Role of the limit:** Ensures $h \neq 0$ during algebraic cancellation of $h$ and eliminates the remaining $+h$ term at the final step $\lim_{h \to 0} (2x + h) = 2x$.
