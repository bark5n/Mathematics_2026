### Essential Formulas

**Power Rule for Differentiation:**
For any real exponent $n$:

$$
\frac{d}{dx}\left(x^n\right) = n x^{n-1}
$$

**Linearity of Differentiation:**

$$
\frac{d}{dx}\big(a f(x) + b g(x)\big) = a f'(x) + b g'(x), \qquad \frac{d}{dx}(c) = 0
$$

---

### Problem Statement

**Problem 1. Derivative of a Polynomial and the Slope of a Tangent Line**

For

$$
f(x) = 3x^5 - 2x^3 + 7x - 4
$$

find $f'(x)$. Then compute $f'(0)$ and $f'(1)$, determine the signs of the obtained values, and explain what they say about the slope of the tangent line to the graph at these two points.

> **Why this problem:** it reinforces the power rule and connects the value of the derivative at a point with the geometric meaning of the tangent slope.

---

### Solution

**Step 1: Differentiate $f(x)$ term by term using the power rule and linearity**

Apply the power rule $\frac{d}{dx}(x^n) = n x^{n-1}$ to each term:

$$
\begin{aligned}
f'(x) &= 3 \cdot (5x^4) - 2 \cdot (3x^2) + 7 \cdot (1) - 0 \\
      &= 15x^4 - 6x^2 + 7
\end{aligned}
$$

**Step 2: Evaluate $f'(0)$ and $f'(1)$**

* **At $x = 0$:**
  $$
  f'(0) = 15(0)^4 - 6(0)^2 + 7 = 7
  $$

* **At $x = 1$:**
  $$
  f'(1) = 15(1)^4 - 6(1)^2 + 7 = 15 - 6 + 7 = 16
  $$

**Step 3: Determine the signs and interpret the tangent slopes geometrically**

* **At $x = 0$:** $f'(0) = 7 > 0$ (**positive**). Geometrically, the tangent line to the graph $y = f(x)$ at $(0, -4)$ has a positive slope of $7$, meaning the tangent line rises upward from left to right and the function is locally increasing at $x = 0$.
* **At $x = 1$:** $f'(1) = 16 > 0$ (**positive**). Geometrically, the tangent line to the graph $y = f(x)$ at $(1, 4)$ has an even steeper positive slope of $16$ ($16 > 7$), meaning the graph rises more steeply at $x = 1$ than at $x = 0$.

---

### Final Answer

1. **Derivative:** $f'(x) = 15x^4 - 6x^2 + 7$.
2. **Values and signs:** $f'(0) = 7 > 0$ (positive) and $f'(1) = 16 > 0$ (positive).
3. **Geometric interpretation:** Both tangent lines slope upward from left to right, with the tangent line at $x = 1$ (slope $16$) being steeper than the tangent line at $x = 0$ (slope $7$).
