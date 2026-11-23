### Essential Formulas

**Domain and Derivative of the Natural Logarithm:**

$$
\ln x \quad \mathrm{is\ defined\ for\ } x > 0, \qquad \frac{d}{dx}(\ln x) = \frac{1}{x} \quad (x > 0)
$$

---

### Problem Statement

**Problem 6. A Logarithmic Function**

Analyze the domain, zero, and monotonicity of

$$
f(x) = \ln x - x + 1.
$$

Explain why the analysis must begin with the domain.

> **Why this problem:** it reinforces the role of the domain and derivative in the analysis of a logarithmic function.

---

### Solution

**Step 1: Determine the domain**

The term $\ln x$ is defined only for strictly positive real numbers, while $-x + 1$ is defined for all $x \in \mathbb{R}$. Intersecting both requirements gives the domain:

$$
D_f = (0, +\infty)
$$

**Step 2: Compute the derivative and analyze monotonicity on $D_f$**

Differentiate $f(x) = \ln x - x + 1$ for $x \in (0, +\infty)$:

$$
f'(x) = \frac{1}{x} - 1 = \frac{1 - x}{x}
$$

Find the critical point in $(0, +\infty)$ by setting $f'(x) = 0$:

$$
\frac{1 - x}{x} = 0 \implies 1 - x = 0 \implies x = 1 \in (0, +\infty)
$$

Since $x > 0$ on the entire domain $D_f$, the sign of $f'(x) = \frac{1 - x}{x}$ depends solely on $1 - x$:
* **On $(0, 1)$:** $1 - x > 0 \implies f'(x) > 0$, so $f$ is **strictly increasing**.
* **On $(1, +\infty)$:** $1 - x < 0 \implies f'(x) < 0$, so $f$ is **strictly decreasing**.

Consequently, $f$ attains its **unique global maximum** on $(0, +\infty)$ at $x = 1$:

$$
f(1) = \ln(1) - 1 + 1 = 0 - 1 + 1 = 0
$$

**Step 3: Find the zeros of $f(x)$**

From Step 2:
* At $x = 1$, $f(1) = 0$, so $x = 1$ is a zero.
* Because $f$ is strictly increasing on $(0, 1)$ up to $f(1) = 0$, $f(x) < 0$ for all $x \in (0, 1)$.
* Because $f$ is strictly decreasing on $(1, +\infty)$ down from $f(1) = 0$, $f(x) < 0$ for all $x \in (1, +\infty)$.

Thus $x = 1$ is the **unique zero** of $f(x)$ (and the graph satisfies $\ln x \le x - 1$ for all $x > 0$, touching the $x$-axis only at $(1, 0)$).

**Step 4: Explain why the analysis must begin with the domain**

1. **Restricting algebraic solutions:** Solving $f'(x) = \frac{1 - x}{x} = 0$ or analyzing the sign of $\frac{1 - x}{x}$ without first fixing $D_f = (0, +\infty)$ would falsely include the interval $(-\infty, 0)$, where $\ln x$ does not exist as a real function.
2. **Preventing false sign changes:** At $x = 0$, the algebraic rational expression $\frac{1 - x}{x}$ changes sign, which could be misinterpreted as a boundary or extremum if one forgot that $x = 0$ is already an endpoint outside the domain $(0, +\infty)$. Every subsequent calculus step—limits, derivatives, sign charts, and zeros—is meaningful only inside $D_f$.

---

### Final Answer

1. **Domain:** $D_f = (0, +\infty)$.
2. **Zero:** Unique zero at $x = 1$ ($f(1) = 0$).
3. **Monotonicity:** Strictly increasing on $(0, 1)$ and strictly decreasing on $(1, +\infty)$, with a global maximum at $(1, 0)$.
4. **Why begin with the domain:** All algebraic expressions for $f'(x)$ and its sign analysis are valid only where $\ln x$ is defined ($x > 0$), preventing meaningless conclusions on $(-\infty, 0]$.
