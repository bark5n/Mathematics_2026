### Essential Formulas

**Limit of a Rational Function at a Removable Discontinuity:**
If $f(x) = g(x)$ for all $x \neq a$ in an open interval around $a$, then:

$$
\lim_{x \to a} f(x) = \lim_{x \to a} g(x)
$$

provided the latter limit exists.

---

### Problem Statement

**Exercise 7. Limit at a Point and Canceling a Factor**

Compute

$$
\lim_{x \to 3} \frac{x^2 - 4x + 3}{x - 3}.
$$

Explain why the value of the function at $x = 3$ is not needed to compute the limit.

> **Why this exercise:** separates the concept of a limit from the value of a function at a point.

---

### Solution

**Step 1: Identify the indeterminate form**

Substituting $x = 3$ directly gives $\frac{3^2 - 4(3) + 3}{3 - 3} = \frac{0}{0}$, which is an indeterminate form.

**Step 2: Factor the numerator and cancel the common factor**

Factor the quadratic numerator $x^2 - 4x + 3 = (x - 1)(x - 3)$. For all $x \neq 3$, we have $x - 3 \neq 0$, so division by $x - 3$ is valid:

$$
\frac{x^2 - 4x + 3}{x - 3} = \frac{(x - 1)(x - 3)}{x - 3} = x - 1 \qquad (x \neq 3)
$$

**Step 3: Evaluate the limit**

Because the limit as $x \to 3$ depends only on values of $x$ strictly close to $3$ ($x \neq 3$):

$$
\lim_{x \to 3} \frac{x^2 - 4x + 3}{x - 3} = \lim_{x \to 3} (x - 1) = 3 - 1 = 2
$$

**Step 4: Explain why the function value at $x = 3$ is not needed**

By definition, $\lim_{x \to 3} f(x)$ describes the behavior of $f(x)$ as $x$ approaches $3$ through punctured neighborhoods $0 < |x - 3| < \delta$, which explicitly exclude the point $x = 3$ itself. Even though $f(x) = \frac{x^2 - 4x + 3}{x - 3}$ is undefined at $x = 3$, it agrees with the continuous function $g(x) = x - 1$ at every $x \neq 3$, so its limit is completely determined by nearby points.

---

### Final Answer

1. **Limit value:** $2$.
2. **Independence from $f(3)$:** A limit at $x = 3$ depends solely on values of $f(x)$ for $x \neq 3$ near $3$, so whether $f(3)$ is defined or what value it takes has no effect on the limit.
