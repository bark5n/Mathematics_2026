### Essential Formulas

1. **Volume of a Rectangular Box:**
   For a box with length $l$, width $w$, and height $h$:

   $$
   V = l \cdot w \cdot h
   $$

2. **Geometric Folding Relations:**
   From a flat sheet of dimensions $L \times W$, cutting corner squares of side length $x$ yields an open box with:
   * Height: $h = x$
   * Length: $l = L - 2x$
   * Width: $w = W - 2x$

3. **Quadratic Formula:**
   For $a x^2 + b x + c = 0$:

   $$
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   $$

---

### Problem Statement

From a $30\,\mathrm{cm}\times40\,\mathrm{cm}$ sheet, squares of side length $x$ are cut from the corners and the edges are folded up to form an open box.

Write the volume as a function of $x$, determine the physically meaningful domain, and find the value of $x$ for which the volume is greatest.

> **Why this problem:** it develops optimization modeling in a situation where the objective function is not given and must be built independently from the geometry.

---

### Solution

**Step 1: Formulate the volume as a function of $x$**

The original sheet has dimensions $40\ \mathrm{cm} \times 30\ \mathrm{cm}$.
When a square of side length $x$ is excised from each of the four corners and the four flaps are folded upward at right angles:
* The height of the box is:

  $$
  h = x
  $$

* The length of the base is:

  $$
  l = 40 - 2x
  $$

* The width of the base is:

  $$
  w = 30 - 2x
  $$

The volume $V(x)$ is the product of these three dimensions:

$$
V(x) = x(40 - 2x)(30 - 2x)
$$

Expand the polynomial:

$$
V(x) = x(1200 - 80x - 60x + 4x^2) = x(4x^2 - 140x + 1200)
$$

$$
V(x) = 4x^3 - 140x^2 + 1200x
$$

---

**Step 2: Determine the physically meaningful domain**

For the box to have positive physical dimensions, each side must be strictly greater than zero:
1. $h > 0 \implies x > 0$
2. $w > 0 \implies 30 - 2x > 0 \implies 2x < 30 \implies x < 15$
3. $l > 0 \implies 40 - 2x > 0 \implies 2x < 40 \implies x < 20$

The most restrictive upper bound is $x < 15$. Therefore, the physically meaningful domain is:

$$
D_V = (0, 15)
$$

At the boundaries $x = 0$ and $x = 15$, the volume drops to $0$.

---

**Step 3: Differentiate and find the critical points**

Compute the first derivative of $V(x)$:

$$
V'(x) = \frac{d}{dx}[4x^3 - 140x^2 + 1200x] = 12x^2 - 280x + 1200
$$

Factor out the greatest common divisor $4$:

$$
V'(x) = 4(3x^2 - 70x + 300)
$$

Set $V'(x) = 0$:

$$
3x^2 - 70x + 300 = 0
$$

Solve using the quadratic formula with $a = 3$, $b = -70$, $c = 300$:

$$
\Delta = b^2 - 4ac = (-70)^2 - 4(3)(300) = 4900 - 3600 = 1300
$$

The square root of the discriminant is:

$$
\sqrt{\Delta} = \sqrt{1300} = 10\sqrt{13}
$$

The two algebraic roots are:

$$
x = \frac{70 \pm 10\sqrt{13}}{2(3)} = \frac{35 \pm 5\sqrt{13}}{3}
$$

Evaluate both numerical values:
1. **First root $x_1$:**

   $$
   x_1 = \frac{35 - 5\sqrt{13}}{3} \approx \frac{35 - 18.0278}{3} = \frac{16.9722}{3} \approx 5.6574\ \mathrm{cm}
   $$

   Notice that $x_1 \approx 5.66 \in (0, 15)$, so it lies within the physical domain.

2. **Second root $x_2$:**

   $$
   x_2 = \frac{35 + 5\sqrt{13}}{3} \approx \frac{35 + 18.0278}{3} = \frac{53.0278}{3} \approx 17.6759\ \mathrm{cm}
   $$

   Notice that $x_2 \approx 17.68 > 15$, so it falls outside the feasible domain and is discarded.

---

**Step 4: Verify that $x_1$ yields the maximum volume**

Compute the second derivative:

$$
V''(x) = \frac{d}{dx}[12x^2 - 280x + 1200] = 24x - 280
$$

Evaluate at $x_1 = \frac{35 - 5\sqrt{13}}{3}$:

$$
V''(x_1) = 24\left(\frac{35 - 5\sqrt{13}}{3}\right) - 280 = 8(35 - 5\sqrt{13}) - 280
$$

$$
V''(x_1) = 280 - 40\sqrt{13} - 280 = -40\sqrt{13} \approx -144.22 < 0
$$

Because $V''(x_1) < 0$, the function attains a strict local and global maximum at $x_1$.

The maximum volume attained is:

$$
V(x_1) \approx 5.6574 \times (40 - 2(5.6574)) \times (30 - 2(5.6574)) \approx 3032.3\ \mathrm{cm}^3
$$

---

### Final Answer

1. **Volume Function:**

   $$
   V(x) = 4x^3 - 140x^2 + 1200x
   $$

2. **Physically Meaningful Domain:**

   $$
   D_V = (0, 15)
   $$

3. **Optimal Corner Cut Length:**

   $$
   x = \frac{35 - 5\sqrt{13}}{3} \approx 5.66\ \mathrm{cm}
   $$

4. **Maximum Volume:**

   $$
   V_{\max} \approx 3032.3\ \mathrm{cm}^3
   $$
