### Essential Formulas

**Product Rule for Differentiation:**
If $u(x)$ and $v(x)$ are differentiable functions, then:

$$
\big(u(x) v(x)\big)' = u'(x) v(x) + u(x) v'(x)
$$

**Derivative of the Natural Exponential Function:**

$$
\frac{d}{dx}\left(e^x\right) = e^x
$$

---

### Problem Statement

**Problem 3. The Product Rule — Why Is It Needed?**

For

$$
f(x) = (x^2 + 1) e^x
$$

compute the derivative. Then compare the correct result with the incorrect idea

$$
f'(x) \stackrel{?}{=} (2x) e^x
$$

and explain which term is missing.

> **Why this problem:** it teaches the product rule by analyzing a common mistake.

---

### Solution

**Step 1: Identify the two factors and apply the product rule**

Let $u(x) = x^2 + 1$ and $v(x) = e^x$. Their individual derivatives are:

$$
u'(x) = 2x, \qquad v'(x) = e^x
$$

Using the product rule $f'(x) = u'(x) v(x) + u(x) v'(x)$:

$$
\begin{aligned}
f'(x) &= (2x) e^x + (x^2 + 1) e^x \\
      &= (x^2 + 2x + 1) e^x \\
      &= (x + 1)^2 e^x
\end{aligned}
$$

**Step 2: Compare with the incorrect formula and identify the missing term**

* **Incorrect formula:** $f'_{\mathrm{incorrect}}(x) = (2x) e^x = u'(x) v'(x)$.
* **Difference (missing term):**
  $$
  f'(x) - f'_{\mathrm{incorrect}}(x) = \big[(2x) e^x + (x^2 + 1) e^x\big] - (2x) e^x = (x^2 + 1) e^x
  $$

**Explanation:** The incorrect formula differentiates each factor separately and multiplies the derivatives ($u' v'$), treating $e^x$ as if it were a constant coefficient multiplying $x^2 + 1$. Because both factors vary simultaneously with $x$, the total rate of change also includes the contribution from holding $x^2 + 1$ fixed while $e^x$ changes, which is precisely the missing term $u(x) v'(x) = (x^2 + 1) e^x$.

---

### Final Answer

1. **Correct derivative:** $f'(x) = (2x)e^x + (x^2 + 1)e^x = (x + 1)^2 e^x$.
2. **Missing term:** The incorrect expression $(2x)e^x$ omits the second term of the product rule, $(x^2 + 1)e^x$.
