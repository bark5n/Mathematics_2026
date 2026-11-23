### Essential Formulas

**Derivative of a Parameterized Cubic Polynomial:**

$$
f_a(x) = x^3 - 3ax \implies f'_a(x) = 3x^2 - 3a = 3(x^2 - a)
$$

**Second Derivative for Classifying Stationary Points:**

$$
f''_a(x) = 6x
$$

---

### Problem Statement

**Problem 11. A Parameter and the Number of Extrema**

For

$$
f_a(x) = x^3 - 3ax
$$

depending on $a$, determine the number of critical points and their character. Separate the parameter cases and justify why the structure of the graph changes.

> **Why this problem:** it teaches how to analyze an entire family of functions instead of a single example.

---

### Solution

**Step 1: Compute the derivative and set up the critical-point equation**

Differentiate $f_a(x) = x^3 - 3ax$ with respect to $x$ (treating $a \in \mathbb{R}$ as a fixed parameter):

$$
f'_a(x) = 3x^2 - 3a = 3(x^2 - a)
$$

Critical points satisfy $f'_a(x) = 0 \iff x^2 = a$. The number of real solutions to $x^2 = a$ splits naturally into three cases depending on the sign of $a$.

**Step 2: Analyze the three parameter cases**

**Case 1: $a < 0$**
* **Number of critical points:** $0$. Since $x^2 \ge 0$ for all $x \in \mathbb{R}$ and $a < 0$, the equation $x^2 = a$ has no real solutions.
* **Monotonicity and extrema:** Because $x^2 - a > 0$ for every $x \in \mathbb{R}$, we have $f'_a(x) = 3(x^2 - a) > 0$ everywhere. Thus $f_a$ is **strictly increasing on all of $\mathbb{R}$** and has **no local extrema** (only an inflection point at $(0, 0)$ where $f''_a(0) = 0$).

**Case 2: $a = 0$**
* **Number of critical points:** $1$. Here $f_0(x) = x^3$ and $f'_0(x) = 3x^2 = 0 \implies x = 0$.
* **Character of the critical point:** Since $f'_0(x) = 3x^2 > 0$ for all $x \neq 0$, the derivative does not change sign across $x = 0$ (positive on both $(-\infty, 0)$ and $(0, +\infty)$). Thus $f_0$ is still **strictly increasing on all of $\mathbb{R}$**, and $(0, 0)$ is a **stationary horizontal inflection point**, **not** a local extremum.

**Case 3: $a > 0$**
* **Number of critical points:** $2$. Solving $x^2 = a$ yields two distinct critical points:
  $$
  x_1 = -\sqrt{a}, \qquad x_2 = \sqrt{a}
  $$
* **Character of the critical points:** Factor $f'_a(x) = 3(x - \sqrt{a})(x + \sqrt{a})$:
  * On $(-\infty, -\sqrt{a})$: $f'_a(x) > 0$ (increasing).
  * On $(-\sqrt{a}, \sqrt{a})$: $f'_a(x) < 0$ (decreasing).
  * On $(\sqrt{a}, +\infty)$: $f'_a(x) > 0$ (increasing).
  Evaluating $f_a$ (or using $f''_a(\pm \sqrt{a}) = \pm 6\sqrt{a}$):
  * At $x_1 = -\sqrt{a}$: $f_a(-\sqrt{a}) = (-\sqrt{a})^3 - 3a(-\sqrt{a}) = 2a\sqrt{a}$, giving a **local maximum** at $\big(-\sqrt{a}, \, 2a\sqrt{a}\big)$.
  * At $x_2 = \sqrt{a}$: $f_a(\sqrt{a}) = (\sqrt{a})^3 - 3a(\sqrt{a}) = -2a\sqrt{a}$, giving a **local minimum** at $\big(\sqrt{a}, \, -2a\sqrt{a}\big)$.

**Step 3: Justify why the structure of the graph changes**

The function $f_a(x) = x^3 - 3ax$ is the sum of the monotonic cubic $x^3$ (slope $3x^2 \ge 0$) and the linear term $-3ax$ (constant slope $-3a$):
* When $a < 0$, $-3ax$ adds a strictly positive slope $-3a > 0$, reinforcing the upward climb of $x^3$ so the graph rises everywhere without ever flattening out.
* At the threshold $a = 0$, the linear term disappears, leaving $x^3$ with a single momentary horizontal tangent at $(0, 0)$.
* When $a > 0$, $-3ax$ introduces a negative slope $-3a < 0$ near the origin where $3x^2 < 3a$, pulling the middle section downward into a wave with a peak at $-\sqrt{a}$ and a valley at $+\sqrt{a}$ before $3x^2$ dominates again for $|x| > \sqrt{a}$.

---

### Final Answer

1. **$a < 0$:** **$0$ critical points** and **$0$ extrema** ($f_a$ is strictly increasing on $\mathbb{R}$).
2. **$a = 0$:** **$1$ critical point** at $x = 0$, which is a **horizontal inflection point** (not an extremum; $f_0$ is strictly increasing on $\mathbb{R}$).
3. **$a > 0$:** **$2$ critical points** at $x = \pm \sqrt{a}$: a **local maximum** at $\big(-\sqrt{a}, \, 2a\sqrt{a}\big)$ and a **local minimum** at $\big(\sqrt{a}, \, -2a\sqrt{a}\big)$.
