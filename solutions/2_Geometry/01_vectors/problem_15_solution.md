### Problem Statement

Given

$$
a=(1,2,1),\qquad b=(2,4,2),\qquad c=(2,0,3).
$$

For each pair, compute

$$
\frac{u\cdot v}{\|u\|\,\|v\|}.
$$

Order the pairs by increasing angle between the vectors. Explain why for $a$ and $b$ the value is $1$ even though the vectors have different lengths.

> **Why this exercise:** reinforces the connection between the dot product and angle, and the distinction between direction and length.

---

### Solution

#### Essential Formulas

1. **Cosine Similarity (Cosine of the Angle):**
   For two non-zero vectors $u$ and $v$ in $\mathbb{R}^3$, the cosine of the angle $\theta \in [0, \pi]$ between them is defined by:

   $$
   \cos\theta = \frac{u \cdot v}{\|u\| \|v\|}
   $$

2. **Angle Monotonicity:**
   Because $\cos\theta$ is a strictly decreasing function on the interval $\theta \in [0, \pi]$:
   * A larger value of $\cos\theta$ corresponds to a **smaller** angle $\theta$.
   * $\cos\theta = 1 \iff \theta = 0$ (parallel with identical orientation).
   * $\cos\theta = 0 \iff \theta = \frac{\pi}{2} = 90^\circ$ (perpendicular).
   * $\cos\theta = -1 \iff \theta = \pi = 180^\circ$ (opposite orientation).

3. **Scale Invariance of Direction:**
   If $v = \lambda u$ with $\lambda > 0$, then:

   $$
   \frac{u \cdot (\lambda u)}{\|u\| \|\lambda u\|} = \frac{\lambda (u \cdot u)}{\lambda \|u\|^2} = \frac{\|u\|^2}{\|u\|^2} = 1
   $$

   The cosine formula normalizes both vectors by their lengths, eliminating the magnitude and isolating the pure geometric orientation.

---

**Step 1: Compute the Norms of All Three Vectors**

* **Norm of $a = (1, 2, 1)$:**

  $$
  \|a\| = \sqrt{1^2 + 2^2 + 1^2} = \sqrt{1 + 4 + 1} = \sqrt{6}
  $$

* **Norm of $b = (2, 4, 2)$:**

  $$
  \|b\| = \sqrt{2^2 + 4^2 + 2^2} = \sqrt{4 + 16 + 4} = \sqrt{24} = 2\sqrt{6}
  $$

* **Norm of $c = (2, 0, 3)$:**

  $$
  \|c\| = \sqrt{2^2 + 0^2 + 3^2} = \sqrt{4 + 0 + 9} = \sqrt{13}
  $$

---

**Step 2: Compute $\frac{u \cdot v}{\|u\| \|v\|}$ for Each Pair**

* **Pair $(a, b)$:**

  $$
  a \cdot b = (1)(2) + (2)(4) + (1)(2) = 2 + 8 + 2 = 12
  $$

  $$
  \|a\| \|b\| = \sqrt{6} \cdot \sqrt{24} = \sqrt{144} = 12
  $$

  $$
  \cos\theta_{ab} = \frac{a \cdot b}{\|a\| \|b\|} = \frac{12}{12} = 1
  $$

  $$
  \theta_{ab} = \arccos(1) = 0 \ \mathrm{rad} = 0^\circ
  $$

* **Pair $(a, c)$:**

  $$
  a \cdot c = (1)(2) + (2)(0) + (1)(3) = 2 + 0 + 3 = 5
  $$

  $$
  \|a\| \|c\| = \sqrt{6} \cdot \sqrt{13} = \sqrt{78}
  $$

  $$
  \cos\theta_{ac} = \frac{a \cdot c}{\|a\| \|c\|} = \frac{5}{\sqrt{78}} \approx 0.5661
  $$

  $$
  \theta_{ac} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 0.9690 \ \mathrm{rad} \approx 55.52^\circ
  $$

