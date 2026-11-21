### Essential Formulas

**Extracting a Dominant Exponential Term:**
For $a > b > 0$:

$$
\sqrt[n]{a^n + b^n} = a \sqrt[n]{1 + \left(\frac{b}{a}\right)^n}
$$

**Limit of an $n$-th Root of a Bounded Quantity:**
For any constant $c > 0$:

$$
\lim_{n \to \infty} \sqrt[n]{c} = 1
$$

---

### Problem Statement

**Exercise 11. An n-th Root**

Compute

$$
\lim_{n \to \infty} \sqrt[n]{5^n + 2^n}.
$$

Explain which term dominates and why the transformation looks different from the case of a quotient of polynomials.

> **Why this exercise:** extends the idea of dominance to exponential expressions.

---

### Solution

**Step 1: Factor out the dominant exponential term $5^n$**

Inside the $n$-th root, compare $5^n$ and $2^n$. Since $5 > 2 > 0$, $5^n$ grows exponentially faster than $2^n$. Factor $5^n$ out of the sum:

$$
\sqrt[n]{5^n + 2^n} = \sqrt[n]{5^n \left(1 + \left(\frac{2}{5}\right)^n\right)} = 5 \sqrt[n]{1 + \left(\frac{2}{5}\right)^n}
$$

**Step 2: Apply the Squeeze Theorem (or root continuity) to evaluate the limit**

Since $0 < \frac{2}{5} < 1$, we have $0 < \left(\frac{2}{5}\right)^n < 1$ for all $n \ge 1$. Therefore:

$$
1 < 1 + \left(\frac{2}{5}\right)^n < 2
$$

Taking the positive $n$-th root preserves the inequalities:

$$
1 < \sqrt[n]{1 + \left(\frac{2}{5}\right)^n} < \sqrt[n]{2}
$$

Because $\lim_{n \to \infty} 1 = 1$ and $\lim_{n \to \infty} \sqrt[n]{2} = 1$, the Squeeze Theorem implies:

$$
\lim_{n \to \infty} \sqrt[n]{1 + \left(\frac{2}{5}\right)^n} = 1
$$

Multiplying by $5$ yields:

$$
\lim_{n \to \infty} \sqrt[n]{5^n + 2^n} = 5 \cdot 1 = 5
$$

**Step 3: Explain term dominance and contrast with polynomial quotients**

* **Dominant term:** $5^n$ dominates because the ratio $\frac{2^n}{5^n} = \left(\frac{2}{5}\right)^n \to 0$ exponentially fast as $n \to \infty$, making $2^n$ negligible compared to $5^n$.
* **Why the transformation differs from polynomial quotients:** In a quotient of polynomials (such as Exercise 1), we divide numerator and denominator by the highest power $n^k$ to cancel unbounded growth between top and bottom. Here, there is no denominator—instead, the expression is wrapped inside an $n$-th root $\left(\cdot\right)^{1/n}$. Factoring out $5^n$ *inside* the radical allows $\sqrt[n]{5^n} = 5$ to exit the root cleanly as a constant while compressing the remaining factor $\sqrt[n]{1 + (2/5)^n}$ to $1$.

---

### Final Answer

1. **Limit value:** $5$.
2. **Dominance and transformation:** $5^n$ dominates $2^n$ because $\left(\frac{2}{5}\right)^n \to 0$; factoring $5^n$ out of the $n$-th root pulls $\sqrt[n]{5^n} = 5$ outside the radical rather than canceling a common factor between a numerator and denominator.
