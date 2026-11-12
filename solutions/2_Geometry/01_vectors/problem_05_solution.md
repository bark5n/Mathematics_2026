### Essential Formulas

**Geometric Dot Product Formula and Angle Between Two Vectors:**
For any two nonzero vectors $u, v \in \mathbb{R}^3$ forming an angle $\theta \in [0, \pi]$ (or $[0^\circ, 180^\circ]$):

$$
u \cdot v = \|u\|\,\|v\|\cos\theta
\qquad \Longleftrightarrow \qquad
\cos\theta = \frac{u \cdot v}{\|u\|\,\|v\|},
\qquad
\theta = \arccos\!\left(\frac{u \cdot v}{\|u\|\,\|v\|}\right)
$$

**Qualitative Angle Classification from the Sign of $u \cdot v$:**
Because $\|u\| > 0$ and $\|v\| > 0$ for nonzero vectors, the sign of $\cos\theta$ is identical to the sign of the dot product $u \cdot v$:

* **$u \cdot v > 0 \iff \cos\theta > 0 \iff 0 \le \theta < \frac{\pi}{2}$ ($0^\circ \le \theta < 90^\circ$):** **Acute angle** (or $0^\circ$ if parallel with the same orientation).
* **$u \cdot v = 0 \iff \cos\theta = 0 \iff \theta = \frac{\pi}{2}$ ($\theta = 90^\circ$):** **Right angle** (perpendicular / orthogonal vectors).
* **$u \cdot v < 0 \iff \cos\theta < 0 \iff \frac{\pi}{2} < \theta \le \pi$ ($90^\circ < \theta \le 180^\circ$):** **Obtuse angle** (or $180^\circ$ if parallel with opposite orientation).

---

### Problem Statement

**Exercise 5. Angle Between Vectors**

Given $u=(1,1,0)$ and $v=(1,0,1)$:

1. Use the sign of $u\cdot v$ to predict the type of angle.
2. Compute the angle.
3. Compare the result with the prediction.

> **Why this exercise:** teaches how to extract qualitative information first and only then perform the exact calculation.

---

### Solution

**Step 1: Compute $u \cdot v$ and use its sign to predict the type of angle**

Compute the dot product of $u = (1, 1, 0)$ and $v = (1, 0, 1)$:

$$
\begin{aligned}
u \cdot v &= (1, 1, 0) \cdot (1, 0, 1) \\
&= 1 \cdot 1 + 1 \cdot 0 + 0 \cdot 1 \\
&= 1 + 0 + 0 \\
&= 1
\end{aligned}
$$

* **Qualitative prediction:** Because $u \cdot v = 1 > 0$ and both vectors are nonzero, we have $\cos\theta = \frac{u \cdot v}{\|u\|\,\|v\|} > 0$. Since $\cos\theta > 0$ on $[0^\circ, 180^\circ]$ holds precisely when $0^\circ \le \theta < 90^\circ$ (and $u$ is not a scalar multiple of $v$, so $\theta \neq 0^\circ$), the angle $\theta$ between $u$ and $v$ must be **strictly acute** ($0^\circ < \theta < 90^\circ$, or $0 < \theta < \frac{\pi}{2}$).

**Step 2: Compute the exact angle $\theta$ between $u$ and $v$**

First, find the Euclidean lengths $\|u\|$ and $\|v\|$:

$$
\begin{aligned}
\|u\| &= \sqrt{1^2 + 1^2 + 0^2} = \sqrt{1 + 1 + 0} = \sqrt{2}, \\
\|v\| &= \sqrt{1^2 + 0^2 + 1^2} = \sqrt{1 + 0 + 1} = \sqrt{2}.
\end{aligned}
$$

Now substitute $u \cdot v = 1$, $\|u\| = \sqrt{2}$, and $\|v\| = \sqrt{2}$ into the cosine formula:

$$
\begin{aligned}
\cos\theta &= \frac{u \cdot v}{\|u\|\,\|v\|} \\
&= \frac{1}{\sqrt{2} \cdot \sqrt{2}} \\
&= \frac{1}{2}
\end{aligned}
$$

Taking the inverse cosine on $[0, \pi]$ gives the exact angle:

$$
\theta = \arccos\!\left(\frac{1}{2}\right) = \frac{\pi}{3}\ \mathrm{rad} = 60^\circ
$$

**Step 3: Compare the exact result with the qualitative prediction**

* **Prediction from Step 1:** Strictly acute angle ($0^\circ < \theta < 90^\circ$).
* **Exact result from Step 2:** $\theta = 60^\circ = \frac{\pi}{3}\ \mathrm{rad}$.
* **Comparison:** The computed angle $\theta = 60^\circ$ lies strictly between $0^\circ$ and $90^\circ$, so it **completely agrees** with the qualitative prediction made solely from the positive sign of $u \cdot v = 1 > 0$ before calculating any lengths or inverse cosines.

**Step 4: Verification**

* **Equilateral triangle geometric check:**
  Consider the points $O = (0, 0, 0)$, $A = (1, 1, 0)$, and $B = (1, 0, 1)$, so that $\overrightarrow{OA} = u$ and $\overrightarrow{OB} = v$. Compute all three side lengths of $\triangle OAB$:
  * $OA = \|u\| = \sqrt{2}$
  * $OB = \|v\| = \sqrt{2}$
  * $AB = \|v - u\| = \|(0, -1, 1)\| = \sqrt{0^2 + (-1)^2 + 1^2} = \sqrt{2}$

  Because $OA = OB = AB = \sqrt{2}$, $\triangle OAB$ is an **equilateral triangle**, which immediately guarantees that every interior angle—including $\theta = \angle AOB$ between $u$ and $v$—equals $60^\circ$ ($\frac{\pi}{3}\ \mathrm{rad}$).

---

### Final Answer

1. **Qualitative prediction from $u \cdot v$:** Since $u \cdot v = 1 > 0$, $\cos\theta > 0$, predicting an **acute angle** ($0^\circ < \theta < 90^\circ$).
2. **Exact angle between $u$ and $v$:**

$$
\theta = \frac{\pi}{3}\ \mathrm{rad} = 60^\circ \qquad \left(\cos\theta = \frac{1}{2}\right)
$$

3. **Comparison:** The exact angle $\theta = 60^\circ$ falls strictly inside $(0^\circ, 90^\circ)$, confirming the qualitative prediction from the sign of the dot product.
