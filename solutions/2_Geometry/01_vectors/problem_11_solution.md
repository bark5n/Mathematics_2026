### Essential Formulas

**Orthogonal Decomposition of a Vector $u$ Relative to a Nonzero Direction $v$:**
Given any vector $u \in \mathbb{R}^n$ and any nonzero vector $v \in \mathbb{R}^n \setminus \{\mathbf{0}\}$, $u$ decomposes uniquely into a component $u_{\parallel}$ parallel to $v$ and a component $u_{\perp}$ perpendicular to $v$:

$$
u = u_{\parallel} + u_{\perp}
$$

where:

$$
u_{\parallel} = \mathrm{proj}_v\,u = \frac{u \cdot v}{v \cdot v} v,
\qquad
u_{\perp} = u - u_{\parallel} = u - \frac{u \cdot v}{v \cdot v} v
$$

**Defining Properties of the Decomposition:**
1. **Parallelism & Additivity:** $u_{\parallel} = c v$ for a unique scalar $c = \frac{u \cdot v}{v \cdot v}$, and $u_{\parallel} + u_{\perp} = u$.
2. **Orthogonality:** $u_{\perp} \cdot v = 0$ (equivalently, $u_{\perp} \cdot u_{\parallel} = 0$).

---

### Problem Statement

**Exercise 11. Decomposition into Parallel and Perpendicular Components**

Decompose $u=(3,4)$ into components parallel and perpendicular to $v=(1,2)$. Check

$$
u=u_{\parallel}+u_{\perp},\qquad u_{\perp}\cdot v=0.
$$

Explain why these are two independent checks of correctness.

> **Why this exercise:** deepens the idea of projection through construction and verification.

---

### Solution

**Step 1: Compute the parallel component $u_{\parallel}$ (orthogonal projection of $u$ onto $v$)**

First compute the dot products $u \cdot v$ and $v \cdot v$ for $u = (3, 4)$ and $v = (1, 2)$:

$$
\begin{aligned}
u \cdot v &= (3, 4) \cdot (1, 2) = 3 \cdot 1 + 4 \cdot 2 = 3 + 8 = 11, \\
v \cdot v &= \|v\|^2 = (1, 2) \cdot (1, 2) = 1^2 + 2^2 = 1 + 4 = 5.
\end{aligned}
$$

Apply the orthogonal projection formula to obtain $u_{\parallel}$:

$$
\begin{aligned}
u_{\parallel} &= \mathrm{proj}_v\,u = \frac{u \cdot v}{v \cdot v} v \\
&= \frac{11}{5} (1, 2) \\
&= \left(\frac{11}{5}, \frac{22}{5}\right)
\end{aligned}
$$

Because $u_{\parallel} = \frac{11}{5} v$, $u_{\parallel}$ is an explicit scalar multiple of $v$ and therefore lies strictly along the direction of $v$.

**Step 2: Compute the perpendicular component $u_{\perp}$**

Subtract $u_{\parallel} = \left(\frac{11}{5}, \frac{22}{5}\right)$ from $u = (3, 4) = \left(\frac{15}{5}, \frac{20}{5}\right)$ componentwise:

$$
\begin{aligned}
u_{\perp} &= u - u_{\parallel} \\
&= (3, 4) - \left(\frac{11}{5}, \frac{22}{5}\right) \\
&= \left(\frac{15}{5} - \frac{11}{5}, \, \frac{20}{5} - \frac{22}{5}\right) \\
&= \left(\frac{4}{5}, -\frac{2}{5}\right)
\end{aligned}
$$

**Step 3: Check both $u = u_{\parallel} + u_{\perp}$ and $u_{\perp} \cdot v = 0$**

1. **First check ($u = u_{\parallel} + u_{\perp}$):**

$$
\begin{aligned}
u_{\parallel} + u_{\perp} &= \left(\frac{11}{5}, \frac{22}{5}\right) + \left(\frac{4}{5}, -\frac{2}{5}\right) \\
&= \left(\frac{11 + 4}{5}, \, \frac{22 - 2}{5}\right) \\
&= \left(\frac{15}{5}, \frac{20}{5}\right) \\
&= (3, 4) \\
&= u
\end{aligned}
$$

2. **Second check ($u_{\perp} \cdot v = 0$):**

