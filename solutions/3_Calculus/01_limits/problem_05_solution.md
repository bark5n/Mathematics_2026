### Essential Formulas

**Definition of Euler's Number $e$:**

$$
\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e \approx 2.718281828459\dots
$$

---

### Problem Statement

**Exercise 5. The Classical Limit Leading to the Number $e$**

Compute

$$
\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n.
$$

Calculate several values for increasing $n$ and compare the observed behavior with the value of the limit. Explain why a few values do not constitute a proof.

> **Why this exercise:** connects a central limit with intuition based on concrete terms of a sequence.

---

### Solution

**Step 1: State the limit**

As $n \to \infty$, the base $1 + \frac{1}{n} \to 1$ while the exponent $n \to \infty$, producing an indeterminate form of type $1^\infty$. By definition of Euler's constant:

$$
\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e \approx 2.71828
$$

**Step 2: Compute sequence values for increasing $n$**

Let $a_n = \left(1 + \frac{1}{n}\right)^n$. Evaluating for several increasing values of $n$:

| $n$ | Formula $\left(1 + \frac{1}{n}\right)^n$ | Approximate Value | Difference $e - a_n$ |
| :--- | :--- | :--- | :--- |
| $1$ | $(1 + 1)^1$ | $2.00000$ | $0.71828$ |
| $2$ | $(1 + 0.5)^2$ | $2.25000$ | $0.46828$ |
| $10$ | $(1 + 0.1)^{10}$ | $2.59374$ | $0.12454$ |
| $100$ | $(1 + 0.01)^{100}$ | $2.70481$ | $0.01347$ |
| $1000$ | $(1 + 0.001)^{1000}$ | $2.71692$ | $0.00136$ |
| $10000$ | $(1 + 0.0001)^{10000}$ | $2.71815$ | $0.00013$ |

**Step 3: Compare numerical observations with the limit**

The computed values increase steadily from $2$ toward $e \approx 2.71828$, remaining strictly below $e$ while the gap $e - a_n$ narrows approximately inversely with $n$.

**Step 4: Explain why a few numerical values do not constitute a proof**

A limit describes the asymptotic behavior of a sequence for **all** sufficiently large $n$ (infinitely many terms beyond any chosen threshold $N$). Evaluating finitely many terms—even up to $n = 10000$—only checks the initial segment of the sequence and cannot rule out divergence, oscillation, or drift to a slightly different value at much larger $n$ (for example, $n = 10^{100}$). A valid proof requires a general deductive argument valid for all $n$, such as proving via the Binomial Theorem that $a_n$ is strictly increasing and bounded above by $3$, hence convergent by the Monotone Convergence Theorem.

---

### Final Answer

1. **Limit value:** $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e \approx 2.71828$.
2. **Numerical comparison:** Terms grow monotonically ($a_1 = 2$, $a_{10} \approx 2.59374$, $a_{100} \approx 2.70481$, $a_{1000} \approx 2.71692$) and approach $e$ from below.
3. **Why finite values are not a proof:** A limit is a statement about infinitely many terms as $n \to \infty$; checking finitely many terms cannot guarantee asymptotic behavior without a general analytical argument.
