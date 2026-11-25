### Essential Formulas

**Power Rewrite Rules:**

$$
\sqrt{x} = x^{1/2} \quad (x \ge 0), \qquad \frac{1}{x^2} = x^{-2} \quad (x \neq 0)
$$

**Power Rule for Integration:**

$$
\int x^r \, dx = \frac{x^{r+1}}{r+1} + C \qquad (r \neq -1)
$$

---

### Problem Statement

**Problem 2. Powers, Roots, and the Domain**

Compute

$$
\int \left(2\sqrt{x} + \frac{3}{x^2} - x^{1/3}\right) \, dx.
$$

First rewrite the terms as powers, determine the domain of the original expression, and verify the result by differentiation.

> **Why this problem:** it reinforces the power rule and reminds the student to keep track of the domain.

---

### Solution

**Step 1: Rewrite the terms as powers**

Express the square root and reciprocal power using fractional and negative exponents:

$$
2\sqrt{x} + \frac{3}{x^2} - x^{1/3} = 2x^{1/2} + 3x^{-2} - x^{1/3}
$$

**Step 2: Determine the domain of the original integrand**

Check the domain of each term:
* $2\sqrt{x}$ requires $x \ge 0$.
* $\frac{3}{x^2}$ requires $x \neq 0$.
* $-x^{1/3} = -\sqrt[3]{x}$ is defined for all $x \in \mathbb{R}$.

Intersecting all three conditions gives the domain of the integrand:

$$
D = (0, +\infty)
$$

**Step 3: Compute the indefinite integral on $(0, +\infty)$**

Apply the power rule $\int x^r \, dx = \frac{x^{r+1}}{r+1}$ to each term:

$$
\begin{aligned}
\int \left(2x^{1/2} + 3x^{-2} - x^{1/3}\right) \, dx
&= 2 \cdot \frac{x^{\frac{1}{2} + 1}}{\frac{1}{2} + 1} + 3 \cdot \frac{x^{-2 + 1}}{-2 + 1} - \frac{x^{\frac{1}{3} + 1}}{\frac{1}{3} + 1} + C \\
&= 2 \cdot \frac{x^{3/2}}{3/2} + 3 \cdot \frac{x^{-1}}{-1} - \frac{x^{4/3}}{4/3} + C \\
&= \frac{4}{3} x^{3/2} - \frac{3}{x} - \frac{3}{4} x^{4/3} + C
\end{aligned}
$$

**Step 4: Verify the result by differentiation**

Differentiate $F(x) = \frac{4}{3} x^{3/2} - 3x^{-1} - \frac{3}{4} x^{4/3} + C$ for $x > 0$:

$$
\begin{aligned}
F'(x) &= \frac{4}{3} \cdot \frac{3}{2} x^{1/2} - 3(-1) x^{-2} - \frac{3}{4} \cdot \frac{4}{3} x^{1/3} + 0 \\
      &= 2x^{1/2} + 3x^{-2} - x^{1/3} \\
      &= 2\sqrt{x} + \frac{3}{x^2} - x^{1/3}
\end{aligned}
$$

The derivative reproduces the original integrand on $(0, +\infty)$.

---

### Final Answer

1. **Power form:** $2x^{1/2} + 3x^{-2} - x^{1/3}$.
2. **Domain:** $D = (0, +\infty)$.
3. **Indefinite integral:**
   $$
   \int \left(2\sqrt{x} + \frac{3}{x^2} - x^{1/3}\right) \, dx = \frac{4}{3} x^{3/2} - \frac{3}{x} - \frac{3}{4} x^{4/3} + C \qquad (x > 0)
   $$
