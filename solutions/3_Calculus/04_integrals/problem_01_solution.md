### Essential Formulas

**Power Rule for Indefinite Integration:**

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \qquad (n \neq -1)$$

**Linearity of the Indefinite Integral:**

$$\int \big(a f(x) + b g(x)\big) \, dx = a \int f(x) \, dx + b \int g(x) \, dx$$

---

### Problem Statement

**Problem 1. Antiderivative and Verification**

For

$$f(x) = 3x^2 - 4x + 5$$

find one antiderivative $F(x)$. Write the entire family of antiderivatives, verify the result by differentiation, and explain the meaning of the constant $C$.

> **Why this problem:** it introduces integration as the inverse operation to differentiation.

---

### Solution

**Step 1: Find one antiderivative $F(x)$**

Apply the power rule $\int x^n \, dx = \frac{x^{n+1}}{n+1}$ to each term of $f(x) = 3x^2 - 4x + 5$ (choosing the constant of integration to be $0$ for one specific antiderivative):

$$\begin{aligned} F(x) &= 3 \cdot \frac{x^3}{3} - 4 \cdot \frac{x^2}{2} + 5x \\ &= x^3 - 2x^2 + 5x \end{aligned}$$

**Step 2: Write the entire family of antiderivatives**

Adding an arbitrary real constant $C \in \mathbb{R}$ gives the general indefinite integral:

$$\int (3x^2 - 4x + 5) \, dx = x^3 - 2x^2 + 5x + C \qquad (C \in \mathbb{R})$$

**Step 3: Verify the result by differentiation**

Differentiate $F_C(x) = x^3 - 2x^2 + 5x + C$ with respect to $x$:

$$\begin{aligned} \frac{d}{dx}\left(x^3 - 2x^2 + 5x + C\right) &= 3x^2 - 2(2x) + 5 + 0 \\ &= 3x^2 - 4x + 5 \\ &= f(x) \end{aligned}$$

The derivative matches the original integrand $f(x)$ identically.

**Step 4: Explain the meaning of the constant $C$**

* **Algebraic meaning:** Because the derivative of any constant is zero ($\frac{d}{dx}(C) = 0$), differentiation erases additive constants. Consequently, infinitely many functions differ only by an additive constant $C$ yet share the exact same derivative $f(x)$ on $\mathbb{R}$.
* **Geometric meaning:** Changing $C$ shifts the graph $y = x^3 - 2x^2 + 5x + C$ vertically without altering its slope at any $x$-coordinate. Thus, the family of antiderivatives is a vertical family of parallel curves all having tangent slope $3x^2 - 4x + 5$ at every $x$.

---

### Final Answer

1. **One antiderivative:** $F(x) = x^3 - 2x^2 + 5x$.
2. **Entire family:** $\int (3x^2 - 4x + 5) \, dx = x^3 - 2x^2 + 5x + C$ ($C \in \mathbb{R}$).
3. **Meaning of $C$:** Represents an arbitrary vertical shift; since $\frac{d}{dx}(C) = 0$, all vertical shifts of $F(x)$ share the same derivative $f(x)$.
