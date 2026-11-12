### Essential Formulas

**Cosine of the Angle Between Two Nonzero Vectors:**
For any two nonzero vectors $u, v \in \mathbb{R}^3$ forming an angle $\theta_{uv} \in [0, \pi]$ (or $[0^\circ, 180^\circ]$):

$$
\cos\theta_{uv} = \frac{u \cdot v}{\|u\|\,\|v\|}
$$

**Monotonicity of Cosine on $[0, \pi]$:**
On the interval $\theta \in [0, \pi]$, the cosine function $\cos\theta$ is **strictly decreasing** from $\cos 0 = 1$ down to $\cos \pi = -1$. Consequently, for any two pairs of nonzero vectors:

$$
\cos\theta_1 > \cos\theta_2 \iff \theta_1 < \theta_2
$$

That is, a **larger** cosine value corresponds to a **smaller** angle between the vectors.

**Scale Invariance of Direction (Positive Scalar Multiples):**
If $v = k u$ for a strictly positive scalar $k > 0$, then $u \cdot v = k(u \cdot u) = k\|u\|^2$ and $\|v\| = |k|\,\|u\| = k\|u\|$, so the length factors cancel completely:

$$
\frac{u \cdot v}{\|u\|\,\|v\|} = \frac{k\|u\|^2}{\|u\| \cdot (k\|u\|)} = 1 \implies \theta_{uv} = 0^\circ
$$

---

### Problem Statement

**Exercise 15. Comparing Directions Using the Cosine of the Angle**

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

**Step 1: Compute the Euclidean lengths $\|a\|$, $\|b\|$, and $\|c\|$**

Evaluate the norm of each given vector:

$$
\begin{aligned}
\|a\| &= \sqrt{1^2 + 2^2 + 1^2} = \sqrt{1 + 4 + 1} = \sqrt{6}, \\
\|b\| &= \sqrt{2^2 + 4^2 + 2^2} = \sqrt{4 + 16 + 4} = \sqrt{24} = 2\sqrt{6}, \\
\|c\| &= \sqrt{2^2 + 0^2 + 3^2} = \sqrt{4 + 0 + 9} = \sqrt{13}.
\end{aligned}
$$

**Step 2: Compute $\frac{u \cdot v}{\|u\|\,\|v\|}$ for each pair of vectors**

There are three distinct unordered pairs among $\{a, b, c\}$:

1. **Pair $(a, b)$:**
   Compute the dot product $a \cdot b$:

$$
a \cdot b = (1, 2, 1) \cdot (2, 4, 2) = 1 \cdot 2 + 2 \cdot 4 + 1 \cdot 2 = 2 + 8 + 2 = 12
$$

   Divide by $\|a\|\,\|b\|$:

$$
\cos\theta_{ab} = \frac{a \cdot b}{\|a\|\,\|b\|} = \frac{12}{\sqrt{6} \cdot 2\sqrt{6}} = \frac{12}{2 \cdot 6} = \frac{12}{12} = 1
$$

   *(Angle: $\theta_{ab} = \arccos(1) = 0^\circ = 0\ \mathrm{rad}$.)*

2. **Pair $(a, c)$:**
   Compute the dot product $a \cdot c$:

$$
a \cdot c = (1, 2, 1) \cdot (2, 0, 3) = 1 \cdot 2 + 2 \cdot 0 + 1 \cdot 3 = 2 + 0 + 3 = 5
$$

   Divide by $\|a\|\,\|c\|$:

$$
\cos\theta_{ac} = \frac{a \cdot c}{\|a\|\,\|c\|} = \frac{5}{\sqrt{6} \cdot \sqrt{13}} = \frac{5}{\sqrt{78}}
$$

   *(Angle: $\theta_{ac} = \arccos\!\left(\frac{5}{\sqrt{78}}\right) \approx \arccos(0.5661) \approx 55.52^\circ$.)*

3. **Pair $(b, c)$:**
   Compute the dot product $b \cdot c$:

$$
b \cdot c = (2, 4, 2) \cdot (2, 0, 3) = 2 \cdot 2 + 4 \cdot 0 + 2 \cdot 3 = 4 + 0 + 6 = 10
$$

   Divide by $\|b\|\,\|c\|$:

$$
\cos\theta_{bc} = \frac{b \cdot c}{\|b\|\,\|c\|} = \frac{10}{2\sqrt{6} \cdot \sqrt{13}} = \frac{5}{\sqrt{78}}
$$

   *(Angle: $\theta_{bc} = \arccos\!\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ$, identical to $\theta_{ac}$.)*

**Step 3: Order the pairs by increasing angle between the vectors**

Compare the computed cosine values:

