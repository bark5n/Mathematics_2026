### Essential Formulas

**Rationalizing a Square-Root Difference:**

$$
\sqrt{x} - \sqrt{a} = \frac{(\sqrt{x} - \sqrt{a})(\sqrt{x} + \sqrt{a})}{\sqrt{x} + \sqrt{a}} = \frac{x - a}{\sqrt{x} + \sqrt{a}} \qquad (x \ge 0, \, \sqrt{x} + \sqrt{a} \neq 0)
$$

---

### Problem Statement

**Exercise 8. A Square Root in a Function Limit**

Compute

$$
\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}
$$

by rationalizing the numerator. Compare the idea with Exercise 3 involving a sequence.

> **Why this exercise:** reinforces transferring the same algebraic technique between two types of limits.

---

### Solution

**Step 1: Identify the indeterminate form**

At $x = 4$, both numerator $\sqrt{4} - 2 = 0$ and denominator $4 - 4 = 0$ vanish, yielding a $\frac{0}{0}$ indeterminate form.

**Step 2: Rationalize the numerator**

Multiply numerator and denominator by the conjugate expression $\sqrt{x} + 2$ (which is positive for all $x \ge 0$):

$$
\begin{aligned}
\frac{\sqrt{x} - 2}{x - 4}
&= \frac{(\sqrt{x} - 2)(\sqrt{x} + 2)}{(x - 4)(\sqrt{x} + 2)} \\
&= \frac{(\sqrt{x})^2 - 2^2}{(x - 4)(\sqrt{x} + 2)} \\
&= \frac{x - 4}{(x - 4)(\sqrt{x} + 2)}
\end{aligned}
$$

**Step 3: Cancel the common factor and evaluate the limit**

For $x \neq 4$ ($x \ge 0$), cancel $x - 4$:

$$
\lim_{x \to 4} \frac{x - 4}{(x - 4)(\sqrt{x} + 2)} = \lim_{x \to 4} \frac{1}{\sqrt{x} + 2} = \frac{1}{\sqrt{4} + 2} = \frac{1}{2 + 2} = \frac{1}{4}
$$

**Step 4: Compare the algebraic idea with Exercise 3**

In both Exercise 3 (sequence limit as $n \to \infty$) and Exercise 8 (function limit as $x \to 4$), a square-root difference blocks direct evaluation by creating an indeterminate form ($\infty - \infty$ in Exercise 3 and $\frac{0}{0}$ in Exercise 8). In both cases, multiplying by the conjugate $\sqrt{A} + B$ applies the identity $(\sqrt{A} - B)(\sqrt{A} + B) = A - B^2$ to eliminate the radical from the numerator, revealing a clean cancellation ($n^2 - n^2$ in Exercise 3 and $x - 4$ in Exercise 8) while leaving a non-vanishing sum of positive terms in the denominator.

---

### Final Answer

1. **Limit value:** $\frac{1}{4}$.
2. **Comparison with Exercise 3:** Both solutions use conjugate multiplication $(\sqrt{A} - B)(\sqrt{A} + B) = A - B^2$ to remove the square root from the numerator and convert an indeterminate difference into a clean algebraic cancellation.
