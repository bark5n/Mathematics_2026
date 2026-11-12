### Essential Formulas

**Normal Vector of a Plane from Three Non-Collinear Points:**
Given three non-collinear points $A, B, C \in \mathbb{R}^3$, the vectors $\overrightarrow{AB} = B - A$ and $\overrightarrow{AC} = C - A$ span the plane $\Pi$ passing through $A, B, C$, and their cross product gives a normal vector $n$ perpendicular to $\Pi$:

$$
n = \overrightarrow{AB} \times \overrightarrow{AC} = (u_2 v_3 - u_3 v_2, \; u_3 v_1 - u_1 v_3, \; u_1 v_2 - u_2 v_1)
$$

**Coplanarity Criterion (Scalar Triple Product Condition):**
A fourth point $D \in \mathbb{R}^3$ lies in the plane $\Pi$ determined by $A, B, C$ if and only if the displacement vector $\overrightarrow{AD} = D - A$ is perpendicular to the plane's normal vector $n = \overrightarrow{AB} \times \overrightarrow{AC}$:

$$
D \in \Pi \iff \overrightarrow{AD} \cdot n = \overrightarrow{AD} \cdot (\overrightarrow{AB} \times \overrightarrow{AC}) = 0
$$

*(Equivalently, $\overrightarrow{AD}$ is a linear combination $\overrightarrow{AD} = \alpha \overrightarrow{AB} + \beta \overrightarrow{AC}$ of the two in-plane basis vectors.)*

---

### Problem Statement

**Exercise 13. Do Four Points Lie in One Plane?**

Given

$$
A=(0,0,0),\qquad B=(1,2,0),\qquad C=(0,1,1),\qquad D=(2,5,1).
$$

1. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Find $n=\overrightarrow{AB}\times\overrightarrow{AC}$.
3. Construct $\overrightarrow{AD}$ and check whether $\overrightarrow{AD}\cdot n=0$.
4. Based on this, decide whether $D$ lies in the plane determined by $A,B,C$, and justify the criterion.

> **Why this exercise:** combines the known cross and dot products into a geometric criterion needed for planes, without introducing a separate concept used only once.

---

### Solution

**Step 1: Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$**

Subtract the coordinates of $A = (0, 0, 0)$ from $B = (1, 2, 0)$ and $C = (0, 1, 1)$:

$$
\begin{aligned}
\overrightarrow{AB} &= B - A = (1 - 0, \, 2 - 0, \, 0 - 0) = (1, 2, 0), \\
\overrightarrow{AC} &= C - A = (0 - 0, \, 1 - 0, \, 1 - 0) = (0, 1, 1).
\end{aligned}
$$

Because $(1, 2, 0)$ and $(0, 1, 1)$ are not scalar multiples of each other, $A, B, C$ are non-collinear and uniquely determine a plane $\Pi$ through the origin.

**Step 2: Find $n = \overrightarrow{AB} \times \overrightarrow{AC}$**

Compute the cross product of $\overrightarrow{AB} = (1, 2, 0)$ and $\overrightarrow{AC} = (0, 1, 1)$:

$$
\begin{aligned}
n &= \overrightarrow{AB} \times \overrightarrow{AC} = (1, 2, 0) \times (0, 1, 1) \\
&= \bigl(2 \cdot 1 - 0 \cdot 1, \; 0 \cdot 0 - 1 \cdot 1, \; 1 \cdot 1 - 2 \cdot 0\bigr) \\
&= (2 - 0, \; 0 - 1, \; 1 - 0) \\
&= (2, -1, 1)
\end{aligned}
$$

Since $n = (2, -1, 1) \neq \mathbf{0}$, it is a nonzero normal vector perpendicular to the plane $\Pi$ determined by $A, B, C$.

**Step 3: Construct $\overrightarrow{AD}$ and check whether $\overrightarrow{AD} \cdot n = 0$**

First construct the displacement vector from $A = (0, 0, 0)$ to $D = (2, 5, 1)$:

$$
\overrightarrow{AD} = D - A = (2 - 0, \, 5 - 0, \, 1 - 0) = (2, 5, 1)
$$