$$
1 > \frac{5}{\sqrt{78}} = \frac{5}{\sqrt{78}} \qquad \left(\mathrm{since}\quad 5 < \sqrt{78} \approx 8.832 \implies \frac{5}{\sqrt{78}} < 1\right)
$$

Because $\cos\theta$ is strictly decreasing for $\theta \in [0^\circ, 180^\circ]$, a larger cosine value implies a smaller angle:

$$
\theta_{ab} = 0^\circ < \theta_{ac} = \theta_{bc} = \arccos\!\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ
$$

Therefore, ordered by **increasing angle** from smallest to largest:

1. **Smallest angle ($0^\circ$):** Pair **$(a, b)$** ($\cos\theta_{ab} = 1$)
2. **Tied for largest angle ($\approx 55.52^\circ$):** Pairs **$(a, c)$ and $(b, c)$** have the **exact same angle** ($\cos\theta_{ac} = \cos\theta_{bc} = \frac{5}{\sqrt{78}}$)

**Step 4: Explain why for $a$ and $b$ the value is $1$ even though the vectors have different lengths**

Inspecting the coordinates of $a$ and $b$ shows that $b$ is a positive scalar multiple of $a$:

$$
b = (2, 4, 2) = 2(1, 2, 1) = 2a
$$

1. **Normalized unit directions are identical:** Dividing by $\|u\|$ and $\|v\|$ in the formula $\frac{u \cdot v}{\|u\|\,\|v\|} = \left(\frac{u}{\|u\|}\right) \cdot \left(\frac{v}{\|v\|}\right)$ normalizes each vector to unit length **before** comparing them. Here:

$$
e_a = \frac{a}{\|a\|} = \frac{1}{\sqrt{6}}(1, 2, 1), \qquad e_b = \frac{b}{\|b\|} = \frac{1}{2\sqrt{6}}(2, 4, 2) = \frac{1}{\sqrt{6}}(1, 2, 1) = e_a
$$

   The extra factor of $2$ in the numerator ($a \cdot (2a) = 2\|a\|^2$) cancels identically against the extra factor of $2$ in the denominator ($\|a\|\,\|2a\| = 2\|a\|^2$).
2. **Distinction between direction and length:** Because $b = 2a$ has a strictly positive scaling factor $2 > 0$, $a$ and $b$ point in the **exact same direction and orientation** in $\mathbb{R}^3$ (so the angle between them is $\theta_{ab} = 0^\circ$, giving $\cos 0^\circ = 1$), differing only in length ($\|b\| = 2\sqrt{6}$ vs. $\|a\| = \sqrt{6}$). For the same geometric reason, $b$ and $a$ make the exact same angle with $c$ ($\theta_{bc} = \theta_{ac}$).

**Step 5: Verification**

* **Algebraic scaling identity check for $(b, c)$ from $(a, c)$:**
  Using $b = 2a$ and homogeneity of the dot product and norm for positive scalars:

$$
\frac{b \cdot c}{\|b\|\,\|c\|} = \frac{(2a) \cdot c}{\|2a\|\,\|c\|} = \frac{2(a \cdot c)}{2\|a\|\,\|c\|} = \frac{a \cdot c}{\|a\|\,\|c\|} = \frac{5}{\sqrt{78}}
$$

  confirming why pairs $(a, c)$ and $(b, c)$ yield the exact same cosine value and angle.

---

### Final Answer

1. **Cosine values $\frac{u \cdot v}{\|u\|\,\|v\|}$ for each pair:**

$$
\frac{a \cdot b}{\|a\|\,\|b\|} = 1, \qquad \frac{a \cdot c}{\|a\|\,\|c\|} = \frac{5}{\sqrt{78}}, \qquad \frac{b \cdot c}{\|b\|\,\|c\|} = \frac{5}{\sqrt{78}}
$$

2. **Order by increasing angle:**

$$
\theta_{ab} = 0^\circ \;<\; \theta_{ac} = \theta_{bc} = \arccos\!\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ
$$

   So **$(a, b)$** has the smallest angle ($0^\circ$), followed by **$(a, c)$ and $(b, c)$ tied** for the largest angle.
3. **Why $\frac{a \cdot b}{\|a\|\,\|b\|} = 1$ despite different lengths:** Because $b = 2a$ is a positive scalar multiple of $a$, both vectors have the exact same unit direction vector $\frac{1}{\sqrt{6}}(1, 2, 1)$ and point along the same ray ($\theta_{ab} = 0^\circ$, $\cos 0^\circ = 1$); dividing by $\|a\|\,\|b\|$ cancels the length factor $2$ completely, isolating pure direction from magnitude.
