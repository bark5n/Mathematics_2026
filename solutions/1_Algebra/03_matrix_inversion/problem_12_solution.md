### Essential Formulas

**Properties of Matrix Inverses:**
1. **Inverse of a Scalar Multiple:**
   For any nonzero scalar $c \neq 0$:

$$
   (c A)^{-1} = \frac{1}{c} A^{-1}
$$

2. **Inverse of a Transpose:**
   The operations of transposition and inversion commute:

$$
   (A^T)^{-1} = (A^{-1})^T
$$

3. **Inverse of a Matrix Power:**
   For any positive integer $k$:

$$
   (A^k)^{-1} = (A^{-1})^k
$$

   In particular for $k = 2$:

$$
   (A^2)^{-1} = (A^{-1})^2 = A^{-1} A^{-1}
$$

---

### Problem Statement

**Exercise 12. Finding Inverses Without Starting from Scratch**

It is known that

$$
A^{-1}=
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}.
$$

Without finding $A$, compute $(3A)^{-1}$, $(A^T)^{-1}$, and $(A^2)^{-1}$. Justify each result using the appropriate property.

> **Why this exercise:** teaches how to use inverse properties instead of carrying out unnecessary full calculations.

---

### Solution

**Step 1: Compute $(3A)^{-1}$ using the scalar multiple property**

Using the property $(cA)^{-1} = \frac{1}{c} A^{-1}$ with $c = 3$:

$$
\begin{aligned}
(3A)^{-1} &= \frac{1}{3} A^{-1} \\
&= \frac{1}{3} \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix}
\end{aligned}
$$

*Justification:* $(3A)\left(\frac{1}{3}A^{-1}\right) = \left(3 \cdot \frac{1}{3}\right)(A A^{-1}) = 1 \cdot I = I$.

**Step 2: Compute $(A^T)^{-1}$ using the transpose property**

Using the property that inversion and transposition commute, $(A^T)^{-1} = (A^{-1})^T$:

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

*Justification:* $A^T (A^{-1})^T = (A^{-1} A)^T = I^T = I$.

**Step 3: Compute $(A^2)^{-1}$ using the power property**

Using the property $(A^2)^{-1} = (A^{-1})^2 = A^{-1} A^{-1}$:

$$
\begin{aligned}
(A^2)^{-1} &= A^{-1} A^{-1} \\
&= \begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}
\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
(2)(2) + (-1)(-3) & (2)(-1) + (-1)(2) \\
(-3)(2) + (2)(-3) & (-3)(-1) + (2)(2) \\
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

*Justification:* $A^2 (A^{-1})^2 = (A \cdot A)(A^{-1} \cdot A^{-1}) = A (A A^{-1}) A^{-1} = A I A^{-1} = A A^{-1} = I$.

---

### Final Answer

1. Scalar multiple inverse:

$$
(3A)^{-1} = \begin{pmatrix}
\frac{2}{3} & -\frac{1}{3} \\
-1 & \frac{2}{3} \\
\end{pmatrix}
$$

2. Transpose inverse:

$$
(A^T)^{-1} = \begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix}
$$

3. Square inverse:

$$
(A^2)^{-1} = \begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}
$$
