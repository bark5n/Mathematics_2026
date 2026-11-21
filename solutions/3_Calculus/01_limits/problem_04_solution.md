### Essential Formulas

**Geometric Sequence Behavior:**
For a real base $q$:

$$\lim_{n \to \infty} q^n = \begin{cases} 0, & \vert{}q\vert{} < 1, \\ 1, & q = 1, \\ +\infty, & q > 1, \\ \mathrm{does\ not\ exist}, & q \le -1. \end{cases}$$

**Squeeze Theorem for Sequences:**
If $a_n \le b_n \le c_n$ for all sufficiently large $n$ and $\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = L$, then $\lim_{n \to \infty} b_n = L$.

---

### Problem Statement

**Exercise 4. Powers and Oscillation**

Analyze

$$\left(\frac{2}{3}\right)^n, \qquad \left(\frac{3}{2}\right)^n, \qquad (-1)^n, \qquad \frac{(-1)^n}{n}.$$

For each sequence, describe the type of behavior and justify your answer.

> **Why this exercise:** organizes the basic types of sequence behavior and shows that oscillation does not always rule out convergence.

---

### Solution

**1. Sequence $a_n = \left(\frac{2}{3}\right)^n$**

* **Behavior:** Monotonically decreasing and **convergent to $0$**.
* **Justification:** This is a geometric sequence with base $q = \frac{2}{3}$. Since $0 < \frac{2}{3} < 1$, each multiplication by $\frac{2}{3}$ reduces the term by one third, so $\lim_{n \to \infty} \left(\frac{2}{3}\right)^n = 0$.

**2. Sequence $b_n = \left(\frac{3}{2}\right)^n$**

* **Behavior:** Monotonically increasing and **divergent to $+\infty$**.
* **Justification:** This is a geometric sequence with base $q = \frac{3}{2} = 1.5 > 1$. Writing $\frac{3}{2} = 1 + \frac{1}{2}$ and applying Bernoulli's inequality gives:
  $$\left(1 + \frac{1}{2}\right)^n \ge 1 + \frac{n}{2} \to +\infty \qquad (n \to \infty)$$
  Thus $\lim_{n \to \infty} \left(\frac{3}{2}\right)^n = +\infty$.

**3. Sequence $c_n = (-1)^n$**

* **Behavior:** Bounded and **oscillating (divergent, no limit)**.
* **Justification:** The sequence alternates strictly between two constant values:
  * For even indices $n = 2k$, $c_{2k} = (-1)^{2k} = 1 \to 1$.
  * For odd indices $n = 2k + 1$, $c_{2k+1} = (-1)^{2k+1} = -1 \to -1$.
  Because two subsequences converge to different limits ($1 \neq -1$), the sequence fails to approach a single value and diverges by oscillation.

**4. Sequence $d_n = \frac{(-1)^n}{n}$**

* **Behavior:** Alternating (oscillating in sign) and **convergent to $0$**.
* **Justification:** Although the sign alternates between $+$ and $-$, the amplitude $\frac{1}{n}$ shrinks to zero. For every $n \ge 1$:
  $$-\frac{1}{n} \le \frac{(-1)^n}{n} \le \frac{1}{n}$$
  Since $\lim_{n \to \infty} \left(-\frac{1}{n}\right) = 0$ and $\lim_{n \to \infty} \frac{1}{n} = 0$, the Squeeze Theorem guarantees that $\lim_{n \to \infty} \frac{(-1)^n}{n} = 0$. This shows that oscillation with vanishing amplitude still produces convergence.

---

### Final Answer

1. **$\left(\frac{2}{3}\right)^n$:** Converges monotonically to $0$ ($\vert{}q\vert{} = \frac{2}{3} < 1$).
2. **$\left(\frac{3}{2}\right)^n$:** Diverges monotonically to $+\infty$ ($q = \frac{3}{2} > 1$).
3. **$(-1)^n$:** Diverges by bounded oscillation between $-1$ and $1$ (two distinct subsequence limits).
4. **$\frac{(-1)^n}{n}$:** Oscillates in sign but converges to $0$ by the Squeeze Theorem because $-\frac{1}{n} \le \frac{(-1)^n}{n} \le \frac{1}{n}$.
