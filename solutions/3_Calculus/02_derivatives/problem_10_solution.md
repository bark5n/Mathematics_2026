### Essential Formulas

**Equation of the Tangent Line at $x = x_0$:**
If $f$ is differentiable at $x_0$, the tangent line to $y = f(x)$ at the point $\big(x_0, f(x_0)\big)$ is:

$$
y - f(x_0) = f'(x_0)(x - x_0)
$$

---

### Problem Statement

**Problem 10. The Tangent Line as an Application of the Derivative**

For

$$
f(x) = x^2 - 3x + 1
$$

find the equation of the tangent line at the point with $x = 2$. Give the point of tangency, the value $f'(2)$, the equation of the line, and verify that the point lies on the obtained tangent line.

> **Why this problem:** it combines the derivative and the equation of a line into a complete geometric problem.

---

### Solution

**Step 1: Find the point of tangency at $x = 2$**

Evaluate $f(2)$:

$$
f(2) = 2^2 - 3(2) + 1 = 4 - 6 + 1 = -1
$$

The point of tangency on the parabola is $P = (2, -1)$.

**Step 2: Compute the derivative $f'(x)$ and evaluate $f'(2)$**

Differentiate $f(x) = x^2 - 3x + 1$:

$$
f'(x) = 2x - 3
$$

Substitute $x = 2$ to obtain the slope $m$ of the tangent line:

$$
m = f'(2) = 2(2) - 3 = 4 - 3 = 1
$$

**Step 3: Write the equation of the tangent line**

Use the point-slope formula $y - y_0 = m(x - x_0)$ with $(x_0, y_0) = (2, -1)$ and $m = 1$:

$$
y - (-1) = 1(x - 2)
$$

Simplify to slope-intercept form:

$$
y + 1 = x - 2 \implies y = x - 3
$$

**Step 4: Verify that the point of tangency $(2, -1)$ lies on the tangent line**

Substitute $x = 2$ into the tangent line equation $y = x - 3$:

$$
y = 2 - 3 = -1
$$

Since $y = -1$ matches the $y$-coordinate of $P = (2, -1)$, the point of tangency lies on the line $y = x - 3$.

---

### Final Answer

1. **Point of tangency:** $(2, -1)$.
2. **Derivative at $x = 2$:** $f'(2) = 1$.
3. **Equation of the tangent line:** $y = x - 3$ (or $x - y - 3 = 0$).
4. **Verification:** Substituting $x = 2$ into $y = x - 3$ gives $y = -1$, confirming $(2, -1)$ lies on the line.
