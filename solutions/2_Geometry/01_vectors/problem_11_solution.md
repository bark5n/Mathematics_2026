### Essential Formulas

1. **Parallel Component (Orthogonal Projection):**
   The component of a vector $u$ in the direction of a non-zero vector $v$ is given by:

   $$
   u_{\parallel} = \left(\frac{u \cdot v}{v \cdot v}\right) v
   $$

   By construction, $u_{\parallel}$ is collinear with $v$.

2. **Perpendicular Component (Orthogonal Complement):**
   The component of $u$ orthogonal to $v$ is obtained by subtraction:

   $$
   u_{\perp} = u - u_{\parallel}
   $$

3. **Conditions for a Valid Orthogonal Decomposition:**
   For any vector $u$ and reference direction $v$, the decomposition $u = u_{\parallel} + u_{\perp}$ is unique and characterized by two defining properties:
   * **Reconstitution (Sum Property):**

     $$
     u_{\parallel} + u_{\perp} = u
     $$

   * **Orthogonality Property:**

     $$
     u_{\perp} \cdot v = 0
     $$

---

### Problem Statement

Decompose $u=(3,4)$ into components parallel and perpendicular to $v=(1,2)$. Check

$$
u=u_{\parallel}+u_{\perp},\qquad u_{\perp}\cdot v=0.
$$

Explain why these are two independent checks of correctness.

> **Why this exercise:** deepens the idea of projection through construction and verification.

---

### Solution

**Step 1: Compute the Parallel Component $u_{\parallel}$**

Given $u = (3, 4)$ and $v = (1, 2)$:

* Compute the dot product $u \cdot v$:

  $$
  u \cdot v = (3)(1) + (4)(2) = 3 + 8 = 11
  $$

* Compute the squared norm $v \cdot v = \|v\|^2$:

  $$
  v \cdot v = 1^2 + 2^2 = 1 + 4 = 5
  $$

* Compute $u_{\parallel} = \mathrm{proj}_v u$:

  $$
  u_{\parallel} = \frac{11}{5}(1, 2) = \left(\frac{11}{5}, \ \frac{22}{5}\right)
  $$

In decimal notation:

$$
u_{\parallel} = (2.2, \ 4.4)
$$

---

**Step 2: Compute the Perpendicular Component $u_{\perp}$**

Subtract $u_{\parallel}$ from $u = (3, 4) = \left(\frac{15}{5}, \frac{20}{5}\right)$:

$$
u_{\perp} = u - u_{\parallel} = (3, 4) - \left(\frac{11}{5}, \ \frac{22}{5}\right)
$$

Compute the components:

$$
u_{\perp} = \left(\frac{15 - 11}{5}, \ \frac{20 - 22}{5}\right) = \left(\frac{4}{5}, \ -\frac{2}{5}\right)
$$

In decimal notation:

$$
u_{\perp} = (0.8, \ -0.4)
$$

---

**Step 3: Verification of Check 1 ($u = u_{\parallel} + u_{\perp}$)**

Add the two components together:

$$
u_{\parallel} + u_{\perp} = \left(\frac{11}{5}, \ \frac{22}{5}\right) + \left(\frac{4}{5}, \ -\frac{2}{5}\right)
$$

$$
u_{\parallel} + u_{\perp} = \left(\frac{11 + 4}{5}, \ \frac{22 - 2}{5}\right) = \left(\frac{15}{5}, \ \frac{20}{5}\right) = (3, \ 4) = u
$$

Check 1 is verified.

---

**Step 4: Verification of Check 2 ($u_{\perp} \cdot v = 0$)**

Compute the dot product of $u_{\perp} = \left(\frac{4}{5}, -\frac{2}{5}\right)$ with $v = (1, 2)$:

$$
u_{\perp} \cdot v = \left(\frac{4}{5}\right)(1) + \left(-\frac{2}{5}\right)(2) = \frac{4}{5} - \frac{4}{5} = 0
$$

Check 2 is verified ($u_{\perp} \perp v$).

---

**Step 5: Why These Are Two Independent Checks of Correctness**

The two checks test two fundamentally different and logically decoupled requirements:

1. **Check 1 ($u_{\parallel} + u_{\perp} = u$) verifies algebraic completeness:**
   * This check confirms that no part of the original vector has been lost in the arithmetic and that the two pieces sum back to the original vector $u$.
   * However, this check does **not** test whether the components are oriented correctly. For instance, any arbitrary partition like $(1, 1) + (2, 3) = (3, 4)$ would satisfy Check 1, even though neither piece is parallel or perpendicular to $v$.

2. **Check 2 ($u_{\perp} \cdot v = 0$) verifies geometric direction (orthogonality):**
   * This check confirms that the residual vector is at a right angle to the reference direction $v$.
   * However, this check does **not** verify that the pieces add up to $u$. For instance, the vector $(2, -1)$ satisfies $(2, -1) \cdot (1, 2) = 0$, but adding it to $u_{\parallel}$ does not yield $u$.

Because satisfying either condition alone does not imply the other, both checks are necessary and independent. Together, they uniquely confirm that the decomposition is correct according to the orthogonal decomposition theorem.

---

### Final Answer

1. **Parallel Component:**

   $$
   u_{\parallel} = \left(\frac{11}{5}, \ \frac{22}{5}\right) = (2.2, \ 4.4)
   $$

2. **Perpendicular Component:**

   $$
   u_{\perp} = \left(\frac{4}{5}, \ -\frac{2}{5}\right) = (0.8, \ -0.4)
   $$

3. **Verifications:**
   * **Sum Check:**

     $$
     u_{\parallel} + u_{\perp} = \left(\frac{11}{5}, \frac{22}{5}\right) + \left(\frac{4}{5}, -\frac{2}{5}\right) = (3, 4) = u
     $$

   * **Orthogonality Check:**

     $$
     u_{\perp} \cdot v = \left(\frac{4}{5}\right)(1) + \left(-\frac{2}{5}\right)(2) = \frac{4 - 4}{5} = 0 \implies u_{\perp} \perp v
     $$

4. **Independence of Checks:**
   Check 1 ensures the parts reconstruct the vector $u$ (algebraic consistency), while Check 2 ensures the perpendicular component forms a $90^\circ$ angle with $v$ (geometric orthogonality). Neither condition guarantees the other on its own; both are required for a unique orthogonal decomposition.