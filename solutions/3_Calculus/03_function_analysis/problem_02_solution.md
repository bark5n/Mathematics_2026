### Essential Formulas

**Stationary Point Condition for Differentiable Functions:**
If $f$ is differentiable and has a local minimum at $x_0$, then:

$$
f'(x_0) = 0
$$

**Vertex Form of a Quadratic Function:**

$$
f(x) = a(x - h)^2 + k
$$

For $a > 0$, the global minimum occurs at the vertex $(h, k)$.

---

### Problem Statement

**Problem 2. A Parabola from the Perspective of the Derivative**

For $f(x) = x^2 - 4x + 1$, find the minimum using the derivative. Compare the result with the vertex form and explain why both approaches lead to the same point.

> **Why this problem:** it connects a new tool with the familiar geometry of a parabola.

---

### Solution

**Step 1: Find the minimum using the derivative**

Differentiate $f(x) = x^2 - 4x + 1$:

$$
f'(x) = 2x - 4
$$

Set $f'(x) = 0$:

$$
2x - 4 = 0 \implies x = 2
$$

Check the sign of $f'(x) = 2(x - 2)$:
* For $x < 2$: $f'(x) < 0$ ($f$ is strictly decreasing).
* For $x > 2$: $f'(x) > 0$ ($f$ is strictly increasing).

Therefore, $f$ attains its **global minimum** at $x = 2$ with value:

$$
f(2) = 2^2 - 4(2) + 1 = 4 - 8 + 1 = -3
$$

The minimum point is $(2, -3)$.

**Step 2: Find the minimum using the vertex form**

Complete the square in $f(x) = x^2 - 4x + 1$:

$$
f(x) = (x^2 - 4x + 4) - 4 + 1 = (x - 2)^2 - 3
$$

Because $(x - 2)^2 \ge 0$ for all $x \in \mathbb{R}$ with equality if and only if $x = 2$, we have $f(x) \ge -3$ for all $x$, and the vertex (minimum point) is $(2, -3)$.

**Step 3: Explain why both approaches lead to the same point**

Both methods characterize the unique turning point of an upward-opening parabola ($a = 1 > 0$) from complementary viewpoints:
* **Geometric / Algebraic viewpoint (vertex form):** Writing $f(x) = (x - 2)^2 - 3$ expresses the parabola as a symmetric shift of $y = x^2$ to the vertex $(2, -3)$, which is the lowest point on the curve.
* **Calculus viewpoint (derivative):** At the lowest point of a smooth curve, the tangent line must be horizontal (slope $0$), because the curve transitions from descending ($f'(x) < 0$) to ascending ($f'(x) > 0$). Differentiating $(x - h)^2 + k$ gives $2(x - h) = 0 \iff x = h$, so setting $f'(x) = 0$ algebraically isolates the exact vertex coordinate $x = 2$.

---

### Final Answer

1. **Minimum via derivative:** Global minimum value $f(2) = -3$ at the point $(2, -3)$.
2. **Vertex form:** $f(x) = (x - 2)^2 - 3$, giving the exact same vertex $(2, -3)$.
3. **Why they agree:** At the vertex of a smooth upward-opening parabola, the tangent line is horizontal ($f'(x) = 0$), so solving $2(x - 2) = 0$ locates the same symmetry center as completing the square.
