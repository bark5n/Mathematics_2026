### Problem Statement

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

#### Essential Formulas

1. **Vectors Originating from a Base Point:**
   Given four points $A, B, C, D \in \mathbb{R}^3$, the displacement vectors originating from the base point $A$ are:

   $$
   \overrightarrow{AB} = B - A, \qquad \overrightarrow{AC} = C - A, \qquad \overrightarrow{AD} = D - A
   $$

2. **Normal Vector to the Plane of Three Points:**
   The cross product $n = \overrightarrow{AB} \times \overrightarrow{AC}$ produces a normal vector perpendicular to the plane containing $A, B, C$.

3. **Coplanarity Criterion (Scalar Triple Product):**
   A point $D$ lies in the plane determined by points $A, B, C$ if and only if the displacement vector $\overrightarrow{AD}$ lies in the plane, which requires it to be perpendicular to the normal vector $n$:

   $$
   D \in \mathrm{plane}(A, B, C) \iff \overrightarrow{AD} \cdot n = 0
   $$

   In terms of the scalar triple product, this is equivalent to:

   $$
   (\overrightarrow{AB} \times \overrightarrow{AC}) \cdot \overrightarrow{AD} = 0
   $$

   which states that the volume of the parallelepiped spanned by the three vectors is zero.

---

**Step 1: Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$**

Given the coordinates $A(0, 0, 0)$, $B(1, 2, 0)$, and $C(0, 1, 1)$:

* Construct $\overrightarrow{AB}$:

  $$
  \overrightarrow{AB} = (1 - 0, \ 2 - 0, \ 0 - 0) = (1, \ 2, \ 0)
  $$

* Construct $\overrightarrow{AC}$:

  $$
  \overrightarrow{AC} = (0 - 0, \ 1 - 0, \ 1 - 0) = (0, \ 1, \ 1)
  $$

---

**Step 2: Compute the Normal Vector $n = \overrightarrow{AB} \times \overrightarrow{AC}$**

Compute the components of the cross product:

* First component ($x$):

  $$
  (2)(1) - (0)(1) = 2 - 0 = 2
  $$

* Second component ($y$):

  $$
  (0)(0) - (1)(1) = 0 - 1 = -1
  $$

* Third component ($z$):

  $$
  (1)(1) - (2)(0) = 1 - 0 = 1
  $$

Thus:

$$
n = \overrightarrow{AB} \times \overrightarrow{AC} = (2, \ -1, \ 1)
$$

* **Verification of Orthogonality:**

  $$
  n \cdot \overrightarrow{AB} = (2)(1) + (-1)(2) + (1)(0) = 2 - 2 + 0 = 0
  $$

  $$
  n \cdot \overrightarrow{AC} = (2)(0) + (-1)(1) + (1)(1) = 0 - 1 + 1 = 0
  $$

The normal vector $n = (2, -1, 1)$ is orthogonal to both spanning vectors.

---

**Step 3: Construct $\overrightarrow{AD}$ and Check Whether $\overrightarrow{AD} \cdot n = 0$**

Given $D(2, 5, 1)$ and $A(0, 0, 0)$:

* Construct $\overrightarrow{AD}$:

  $$
  \overrightarrow{AD} = (2 - 0, \ 5 - 0, \ 1 - 0) = (2, \ 5, \ 1)
  $$

* Compute the dot product $\overrightarrow{AD} \cdot n$:

  $$
  \overrightarrow{AD} \cdot n = (2)(2) + (5)(-1) + (1)(1)
  $$

  $$
  \overrightarrow{AD} \cdot n = 4 - 5 + 1 = 0
  $$

The dot product evaluates exactly to $0$.

---

**Step 4: Decision and Justification of the Criterion**

* **Decision:**
  Because $\overrightarrow{AD} \cdot n = 0$, point $D$ **lies in the plane** determined by points $A, B$, and $C$.

* **Justification of the Criterion:**
  1. The cross product $n = \overrightarrow{AB} \times \overrightarrow{AC}$ defines the unique perpendicular (normal) direction to the plane containing $A, B$, and $C$.
  2. Every point $P$ belonging to that plane must satisfy the condition that the displacement vector $\overrightarrow{AP}$ is perpendicular to the normal vector $n$, meaning $\overrightarrow{AP} \cdot n = 0$.
  3. Because the displacement vector $\overrightarrow{AD}$ satisfies $\overrightarrow{AD} \cdot n = 0$, moving from point $A$ (which lies in the plane) along vector $\overrightarrow{AD}$ involves zero motion in the normal direction. Therefore, the terminal point $D$ remains strictly within the plane.
  4. From the perspective of 3D volume, the scalar triple product $(\overrightarrow{AB} \times \overrightarrow{AC}) \cdot \overrightarrow{AD} = 0$ indicates that the 3-dimensional volume of the parallelepiped formed by these three vectors is $0$, which occurs if and only if all three vectors are coplanar.

---

### Final Answer

1. **Constructed Vectors:**

   $$
   \overrightarrow{AB} = (1, \ 2, \ 0), \qquad \overrightarrow{AC} = (0, \ 1, \ 1)
   $$

2. **Normal Vector $n$:**

   $$
   n = \overrightarrow{AB} \times \overrightarrow{AC} = (2, \ -1, \ 1)
   $$

3. **Check with $\overrightarrow{AD}$:**

   $$
   \overrightarrow{AD} = (2, \ 5, \ 1)
   $$

   $$
   \overrightarrow{AD} \cdot n = (2)(2) + (5)(-1) + (1)(1) = 4 - 5 + 1 = 0
   $$

4. **Conclusion and Justification:**
   Point $D$ **lies in the plane** determined by $A, B, C$. The criterion $\overrightarrow{AD} \cdot n = 0$ requires the displacement from $A$ to $D$ to be strictly orthogonal to the normal vector of the plane, which guarantees that $D$ does not deviate from the plane containing $A, B$, and $C$.