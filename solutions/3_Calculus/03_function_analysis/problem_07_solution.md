### Essential Formulas

**Trigonometric Derivatives:**

$$
\frac{d}{dx}(\sin x) = \cos x, \qquad \frac{d}{dx}(\cos x) = -\sin x
$$

**Extreme Value Theorem on a Closed Interval $[a, b]$:**
A continuous function on $[a, b]$ attains its absolute maximum and minimum either at interior critical points where $f'(x) = 0$ or at the endpoints $x = a$ and $x = b$.

---

### Problem Statement

**Problem 7. A Trigonometric Function**

On $[0, 2\pi]$, find the intervals of monotonicity and the extrema of

$$
f(x) = \sin x + \cos x.
$$

Include the endpoints of the interval and compare the function values at the critical points and at the endpoints.

> **Why this problem:** it practices the analysis of a periodic function on a bounded interval.

---

### Solution

**Step 1: Compute the derivative and find critical points in $(0, 2\pi)$**

Differentiate $f(x) = \sin x + \cos x$:

$$
f'(x) = \cos x - \sin x
$$

Set $f'(x) = 0$:

$$
\cos x - \sin x = 0 \implies \sin x = \cos x
$$

Since $\cos x = 0$ gives $\sin x = \pm 1 \neq 0$, we may divide by $\cos x$:

$$
\tan x = 1
$$

In the open interval $(0, 2\pi)$, the solutions to $\tan x = 1$ are:

$$
x_1 = \frac{\pi}{4}, \qquad x_2 = \frac{5\pi}{4}
$$

**Step 2: Determine the sign of $f'(x)$ and intervals of monotonicity on $[0, 2\pi]$**

Test the sign of $f'(x) = \cos x - \sin x$ on each subinterval of $[0, 2\pi]$:
* **On $\left(0, \frac{\pi}{4}\right)$:** At $x = 0$, $f'(0) = 1 - 0 = 1 > 0 \implies f'(x) > 0$, so $f$ is **strictly increasing**.
* **On $\left(\frac{\pi}{4}, \frac{5\pi}{4}\right)$:** At $x = \frac{\pi}{2}$, $f'\left(\frac{\pi}{2}\right) = 0 - 1 = -1 < 0 \implies f'(x) < 0$, so $f$ is **strictly decreasing**.
* **On $\left(\frac{5\pi}{4}, 2\pi\right)$:** At $x = \frac{3\pi}{2}$, $f'\left(\frac{3\pi}{2}\right) = 0 - (-1) = 1 > 0 \implies f'(x) > 0$, so $f$ is **strictly increasing**.

**Step 3: Evaluate $f(x)$ at the critical points and endpoints**

1. **Left endpoint $x = 0$:**
   $$
   f(0) = \sin(0) + \cos(0) = 0 + 1 = 1
   $$

2. **First critical point $x = \frac{\pi}{4}$:**
   $$
   f\left(\frac{\pi}{4}\right) = \sin\left(\frac{\pi}{4}\right) + \cos\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2} \approx 1.414
   $$

3. **Second critical point $x = \frac{5\pi}{4}$:**
   $$
   f\left(\frac{5\pi}{4}\right) = \sin\left(\frac{5\pi}{4}\right) + \cos\left(\frac{5\pi}{4}\right) = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = -\sqrt{2} \approx -1.414
   $$

4. **Right endpoint $x = 2\pi$:**
   $$
   f(2\pi) = \sin(2\pi) + \cos(2\pi) = 0 + 1 = 1
   $$

**Step 4: Compare values and classify all local and global extrema**

Ordering the four values gives:

$$
f\left(\frac{5\pi}{4}\right) = -\sqrt{2} < f(0) = f(2\pi) = 1 < f\left(\frac{\pi}{4}\right) = \sqrt{2}
$$

* **Global (and local) maximum:** $\sqrt{2}$ at $x = \frac{\pi}{4}$ (where $f'$ changes from $+$ to $-$).
* **Global (and local) minimum:** $-\sqrt{2}$ at $x = \frac{5\pi}{4}$ (where $f'$ changes from $-$ to $+$).
* **Endpoints:** At $x = 0$, $f$ increases immediately to the right, making $(0, 1)$ a **local (boundary) minimum**; at $x = 2\pi$, $f$ increases into the right endpoint, making $(2\pi, 1)$ a **local (boundary) maximum**. Neither endpoint is a global extremum because $-\sqrt{2} < 1 < \sqrt{2}$.

---

### Final Answer

1. **Monotonicity on $[0, 2\pi]$:** Strictly increasing on $\left[0, \frac{\pi}{4}\right]$ and $\left[\frac{5\pi}{4}, 2\pi\right]$; strictly decreasing on $\left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$.
2. **Comparison of values:** $f(0) = f(2\pi) = 1$, $f\left(\frac{\pi}{4}\right) = \sqrt{2}$, and $f\left(\frac{5\pi}{4}\right) = -\sqrt{2}$.
3. **Extrema:** Global maximum $\sqrt{2}$ at $x = \frac{\pi}{4}$; global minimum $-\sqrt{2}$ at $x = \frac{5\pi}{4}$; boundary local minimum $1$ at $x = 0$ and boundary local maximum $1$ at $x = 2\pi$.
