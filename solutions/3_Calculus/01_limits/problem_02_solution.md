### Essential Formulas

**Asymptotic Behavior of Rational Sequences:**
Let $P(n) = a_p n^p + \dots + a_0$ ($a_p \neq 0$) and $Q(n) = b_q n^q + \dots + b_0$ ($b_q \neq 0$) be polynomials of degrees $p$ and $q$:

$$
\lim_{n \to \infty} \frac{P(n)}{Q(n)} =
\begin{cases}
0, & p < q, \\
\frac{a_p}{b_q}, & p = q, \\
\pm \infty, & p > q.
\end{cases}
$$

---

### Problem Statement

**Exercise 2. Different Growth Rates**

Compute

$$
\lim_{n \to \infty} \frac{3n + 1}{n^2 + 4}, \qquad \lim_{n \to \infty} \frac{2n^3 - n}{5n^2 + 1}.
$$

Compare the two cases and formulate a general observation about the degrees of the polynomials in the numerator and denominator.

> **Why this exercise:** teaches how to compare growth rates and recognize qualitatively different cases.

---

### Solution

**Step 1: Compute the first limit ($\lim_{n \to \infty} \frac{3n + 1}{n^2 + 4}$)**

Divide numerator and denominator by $n^2$, the highest power of $n$ in the denominator:

$$
\lim_{n \to \infty} \frac{3n + 1}{n^2 + 4} = \lim_{n \to \infty} \frac{\frac{3}{n} + \frac{1}{n^2}}{1 + \frac{4}{n^2}} = \frac{0 + 0}{1 + 0} = 0
$$

Here, the denominator grows quadratically ($n^2$) while the numerator grows only linearly ($n$), forcing the quotient to $0$.

**Step 2: Compute the second limit ($\lim_{n \to \infty} \frac{2n^3 - n}{5n^2 + 1}$)**

Divide numerator and denominator by $n^2$, the highest power of $n$ in the denominator:

$$
\lim_{n \to \infty} \frac{2n^3 - n}{5n^2 + 1} = \lim_{n \to \infty} \frac{2n - \frac{1}{n}}{5 + \frac{1}{n^2}}
$$

As $n \to \infty$, the numerator $2n - \frac{1}{n} \to +\infty$ while the denominator $5 + \frac{1}{n^2} \to 5 > 0$. Therefore:

$$
\lim_{n \to \infty} \frac{2n^3 - n}{5n^2 + 1} = +\infty
$$

Here, the cubic numerator ($n^3$) outpaces the quadratic denominator ($n^2$) by a factor proportional to $n$, causing unbounded growth.

**Step 3: Formulate a general observation about polynomial degrees**

Comparing the degree $p$ of the numerator polynomial and the degree $q$ of the denominator polynomial yields three distinct regimes as $n \to \infty$:
1. **Denominator dominates ($p < q$):** The denominator grows faster than the numerator, so the limit is always $0$.
2. **Balanced growth ($p = q$):** Numerator and denominator grow at the same rate, so the sequence converges to the finite nonzero ratio of their leading coefficients $\frac{a_p}{b_q}$.
3. **Numerator dominates ($p > q$):** The numerator grows faster than the denominator, so the sequence diverges to $+\infty$ or $-\infty$ (depending on the sign of $\frac{a_p}{b_q}$).

---

### Final Answer

1. **First limit:** $\lim_{n \to \infty} \frac{3n + 1}{n^2 + 4} = 0$.
2. **Second limit:** $\lim_{n \to \infty} \frac{2n^3 - n}{5n^2 + 1} = +\infty$.
3. **General rule:** For polynomial quotients of degrees $p$ (numerator) and $q$ (denominator), the limit is $0$ when $p < q$, finite and nonzero ($\frac{a_p}{b_q}$) when $p = q$, and $\pm \infty$ when $p > q$.
