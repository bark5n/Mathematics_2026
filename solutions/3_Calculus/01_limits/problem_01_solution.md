### Essential Formulas

**Limit of a Rational Sequence at Infinity:**
For a quotient of two polynomials of equal degree $k$:

$$
\lim_{n \to \infty} \frac{a_k n^k + a_{k-1} n^{k-1} + \dots + a_0}{b_k n^k + b_{k-1} n^{k-1} + \dots + b_0} = \frac{a_k}{b_k} \qquad (b_k \neq 0)
$$

**Basic Reciprocal Sequence Limit:**

$$
\lim_{n \to \infty} \frac{1}{n^p} = 0 \qquad (p > 0)
$$

---

### Problem Statement

**Exercise 1. Dominant Terms in a Sequence**

Compute

$$
\lim_{n \to \infty} \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}.
$$

Explain why the highest-degree terms determine the result.

> **Why this exercise:** introduces the idea of a dominant term and teaches how to simplify the behavior of expressions for large arguments.

---

### Solution

**Step 1: Factor out the highest-degree power $n^2$ from numerator and denominator**

Divide both the numerator and the denominator by the highest power of $n$ appearing in the expression, which is $n^2$:

$$
\begin{aligned}
\lim_{n \to \infty} \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}
&= \lim_{n \to \infty} \frac{n^2 \left(4 - \frac{3}{n} + \frac{1}{n^2}\right)}{n^2 \left(2 + \frac{5}{n} - \frac{7}{n^2}\right)} \\
&= \lim_{n \to \infty} \frac{4 - \frac{3}{n} + \frac{1}{n^2}}{2 + \frac{5}{n} - \frac{7}{n^2}}
\end{aligned}
$$

**Step 2: Evaluate the limit using standard null sequences**

As $n \to \infty$, all terms with positive powers of $n$ in the denominator vanish:

$$
\lim_{n \to \infty} \frac{3}{n} = 0, \qquad \lim_{n \to \infty} \frac{1}{n^2} = 0, \qquad \lim_{n \to \infty} \frac{5}{n} = 0, \qquad \lim_{n \to \infty} \frac{7}{n^2} = 0
$$

Applying the quotient rule for limits gives:

$$
\frac{4 - 0 + 0}{2 + 0 - 0} = \frac{4}{2} = 2
$$

**Step 3: Explain why the highest-degree terms determine the result**

As $n$ becomes very large, $n^2$ grows vastly faster than lower-degree terms such as $n$ and $1$. Relative to $n^2$, the ratios $\frac{n}{n^2} = \frac{1}{n}$ and $\frac{1}{n^2}$ shrink arbitrarily close to zero. Consequently, the lower-degree terms contribute negligibly to the overall value for large $n$, leaving only the ratio of the leading coefficients $\frac{4}{2} = 2$.

---

### Final Answer

1. **Limit value:** $2$.
2. **Dominance explanation:** Dividing by $n^2$ turns all lower-degree terms into multiples of $\frac{1}{n}$ and $\frac{1}{n^2}$, which tend to $0$ as $n \to \infty$, so only the leading coefficients $4$ and $2$ determine the limit.
