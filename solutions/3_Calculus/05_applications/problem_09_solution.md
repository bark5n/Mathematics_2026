### Essential Formulas

1. **Geometry of a Closed Cylinder:**
   For a right circular cylinder of radius $r$ and height $h$:
   * **Volume:**

     $$
     V = \pi r^2 h
     $$

   * **Total Surface Area (Material Usage):**

     $$
     S = 2\pi r^2 + 2\pi r h
     $$

2. **Optimization with an Equality Constraint:**
   * Solve the constraint equation $V = \pi r^2 h$ for one variable ($h$).
   * Substitute into the objective function to obtain a single-variable function $S(r)$.
   * Find stationary points where $S'(r) = 0$, and verify the minimum using the second derivative ($S''(r) > 0$).

---

### Problem Statement

A closed cylinder has fixed volume $V$.

1. Write the volume constraint.
2. Eliminate one of the variables.
3. Express the surface area as a function of the radius $r$.
4. Find the relation between the height $h$ and the radius $r$ for which the material usage is minimal.

Interpret the obtained relation geometrically.

> **Why this problem:** it requires independent reduction of a problem with two variables to one objective function and control of the geometric constraint.

---

### Solution

**Step 1: Write the volume constraint**

The cylinder has a circular base of radius $r$ and a vertical height $h$. The fixed volume $V$ is given by:

$$
V = \pi r^2 h
$$

---

**Step 2: Eliminate one of the variables**

Isolate the height $h$ in terms of the fixed volume $V$ and the radius $r$:

$$
h = \frac{V}{\pi r^2}
$$

Because dimensions must be positive, this relation requires $r > 0$ and $h > 0$.

---

**Step 3: Express the surface area as a function of $r$**

A closed cylinder comprises two circular bases (top and bottom) and a lateral curved side:
* Area of the two circular lids: $2 \cdot (\pi r^2) = 2\pi r^2$
* Area of the unrolled lateral rectangular wall: $2\pi r \cdot h$

The total surface area function is:

$$
S = 2\pi r^2 + 2\pi r h
$$

Substitute the expression for $h = \frac{V}{\pi r^2}$ into $S$:

$$
S(r) = 2\pi r^2 + 2\pi r \left(\frac{V}{\pi r^2}\right)
$$

Cancel the common factor $\pi r$:

$$
S(r) = 2\pi r^2 + \frac{2V}{r} = 2\pi r^2 + 2V r^{-1}
$$

The domain of the objective function is $r \in (0, \infty)$.

---

**Step 4: Find the relation between $h$ and $r$ that minimizes material usage**

Differentiate $S(r)$ with respect to $r$:

$$
S'(r) = \frac{d}{dr}\left[2\pi r^2 + 2V r^{-1}\right] = 4\pi r - 2V r^{-2} = 4\pi r - \frac{2V}{r^2}
$$

Set the derivative equal to zero to find the critical point:

$$
4\pi r - \frac{2V}{r^2} = 0 \iff 4\pi r = \frac{2V}{r^2}
$$

Multiply both sides by $r^2$:

$$
4\pi r^3 = 2V \iff 2\pi r^3 = V
$$

Now substitute the volume constraint $V = \pi r^2 h$ into this equation:

$$
2\pi r^3 = \pi r^2 h
$$

Because $r > 0$, divide both sides by the non-zero quantity $\pi r^2$:

$$
2r = h \iff h = 2r
$$

---

**Step 5: Verify that this relation gives a minimum**

Compute the second derivative:

$$
S''(r) = \frac{d}{dr}\left[4\pi r - 2V r^{-2}\right] = 4\pi + 4V r^{-3} = 4\pi + \frac{4V}{r^3}
$$

Because $V > 0$ and $r > 0$, both terms are strictly positive:

$$
S''(r) > 0 \quad \forall r \in (0, \infty)
$$

Since the second derivative is strictly positive everywhere on the domain, the function $S(r)$ is strictly convex, and the stationary point represents the unique **strict global minimum**.

---

**Step 6: Geometric interpretation of the optimal relation**

1. **Height Equals Diameter:**
   The relation $h = 2r$ demonstrates that the optimal height of the can equals its base diameter ($d = 2r$).
2. **Square Axial Cross-Section:**
   If the optimal cylinder is sliced vertically in half through its central axis of symmetry, the resulting cross-section is a rectangle of width $2r$ and height $h = 2r$, which is a **square**.
3. **Isoperimetric Compactness:**
   A sphere has the smallest surface area for a given volume among all three-dimensional shapes. By setting $h = 2r$, the cylinder achieves maximum geometric compactness (fitting neatly inside a sphere of diameter $2r\sqrt{2}$ and touching the cube circumscribing it symmetrically), minimizing boundary exposure and material waste.

---

### Final Answer

1. **Volume Constraint:**

   $$
   V = \pi r^2 h
   $$

2. **Elimination of Variable:**

   $$
   h = \frac{V}{\pi r^2}
   $$

3. **Surface Area Function:**

   $$
   S(r) = 2\pi r^2 + \frac{2V}{r}
   $$

4. **Optimal Relation for Minimum Material:**

   $$
   h = 2r
   $$

5. **Geometric Interpretation:**
   The height of the cylinder equals its diameter ($h = d$). The central axial cross-section of the most efficient can is a square ($2r \times 2r$), which provides the most compact shape and minimizes surface area per unit volume.
