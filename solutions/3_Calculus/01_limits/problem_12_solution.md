### Essential Formulas

**Continuous-Variable Form of Euler's Limit:**

$$\lim_{u \to 0} (1 + u)^{1/u} = e$$

---

### Problem Statement

**Exercise 12. Exponential Function Limit**

Compute

$$\lim_{x \to 0} (1 + 3x)^{1/x}.$$

Connect the result with the limit from Exercise 5 and show the appropriate transformation.

> **Why this exercise:** teaches how to recognize the classical pattern after a transformation.

---

### Solution

**Step 1: Identify the indeterminate form**

As $x \to 0$, the base $1 + 3x \to 1$ while the exponent $\frac{1}{x} \to \pm \infty$, giving an indeterminate form of type $1^\infty$.

**Step 2: Transform the exponent to match the standard pattern**

Rewrite the exponent $\frac{1}{x}$ as $\frac{3}{3x} = \frac{1}{3x} \cdot 3$ so that the denominator of the inner exponent matches the added term $3x$ in the base:

$$(1 + 3x)^{1/x} = (1 + 3x)^{\frac{1}{3x} \cdot 3} = \left[(1 + 3x)^{\frac{1}{3x}}\right]^3$$

**Step 3: Substitute $u = 3x$ and connect with Exercise 5**

Let $u = 3x$. As $x \to 0$, we also have $u \to 0$ (with $u \neq 0$ for $x \neq 0$). In Exercise 5, we established that $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e$; setting $u = \frac{1}{n}$ extends this classical pattern to a continuous variable approaching zero:

$$\lim_{u \to 0} (1 + u)^{1/u} = e$$

Because the power function $t \mapsto t^3$ is continuous at $t = e$:

$$\lim_{x \to 0} (1 + 3x)^{1/x} = \left[\lim_{u \to 0} (1 + u)^{1/u}\right]^3 = e^3$$

---

### Final Answer

1. **Limit value:** $e^3$.
2. **Transformation:** Rewriting $(1 + 3x)^{1/x} = \left[(1 + 3x)^{1/(3x)}\right]^3$ and substituting $u = 3x \to 0$ reduces the expression directly to the classical Euler limit $\lim_{u \to 0} (1 + u)^{1/u} = e$, yielding $e^3$.
