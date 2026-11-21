### Essential Formulas

**Derivative as the Limit of the Difference Quotient:**

$$
f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}
$$

---

### Problem Statement

**Problem 15. The Difference Quotient as a Check of the Derivative**

Choose one function from the problem set and a point $x_0$ at which the derivative exists. Compute $f'(x_0)$ exactly, and then calculate

$$
\frac{f(x_0 + h) - f(x_0)}{h}
$$

for $h = 1$, $0.1$, and $0.01$. Compare the values with $f'(x_0)$ and explain why the difference quotient approaching a single number is consistent with the definition of the derivative, while a few computations do not replace a limit argument.

> **Why this problem:** it connects the definition of the derivative with concrete calculations and teaches the distinction between observation and proof.

---

### Solution

**Step 1: Choose a function and point, and compute $f'(x_0)$ exactly**

Select the function from Problem 10:

$$
f(x) = x^2 - 3x + 1
$$

and choose the point $x_0 = 2$.

* **Exact derivative:** Differentiating gives $f'(x) = 2x - 3$. Evaluating at $x_0 = 2$:
  $$
  f'(2) = 2(2) - 3 = 1
  $$
* **Reference function value:** $f(2) = 2^2 - 3(2) + 1 = -1$.

**Step 2: Compute the difference quotient for $h = 1$, $0.1$, and $0.01$**

Let $Q(h) = \frac{f(2 + h) - f(2)}{h}$:

1. **For $h = 1$:**
   $$
   f(2 + 1) = f(3) = 3^2 - 3(3) + 1 = 1
   $$
   $$
   Q(1) = \frac{1 - (-1)}{1} = \frac{2}{1} = 2
   $$

2. **For $h = 0.1$:**
   $$
   f(2 + 0.1) = f(2.1) = (2.1)^2 - 3(2.1) + 1 = 4.41 - 6.30 + 1 = -0.89
   $$
   $$
   Q(0.1) = \frac{-0.89 - (-1)}{0.1} = \frac{0.11}{0.1} = 1.1
   $$

3. **For $h = 0.01$:**
   $$
   f(2 + 0.01) = f(2.01) = (2.01)^2 - 3(2.01) + 1 = 4.0401 - 6.0300 + 1 = -0.9899
   $$
   $$
   Q(0.01) = \frac{-0.9899 - (-1)}{0.01} = \frac{0.0101}{0.01} = 1.01
   $$

**Summary Table:**

| Step Size $h$ | $f(2 + h)$ | Difference Quotient $\frac{f(2 + h) - f(2)}{h}$ | Error $|Q(h) - f'(2)|$ |
| :--- | :--- | :--- | :--- |
| $1$ | $1$ | $2$ | $1$ |
| $0.1$ | $-0.89$ | $1.1$ | $0.1$ |
| $0.01$ | $-0.9899$ | $1.01$ | $0.01$ |

**Step 3: Compare with $f'(2)$ and explain why finite checks do not replace a limit proof**

* **Consistency with the definition:** As $h$ decreases ($1 \to 0.1 \to 0.01$), the secant slopes $Q(h)$ take the values $2 \to 1.1 \to 1.01$, approaching the exact tangent slope $f'(2) = 1$ with error equal to $h$. This numerical convergence matches the limit definition $f'(2) = \lim_{h \to 0} Q(h) = 1$.
* **Why a few computations do not replace a limit argument:**
  1. **One-sided and finitely many samples:** Evaluating $Q(h)$ at only three positive values ($h = 1, 0.1, 0.01$) leaves negative increments ($h < 0$) and infinitely many smaller increments ($0 < |h| < 0.01$) untested.
  2. **Possibility of non-differentiability at smaller scales:** A function with a sharp corner or rapid oscillation at scales smaller than $0.01$ (for instance, $g(x) = |x - 2| + (x - 2) + (x - 2)^2 - 1$, which agrees with $f(x)$ for all $x \ge 2$ yet has left-hand derivative $0 \neq 2$ at $x_0 = 2$) would produce the exact same values $2, 1.1, 1.01$ for $h = 1, 0.1, 0.01$, even though $g'(2)$ does not exist. Only a general algebraic limit calculation valid for all $h \to 0$ from both sides proves differentiability.

---

### Final Answer

1. **Chosen function and exact derivative:** For $f(x) = x^2 - 3x + 1$ at $x_0 = 2$, $f'(2) = 1$.
2. **Difference quotients:** $Q(1) = 2$, $Q(0.1) = 1.1$, and $Q(0.01) = 1.01$.
3. **Conclusion:** The values converge cleanly toward $1$, confirming the limit definition numerically, but finite samples cannot rule out left-hand disagreements or micro-scale singularities without a general two-sided limit proof.
