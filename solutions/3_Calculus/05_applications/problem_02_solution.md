### Essential Formulas

1. **Perimeter and Area of a Rectangle:**
   For a rectangle with side lengths $x$ and $y$:
   * Perimeter:

     $$
     P = 2x + 2y
     $$

   * Area:

     $$
     A = x \cdot y
     $$

2. **Single-Variable Optimization:**
   Express the objective function in terms of a single variable $x$, identify the geometrically feasible domain, locate stationary points where $A'(x) = 0$, and verify the nature of the extremum using the second derivative ($A''(x) < 0 \implies$ maximum).

---

### Problem Statement

A rectangle has perimeter $40$.

1. Write its area as a function of the length of one side.
2. Determine the domain of this function resulting from the geometry of the problem.
3. Find the dimensions that give the maximum area.
4. Justify that the point found actually gives a maximum.

> **Why this problem:** it teaches the complete optimization scheme: model → domain → derivative → verification and interpretation of the maximum.

---

### Solution

**Step 1: Write the area as a function of one side**

Let $x$ and $y$ denote the side lengths of the rectangle.
The perimeter constraint is:

$$
2x + 2y = 40
$$

Divide both sides by $2$:

$$
x + y = 20 \implies y = 20 - x
$$

Express the area $A$ in terms of the single variable $x$:

$$
A(x) = x \cdot y = x(20 - x) = 20x - x^2
$$

---

**Step 2: Determine the domain from the geometry**

In physical geometry, side lengths must be strictly positive:
1. $x > 0$
2. $y > 0 \implies 20 - x > 0 \implies x < 20$

Combining both conditions gives the open interval domain:

$$
D_A = (0, 20)
$$

---

**Step 3: Find the dimensions that maximize the area**

Compute the first derivative of the area function:

$$
A'(x) = \frac{d}{dx}[20x - x^2] = 20 - 2x
$$

Set $A'(x) = 0$ to find the critical point:

$$
20 - 2x = 0 \implies 2x = 20 \implies x = 10
$$

The value $x = 10$ lies in the interior of the domain $(0, 20)$.
Compute the corresponding side length $y$:

$$
y = 20 - 10 = 10
$$

The dimensions are $10 \times 10$, which represents a square.
The maximum area is:

$$
A(10) = 10 \cdot 10 = 100
$$

---

**Step 4: Justify that the point yields a maximum**

1. **Second Derivative Test:**
   Compute the second derivative:

   $$
   A''(x) = \frac{d}{dx}[20 - 2x] = -2
   $$

   Since $A''(10) = -2 < 0$, the function is strictly concave downward everywhere on $(0, 20)$.

2. **Global Nature of the Extremum:**
   Because $A''(x) = -2 < 0$ on the entire domain $(0, 20)$, $x = 10$ is the unique critical point and therefore the **strict global maximum**.
   Furthermore, at the domain boundaries:

   $$
   \lim_{x \to 0^+} A(x) = 0, \qquad \lim_{x \to 20^-} A(x) = 0
   $$

   Because the area vanishes at both endpoints and reaches $100$ at $x = 10$, the maximum is mathematically guaranteed.

---

### Final Answer

1. **Area Function:**

   $$
   A(x) = 20x - x^2
   $$

2. **Geometric Domain:**

   $$
   D_A = (0, 20)
   $$

3. **Optimal Dimensions and Maximum Area:**
   * Length: $x = 10$
   * Width: $y = 10$ (a square)
   * Maximum Area: $A = 100$

4. **Justification:**
   $A''(x) = -2 < 0$ on $(0, 20)$, proving that $x = 10$ is a strict global maximum.
