### Essential Formulas

**Circular Paraboloid:**
A surface whose horizontal cross-sections are concentric circles and whose vertical cross-sections through the axis of symmetry are parabolas is described by the canonical equation of a circular (elliptic) paraboloid:

$$
z = a(x^2 + y^2) \quad (\text{or } x^2 + y^2 = kz \text{ for } k > 0)
$$

where $a > 0$ (or $k > 0$) determines the vertical stretching scale.

---

### Problem Statement

**Exercise 12. Recognizing a Surface from Cross-Sections**

A certain surface has the following properties:
- the cross-section $z=0$ is a point,
- for $z>0$, the cross-sections $z=\mathrm{const}$ are circles with increasing radius,
- vertical cross-sections through the $Oz$ axis are parabolas.

Propose a simple equation for such a surface and justify your choice[cite: 1].

> **Why this exercise:** reverses the usual reasoning: from geometry to an equation[cite: 1].

---

### Solution

**Step 1: Analyze the geometric properties**
* **Property 1 ($z = 0$ is a point):** At the level $z = 0$, the intersection of the surface reduces to a single coordinate point, typically the origin $(0,0,0)$. This indicates that the surface touches or originates from a single point at the base level.
* **Property 2 (Horizontal cross-sections $z = c > 0$ are circles with increasing radius):** For any fixed positive constant $z = c > 0$, the cross-section in the $xy$-plane is a circle. As $c$ increases, the radius of these circles grows larger, meaning the surface expands outward as it moves up along the $z$-axis.
* **Property 3 (Vertical cross-sections through the $Oz$ axis are parabolas):** Cutting the surface with any vertical plane passing through the $Oz$ axis (such as $x = 0$ or $y = 0$) yields a parabola opening upward.

**Step 2: Propose a simple equation**
Based on these geometric clues:
* Circular cross-sections in planes parallel to the $xy$-plane suggest a sum of squared terms: $x^2 + y^2 = \text{function of } z$.
* Parabolas in vertical planes passing through the $Oz$ axis imply a linear relationship with $z$, such that $x^2 + y^2 = kz$ (or equivalently, $z = \frac{1}{k}(x^2 + y^2)$).

Let us propose the simplest standard equation:

$$
z = x^2 + y^2
$$

**Step 3: Verify the proposed equation against the properties**
1. **Check $z = 0$:** Substituting $z = 0$ into $z = x^2 + y^2$ gives $0 = x^2 + y^2$, which has the unique real solution $(x, y) = (0, 0)$. Thus, the cross-section at $z = 0$ is the single point $(0, 0, 0)$. **(Matches Property 1)**
2. **Check $z = c > 0$:** Substituting $z = c$ gives $x^2 + y^2 = c$. For $c > 0$, this represents a circle centered on the $z$-axis with radius $r = \sqrt{c}$. As $c$ increases, the radius $\sqrt{c}$ strictly increases. **(Matches Property 2)**
3. **Check vertical cross-sections through $Oz$:** Restricting the surface to the vertical plane $x = 0$ (the $yz$-plane) gives $z = 0 + y^2 = y^2$, which is a parabola opening upward. Similarly, restricting to $y = 0$ gives $z = x^2$, also an upward-opening parabola. **(Matches Property 3)**

---

### Final Answer

1. **Proposed equation:** 

$$
z = x^2 + y^2 \quad (\text{or } x^2 + y^2 = z)
$$

2. **Justification:** The equation satisfies all three geometric conditions: $z = 0$ yields the single origin point, horizontal levels $z = c > 0$ yield circles of radius $r = \sqrt{c}$ that expand with $z$, and vertical planes through the $Oz$ axis yield parabolas[cite: 1].
