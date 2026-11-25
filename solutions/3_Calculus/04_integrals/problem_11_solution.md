### Essential Formulas

**1. Linear Substitution ($\int f(ax + b) \, dx$):**

$$
\int \sin(kx) \, dx = -\frac{1}{k}\cos(kx) + C \qquad (k \neq 0)
$$

**2. Integration by Parts:**

$$
\int u \, dv = uv - \int v \, du
$$

**3. Standard Substitution ($\int g(u(x)) u'(x) \, dx$):**

$$
\int u^{-1/2} \, du = 2\sqrt{u} + C \qquad (u > 0)
$$

---

### Problem Statement

**Problem 11. Choose the Method First**

For each integral, first write which method you choose and how you recognize it, and then compute:

1. $\int \sin(3x) \, dx$,
2. $\int x \ln x \, dx$,
3. $\int \frac{x}{\sqrt{x^2 + 1}} \, dx$.

> **Why this problem:** it tests the choice of method based on the structure of the problem.

---

### Solution

**1. $\int \sin(3x) \, dx$**

* **Method chosen and recognition:** **Simple linear substitution** ($u = 3x$). The integrand is a single elementary trigonometric function whose argument is a constant multiple $3x$ (derivative $3$, a nonzero constant).
* **Calculation:**
  Let $u = 3x \implies du = 3 \, dx \implies dx = \frac{1}{3} \, du$:
  $$
  \begin{aligned}
  \int \sin(3x) \, dx
  &= \int \sin u \cdot \frac{1}{3} \, du \\
  &= \frac{1}{3}(-\cos u) + C \\
  &= -\frac{1}{3}\cos(3x) + C
  \end{aligned}
  $$

---

**2. $\int x \ln x \, dx$ ($x > 0$)**

* **Method chosen and recognition:** **Integration by parts** ($u = \ln x$, $dv = x \, dx$). The integrand is a product of two unrelated function families—a polynomial ($x$) and a logarithm ($\ln x$)—with no inner-derivative match for substitution. Choosing $u = \ln x$ eliminates the logarithm upon differentiation ($du = \frac{1}{x} \, dx$), turning the remaining integral into a simple power of $x$.
* **Calculation:**
  Set:
  $$
  u = \ln x \implies du = \frac{1}{x} \, dx
  $$
  $$
  dv = x \, dx \implies v = \frac{x^2}{2}
  $$
  Apply $\int u \, dv = uv - \int v \, du$:
  $$
  \begin{aligned}
  \int x \ln x \, dx
  &= \frac{x^2}{2}\ln x - \int \frac{x^2}{2} \cdot \frac{1}{x} \, dx \\
  &= \frac{x^2}{2}\ln x - \frac{1}{2} \int x \, dx \\
  &= \frac{x^2}{2}\ln x - \frac{x^2}{4} + C \qquad (x > 0)
  \end{aligned}
  $$

---

**3. $\int \frac{x}{\sqrt{x^2 + 1}} \, dx$**

* **Method chosen and recognition:** **Substitution** ($u = x^2 + 1$). The denominator contains the composite expression $\sqrt{x^2 + 1}$, and the numerator $x \, dx$ is a constant multiple of the derivative of the inner function $x^2 + 1$ ($du = 2x \, dx$).
* **Calculation:**
  Let $u = x^2 + 1 \implies du = 2x \, dx \implies x \, dx = \frac{1}{2} \, du$:
  $$
  \begin{aligned}
  \int \frac{x}{\sqrt{x^2 + 1}} \, dx
  &= \int \frac{1}{\sqrt{u}} \cdot \frac{1}{2} \, du \\
  &= \frac{1}{2} \int u^{-1/2} \, du \\
  &= \frac{1}{2} \cdot \frac{u^{1/2}}{1/2} + C \\
  &= \sqrt{u} + C \\
  &= \sqrt{x^2 + 1} + C
  \end{aligned}
  $$

---

### Final Answer

1. **Method:** Linear substitution ($u = 3x$); **Result:** $-\frac{1}{3}\cos(3x) + C$.
2. **Method:** Integration by parts ($u = \ln x$, $dv = x \, dx$); **Result:** $\frac{x^2}{2}\ln x - \frac{x^2}{4} + C$ ($x > 0$).
3. **Method:** Substitution ($u = x^2 + 1$); **Result:** $\sqrt{x^2 + 1} + C$.
