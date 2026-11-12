### Essential Formulas

**Definition of the Inverse Matrix:**
Let $A \in \mathbb{R}^{n \times n}$ be a square matrix. A square matrix $B \in \mathbb{R}^{n \times n}$ of the same size is called the **inverse** of $A$, denoted $B = A^{-1}$, if multiplying $A$ and $B$ in both orders yields the $n \times n$ identity matrix $I_n$:

$$
AB = I_n \qquad \mathrm{and} \qquad BA = I_n
$$

**The $2 \times 2$ Identity Matrix:**
In $\mathbb{R}^{2 \times 2}$, the identity matrix $I_2$ has $1$s on the main diagonal and $0$s elsewhere:

$$
I_2 = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

**Uniqueness and Symmetry of the Inverse:**
If an inverse matrix $A^{-1}$ exists, it is unique. Furthermore, the relation $AB = BA = I_n$ is symmetric, meaning $B = A^{-1}$ if and only if $A = B^{-1}$.

---

### Problem Statement

**Exercise 1. Definition of the Inverse**

For

$$
A = \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
$$

check, without using a formula, whether $B=A^{-1}$. Compute $AB$ and $BA$ and relate the result to the definition of the inverse.

> **Why this exercise:** starts from the definition of the inverse through multiplication before any formulas or computational methods are introduced.

---

### Solution

**Step 1: Compute the matrix product $AB$**

Multiply $A$ on the right by $B$ using the row-by-column dot-product rule:

$$
\begin{aligned}
AB &= \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 \cdot 1 + 1 \cdot (-1) & 2 \cdot (-1) + 1 \cdot 2 \\
1 \cdot 1 + 1 \cdot (-1) & 1 \cdot (-1) + 1 \cdot 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 - 1 & -2 + 2 \\
1 - 1 & -1 + 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I_2
\end{aligned}
$$

**Step 2: Compute the matrix product $BA$**

Multiply $B$ on the right by $A$ to check the reverse multiplication order:

$$
\begin{aligned}
BA &= \begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot 2 + (-1) \cdot 1 & 1 \cdot 1 + (-1) \cdot 1 \\
(-1) \cdot 2 + 2 \cdot 1 & (-1) \cdot 1 + 2 \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 - 1 & 1 - 1 \\
-2 + 2 & -1 + 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I_2
\end{aligned}
$$

**Step 3: Relate the results to the definition of the inverse**

By definition, a $2 \times 2$ matrix $B$ is the inverse of $A$ if and only if both $AB = I_2$ and $BA = I_2$ hold:

* From Step 1, $AB = I_2$.
* From Step 2, $BA = I_2$.

Because both products equal the $2 \times 2$ identity matrix $I_2$, the matrix $B$ satisfies the definition of the multiplicative inverse of $A$. Therefore, $B = A^{-1}$ (and symmetrically $A = B^{-1}$).

**Step 4: Verification**

* **Action on an arbitrary vector $x = (x_1, x_2)^T \in \mathbb{R}^2$:**
  First apply $A$ to $x$:

$$
Ax = \begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix}
\begin{pmatrix}
x_1 \\
x_2 \\
\end{pmatrix}
= \begin{pmatrix}
2x_1 + x_2 \\
x_1 + x_2 \\
\end{pmatrix}
$$

  Then apply $B$ to the resulting vector $Ax$:

$$
\begin{aligned}
B(Ax) &= \begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2x_1 + x_2 \\
x_1 + x_2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot (2x_1 + x_2) + (-1) \cdot (x_1 + x_2) \\
(-1) \cdot (2x_1 + x_2) + 2 \cdot (x_1 + x_2) \\
\end{pmatrix} \\
&= \begin{pmatrix}
2x_1 + x_2 - x_1 - x_2 \\
-2x_1 - x_2 + 2x_1 + 2x_2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
x_1 \\
x_2 \\
\end{pmatrix} \\
&= x
\end{aligned}
$$

  Since $B$ recovers every vector $x$ after $A$ transforms it (and similarly $A(Bx) = x$), $B$ is confirmed to be $A^{-1}$.

---

### Final Answer

1. **Computed matrix products:**

$$
AB = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} = I_2,
\qquad
BA = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} = I_2
$$

2. **Conclusion from the definition of the inverse:** Yes, $B = A^{-1}$, because multiplying $A$ and $B$ in both orders produces the $2 \times 2$ identity matrix $I_2$.