Now compute the dot product $\overrightarrow{AD} \cdot n$:

$$
\begin{aligned}
\overrightarrow{AD} \cdot n &= (2, 5, 1) \cdot (2, -1, 1) \\
&= 2 \cdot 2 + 5 \cdot (-1) + 1 \cdot 1 \\
&= 4 - 5 + 1 \\
&= 0
\end{aligned}
$$

Thus, $\overrightarrow{AD} \cdot n = 0$ holds identically.

**Step 4: Decide whether $D$ lies in the plane determined by $A, B, C$ and justify the criterion**

* **Decision:** **Yes — the point $D = (2, 5, 1)$ lies in the plane determined by $A, B, C$** (so all four points $A, B, C, D$ are coplanar).
* **Justification of the criterion ($\overrightarrow{AD} \cdot n = 0$):**
  1. **Geometric normal characterization of a plane:** A plane $\Pi$ passing through point $A$ with normal vector $n = \overrightarrow{AB} \times \overrightarrow{AC} \neq \mathbf{0}$ consists of **all** points $X \in \mathbb{R}^3$ whose displacement vector $\overrightarrow{AX}$ from $A$ is perpendicular to $n$, i.e., $\overrightarrow{AX} \cdot n = 0$.
  2. **Perpendicularity vs. off-plane elevation:** If $D$ did not lie in $\Pi$, the vector $\overrightarrow{AD}$ would have a nonzero component along $n$ (equal to the signed distance from $D$ to $\Pi$ times $\|n\|$), giving $\overrightarrow{AD} \cdot n \neq 0$. Conversely, $\overrightarrow{AD} \cdot n = 0$ shows that $\overrightarrow{AD}$ has zero component perpendicular to the plane—meaning $D$ stays completely inside $\Pi$ and can be written as a linear combination of $\overrightarrow{AB}$ and $\overrightarrow{AC}$.

**Step 5: Verification**

* **Check perpendicularity of $n = (2, -1, 1)$ to $\overrightarrow{AB}$ and $\overrightarrow{AC}$:**
  * $n \cdot \overrightarrow{AB} = (2, -1, 1) \cdot (1, 2, 0) = 2 - 2 + 0 = 0$
  * $n \cdot \overrightarrow{AC} = (2, -1, 1) \cdot (0, 1, 1) = 0 - 1 + 1 = 0$
* **Direct linear-combination verification ($\overrightarrow{AD} = \alpha \overrightarrow{AB} + \beta \overrightarrow{AC}$):**
  Taking $\alpha = 2$ and $\beta = 1$ gives:

$$
2\overrightarrow{AB} + 1\overrightarrow{AC} = 2(1, 2, 0) + 1(0, 1, 1) = (2, 4, 0) + (0, 1, 1) = (2, 5, 1) = \overrightarrow{AD}
$$

  Expressing $\overrightarrow{AD}$ explicitly as $2\overrightarrow{AB} + \overrightarrow{AC}$ proves independently that $D$ lies in the plane spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$ from $A$.

---

### Final Answer

1. **In-plane edge vectors:**

$$
\overrightarrow{AB} = (1, 2, 0), \qquad \overrightarrow{AC} = (0, 1, 1)
$$

2. **Normal vector to the plane:**

$$
n = \overrightarrow{AB} \times \overrightarrow{AC} = (2, -1, 1)
$$

3. **Vector $\overrightarrow{AD}$ and dot-product check:**

$$
\overrightarrow{AD} = (2, 5, 1), \qquad \overrightarrow{AD} \cdot n = (2, 5, 1) \cdot (2, -1, 1) = 4 - 5 + 1 = 0
$$

4. **Coplanarity conclusion and justification:** **Yes**, $D$ lies in the plane determined by $A, B, C$. Because $n = \overrightarrow{AB} \times \overrightarrow{AC}$ is perpendicular to the plane through $A$, a point $D$ belongs to that plane if and only if the displacement vector $\overrightarrow{AD}$ is orthogonal to $n$ ($\overrightarrow{AD} \cdot n = 0$), which holds here (and is further confirmed by $\overrightarrow{AD} = 2\overrightarrow{AB} + \overrightarrow{AC}$).
