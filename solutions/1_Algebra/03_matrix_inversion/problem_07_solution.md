### Essential Formulas

**Inverse of a Matrix Product (Reversal Law):**
If $A$ and $B$ are invertible square matrices of the same size, their product $AB$ is also invertible, and the inverse is given by the product of the inverses in reverse order:

$$
(AB)^{-1} = B^{-1} A^{-1}
$$

**Algebraic Proof of the Reversal Law:**
Multiplying $(AB)$ by $(B^{-1} A^{-1})$:

$$
(AB)(B^{-1} A^{-1}) = A (B B^{-1}) A^{-1} = A I A^{-1} = A A^{-1} = I
$$

Similarly:

$$
(B^{-1} A^{-1})(AB) = B^{-1} (A^{-1} A) B = B^{-1} I B = B^{-1} B = I
$$

Because matrix multiplication is non-commutative ($AB \neq BA$), the inner matrices must cancel first, necessitating the reversed order.

---

### Problem Statement

**Exercise 7. Inverse of a Product**

For

$$
A=
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
2 & 0 \\
0 & 3 \\
\end{pmatrix}
$$

compute $(AB)^{-1}$ and $B^{-1}A^{-1}$. Check that the results are the same and explain the meaning of the reversed order.

> **Why this exercise:** reinforces the inverse-of-a-product property and requires its interpretation.

---

### Solution

**Step 1: Compute the product $AB$ and then $(AB)^{-1}$**

Compute the matrix product $AB$:

$$
\begin{aligned}
AB &= \begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
0 & 3 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1(2) + 1(0) & 1(0) + 1(3) \\
0(2) + 1(0) & 0(0) + 1(3) \\
\end{pmatrix} \\
&= \begin{pmatrix}
2 & 3 \\
0 & 3 \\
\end{pmatrix}
\end{aligned}
$$

Compute the determinant of $AB$:

$$
\det(AB) = (2)(3) - (3)(0) = 6
$$

Apply the $2 \times 2$ inverse formula to $AB$:

$$
\begin{aligned}
(AB)^{-1} &= \frac{1}{6} \begin{pmatrix}
3 & -3 \\
0 & 2 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{3}{6} & -\frac{3}{6} \\
0 & \frac{2}{6} \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
\end{aligned}
$$

**Step 2: Compute $A^{-1}$ and $B^{-1}$ separately**

For matrix $A$: $\det A = (1)(1) - (1)(0) = 1$.

$$
A^{-1} = \frac{1}{1} \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}
$$

For matrix $B$ (diagonal matrix): $\det B = (2)(3) - (0)(0) = 6$.

$$
B^{-1} = \frac{1}{6} \begin{pmatrix}
3 & 0 \\
0 & 2 \\
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

**Step 3: Compute $B^{-1} A^{-1}$**

Multiply $B^{-1}$ and $A^{-1}$ in reverse order:

$$
\begin{aligned}
B^{-1} A^{-1} &= \begin{pmatrix}
\frac{1}{2} & 0 \\
0 & \frac{1}{3} \\
\end{pmatrix}
\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2}(1) + 0 & \frac{1}{2}(-1) + 0 \\
0 + \frac{1}{3}(0) & 0 + \frac{1}{3}(1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
\end{aligned}
$$

**Step 4: Compare results and explain the reversed order**

Both matrices are identical:

$$
(AB)^{-1} = B^{-1} A^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$

*Explanation of the reversed order:*
When applying the transformation $AB$ to a vector $x$, matrix $B$ acts first, followed by matrix $A$:
$$
y = A(Bx)
$$
To undo this sequence and recover $x$, one must first undo the last operation that was applied (which is $A$, undone by $A^{-1}$), and only then undo the earlier operation (which is $B$, undone by $B^{-1}$):
$$
x = B^{-1}(A^{-1} y) = (B^{-1} A^{-1}) y
$$
This is the "shoes and socks" principle: you put on socks first, then shoes; but to undo, you must remove the shoes first, then the socks.

---

### Final Answer

$$
(AB)^{-1} = B^{-1} A^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{1}{3} \\
\end{pmatrix}
$$
