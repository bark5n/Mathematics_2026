### Essential Formulas

**Exponent Rewrite Identities:**

$$
\sqrt{x} = x^{1/2} \quad (x \ge 0), \qquad \frac{1}{x^k} = x^{-k} \quad (x \neq 0)
$$

**Power Rule for Real Exponents:**

$$
\frac{d}{dx}\left(x^r\right) = r x^{r-1}
$$

---

### Problem Statement

**Problem 2. Powers, Roots, and the Domain**

For

$$
f(x) = 2\sqrt{x} - \frac{3}{x^2} + x^{3/2}
$$

1. rewrite the function using powers,
2. determine the domain,
3. compute the derivative,
4. compare the domain of the function with the domain of its derivative.

> **Why this problem:** it teaches how to rewrite different forms so that the power rule can be applied and how to keep track of the domain.

---

### Solution

**1. Rewrite the function using powers**

Convert $\sqrt{x}$ to $x^{1/2}$ and $\frac{3}{x^2}$ to $3x^{-2}$:

$$
f(x) = 2x^{1/2} - 3x^{-2} + x^{3/2}
$$

**2. Determine the domain of $f$**

Inspect the domain restrictions of each term in the original expression:
* $2\sqrt{x}$ and $x^{3/2} = (\sqrt{x})^3$ require $x \ge 0$ for real outputs.
* $-\frac{3}{x^2}$ requires $x \neq 0$ to avoid division by zero.

Combining $x \ge 0$ and $x \neq 0$ yields the domain of $f$:

$$
D_f = (0, +\infty)
$$

**3. Compute the derivative $f'(x)$**

Apply the power rule $\frac{d}{dx}(x^r) = r x^{r-1}$ to each power term for $x > 0$:

$$
\begin{aligned}
f'(x) &= 2 \cdot \frac{1}{2} x^{\frac{1}{2} - 1} - 3 \cdot (-2) x^{-2 - 1} + \frac{3}{2} x^{\frac{3}{2} - 1} \\
      &= x^{-1/2} + 6x^{-3} + \frac{3}{2} x^{1/2} \\
      &= \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}
\end{aligned}
$$

**4. Compare the domain of $f$ with the domain of $f'$**

In $f'(x) = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}$:
* The terms $\frac{1}{\sqrt{x}}$ and $\frac{3}{2}\sqrt{x}$ require $x > 0$ (since $\sqrt{x}$ is now in the denominator, $x = 0$ is doubly excluded).
* The term $\frac{6}{x^3}$ requires $x \neq 0$.

Thus, the domain of $f'$ is:

$$
D_{f'} = (0, +\infty)
$$

**Comparison:** Here $D_{f'} = D_f = (0, +\infty)$, so the domain of the derivative coincides with the domain of the original function (note that even if the $-\frac{3}{x^2}$ term were absent, $x = 0$ would still be lost upon differentiating $\sqrt{x}$ because $\frac{1}{\sqrt{x}}$ is undefined at $x = 0$).

---

### Final Answer

1. **Power form:** $f(x) = 2x^{1/2} - 3x^{-2} + x^{3/2}$.
2. **Domain of $f$:** $D_f = (0, +\infty)$.
3. **Derivative:** $f'(x) = x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2} = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}$.
4. **Domain comparison:** $D_{f'} = (0, +\infty) = D_f$; both domains are identical because $x = 0$ was already excluded by the $\frac{3}{x^2}$ term.
