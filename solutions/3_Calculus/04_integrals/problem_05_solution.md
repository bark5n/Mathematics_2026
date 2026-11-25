### Essential Formulas

**Substitution with a Constant Adjustment:**
If $u = h(x)$ and $du = h'(x) \, dx$:

$$
\int g\big(h(x)\big) h'(x) \, dx = \int g(u) \, du
$$

---

### Problem Statement

**Problem 5. The Same Substitution in a Different Context**

Compute

$$
\int x e^{x^2} \, dx.
$$

First compare the structure with Problem 4 and explain what is common despite the different appearance of the function.

> **Why this problem:** it shows that the substitution mechanism is recognized by structure, not by the type of function.

---

### Solution

**Step 1: Compare the structure with Problem 4**

* **Problem 4:** $\int 2x (x^2 + 1)^4 \, dx$ has the form $\int g(u(x)) u'(x) \, dx$ where the outer function is a power $g(u) = u^4$ and the inner function is quadratic ($u = x^2 + 1$, $du = 2x \, dx$).
* **Problem 5:** $\int x e^{x^2} \, dx$ has the **exact same composite-times-derivative structure** $\int g(u(x)) u'(x) \, dx$, except that the outer function is now exponential ($g(u) = e^u$) and the inner function is $u = x^2$.
* **What is common:** Despite replacing a polynomial power $(\cdot)^4$ with an exponential $e^{(\cdot)}$, both integrands contain a function of $x^2$ multiplied by $x \, dx$, which is proportional to the derivative of $x^2$ ($d(x^2) = 2x \, dx$). Thus the identical substitution mechanism applies.

**Step 2: Apply the substitution $u = x^2$**

Set:

$$
u = x^2 \implies du = 2x \, dx \implies x \, dx = \frac{1}{2} \, du
$$

Substitute into the integral:

$$
\begin{aligned}
\int x e^{x^2} \, dx
&= \int e^u \cdot \frac{1}{2} \, du \\
&= \frac{1}{2} \int e^u \, du \\
&= \frac{1}{2} e^u + C \\
&= \frac{1}{2} e^{x^2} + C
\end{aligned}
$$

**Step 3: Verify by differentiation**

Differentiate $F(x) = \frac{1}{2} e^{x^2} + C$ using the chain rule:

$$
F'(x) = \frac{1}{2} e^{x^2} \cdot \frac{d}{dx}(x^2) = \frac{1}{2} e^{x^2} \cdot 2x = x e^{x^2}
$$

---

### Final Answer

1. **Structural commonality:** Just like Problem 4, the integrand is a composite function of $x^2$ multiplied by $x \, dx$ (a constant multiple of $d(x^2) = 2x \, dx$).
2. **Indefinite integral:**
   $$
   \int x e^{x^2} \, dx = \frac{1}{2} e^{x^2} + C
   $$
