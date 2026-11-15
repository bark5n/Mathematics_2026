### Essential Formulas

**Completing the Square for Shifted Conics:**
To reduce a general second-degree equation with linear terms:
$$
Ax^2 + By^2 + Dx + Ey + F = 0
$$
group the variables, factor out the leading coefficients, and complete the square to obtain the canonical form:
$$
\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
$$

**Elliptic Cone in Space:**
A surface whose horizontal cross-sections are ellipses and whose vertical cross-sections through the origin are pairs of intersecting lines is described by an equation of the form:
$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z^2}{c^2} \quad (\text{or } 4x^2 + y^2 = z^2)
$$

---

### Problem Statement

**Exercise 15. Recognition and Sketch Without a Given Name**

Consider the two equations:

$$
4x^2+9y^2-8x+36y+4=0,
$$

$$
4x^2+y^2=z^2.
$$

For the first equation, reduce it to canonical form, recognize the curve, give its most important features, and make a sketch.

For the second equation, do not begin by using a ready-made name for the surface. First describe the cross-sections $z=c$ and the cross-sections by the planes $x=0$ and $y=0$, paying attention to the different scales along the axes. Only then identify the surface and make a sketch[cite: 1].

> **Why this exercise:** tests transfer of the two main mechanisms of the set—moving to canonical form and recognizing an object through cross-sections—without allowing the easiest example to be chosen[cite: 1].

---

### Solution

**Part 1: Analyzing the First Equation ($4x^2 + 9y^2 - 8x + 36y + 4 = 0$)**

1. **Group the terms by variable:**
   Rearrange the equation by grouping the $x$-terms and $y$-terms together, and move the constant term to the right-hand side:
   $$
   (4x^2 - 8x) + (9y^2 + 36y) = -4
   $$

2. **Factor out the leading coefficients:**
   Factor out $4$ from the $x$-group and $9$ from the $y$-group:
   $$
   4(x^2 - 2x) + 9(y^2 + 4y) = -4
   $$

3. **Complete the square inside each parenthesis:**
   * For $x^2 - 2x$, add $\left(\frac{-2}{2}\right)^2 = 1$ inside, and add $4 \cdot 1 = 4$ to the right-hand side.
   * For $y^2 + 4y$, add $\left(\frac{4}{2}\right)^2 = 4$ inside, and add $9 \cdot 4 = 36$ to the right-hand side.

   $$
   4(x^2 - 2x + 1) + 9(y^2 + 4y + 4) = -4 + 4 + 36
   $$
   $$
   4(x - 1)^2 + 9(y + 2)^2 = 36
   $$

4. **Reduce to canonical form:**
   Divide the entire equation by $36$:
   $$
   \frac{4(x - 1)^2}{36} + \frac{9(y + 2)^2}{36} = \frac{36}{36} \implies \frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1
   $$

5. **Recognize the curve and its features:**
   * **Type:** Ellipse.
   * **Center:** $(h, k) = (1, -2)$.
   * **Semiaxes:** $a = 3$ (along the $x$-direction) and $b = 2$ (along the $y$-direction).
   * **Sketch description:** An ellipse centered at $(1, -2)$ stretched horizontally along the $x$-axis.

---

**Part 2: Analyzing the Second Equation ($4x^2 + y^2 = z^2$)**

1. **Describe the cross-sections $z = c$ (Horizontal planes):**
   Substitute $z = c$ into the equation:
   $$
   4x^2 + y^2 = c^2
   $$
   * If $c = 0$, $4x^2 + y^2 = 0$, which yields a **single point** at the origin $(0, 0, 0)$.
   * If $c \neq 0$, dividing by $c^2$ gives $\frac{x^2}{(c/2)^2} + \frac{y^2}{c^2} = 1$. This represents a family of **ellipses** centered on the $z$-axis whose semiaxes expand linearly as $|c|$ increases.

2. **Describe the cross-section $x = 0$ (Plane $yz$):**
   Substitute $x = 0$ into the equation:
   $$
   4(0)^2 + y^2 = z^2 \implies y^2 = z^2 \implies z = \pm y
   $$
   This represents **two intersecting straight lines** ($z = y$ and $z = -y$) forming an "X" shape in the $yz$-plane.

3. **Describe the cross-section $y = 0$ (Plane $xz$):**
   Substitute $y = 0$ into the equation:
   $$
   4x^2 + 0^2 = z^2 \implies z^2 = 4x^2 \implies z = \pm 2x
   $$
   This represents **two intersecting straight lines** ($z = 2x$ and $z = -2x$) with a steeper slope in the $xz$-plane.

4. **Identify the surface:**
   Since horizontal cross-sections are expanding ellipses and vertical cross-sections through the origin are intersecting lines, the surface is an **elliptic double cone** aligned with the $Oz$ axis, featuring different scaling factors along the $x$ and $y$ axes.

---

### Final Answer

1. **First equation ($4x^2 + 9y^2 - 8x + 36y + 4 = 0$):** Reduces to the canonical ellipse equation **$\frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1$**, centered at $(1, -2)$ with semiaxes $a = 3$ and $b = 2$.
2. **Second equation ($4x^2 + y^2 = z^2$):** Features horizontal elliptical cross-sections that expand with $|c|$ and vertical cross-sections consisting of intersecting lines, identifying the surface as an **elliptic cone**.
