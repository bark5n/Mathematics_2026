### Essential Formulas

**Logarithmic Antiderivative Pattern:**
If $u(x) \neq 0$ is differentiable, then:

$$
\int \frac{u'(x)}{u(x)} \, dx = \ln|u(x)| + C
$$

---

### Problem Statement

**Problem 6. When Does a Logarithm Appear from an Integral?**

Compute

$$
\int \frac{2x}{x^2 + 5} \, dx.
$$

Identify the denominator as a candidate for substitution, compare the numerator with its derivative, and explain the source of the logarithm in the result.

> **Why this problem:** it teaches how to recognize the structure “derivative of the denominator over the denominator.”

---

### Solution

**Step 1: Identify the denominator as $u$ and compare the numerator with $u'(x)$**

Choose the denominator as the new substitution variable:

$$
u = x^2 + 5
$$

Differentiate $u$ with respect to $x$:

$$
\frac{du}{dx} = 2x \implies du = 2x \, dx
$$

Comparing $du$ with the numerator reveals an **exact match**: the numerator $2x$ is literally the derivative of the denominator $x^2 + 5$.

**Step 2: Substitute $u = x^2 + 5$ and evaluate the integral**

Rewrite the integral in terms of $u$:

$$
\begin{aligned}
\int \frac{2x}{x^2 + 5} \, dx
&= \int \frac{1}{u} \, du \\
&= \ln|u| + C \\
&= \ln(x^2 + 5) + C
\end{aligned}
$$

*(Because $x^2 + 5 \ge 5 > 0$ for all $x \in \mathbb{R}$, $|x^2 + 5| = x^2 + 5$, so the absolute value bars simplify cleanly to parentheses.)*

**Step 3: Explain the source of the logarithm in the result**

When integrating powers $u^n$ via the power rule $\int u^n \, du = \frac{u^{n+1}}{n+1} + C$, the exponent $n = -1$ is the unique exception where division by $n + 1 = 0$ fails. Instead, because the derivative of $\ln|u|$ is $\frac{1}{u}$ (and by the chain rule, $\frac{d}{dx}\big(\ln|u(x)|\big) = \frac{u'(x)}{u(x)}$), any fraction whose numerator is the derivative of its denominator reverses the logarithmic chain rule and produces $\ln|u(x)| + C$.

---

### Final Answer

1. **Substitution match:** Denominator $u = x^2 + 5$ has derivative $u'(x) = 2x$, matching the numerator identically.
2. **Indefinite integral:**
   $$
   \int \frac{2x}{x^2 + 5} \, dx = \ln(x^2 + 5) + C
   $$
