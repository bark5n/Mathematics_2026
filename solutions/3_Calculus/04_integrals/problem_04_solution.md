### Essential Formulas

**Integration by Substitution (Reverse Chain Rule):**

$$\int g'\big(u(x)\big) u'(x) \, dx = \int g'(u) \, du = g\big(u(x)\big) + C$$

---

### Problem Statement

**Problem 4. Substitution as Reversing the Chain Rule**

Compute

$$\int 2x (x^2 + 1)^4 \, dx.$$

Before calculating, identify a candidate for the new variable $u$ and show that its derivative appears in the integral. Finally, verify the result by differentiation.

> **Why this problem:** it teaches how to recognize substitution as reversing the chain rule.

---

### Solution

**Step 1: Identify the substitution candidate $u$ and check for $du$**

Look at the composite factor $(x^2 + 1)^4$. Choose the inner expression as the new variable:

$$u = x^2 + 1$$

Compute its differential $du$:

$$\frac{du}{dx} = 2x \implies du = 2x \, dx$$

The exact factor $2x \, dx$ appears multiplying $(x^2 + 1)^4$ inside the integral $\int (x^2 + 1)^4 \cdot (2x \, dx)$.

**Step 2: Rewrite in terms of $u$, integrate, and substitute back**

Replace $x^2 + 1$ with $u$ and $2x \, dx$ with $du$:

$$\begin{aligned} \int 2x (x^2 + 1)^4 \, dx &= \int u^4 \, du \\ &= \frac{u^5}{5} + C \\ &= \frac{(x^2 + 1)^5}{5} + C \end{aligned}$$

**Step 3: Verify the result by differentiation**

Differentiate $F(x) = \frac{1}{5}(x^2 + 1)^5 + C$ using the chain rule:

$$\begin{aligned} F'(x) &= \frac{1}{5} \cdot 5(x^2 + 1)^4 \cdot \frac{d}{dx}(x^2 + 1) + 0 \\ &= (x^2 + 1)^4 \cdot 2x \\ &= 2x (x^2 + 1)^4 \end{aligned}$$

The derivative matches the integrand, confirming that substitution reverses the chain rule.

---

### Final Answer

1. **Substitution:** $u = x^2 + 1$ with $du = 2x \, dx$.
2. **Indefinite integral:**
   $$\int 2x (x^2 + 1)^4 \, dx = \frac{(x^2 + 1)^5}{5} + C$$
