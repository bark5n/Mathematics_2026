### Essential Formulas

**Linear Dependence of Vectors:**
A set of vectors $\{v_1, v_2, \dots, v_k\}$ in a vector space is called **linearly dependent** if there exist scalars $c_1, c_2, \dots, c_k$, not all zero, such that:

$$
c_1 v_1 + c_2 v_2 + \dots + c_k v_k = \mathbf{0}
$$

**Proportionality as a Sufficient Condition:**
If any one vector in a set is a scalar multiple of another vector in the same set (i.e., they are proportional, $v_i = c v_j$), then the entire set of vectors is **automatically linearly dependent**, regardless of how many other vectors are in the set.

---

### Problem Statement

**Exercise 7. Linear Dependence Without Lengthy Calculation**

State $u=(1,2,3)$, $v=(2,4,6)$, $w=(0,1,1)$; show $v=2u$ and explain why the three vectors are linearly dependent without lengthy calculation.

> **Why this exercise:** demonstrates that noticing a simple proportional relationship between two vectors bypasses the need to set up and solve a full system of linear equations to prove dependence.

---

### Solution

**Step 1: State the vectors and show that $v = 2u$**

The three given vectors are:

$$
u = (1, 2, 3), \qquad v = (2, 4, 6), \qquad w = (0, 1, 1)
$$

Multiply the vector $u$ by the scalar $2$:

$$
\begin{aligned}
2u &= 2(1, 2, 3) \\
&= (2 \cdot 1, \, 2 \cdot 2, \, 2 \cdot 3) \\
&= (2, 4, 6)
\end{aligned}
$$

Comparing the result with the coordinates of $v$, we see identically that:

$$
v = 2u
$$

**Step 2: Explain why the three vectors are linearly dependent without a lengthy calculation**

By definition, a set of vectors $\{u, v, w\}$ is linearly dependent if we can find scalars $c_1, c_2, c_3$ (where at least one is not zero) such that:

$$
c_1 u + c_2 v + c_3 w = \mathbf{0}
$$

Because we have already established the direct relationship $v = 2u$, we can rewrite this as:

$$
2u - v = \mathbf{0}
$$

To match the formal definition involving all three vectors, we simply add the vector $w$ with a scalar coefficient of $0$:

$$
2u - 1v + 0w = \mathbf{0}
$$

Here, the coefficients are $c_1 = 2$, $c_2 = -1$, and $c_3 = 0$. Since not all coefficients are zero (in fact, $c_1$ and $c_2$ are nonzero), the vectors $u, v$, and $w$ satisfy the exact definition of linear dependence. 

Because two of the vectors are collinear (they lie on the same line through the origin), the entire set is trapped in at most a 2-dimensional plane, rather than spanning a full 3-dimensional space. We deduced this instantly by noticing $v = 2u$, completely avoiding the need to set up a $3 \times 3$ matrix, compute a determinant, or use Gaussian elimination.

---

### Final Answer

1. **Stating vectors and showing proportionality:**
   Given $u = (1, 2, 3)$, multiplying by $2$ yields $2u = (2, 4, 6) = v$. Therefore, $v = 2u$.
2. **Explanation of linear dependence:** 
   Because $v$ is a scalar multiple of $u$, we can form the non-trivial linear combination $2u - v + 0w = \mathbf{0}$. Since the coefficients $(2, -1, 0)$ are not all zero, the set $\{u, v, w\}$ is strictly linearly dependent by definition. No further calculation is required[cite: 13, 14].
