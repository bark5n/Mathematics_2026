### Essential Formulas

**Definition of Absolute Value:**

$$\vert{}u\vert{} = \begin{cases} u, & u \ge 0, \\ -u, & u < 0. \end{cases}$$

**Non-Differentiability at a Corner:**
A continuous function $f$ fails to be differentiable at $x_0$ if its left-hand and right-hand derivatives disagree:

$$f'_-(x_0) \neq f'_+(x_0)$$

---

### Problem Statement

**Problem 12. A Function with an Absolute Value**

Analyze

$$f(x) = \vert{}x^2 - 4\vert{}.$$

First sketch $x^2 - 4$, then explain the effect of the absolute value. Indicate the points where the derivative does not exist and justify the reason geometrically.

> **Why this problem:** it shows the limits of mechanical application of calculus and the importance of the geometry of the graph.

---

### Solution

**Step 1: Analyze and sketch the inner parabola $g(x) = x^2 - 4$**

The function $g(x) = x^2 - 4$ is an upward-opening parabola with:
* **Vertex (global minimum):** $(0, -4)$
* **Zeros ($x$-intercepts):** $x^2 - 4 = 0 \implies x = -2$ and $x = 2$, giving $(-2, 0)$ and $(2, 0)$
* **Sign:** $g(x) > 0$ on $(-\infty, -2) \cup (2, +\infty)$, and $g(x) < 0$ on $(-2, 2)$.

```text
  (a) Inner Parabola: g(x) = x^2 - 4

                      y ^
                        |
          (-2, 0)       |       (2, 0)
  -----------*----------+----------*-----------> x
              \         |         /
               '.       |       .'
                 ' .    |    . '
                    ' . | . '
                        * (0, -4) Vertex
```

**Step 2: Explain the effect of the absolute value and write $f(x)$ piecewise**

Applying the absolute value leaves all non-negative portions of $g(x)$ unchanged ($\vert{}x^2 - 4\vert{} = x^2 - 4$ where $\vert{}x\vert{} \ge 2$) and **reflects the negative portion below the $x$-axis upward across the $x$-axis** ($\vert{}x^2 - 4\vert{} = -(x^2 - 4) = 4 - x^2$ for $-2 < x < 2$). The vertex $(0, -4)$ reflects to a local maximum at $(0, 4)$, while $(-2, 0)$ and $(2, 0)$ become global minima of value $0$:

$$f(x) = \vert{}x^2 - 4\vert{} = \begin{cases} x^2 - 4, & x \le -2, \\ 4 - x^2, & -2 < x < 2, \\ x^2 - 4, & x \ge 2. \end{cases}$$

```text
  (b) Reflected Graph: f(x) = |x^2 - 4|

                      y ^
                        * (0, 4) Local Max (reflected vertex)
                    . ' | ' .
                 . '    |    ' .
               .'       |       '.
              /         |         \
  -----------*----------+----------*-----------> x
          (-2, 0)       |       (2, 0)
       (Sharp Corner)   |    (Sharp Corner)
```

**Step 3: Analyze monotonicity, extrema, and differentiability**

Differentiating each smooth piece on the open intervals:

$$
f'(x) =
\begin{cases}
2x, & x < -2, \\
-2x, & -2 < x < 2, \\
2x, & x > 2.
\end{cases}
$$

* **Monotonicity:** Strictly decreasing on $(-\infty, -2)$ and $(0, 2)$; strictly increasing on $(-2, 0)$ and $(2, +\infty)$.
* **Extrema:** Global minima at $(-2, 0)$ and $(2, 0)$ (value $0$); local maximum at $(0, 4)$.

**Step 4: Indicate the points of non-differentiability and justify geometrically**

The derivative $f'(x)$ **does not exist at $x = -2$ and $x = 2$**:
* **At $x = -2$:**
  $$
  f'_-(-2) = \lim_{x \to -2^-} (2x) = -4, \qquad f'_+(-2) = \lim_{x \to -2^+} (-2x) = +4
  $$
* **At $x = 2$:**
  $$
  f'_-(2) = \lim_{x \to 2^-} (-2x) = -4, \qquad f'_+(2) = \lim_{x \to 2^+} (2x) = +4
  $$

**Geometric justification:** Because the parabola crosses the $x$-axis at $x = \pm 2$ with nonzero slopes ($\pm 4$), reflecting the negative arc upward creates **sharp corners (kinks)** at $(-2, 0)$ and $(2, 0)$. Approaching $x = 2$ from the left, the tangent line has slope $-4$ (pointing steeply downward), whereas approaching from the right, the tangent line has slope $+4$ (pointing steeply upward). Since there is no unique tangent line at a sharp corner, $f$ is not differentiable at $x = -2$ and $x = 2$.

---

### Final Answer

1. **Effect of absolute value:** Keeps $x^2 - 4$ unchanged for $|x| \ge 2$ and reflects the negative middle arc ($-2 < x < 2$) upward across the $x$-axis to $4 - x^2$, turning $(0, -4)$ into a local maximum $(0, 4)$.
2. **Points where $f'(x)$ does not exist:** $x = -2$ and $x = 2$.
3. **Geometric reason:** Reflection produces sharp corners at $(-2, 0)$ and $(2, 0)$ where the one-sided tangent slopes jump abruptly between $-4$ and $+4$, so no unique tangent line exists.
