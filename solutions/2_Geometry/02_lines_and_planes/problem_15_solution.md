### Essential Formulas

**General Criteria for the Relative Position of a Line and a Plane:**
Let a line be given by $L: p + tv$ with starting point $p$ and direction vector $v$, and let a plane be given by $\Pi: n \cdot x = d$ with normal vector $n$. The relative position is classified into three mutually exclusive cases based on the dot product $n \cdot v$ and whether the point $p$ satisfies the plane equation ($n \cdot p = d$):

1. **One Intersection Point:** 
   $$
   n \cdot v \neq 0
   $$
   The line is not perpendicular to the plane's normal, meaning it pierces the plane at a unique point.

2. **Parallel with No Common Points (Strictly Parallel):** 
   $$
   n \cdot v = 0 \quad \text{and} \quad n \cdot p \neq d
   $$
   The line's direction is orthogonal to the normal vector (making it parallel to the plane), but the base point $p$ does not lie on the plane.

3. **Line Contained in the Plane:** 
   $$
   n \cdot v = 0 \quad \text{and} \quad n \cdot p = d
   $$
   The line's direction is orthogonal to the normal vector, and the base point $p$ satisfies the plane equation, ensuring the entire line rests within the plane.

---

### Problem Statement

**Exercise 15. Complete Classification of a Line Relative to a Plane**

Let

$$
L:p+tv,\qquad \Pi:n\cdot x=d.
$$

State the conditions distinguishing the three cases: one intersection point, parallel with no common points, and the line contained in the plane. Then illustrate each case with your own simple numerical example.

> **Why this exercise:** requires formulating a general mathematical criterion instead of carrying out one isolated calculation[cite: 4].

---

### Solution

**Step 1: State the general conditions**

As defined above, the classification relies entirely on evaluating two indicators:
* The dot product $n \cdot v$ (which determines whether the line is parallel or transverse to the plane).
* The substitution value $n \cdot p$ compared to $d$ (which determines whether a parallel line floats outside or rests inside the plane).

**Step 2: Illustrate Case 1 (One Intersection Point)**

* **Given data:** 
  * Line: $p = (0, 0, 0)$, $v = (1, 1, 1)$ $\implies L: (x, y, z) = t(1, 1, 1)$
  * Plane: $\Pi: x + y + z = 3$ $\implies n = (1, 1, 1), \, d = 3$
* **Check condition:** 
  $$
  n \cdot v = (1)(1) + (1)(1) + (1)(1) = 3 \neq 0
  $$
* **Conclusion:** Since $n \cdot v \neq 0$, the line intersects the plane at a unique point (specifically at $t = 1$, yielding the intersection point $(1, 1, 1)$).

**Step 3: Illustrate Case 2 (Parallel with No Common Points)**

* **Given data:** 
  * Line: $p = (0, 0, 5)$, $v = (1, -1, 0)$ $\implies L: (x, y, z) = (0, 0, 5) + t(1, -1, 0)$
  * Plane: $\Pi: x + y + z = 3$ $\implies n = (1, 1, 1), \, d = 3$
* **Check condition:** 
  $$
  n \cdot v = (1)(1) + (1)(-1) + (1)(0) = 0
  $$
  $$
  n \cdot p = (1)(0) + (1)(0) + (1)(5) = 5 \neq 3 \quad (d)
  $$
* **Conclusion:** Since $n \cdot v = 0$ and $n \cdot p \neq d$, the line is strictly parallel to the plane with no common points.

**Step 4: Illustrate Case 3 (Line Contained in the Plane)**

* **Given data:** 
  * Line: $p = (1, 1, 1)$, $v = (1, -1, 0)$ $\implies L: (x, y, z) = (1, 1, 1) + t(1, -1, 0)$
  * Plane: $\Pi: x + y + z = 3$ $\implies n = (1, 1, 1), \, d = 3$
* **Check condition:** 
  $$
  n \cdot v = (1)(1) + (1)(-1) + (1)(0) = 0
  $$
  $$
  n \cdot p = (1)(1) + (1)(1) + (1)(1) = 3 = d
  $$
* **Conclusion:** Since $n \cdot v = 0$ and $n \cdot p = d$, the entire line lies within the plane.

---

### Final Answer

1. **Conditions for the three cases:**
   * **One intersection point:** $n \cdot v \neq 0$.
   * **Parallel with no common points:** $n \cdot v = 0$ and $n \cdot p \neq d$.
   * **Line contained in the plane:** $n \cdot v = 0$ and $n \cdot p = d$.
2. **Numerical examples:** Illustrated above using transverse, parallel non-intersecting, and fully contained line configurations relative to $\Pi: x + y + z = 3[cite: 4]$.