* **Pair $(b, c)$:**

  $$
  b \cdot c = (2)(2) + (4)(0) + (2)(3) = 4 + 0 + 6 = 10
  $$

  $$
  \|b\| \|c\| = 2\sqrt{6} \cdot \sqrt{13} = 2\sqrt{78}
  $$

  $$
  \cos\theta_{bc} = \frac{b \cdot c}{\|b\| \|c\|} = \frac{10}{2\sqrt{78}} = \frac{5}{\sqrt{78}} \approx 0.5661
  $$

  $$
  \theta_{bc} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 0.9690 \ \mathrm{rad} \approx 55.52^\circ
  $$

Notice that $\cos\theta_{ac} = \cos\theta_{bc}$ and $\theta_{ac} = \theta_{bc}$.

---

**Step 3: Order the Pairs by Increasing Angle**

Comparing the angles:

$$
\theta_{ab} = 0^\circ < \theta_{ac} = \theta_{bc} \approx 55.52^\circ
$$

The ordered sequence from smallest angle to largest angle is:
* Pair $(a, b)$ with angle $\theta = 0^\circ$,
* Pairs $(a, c)$ and $(b, c)$ tied with angle $\theta \approx 55.52^\circ$.

$$
(a, b) \prec (a, c) \sim (b, c)
$$

Because greater cosine values correspond to smaller angles, ordering by decreasing cosine value ($\cos\theta_{ab} = 1 > \cos\theta_{ac} = \cos\theta_{bc} \approx 0.5661$) yields the exact same arrangement.

---

**Step 4: Explain Why the Value Is $1$ for $a$ and $b$ Despite Different Lengths**

1. **Algebraic Cancellation:**
   * Notice that $b = 2a$. The length of $b$ is twice that of $a$ ($\|b\| = 2\|a\|$).
   * Substituting $b = 2a$ into the cosine formula:

     $$
     \frac{a \cdot b}{\|a\| \|b\|} = \frac{a \cdot (2a)}{\|a\| \|2a\|} = \frac{2(a \cdot a)}{\|a\|(2\|a\|)} = \frac{2\|a\|^2}{2\|a\|^2} = 1
     $$

   * The positive scalar multiple $\lambda = 2$ scales both the numerator (dot product) and denominator (product of lengths) by exactly the same factor, canceling out completely.

2. **Geometric Distinction Between Direction and Length:**
   * The quantity $\frac{u \cdot v}{\|u\| \|v\|} = \left(\frac{u}{\|u\|}\right) \cdot \left(\frac{v}{\|v\|}\right) = e_u \cdot e_v$ is the dot product of the normalized unit vectors.
   * Normalization strips away the length of each vector, retaining solely its directional line and orientation.
   * Since $b$ is a positive scalar multiple of $a$, both vectors lie on the exact same ray originating from $(0, 0, 0)$. There is no angular divergence between them ($\theta = 0$).
   * Because $\cos(0) = 1$, the cosine similarity must be $1$, regardless of whether the vectors have lengths $\sqrt{6}$, $2\sqrt{6}$, or any other positive magnitudes.

---

### Final Answer

1. **Computed Values:**
   * **Pair $(a, b)$:**

     $$
     \frac{a \cdot b}{\|a\| \|b\|} = \frac{12}{12} = 1 \implies \theta_{ab} = 0^\circ
     $$

   * **Pair $(a, c)$:**

     $$
     \frac{a \cdot c}{\|a\| \|c\|} = \frac{5}{\sqrt{78}} \approx 0.5661 \implies \theta_{ac} \approx 55.52^\circ
     $$

   * **Pair $(b, c)$:**

     $$
     \frac{b \cdot c}{\|b\| \|c\|} = \frac{5}{\sqrt{78}} \approx 0.5661 \implies \theta_{bc} \approx 55.52^\circ
     $$

2. **Ordering by Increasing Angle:**

   $$
   (a, b) \ (\theta = 0^\circ) \ < \ (a, c) = (b, c) \ (\theta \approx 55.52^\circ)
   $$

3. **Why the Value Is $1$ for $a$ and $b$:**
   Vector $b$ is a positive scalar multiple of $a$ ($b = 2a$). The cosine formula normalizes vectors by their lengths, causing the scaling factor of $2$ to cancel out. Because both vectors point in the identical direction along the same ray, the angle between them is zero, and $\cos(0) = 1$.