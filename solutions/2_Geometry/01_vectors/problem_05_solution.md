### Essential Formulas

1. **Angle Between Two Vectors via Dot Product:**
   For non-zero vectors $u$ and $v$ in $\mathbb{R}^n$, the angle $\theta \in [0, \pi]$ satisfies:

   $$
   \cos\theta = \frac{u \cdot v}{\|u\| \|v\|}
   $$

   $$
   \theta = \arccos\left(\frac{u \cdot v}{\|u\| \|v\|}\right)
   $$

2. **Qualitative Angle Prediction from the Sign of the Dot Product:**
   Because vector norms $\|u\| > 0$ and $\|v\| > 0$ are always positive, the sign of $\cos\theta$ is completely determined by the sign of the dot product $u \cdot v$:
   * **$u \cdot v > 0 \iff \cos\theta > 0$:** The angle is **acute** ($0 \le \theta < \frac{\pi}{2}$, or $0^\circ \le \theta < 90^\circ$).
   * **$u \cdot v = 0 \iff \cos\theta = 0$:** The angle is a **right angle** ($\theta = \frac{\pi}{2}$, or $\theta = 90^\circ$).
   * **$u \cdot v < 0 \iff \cos\theta < 0$:** The angle is **obtuse** ($\frac{\pi}{2} < \theta \le \pi$, or $90^\circ < \theta \le 180^\circ$).

---

### Problem Statement

Given $u=(1,1,0)$ and $v=(1,0,1)$:

1. Use the sign of $u\cdot v$ to predict the type of angle.
2. Compute the angle.
3. Compare the result with the prediction.

> **Why this exercise:** teaches how to extract qualitative information first and only then perform the exact calculation.

---

### Solution

**Step 1: Compute $u \cdot v$ and Predict the Type of Angle**

Given $u = (1, 1, 0)$ and $v = (1, 0, 1)$, compute the dot product:

$$
u \cdot v = (1)(1) + (1)(0) + (0)(1) = 1 + 0 + 0 = 1
$$

* **Sign Analysis:**
  The dot product is strictly positive:

  $$
  u \cdot v = 1 > 0
  $$

* **Prediction:**
  Since $\|u\| > 0$ and $\|v\| > 0$, the denominator in $\cos\theta = \frac{u \cdot v}{\|u\| \|v\|}$ is positive. Therefore:

  $$
  \cos\theta > 0
  $$

  On the fundamental angle interval $\theta \in [0, \pi]$, $\cos\theta > 0$ implies that $\theta$ lies strictly in the first quadrant:

  $$
  0 \le \theta < \frac{\pi}{2} \quad (0^\circ \le \theta < 90^\circ)
  $$

  Hence, the angle between $u$ and $v$ is predicted to be **acute**.

---

**Step 2: Compute the Magnitudes and the Angle**

* **Compute the norm of $u$:**

  $$
  \|u\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{1 + 1 + 0} = \sqrt{2}
  $$

* **Compute the norm of $v$:**

  $$
  \|v\| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{1 + 0 + 1} = \sqrt{2}
  $$

* **Compute $\cos\theta$:**

  $$
  \cos\theta = \frac{u \cdot v}{\|u\| \|v\|} = \frac{1}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2}
  $$

* **Determine the angle $\theta$:**
  Recall the standard trigonometric value on $[0, \pi]$:

  $$
  \cos\theta = \frac{1}{2} \implies \theta = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}
  $$

  In degrees:

  $$
  \theta = \frac{\pi}{3} \cdot \frac{180^\circ}{\pi} = 60^\circ
  $$

---

**Step 3: Compare the Result with the Qualitative Prediction**

* The quantitative computation yields:

  $$
  \theta = 60^\circ = \frac{\pi}{3} \ \mathrm{rad}
  $$

* The initial prediction based on $u \cdot v = 1 > 0$ was that $\theta$ is an acute angle ($0^\circ < \theta < 90^\circ$).
* Since $0^\circ < 60^\circ < 90^\circ$, the exact result perfectly confirms the initial qualitative prediction.
* This verifies that calculating the sign of the dot product is an efficient and reliable way to check the geometric nature of the angle before performing norm calculations and inverse trigonometric evaluations.

---

### Final Answer

1. **Prediction from Sign:**

   $$
   u \cdot v = 1 > 0 \implies \cos\theta > 0
   $$

   The angle is predicted to be **acute** ($0^\circ < \theta < 90^\circ$).

2. **Exact Angle:**

   $$
   \cos\theta = \frac{1}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2} \implies \theta = \frac{\pi}{3} = 60^\circ
   $$

3. **Comparison:**
   The exact calculated angle of $60^\circ$ is acute, strictly confirming the prediction.