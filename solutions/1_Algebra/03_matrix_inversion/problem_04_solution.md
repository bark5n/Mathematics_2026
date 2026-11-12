### Essential Formulas

**Gauss–Jordan Matrix Inversion Algorithm:**
To find the inverse of an invertible $n \times n$ matrix $A$, form the $n \times 2n$ augmented matrix $[A \mid I_n]$ and apply elementary row operations until the left $n \times n$ block is transformed into the identity matrix $I_n$:

$$
\begin{pmatrix}
A & \mid & I_n \\
\end{pmatrix}
\xrightarrow{\mathrm{row\ operations}}
\begin{pmatrix}
I_n & \mid & A^{-1} \\
\end{pmatrix}
$$

If a row of zeros appears on the left side during reduction, then $A$ cannot be reduced to $I_n$ and $A^{-1}$ does not exist.

**Elementary Matrix Representation of Row Operations:**
Every elementary row operation on an $n \times n$ matrix corresponds to multiplication on the left by an $n \times n$ elementary matrix $E_k$. Applying $m$ successive row operations to $[A \mid I_n]$ yields:

$$
E_m \cdots E_2 E_1
\begin{pmatrix}
A & \mid & I_n \\
\end{pmatrix}
=
\begin{pmatrix}
(E_m \cdots E_2 E_1)A & \mid & (E_m \cdots E_2 E_1)I_n \\
\end{pmatrix}
$$

When $(E_m \cdots E_2 E_1)A = I_n$, the product $M = E_m \cdots E_2 E_1$ satisfies $MA = I_n$, so $M = A^{-1}$.

---

### Problem Statement

**Exercise 4. Gauss–Jordan**

Find $A^{-1}$ using the Gauss–Jordan method for

$$
A = \begin{pmatrix}
1 & 2 \\
3 & 5 \\
\end{pmatrix}.
$$

Show the augmented matrix $[A\mid I]$ after successive operations and explain why obtaining $I$ on the left gives the inverse on the right.

> **Why this exercise:** introduces the Gauss–Jordan method together with its meaning, not merely as a sequence of operations.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid I_2]$**

Adjoin the $2 \times 2$ identity matrix $I_2$ to the right of $A$:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
3 & 5 & \mid & 0 & 1 \\
\end{pmatrix}
$$

**Step 2: Eliminate the $(2, 1)$-entry using $R_2 \leftarrow R_2 - 3R_1$**

Use the pivot $1$ in position $(1, 1)$ to create a zero below it by subtracting $3$ times row $1$ from row $2$:

* Left side: $(3, 5) - 3(1, 2) = (3 - 3, 5 - 6) = (0, -1)$
* Right side: $(0, 1) - 3(1, 0) = (0 - 3, 1 - 0) = (-3, 1)$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & -1 & \mid & -3 & 1 \\
\end{pmatrix}
$$

**Step 3: Normalize the second pivot to $1$ using $R_2 \leftarrow -R_2$**

Multiply row $2$ by $-1$ so that the $(2, 2)$-pivot becomes $1$:

* Left side: $-(0, -1) = (0, 1)$
* Right side: $-(-3, 1) = (3, -1)$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

**Step 4: Eliminate the $(1, 2)$-entry using $R_1 \leftarrow R_1 - 2R_2$**

Use the $(2, 2)$-pivot $1$ to create a zero above it by subtracting $2$ times row $2$ from row $1$:

* Left side: $(1, 2) - 2(0, 1) = (1 - 0, 2 - 2) = (1, 0)$
* Right side: $(1, 0) - 2(3, -1) = (1 - 6, 0 - (-2)) = (-5, 2)$

The augmented matrix reaches reduced row echelon form with $I_2$ on the left:

$$
\begin{pmatrix}
1 & 0 & \mid & -5 & 2 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

Reading off the $2 \times 2$ matrix on the right gives:

$$
A^{-1} = \begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$

**Step 5: Explain why obtaining $I$ on the left gives $A^{-1}$ on the right**

There are two equivalent ways to see why reducing $[A \mid I_2]$ to $[I_2 \mid B]$ guarantees $B = A^{-1}$:

1. **Elementary matrix accumulation:** Each elementary row operation acts on both halves of the augmented matrix simultaneously as left-multiplication by an elementary matrix $E_k$. If the product of all elementary matrices used is $M = E_3 E_2 E_1$, then the reduction transforms $[A \mid I_2]$ into $[MA \mid MI_2] = [MA \mid M]$. Because the left block becomes $I_2$, we have $MA = I_2$, which proves $M = A^{-1}$. Consequently, the right block $MI_2 = M$ is automatically $A^{-1}$.
2. **Solving two linear systems at once:** Finding $X = \begin{pmatrix} x_1 & x_2 \\ \end{pmatrix}$ such that $AX = I_2 = \begin{pmatrix} e_1 & e_2 \\ \end{pmatrix}$ means solving $Ax_1 = e_1$ and $Ax_2 = e_2$ simultaneously. Elementary row operations preserve the solution set of each linear system, so transforming $[A \mid e_1 \ e_2]$ into $[I_2 \mid x_1 \ x_2]$ solves $I_2 x_1 = x_1$ and $I_2 x_2 = x_2$, directly displaying the columns of $A^{-1}$ on the right.

**Step 6: Verification**

* **Definition check by matrix multiplication:**

$$
\begin{aligned}
A A^{-1} &= \begin{pmatrix}
1 & 2 \\
3 & 5 \\
\end{pmatrix}
\begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 \cdot (-5) + 2 \cdot 3 & 1 \cdot 2 + 2 \cdot (-1) \\
3 \cdot (-5) + 5 \cdot 3 & 3 \cdot 2 + 5 \cdot (-1) \\
\end{pmatrix} \\
&= \begin{pmatrix}
-5 + 6 & 2 - 2 \\
-15 + 15 & 6 - 5 \\
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix} \\
&= I_2
\end{aligned}
$$

* **Explicit $2 \times 2$ inverse formula check:**
  Since $\det A = 1 \cdot 5 - 2 \cdot 3 = 5 - 6 = -1 \neq 0$,

$$
A^{-1} = \frac{1}{-1}
\begin{pmatrix}
5 & -2 \\
-3 & 1 \\
\end{pmatrix}
= \begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$

  matching the matrix obtained via Gauss–Jordan elimination.

---

### Final Answer

1. **Inverse of $A$:**

$$
A^{-1} = \begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$

2. **Sequence of augmented matrices:**

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
3 & 5 & \mid & 0 & 1 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow R_2 - 3R_1}
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & -1 & \mid & -3 & 1 \\
\end{pmatrix}
\xrightarrow{R_2 \leftarrow -R_2}
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
\xrightarrow{R_1 \leftarrow R_1 - 2R_2}
\begin{pmatrix}
1 & 0 & \mid & -5 & 2 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

3. **Why $I$ on the left yields $A^{-1}$ on the right:** Applying a sequence of elementary row operations corresponds to multiplying both blocks on the left by the same matrix $M$; when $MA = I_2$ appears on the left, $M$ must be $A^{-1}$, so the right block $MI_2 = M$ equals $A^{-1}$.