$$
\begin{aligned}
u_{\perp} \cdot v &= \left(\frac{4}{5}, -\frac{2}{5}\right) \cdot (1, 2) \\
&= \frac{4}{5} \cdot 1 + \left(-\frac{2}{5}\right) \cdot 2 \\
&= \frac{4}{5} - \frac{4}{5} \\
&= 0
\end{aligned}
$$

Both conditions hold identically.

**Step 4: Explain why these are two independent checks of correctness**

An orthogonal decomposition of $u$ relative to $v$ requires **two distinct mathematical properties** to hold simultaneously, and each check tests a different property that the other cannot detect on its own:

1. **What $u = u_{\parallel} + u_{\perp}$ checks (and cannot check):**
   * It verifies **arithmetic consistency of the vector sum**—that no subtraction or fraction error occurred when forming $u_{\perp}$ from $u$ and $u_{\parallel}$, so the two pieces genuinely reassemble back into $u$.
   * **Why it is not enough alone:** Infinitely many pairs of vectors sum to $u$ (for instance, $u = (1, 2) + (2, 2)$ or $u = (2, 4) + (1, 0)$) without the second piece being perpendicular to $v$. Thus, $u = u_{\parallel} + u_{\perp}$ can pass even if the projection scalar $c = \frac{u \cdot v}{v \cdot v}$ was computed completely wrong!
2. **What $u_{\perp} \cdot v = 0$ checks (and cannot check):**
   * It verifies the **geometric orthogonality condition**—that $u_{\perp}$ actually meets the line spanned by $v$ at a $90^\circ$ angle, confirming that the correct projection coefficient $\frac{11}{5}$ was used to remove all of $u$'s component along $v$.
   * **Why it is not enough alone:** Infinitely many vectors are perpendicular to $v = (1, 2)$ (any scalar multiple of $(2, -1)$, such as $(4, -2)$ or $(0, 0)$) without summing with $u_{\parallel}$ to equal $u$. Thus, $u_{\perp} \cdot v = 0$ can pass even if $u_{\perp}$ has the wrong scale or sign.

Together with $u_{\parallel}$ being a scalar multiple of $v$, these two independent checks guarantee that $(u_{\parallel}, u_{\perp})$ is the **unique** orthogonal decomposition of $u$ along and perpendicular to $v$.

**Step 5: Verification**

* **Pythagorean theorem check ($\|u\|^2 = \|u_{\parallel}\|^2 + \|u_{\perp}\|^2$):**
  * $\|u_{\parallel}\|^2 = \left(\frac{11}{5}\right)^2 + \left(\frac{22}{5}\right)^2 = \frac{121 + 484}{25} = \frac{605}{25} = \frac{121}{5}$
  * $\|u_{\perp}\|^2 = \left(\frac{4}{5}\right)^2 + \left(-\frac{2}{5}\right)^2 = \frac{16 + 4}{25} = \frac{20}{25} = \frac{4}{5}$
  * $\|u_{\parallel}\|^2 + \|u_{\perp}\|^2 = \frac{121}{5} + \frac{4}{5} = \frac{125}{5} = 25 = 3^2 + 4^2 = \|u\|^2$

---

### Final Answer

1. **Parallel and perpendicular components of $u = (3, 4)$ relative to $v = (1, 2)$:**

$$
u_{\parallel} = \left(\frac{11}{5}, \frac{22}{5}\right), \qquad u_{\perp} = \left(\frac{4}{5}, -\frac{2}{5}\right)
$$

2. **Verification of both conditions:**
   * **Additivity:** $u_{\parallel} + u_{\perp} = \left(\frac{11}{5}, \frac{22}{5}\right) + \left(\frac{4}{5}, -\frac{2}{5}\right) = \left(\frac{15}{5}, \frac{20}{5}\right) = (3, 4) = u$.
   * **Orthogonality:** $u_{\perp} \cdot v = \left(\frac{4}{5}\right)(1) + \left(-\frac{2}{5}\right)(2) = \frac{4}{5} - \frac{4}{5} = 0$.
3. **Why the two checks are independent:** $u = u_{\parallel} + u_{\perp}$ verifies that the pieces add up to $u$ (which holds for infinitely many non-orthogonal splits, even with a wrong projection scalar), whereas $u_{\perp} \cdot v = 0$ verifies that $u_{\perp}$ is perpendicular to $v$ (which holds for any multiple of $(2, -1)$, regardless of scale). Neither condition implies the other, so passing both confirms the unique orthogonal decomposition.
