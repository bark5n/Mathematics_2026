### Essential Formulas

**Quotient Rule for Differentiation:**
If $u(x)$ and $v(x)$ are differentiable and $v(x) \neq 0$, then:

$$\left(\frac{u(x)}{v(x)}\right)' = \frac{u'(x) v(x) - u(x) v'(x)}{\big(v(x)\big)^2}$$

---

### Problem Statement

**Problem 4. A Quotient and Domain Control**

For

$$f(x) = \frac{x^2 + 1}{x - 1}$$

determine the domain, compute the derivative, simplify the result, and explain why the restriction $x \neq 1$ remains important.

> **Why this problem:** it practices the quotient rule together with domain control.

---

### Solution

**Step 1: Determine the domain of $f$**

The numerator $x^2 + 1$ and denominator $x - 1$ are polynomials defined for all $x \in \mathbb{R}$, so the only restriction is that the denominator cannot vanish:

$$x - 1 \neq 0 \implies x \neq 1$$

Thus, the domain is $D_f = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, +\infty)$.

**Step 2: Apply the quotient rule and simplify**

Let $u(x) = x^2 + 1$ and $v(x) = x - 1$, so $u'(x) = 2x$ and $v'(x) = 1$. For $x \neq 1$, the quotient rule gives:

$$\begin{aligned} f'(x) &= \frac{(2x)(x - 1) - (x^2 + 1)(1)}{(x - 1)^2} \\ &= \frac{2x^2 - 2x - x^2 - 1}{(x - 1)^2} \\ &= \frac{x^2 - 2x - 1}{(x - 1)^2} \end{aligned}$$

**Step 3: Explain why the restriction $x \neq 1$ remains important**

1. **In the formula for $f'(x)$:** The simplified derivative $\frac{x^2 - 2x - 1}{(x - 1)^2}$ still has $(x - 1)^2$ in its denominator, which equals $0$ at $x = 1$ (while the numerator evaluates to $1 - 2 - 1 = -2 \neq 0$).
2. **In the definition of differentiability:** A function cannot have a derivative at a point outside its domain. Since $f(1)$ is undefined (and $f(x)$ has a vertical asymptote at $x = 1$), $f'(1)$ does not exist, and all sign or monotonicity conclusions about $f'(x)$ must be analyzed separately on $(-\infty, 1)$ and $(1, +\infty)$ rather than across $x = 1$.

---

### Final Answer

1. **Domain:** $D_f = \mathbb{R} \setminus \{1\}$.
2. **Simplified derivative:**
   $$f'(x) = \frac{x^2 - 2x - 1}{(x - 1)^2} \qquad (x \neq 1)$$
3. **Importance of $x \neq 1$:** Both $f(x)$ and $f'(x)$ are undefined at $x = 1$ (vertical asymptote), so $x = 1$ splits the domain into two separate intervals $(-\infty, 1)$ and $(1, +\infty)$.
