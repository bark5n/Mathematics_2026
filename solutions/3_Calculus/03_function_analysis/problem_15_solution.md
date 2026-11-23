### Essential Formulas

**Sign of a Factored Quadratic with Positive Leading Coefficient:**
For $f'(x) = a(x - r_1)(x - r_2)$ with $a > 0$ and $r_1 < r_2$:

$$
f'(x) > 0 \quad \mathrm{for}\ x \in (-\infty, r_1) \cup (r_2, +\infty), \qquad f'(x) < 0 \quad \mathrm{for}\ x \in (r_1, r_2)
$$

---

### Problem Statement

**Problem 15. Find the Error in the Monotonicity Analysis**

For the function

$$
f(x) = x^3 - 3x
$$

the derivative was correctly computed as

$$
f'(x) = 3(x - 1)(x + 1).
$$

However, a student wrote the following conclusion:

> The derivative is positive between its zeros and negative outside them. Therefore, the function is decreasing on $(-\infty, -1) \cup (1, \infty)$, increasing on $(-1, 1)$, has a local minimum at $x = -1$, and a local maximum at $x = 1$.

1. Without differentiating again, explain why merely identifying the zeros of the derivative does not justify the stated sign chart, and find the error in the student's reasoning.
2. Construct the correct sign chart for $f'(x)$.
3. Give the correct intervals of monotonicity and the character of the extrema.
4. In each of the three intervals, choose one simple test point and show that the sign of the derivative confirms your classification.

> **Why this problem:** it teaches how to diagnose an error in a completed argument and shows that a correct derivative formula is not enough if its sign is interpreted incorrectly.

---

### Solution

**1. Diagnosis of the error in the student's reasoning**

* **Why zeros alone do not determine the sign:** The zeros $x = -1$ and $x = 1$ partition $\mathbb{R}$ into three intervals where $f'(x)$ maintains a constant sign, but the zeros alone do not tell us whether $f'(x)$ is positive or negative on each interval—that depends on the **leading coefficient** (here $+3 > 0$, an upward-opening parabola) and the signs of the individual factors $(x - 1)$ and $(x + 1)$.
* **The student's error:** The student **inverted the sign of the quadratic $f'(x) = 3(x - 1)(x + 1)$**. Because the leading coefficient is positive ($3 > 0$), the parabola $y = 3(x^2 - 1)$ opens *upward*, meaning it lies *below* the $x$-axis ($f'(x) < 0$) between its roots $(-1, 1)$ and *above* the $x$-axis ($f'(x) > 0$) outside its roots $(-\infty, -1) \cup (1, +\infty)$. The student mistakenly applied the sign pattern of a downward-opening parabola ($a < 0$), reversing every monotonicity interval and swapping the local maximum and local minimum.

**2. Correct sign chart for $f'(x) = 3(x - 1)(x + 1)$**

| Interval | Sign of $3$ | Sign of $(x + 1)$ | Sign of $(x - 1)$ | Sign of $f'(x)$ | Behavior of $f(x)$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $(-\infty, -1)$ | $+$ | $-$ | $-$ | $+$ | Strictly increasing |
| $(-1, 1)$ | $+$ | $+$ | $-$ | $-$ | Strictly decreasing |
| $(1, +\infty)$ | $+$ | $+$ | $+$ | $+$ | Strictly increasing |

**3. Correct intervals of monotonicity and character of extrema**

* **Intervals of monotonicity:**
  * Strictly increasing on $(-\infty, -1)$ and $(1, +\infty)$.
  * Strictly decreasing on $(-1, 1)$.
* **Character of extrema:**
  * At $x = -1$: $f'(x)$ changes sign from $+$ to $-$, so $f$ has a **local maximum** at $x = -1$ with value $f(-1) = (-1)^3 - 3(-1) = 2$, i.e., $(-1, 2)$.
  * At $x = 1$: $f'(x)$ changes sign from $-$ to $+$, so $f$ has a **local minimum** at $x = 1$ with value $f(1) = 1^3 - 3(1) = -2$, i.e., $(1, -2)$.

**4. Confirmation via test points in each interval**

1. **Interval $(-\infty, -1)$ — choose $x = -2$:**
   $$
   f'(-2) = 3(-2 - 1)(-2 + 1) = 3(-3)(-1) = +9 > 0
   $$
   Positive sign confirms $f$ is **strictly increasing** on $(-\infty, -1)$.

2. **Interval $(-1, 1)$ — choose $x = 0$:**
   $$
   f'(0) = 3(0 - 1)(0 + 1) = 3(-1)(1) = -3 < 0
   $$
   Negative sign confirms $f$ is **strictly decreasing** on $(-1, 1)$.

3. **Interval $(1, +\infty)$ — choose $x = 2$:**
   $$
   f'(2) = 3(2 - 1)(2 + 1) = 3(1)(3) = +9 > 0
   $$
   Positive sign confirms $f$ is **strictly increasing** on $(1, +\infty)$.

---

### Final Answer

1. **Error:** Knowing the roots $-1$ and $1$ does not fix the sign without checking the leading coefficient ($+3 > 0$) or factor signs; the student reversed the signs of $f'(x) = 3(x^2 - 1)$.
2. **Correct monotonicity:** Strictly increasing on $(-\infty, -1)$ and $(1, +\infty)$; strictly decreasing on $(-1, 1)$.
3. **Correct extrema:** Local maximum at $(-1, 2)$ and local minimum at $(1, -2)$.
4. **Test-point check:** $f'(-2) = 9 > 0$, $f'(0) = -3 < 0$, and $f'(2) = 9 > 0$.
