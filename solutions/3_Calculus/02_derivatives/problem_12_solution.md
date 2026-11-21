### Essential Formulas

**Product Rule:**

$$
\big(u(x) v(x)\big)' = u'(x) v(x) + u(x) v'(x)
$$

**Chain Rule:**

$$
\frac{d}{dx}\Big(\big(h(x)\big)^n\Big) = n \big(h(x)\big)^{n-1} \cdot h'(x)
$$

---

### Problem Statement

**Problem 12. Several Rules at Once**

For

$$
f(x) = (x^2 + 1)^3 e^x
$$

compute the derivative. Before calculating, write down a plan: which rule applies to the whole expression and which rule applies to one of its factors. Finally, organize the result by factoring out common factors.

> **Why this problem:** it practices the order of decisions when combining familiar differentiation rules.

---

### Solution

**Step 1: Differentiation plan**

1. **Top-level structure (whole expression):** The function $f(x) = (x^2 + 1)^3 \cdot e^x$ is a product of two functions, $u(x) = (x^2 + 1)^3$ and $v(x) = e^x$. Therefore, the **product rule** applies first to the whole expression.
2. **Inner structure (first factor):** When computing $u'(x) = \frac{d}{dx}\big((x^2 + 1)^3\big)$, the factor is a composite function with outer layer $(\cdot)^3$ and inner layer $x^2 + 1$. Therefore, the **chain rule** applies to differentiate $u(x)$ (while $v'(x) = e^x$ uses the standard exponential rule).

**Step 2: Differentiate the individual factors**

* Using the chain rule on $u(x) = (x^2 + 1)^3$:
  $$
  u'(x) = 3(x^2 + 1)^2 \cdot \frac{d}{dx}(x^2 + 1) = 3(x^2 + 1)^2 (2x) = 6x(x^2 + 1)^2
  $$

* Differentiating $v(x) = e^x$:
  $$
  v'(x) = e^x
  $$

**Step 3: Apply the product rule and factor out common terms**

Combine via $f'(x) = u'(x) v(x) + u(x) v'(x)$:

$$
f'(x) = 6x(x^2 + 1)^2 e^x + (x^2 + 1)^3 e^x
$$

Factor out the common factors $(x^2 + 1)^2$ and $e^x$:

$$
\begin{aligned}
f'(x) &= (x^2 + 1)^2 e^x \big[6x + (x^2 + 1)\big] \\
      &= (x^2 + 1)^2 (x^2 + 6x + 1) e^x
\end{aligned}
$$

---

### Final Answer

1. **Plan:** Apply the **product rule** to the overall product $(x^2 + 1)^3 \cdot e^x$, and apply the **chain rule** to differentiate the composite factor $(x^2 + 1)^3$.
2. **Factored derivative:**
   $$
   f'(x) = (x^2 + 1)^2 (x^2 + 6x + 1) e^x
   $$
