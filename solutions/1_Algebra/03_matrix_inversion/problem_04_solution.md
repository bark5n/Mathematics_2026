### Essential Formulas

**Gauss–Jordan Inversion Method:**
To compute the inverse of an $n \times n$ matrix $A$, form the augmented matrix $[A \mid I]$ and apply elementary row operations until the left block becomes the identity matrix $I$:

$$
[A \mid I] \xrightarrow{\mathrm{row\ operations}} [I \mid A^{-1}]
$$

**Why this works:**
Each elementary row operation corresponds to multiplying on the left by an elementary matrix $E_k$. When a sequence of operations $E_k \cdots E_2 E_1$ transforms $A$ into $I$:

$$
(E_k \cdots E_2 E_1) A = I \implies E_k \cdots E_2 E_1 = A^{-1}
$$

Applying the exact same operations to the identity matrix on the right produces:

$$
(E_k \cdots E_2 E_1) I = A^{-1}
$$

---

### Problem Statement

**Exercise 4. Gauss–Jordan**

Find $A^{-1}$ using the Gauss–Jordan method for

$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 5 \\
\end{pmatrix}.
$$

Show the augmented matrix $[A\mid I]$ after successive operations and explain why obtaining $I$ on the left gives the inverse on the right.

> **Why this exercise:** introduces the Gauss–Jordan method together with its meaning, not merely as a sequence of operations.

---

### Solution

**Step 1: Set up the augmented matrix $[A \mid I]$**

Place the $2 \times 2$ identity matrix to the right of $A$:

$$
[A \mid I] =
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
3 & 5 & \mid & 0 & 1 \\
\end{pmatrix}
$$

**Step 2: Eliminate the entry in row 2, column 1**

Perform the row operation:
$$
R_2 \leftarrow R_2 - 3R_1
$$

Compute the new row 2:
$$
(3, 5 \mid 0, 1) - 3(1, 2 \mid 1, 0) = (3 - 3, 5 - 6 \mid 0 - 3, 1 - 0) = (0, -1 \mid -3, 1)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & -1 & \mid & -3 & 1 \\
\end{pmatrix}
$$

**Step 3: Normalize the second pivot to $+1$**

Perform the row operation:
$$
R_2 \leftarrow -1 \cdot R_2
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

**Step 4: Eliminate the entry in row 1, column 2**

Perform the row operation:
$$
R_1 \leftarrow R_1 - 2R_2
$$

Compute the new row 1:
$$
(1, 2 \mid 1, 0) - 2(0, 1 \mid 3, -1) = (1 - 0, 2 - 2 \mid 1 - 6, 0 - (-2)) = (1, 0 \mid -5, 2)
$$

The augmented matrix becomes:

$$
\begin{pmatrix}
1 & 0 & \mid & -5 & 2 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

**Step 5: Explain why the right block is $A^{-1}$ and verify**

The left block is now the identity matrix $I$. Each row operation performed is equivalent to multiplying by an elementary matrix $E_i$. Together, these operations form an overall matrix $M = E_3 E_2 E_1$ such that:

$$
M A = I \implies M = A^{-1}
$$

Because the same operations were performed on the right block:

$$
M I = M = A^{-1}
$$

Therefore, the right block is the desired inverse:

$$
A^{-1} = \begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$

*Verification by multiplication:*

$$
A A^{-1} = \begin{pmatrix}
1 & 2 \\
3 & 5 \\
\end{pmatrix}
\begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
= \begin{pmatrix}
1(-5) + 2(3) & 1(2) + 2(-1) \\
3(-5) + 5(3) & 3(2) + 5(-1) \\
\end{pmatrix}
= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
= I
$$

---

### Final Answer

$$
A^{-1} = \begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}
$$
