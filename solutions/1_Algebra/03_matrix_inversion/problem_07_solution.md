### Essential Formulas

**Inverse of a Product of Invertible Matrices:**
If $A, B \in \mathbb{R}^{n \times n}$ are both invertible square matrices of the same size, then their product $AB$ is also invertible, and its inverse is the product of their inverses in **reverse order**:

$$(AB)^{-1} = B^{-1} A^{-1}$$

**Explicit Inverse Formula for a $2 \times 2$ Matrix:**
For a $2 \times 2$ matrix

$$M = \begin{pmatrix} a & b \\ c & d \\ \end{pmatrix}$$

with $\det M = ad - bc \neq 0$, its inverse is:

$$M^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \\ \end{pmatrix}$$

**Associativity of Matrix Multiplication:**
For any matrices $X, Y, Z$ of compatible sizes, $(XY)Z = X(YZ)$, which allows adjacent inverse pairs such as $B$ and $B^{-1}$ to cancel to the identity matrix $I_n$.

---

### Problem Statement

**Exercise 7. Inverse of a Product**

For

$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \\ \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 0 \\ 0 & 3 \\ \end{pmatrix}$$

compute $(AB)^{-1}$ and $B^{-1}A^{-1}$. Check that the results are the same and explain the meaning of the reversed order.

> **Why this exercise:** reinforces the inverse-of-a-product property and requires its interpretation.

---

### Solution

**Step 1: Compute the product $AB$ and its inverse $(AB)^{-1}$**

First multiply $A$ on the right by $B$:

$$\begin{aligned} AB &= \begin{pmatrix} 1 & 1 \\ 0 & 1 \\ \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 3 \\ \end{pmatrix} \\ &= \begin{pmatrix} 1 \cdot 2 + 1 \cdot 0 & 1 \cdot 0 + 1 \cdot 3 \\ 0 \cdot 2 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 3 \\ \end{pmatrix} \\ &= \begin{pmatrix} 2 & 3 \\ 0 & 3 \\ \end{pmatrix} \end{aligned}$$

Compute $\det(AB) = 2 \cdot 3 - 3 \cdot 0 = 6 \neq 0$, and apply the $2 \times 2$ inverse formula to $AB$:

$$\begin{aligned} (AB)^{-1} &= \frac{1}{6} \begin{pmatrix} 3 & -3 \\ 0 & 2 \\ \end{pmatrix} \\ &= \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \\ \end{pmatrix} \end{aligned}$$

**Step 2: Compute $A^{-1}$, $B^{-1}$, and the product $B^{-1}A^{-1}$**

* Find $A^{-1}$ using $\det A = 1 \cdot 1 - 1 \cdot 0 = 1$:

$$A^{-1} = \frac{1}{1} \begin{pmatrix} 1 & -1 \\ 0 & 1 \\ \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \\ \end{pmatrix}$$

* Find $B^{-1}$ using $\det B = 2 \cdot 3 - 0 \cdot 0 = 6$:

$$B^{-1} = \frac{1}{6} \begin{pmatrix} 3 & 0 \\ 0 & 2 \\ \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{3} \\ \end{pmatrix}$$

* Multiply $B^{-1}$ on the right by $A^{-1}$:

$$\begin{aligned} B^{-1} A^{-1} &= \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{3} \\ \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \\ \end{pmatrix} \\ &= \begin{pmatrix} \frac{1}{2} \cdot 1 + 0 \cdot 0 & \frac{1}{2} \cdot (-1) + 0 \cdot 1 \\ 0 \cdot 1 + \frac{1}{3} \cdot 0 & 0 \cdot (-1) + \frac{1}{3} \cdot 1 \\ \end{pmatrix} \\ &= \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \\ \end{pmatrix} \end{aligned}$$

**Step 3: Compare the results and explain the meaning of the reversed order**

Comparing the matrices from Step 1 and Step 2 confirms that they are identical:

$$(AB)^{-1} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \\ \end{pmatrix} = B^{-1} A^{-1}$$

The order of the inverses reverses for two closely connected reasons:

1. **Algebraic cancellation:** For a matrix $X$ to be $(AB)^{-1}$, it must satisfy $(AB)X = I_2$ and $X(AB) = I_2$. Placing $B^{-1}$ immediately next to $B$ allows the inner factors to cancel first by associativity:

$$(AB)(B^{-1}A^{-1}) = A(B B^{-1})A^{-1} = A I_2 A^{-1} = A A^{-1} = I_2$$

   and similarly $(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1} I_2 B = B^{-1}B = I_2$. Because matrix multiplication is noncommutative, the unreversed product $A^{-1}B^{-1}$ traps $B$ between $A$ and $A^{-1}$ so they cannot cancel.

2. **Undoing sequential transformations:** When $AB$ acts on a vector $x$, the matrix $B$ is applied first (scaling $x_1$ by $2$ and $x_2$ by $3$), and $A$ is
