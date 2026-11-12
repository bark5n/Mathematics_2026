### Essential Formulas

**Inverse of a Nonzero Scalar Multiple:**
If $A \in \mathbb{R}^{n \times n}$ is invertible and $c \in \mathbb{R}$ is a nonzero scalar ($c \neq 0$), then $cA$ is invertible and:

$$
(cA)^{-1} = \frac{1}{c} A^{-1}
$$

**Inverse of the Transpose:**
If $A \in \mathbb{R}^{n \times n}$ is invertible, then its transpose $A^T$ is also invertible, and taking the inverse commutes with taking the transpose:

$$
(A^T)^{-1} = (A^{-1})^T
$$

**Inverse of a Matrix Power:**
If $A \in \mathbb{R}^{n \times n}$ is invertible and $k \ge 1$ is a positive integer, then $A^k$ is invertible and:

$$
(A^k)^{-1} = (A^{-1})^k
$$

In particular, for $k = 2$, $(A^2)^{-1} = (A^{-1})^2$ (which also follows from the inverse-of-a-product rule $(AB)^{-1} = B^{-1}A^{-1}$ with $B = A$).

---

### Problem Statement

**Exercise 12. Finding Inverses Without Starting from Scratch**

It is known that

$$
A^{-1} = \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}.
$$

Without finding $A$, compute $(3A)^{-1}$, $(A^T)^{-1}$, and $(A^2)^{-1}$. Justify each result using the appropriate property.

> **Why this exercise:** teaches how to use inverse properties instead of carrying out unnecessary full calculations.

---

### Solution

**Step 1: Compute $(3A)^{-1}$ using the scalar multiple property**

* **Property and justification:** For any invertible matrix $A$ and any nonzero scalar $c \neq 0$, we have $(cA)^{-1} = \frac{1}{c} A^{-1}$, because associativity and scalar commutativity give

$$
(cA)\left(\frac{1}{c} A^{-1}\right) = \left(c \cdot \frac{1}{c}\right)(A A^{-1}) = 1 \cdot I_2 = I_2
$$

  and similarly $\left(\frac{1}{c} A^{-1}\right)(cA) = I_2$.

* **Calculation:** Applying this rule with $c = 3$:

$$
\begin{aligned}
(3A)^{-1} &= \frac{1}{3} A^{-1} \\
&= \frac{1}{3}
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compute $(A^T)^{-1}$ using the transpose inverse property**

* **Property and justification:** For any invertible matrix $A$, $(A^T)^{-1} = (A^{-1})^T$, because transposing both sides of $A A^{-1} = I_2$ and using $(XY)^T = Y^T X^T$ gives

$$
(A^{-1})^T A^T = (A A^{-1})^T = I_2^T = I_2
$$

  and similarly $A^T (A^{-1})^T = (A^{-1} A)^T = I_2^T = I_2$.

* **Calculation:** Transposing the given matrix $A^{-1}$ (interchanging rows and columns):

$$
\begin{aligned}
(A^T)^{-1} &= (A^{-1})^T \\
&= \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}^T \\
&= \begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Compute $(A^2)^{-1}$ using the power (product) inverse property**

* **Property and justification:** For any invertible matrix $A$, $(A^2)^{-1} = (A^{-1})^2$, because $(AB)^{-1} = B^{-1}A^{-1}$ with $B = A$ yields $(AA)^{-1} = A^{-1}A^{-1} = (A^{-1})^2$; directly,

$$
A^2 (A^{-1})^2 = A(A A^{-1})A^{-1} = A I_2 A^{-1} = A A^{-1} = I_2
$$

  and similarly $(A^{-1})^2 A^2 = I_2$.

* **Calculation:** Squaring the given matrix $A^{-1}$:

$$
\begin{aligned}
(A^2)^{-1} &= (A^{-1})^2 \\
&= \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot 2 + (-1) \cdot (-3) & 2 \cdot (-1) + (-1) \cdot 2 \\
(-3) \cdot 2 + 2 \cdot (-3) & (-3) \cdot (-1) + 2 \cdot 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
4 + 3 & -2 - 2 \\
-6 - 6 & 3 + 4 \\
\end{pmatrix} \\
&= \begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}
\end{aligned}
$$

**Step 4: Verification**

To verify all three answers independently, recover $A = (A^{-1})^{-1}$ and multiply each transformed matrix by its computed inverse. Since $\det(A^{-1}) = 2 \cdot 2 - (-1)(-3) = 4 - 3 = 1$,

$$
A = (A^{-1})^{-1} = \frac{1}{1}
\begin{pmatrix}
2 & 1 \\
3 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
2 & 1 \\
3 & 2 \\
\end{pmatrix}
$$

* **Verify $(3A)^{-1}$:**

$$
(3A)(3A)^{-1} = \begin{pmatrix}
6 & 3 \\
9 & 6 \\
\end{pmatrix}
\begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix}
= \begin{pmatrix}
4 - 3 & -2 + 2 \\
6 - 6 & -3 + 4 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I_2
$$

* **Verify $(A^T)^{-1}$:**

$$
A^T (A^T)^{-1} = \begin{pmatrix}
2 & 3 \\
1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
4 - 3 & -6 + 6 \\
2 - 2 & -3 + 4 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I_2
$$

* **Verify $(A^2)^{-1}$:**
  First compute $A^2 = \begin{pmatrix} 2 & 1 \\ 3 & 2 \\ \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 3 & 2 \\ \end{pmatrix} = \begin{pmatrix} 7 & 4 \\ 12 & 7 \\ \end{pmatrix}$, and then multiply by $(A^2)^{-1}$:

$$
A^2 (A^2)^{-1} = \begin{pmatrix}
7 & 4 \\
12 & 7 \\
\end{pmatrix}
\begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}
= \begin{pmatrix}
49 - 48 & -28 + 28 \\
84 - 84 & -48 + 49 \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I_2
$$

All three products equal $I_2$, confirming the results.

---

### Final Answer

1. **Computed inverses:**

$$
(3A)^{-1} = \begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix},
\qquad
(A^T)^{-1} = \begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix},
\qquad
(A^2)^{-1} = \begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}
$$

2. **Property justifications:**
   * $(3A)^{-1} = \frac{1}{3} A^{-1}$ by the nonzero scalar multiple inverse rule $(cA)^{-1} = \frac{1}{c} A^{-1}$.
   * $(A^T)^{-1} = (A^{-1})^T$ by the transpose inverse rule.
   * $(A^2)^{-1} = (A^{-1})^2$ by the product/power inverse rule $(AB)^{-1} = B^{-1}A^{-1}$ with $B = A$.
