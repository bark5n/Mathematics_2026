### Problem Statement

Determine the type of object described by:

1. $4x^2+9y^2=36$,
2. $x^2-y^2=1$,
3. $x^2-4y=0$,
4. $x^2+y^2+1=0$.

In the last case, explain why there are no real points.

> **Why this exercise:** develops quick recognition of the curve type and checking whether real solutions exist.

---

### Solution

#### Essential Formulas

1. **Classification of Second-Degree Equations in $\mathbb{R}^2$:**
   An equation $A x^2 + C y^2 + D x + E y + F = 0$ represents:
   * **Ellipse / Circle:** $A \cdot C > 0$ (both non-zero coefficients have the same sign).
     - Circle if $A = C$.
     - Ellipse if $A \neq C$.
     - Empty set (imaginary ellipse) if completed squares sum to a negative number.
   * **Hyperbola:** $A \cdot C < 0$ (coefficients have opposite signs).
   * **Parabola:** $A \cdot C = 0$ (one quadratic term vanishes, and the other variable appears linearly).
   * **Degenerate cases:** point, intersecting lines, parallel lines, empty set.

2. **Real Non-Negativity of Squares:**
   For any real numbers $x, y \in \mathbb{R}$:

   $$
   x^2 \ge 0, \qquad y^2 \ge 0 \implies x^2 + y^2 \ge 0
   $$

---

**Step 1: Classify Object 1: $4x^2 + 9y^2 = 36$**

Divide both sides by $36$:

$$
\frac{4x^2}{36} + \frac{9y^2}{36} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1
$$

In canonical form:

$$
\frac{x^2}{3^2} + \frac{y^2}{2^2} = 1
$$

* Both variables are squared with positive unequal denominators ($9 \neq 4$).
* **Classification:** **Ellipse** centered at $(0, 0)$ with horizontal semi-major axis $a = 3$ and vertical semi-minor axis $b = 2$.

---

**Step 2: Classify Object 2: $x^2 - y^2 = 1$**

In canonical form:

$$
\frac{x^2}{1^2} - \frac{y^2}{1^2} = 1
$$

* Both variables are squared, but their terms have opposite signs ($+$ for $x^2$, $-$ for $y^2$), equal to $+1$.
* The semiaxes are equal ($a = b = 1$).
* **Classification:** **Hyperbola** (specifically an equilateral or rectangular hyperbola) centered at $(0, 0)$ with vertices $(\pm 1, 0)$ and perpendicular asymptotes $y = \pm x$.

---

**Step 3: Classify Object 3: $x^2 - 4y = 0$**

Isolate the linear term:

$$
x^2 = 4y \iff y = \frac{1}{4} x^2
$$

* Exactly one variable is squared ($x^2$), while the other variable appears linearly ($y$).
* **Classification:** **Parabola** with vertex at $(0, 0)$, vertical axis of symmetry $x = 0$ (the $y$-axis), opening upwards ($y \ge 0$).

---

**Step 4: Classify Object 4: $x^2 + y^2 + 1 = 0$ and Explain the Absence of Real Points**

Isolate the constant term:

$$
x^2 + y^2 = -1
$$

* **Classification:** **Empty set** ($\emptyset$, or an imaginary circle).

* **Explanation of Why There Are No Real Points:**
  1. For every real number $x \in \mathbb{R}$, its square is non-negative:

     $$
     x^2 \ge 0
     $$

  2. Similarly, for every real number $y \in \mathbb{R}$:

     $$
     y^2 \ge 0
     $$

  3. Summing two non-negative quantities yields another non-negative quantity:

     $$
     x^2 + y^2 \ge 0
     $$

  4. Adding $1$ to both sides of this inequality gives:

     $$
     x^2 + y^2 + 1 \ge 0 + 1 = 1 > 0
     $$

  5. Because the left-hand side $x^2 + y^2 + 1$ is strictly greater than or equal to $1$ for all $(x, y) \in \mathbb{R}^2$, it can never equal $0$.
  Equivalently, the sum of two real squares $x^2 + y^2$ cannot equal the negative number $-1$.
  Therefore, no pair of real numbers $(x, y)$ satisfies the equation, and the geometric object has no real points.

---

### Final Answer

1. **Equation 1 ($4x^2 + 9y^2 = 36$):**
   * **Type:** Ellipse
   * **Canonical Form:** $\frac{x^2}{9} + \frac{y^2}{4} = 1$ (center $(0, 0)$, semiaxes $a = 3, b = 2$).

2. **Equation 2 ($x^2 - y^2 = 1$):**
   * **Type:** Hyperbola (equilateral)
   * **Characteristics:** Center $(0, 0)$, vertices $(\pm 1, 0)$, asymptotes $y = \pm x$.

3. **Equation 3 ($x^2 - 4y = 0$):**
   * **Type:** Parabola
   * **Characteristics:** Vertex $(0, 0)$, axis $x = 0$, opens upward ($y = \frac{1}{4}x^2$).

4. **Equation 4 ($x^2 + y^2 + 1 = 0$):**
   * **Type:** Empty set ($\emptyset$, no real locus).
   * **Reason:** For all real numbers $x, y \in \mathbb{R}$, $x^2 \ge 0$ and $y^2 \ge 0$, which implies $x^2 + y^2 + 1 \ge 1 > 0$. The expression cannot equal $0$, so no real solutions exist.