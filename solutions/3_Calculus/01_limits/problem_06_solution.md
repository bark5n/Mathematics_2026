### Essential Formulas

**Limit of a Rational Function at Infinity:**
For a quotient of polynomials of equal degree $k$:

$$
\lim_{x \to \infty} \frac{a_k x^k + \dots + a_0}{b_k x^k + \dots + b_0} = \frac{a_k}{b_k} \qquad (b_k \neq 0)
$$

**Basic Reciprocal Function Limit:**

$$
\lim_{x \to \infty} \frac{1}{x^p} = 0 \qquad (p > 0)
$$

---

### Problem Statement

**Exercise 6. From a Sequence to a Function — Limit at Infinity**

Compute

$$
\lim_{x \to \infty} \frac{3x^2 - x + 1}{5x^2 + 4x - 2}.
$$

Compare the method with Exercise 1. Explain what changes when moving from $n$ to a real variable $x$, and what stays the same.

> **Why this exercise:** deliberately transfers a technique from sequence limits to function limits.

---

### Solution

**Step 1: Divide numerator and denominator by the highest power $x^2$**

For $x > 0$, factor out $x^2$ from both the numerator and denominator:

$$
\begin{aligned}
\lim_{x \to \infty} \frac{3x^2 - x + 1}{5x^2 + 4x - 2}
&= \lim_{x \to \infty} \frac{x^2 \left(3 - \frac{1}{x} + \frac{1}{x^2}\right)}{x^2 \left(5 + \frac{4}{x} - \frac{2}{x^2}\right)} \\
&= \lim_{x \to \infty} \frac{3 - \frac{1}{x} + \frac{1}{x^2}}{5 + \frac{4}{x} - \frac{2}{x^2}}
\end{aligned}
$$

**Step 2: Evaluate the limit as $x \to \infty$**

Using $\lim_{x \to \infty} \frac{1}{x} = 0$ and $\lim_{x \to \infty} \frac{1}{x^2} = 0$:

$$
\frac{3 - 0 + 0}{5 + 0 - 0} = \frac{3}{5}
$$

**Step 3: Compare with Exercise 1 (what stays the same vs. what changes)**

* **What stays the same:** The algebraic technique is completely identical—factoring out the dominant power ($n^2$ or $x^2$), canceling it, using $\frac{1}{\mathrm{variable}^p} \to 0$, and taking the ratio of the leading coefficients ($\frac{3}{5}$).
* **What changes:**
  1. **Domain of the argument:** In Exercise 1, $n \in \mathbb{N}$ takes only discrete positive integer values ($1, 2, 3, \dots$), whereas here $x \in \mathbb{R}$ varies continuously over all sufficiently large real numbers.
  2. **Direction of infinity:** For sequences, $n \to \infty$ always means $n \to +\infty$. For real functions, $x$ could approach $+\infty$ or $-\infty$ (here $x \to +\infty$, though the same algebraic reduction gives $\frac{3}{5}$ as $x \to -\infty$ as well).

---

### Final Answer

1. **Limit value:** $\frac{3}{5}$.
2. **Comparison:** The algebraic dominant-term reduction is identical to Exercise 1, while the argument domain changes from discrete integers $n \in \mathbb{N}$ to continuous real numbers $x \in \mathbb{R}$.
