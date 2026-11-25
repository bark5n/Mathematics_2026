### Essential Formulas

**Recovering a Function from Its Derivative and Initial Value:**

$$
F(x) = \int F'(x) \, dx + C, \qquad \mathrm{with}\ C\ \mathrm{determined\ by}\ F(x_0) = y_0
$$

**Substitution Rule:**

$$
\int e^{u(x)} u'(x) \, dx = e^{u(x)} + C
$$

---

### Problem Statement

**Problem 15. Recovering a Function from Its Derivative and a Condition**

The function $F$ satisfies

$$
F'(x) = 2x e^{x^2}
$$

and

$$
F(0) = 3.
$$

1. Recognize the method needed to find the function $F$.
2. Determine the entire family of functions with the given derivative.
3. Use the condition $F(0) = 3$ to determine the correct constant.
4. Verify the final result by differentiation and substitution of $x = 0$.

> **Why this problem:** it combines recognition of substitution, the meaning of the constant of integration, and an initial condition in one problem, using only mechanisms introduced earlier.

---

### Solution

**1. Recognize the method needed to find $F$**

To recover $F(x)$ from $F'(x) = 2x e^{x^2}$, we compute the indefinite integral $\int 2x e^{x^2} \, dx$. Because the integrand is the exponential composition $e^{x^2}$ multiplied by $2x$, which is the exact derivative of the inner exponent $u = x^2$, the appropriate method is **integration by substitution** with $u = x^2$ and $du = 2x \, dx$.

**2. Determine the entire family of functions with derivative $2x e^{x^2}$**

Substitute $u = x^2$ and $du = 2x \, dx$:

$$
\begin{aligned}
F(x) &= \int 2x e^{x^2} \, dx \\
     &= \int e^u \, du \\
     &= e^u + C \\
     &= e^{x^2} + C \qquad (C \in \mathbb{R})
\end{aligned}
$$

**3. Use the initial condition $F(0) = 3$ to determine $C$**

Substitute $x = 0$ into $F(x) = e^{x^2} + C$ and set equal to $3$:

$$
F(0) = e^{0^2} + C = e^0 + C = 1 + C = 3 \implies C = 2
$$

Thus the unique solution is:

$$
F(x) = e^{x^2} + 2
$$

**4. Verify the final result by differentiation and substitution of $x = 0$**

* **Derivative check:** Differentiate $F(x) = e^{x^2} + 2$ using the chain rule:
  $$
  F'(x) = e^{x^2} \cdot \frac{d}{dx}(x^2) + 0 = 2x e^{x^2}
  $$
  Matches the given derivative.

* **Initial-condition check:** Evaluate $F(x) = e^{x^2} + 2$ at $x = 0$:
  $$
  F(0) = e^{0^2} + 2 = 1 + 2 = 3
  $$
  Matches the given condition $F(0) = 3$.

---

### Final Answer

1. **Method:** Integration by substitution ($u = x^2$, $du = 2x \, dx$).
2. **Family of antiderivatives:** $F(x) = e^{x^2} + C$ ($C \in \mathbb{R}$).
3. **Specific constant and function:** $C = 2$, yielding $F(x) = e^{x^2} + 2$.
4. **Verification:** $F'(x) = 2x e^{x^2}$ and $F(0) = e^0 + 2 = 3$.
