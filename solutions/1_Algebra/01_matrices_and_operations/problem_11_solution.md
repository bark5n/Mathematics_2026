### Essential Formulas

**Commuting Matrices:**
Two square matrices $A, B \in \mathbb{R}^{n \times n}$ are said to commute if their product is independent of the order of multiplication:

$$
AB = BA
$$

**Equality of Matrices:**
Two matrices $X = (x_{ij})$ and $Y = (y_{ij})$ of the same size $m \times n$ are equal if and only if every pair of corresponding entries is equal:

$$
X = Y \iff x_{ij} = y_{ij} \quad \forall \, 1 \le i \le m, \; 1 \le j \le n
$$

**Centralizer of a Matrix:**
For a fixed square matrix $A \in \mathbb{R}^{n \times n}$, the set of all matrices $B \in \mathbb{R}^{n \times n}$ satisfying $AB = BA$ forms a subspace (and subalgebra) of $\mathbb{R}^{n \times n}$, which always contains all scalar multiples of $I_n$ and all powers of $A$.

---

### Problem Statement

**Exercise 11. When Do Matrices Commute?**

Given

$$
A = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix},
\qquad
B = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}.
$$

Find the conditions on $a, b, c, d$ under which $AB = BA$. Describe the general form of all such matrices $B$.

> **Why this exercise:** deepens the idea of noncommutativity by finding the conditions under which commutativity does hold.

---

### Solution

**Step 1: Compute $AB$**

Multiply $A$ on the left and $B$ on the right:

$$
\begin{aligned}
AB &= \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot a + 1 \cdot c & 1 \cdot b + 1 \cdot d \\
0 \cdot a + 1 \cdot c & 0 \cdot b + 1 \cdot d \\
\end{pmatrix} \\
&= \begin{pmatrix}
a + c & b + d \\
c & d \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compute $BA$**

Multiply $B$ on the left and $A$ on the right:

$$
\begin{aligned}
BA &= \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
a \cdot 1 + b \cdot 0 & a \cdot 1 + b \cdot 1 \\
c \cdot 1 + d \cdot 0 & c \cdot 1 + d \cdot 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
a & a + b \\
c & c + d \\
\end{pmatrix}
\end{aligned}
$$

**Step 3: Equate $AB$ and $BA$ to find conditions on $a, b, c, d$**

Setting $AB = BA$ yields:

$$
\begin{pmatrix}
a + c & b + d \\
c & d \\
\end{pmatrix}
=
\begin{pmatrix}
a & a + b \\
c & c + d \\
\end{pmatrix}
$$

Matching each of the four corresponding entries produces the system of equations:

$$
\begin{cases}
a + c = a, \\
b + d = a + b, \\
c = c, \\
d = c + d.
\end{cases}
$$

Solving each equation:

* From the $(1, 1)$-entry: $a + c = a \implies c = 0$.
* From the $(1, 2)$-entry: $b + d = a + b \implies d = a$.
* From the $(2, 1)$-entry: $c = c$ holds identically.
* From the $(2, 2)$-entry: $d = c + d \implies c = 0$, consistent with the first condition.

Notice that $b$ cancels out from $b + d = a + b$, so $b \in \mathbb{R}$ can take any real value.

**Step 4: Describe the general form of $B$**

Substituting $c = 0$ and $d = a$ into $B$ shows that every matrix $B$ that commutes with $A$ has the upper triangular form with equal diagonal entries:

$$
B = \begin{pmatrix}
a & b \\
0 & a \\
\end{pmatrix},
\qquad
a, b \in \mathbb{R}
$$

Equivalently, splitting $B$ into its diagonal and strictly upper triangular parts gives:

$$
B = a\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
+ b\begin{pmatrix}
0 & 1 \\
0 & 0 \\
\end{pmatrix}
= (a - b)I + bA
$$

Thus, the matrices commuting with $A$ are precisely all linear combinations of the identity matrix $I$ and $A$ itself (the two-dimensional space of upper triangular Toeplitz matrices of size $2 \times 2$).

**Step 5: Verification**

Substitute the general form $B = \begin{pmatrix} a & b \\ 0 & a \\ \end{pmatrix}$ directly into both products $AB$ and $BA$:

* Product $AB$:

$$
AB = \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
a & b \\
0 & a \\
\end{pmatrix}
= \begin{pmatrix}
1 \cdot a + 1 \cdot 0 & 1 \cdot b + 1 \cdot a \\
0 \cdot a + 1 \cdot 0 & 0 \cdot b + 1 \cdot a \\
\end{pmatrix}
= \begin{pmatrix}
a & a + b \\
0 & a \\
\end{pmatrix}
$$

* Product $BA$:

$$
BA = \begin{pmatrix}
a & b \\
0 & a \\
\end{pmatrix}
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
a \cdot 1 + b \cdot 0 & a \cdot 1 + b \cdot 1 \\
0 \cdot 1 + a \cdot 0 & 0 \cdot 1 + a \cdot 1 \\
\end{pmatrix}
= \begin{pmatrix}
a & a + b \\
0 & a \\
\end{pmatrix}
$$

Both products evaluate to the exact same matrix for all $a, b \in \mathbb{R}$.

---

### Final Answer

1. **Conditions for $AB = BA$:**

$$
c = 0, \qquad a = d, \qquad b \in \mathbb{R}
$$

2. **General form of $B$:** All $2 \times 2$ matrices that commute with $A$ have the form

$$
B = \begin{pmatrix}
a & b \\
0 & a \\
\end{pmatrix}
= aI + b(A - I)
$$

where $a, b \in \mathbb{R}$ are arbitrary real numbers.
