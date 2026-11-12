### Essential Formulas

**Effect of Row Operations on the Determinant:**
1. **Row Replacement ($R_i \leftarrow R_i + cR_j$):** Adding a multiple of one row to another row **does not change** the value of the determinant.
2. **Row Swap ($R_i \leftrightarrow R_j$):** Swapping two rows multiplies the determinant by $-1$.
3. **Row Scaling ($R_i \leftarrow cR_i$):** Multiplying a row by a nonzero scalar $c$ multiplies the determinant by $c$.

**Determinant of a Triangular Matrix:**
If a square matrix is in upper triangular form (all entries below the main diagonal are zero), its determinant is the simple product of its main diagonal entries.

---

### Problem Statement

**Exercise 11. Shortening the Calculation with Row Operations**

Compute

$$
\det
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

by first performing row operations that create as many zeros as possible. State which operations do not change the determinant.

> **Why this exercise:** develops planning instead of mechanically repeating the same procedure.

---

### Solution

**Step 1: Perform row operations to create zeros in the first column**

Let the original matrix be $A$. We want to transform it into an upper triangular matrix. We can use the pivot $1$ in the $(1,1)$ position to eliminate the $1$s below it. 

Perform the row replacement operations $R_2 \leftarrow R_2 - R_1$ and $R_3 \leftarrow R_3 - R_1$:

$$
\det A =
\det
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
=
\det
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 2 & 3 \\
\end{pmatrix}
$$

* **Property used:** Row replacement ($R_i \leftarrow R_i + cR_j$) leaves the determinant **unchanged**.

**Step 2: Create a zero in the second column**

Now use the pivot $1$ in the $(2,2)$ position to eliminate the $2$ below it. Perform the row replacement operation $R_3 \leftarrow R_3 - 2R_2$:

$$
\det A =
\det
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 2 & 3 \\
\end{pmatrix}
=
\det
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

* **Property used:** Again, row replacement does not change the determinant.

**Step 3: Compute the determinant of the triangular matrix**

The matrix is now in upper triangular form. The determinant of an upper triangular matrix is simply the product of its diagonal entries:

$$
\det A = 1 \cdot 1 \cdot 1 = 1
$$

**Step 4: Verification (Cofactor Expansion)**

To verify the result, we can compute the determinant of the original matrix using cofactor expansion along the first column:

$$
\begin{aligned}
\det
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
&= 1 \cdot \det\begin{pmatrix} 3 & 4 \\ 4 & 6 \end{pmatrix} - 1 \cdot \det\begin{pmatrix} 2 & 3 \\ 4 & 6 \end{pmatrix} + 1 \cdot \det\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix} \\
&= 1(18 - 16) - 1(12 - 12) + 1(8 - 9) \\
&= 1(2) - 1(0) + 1(-1) \\
&= 2 - 0 - 1 \\
&= 1
\end{aligned}
$$

The result perfectly matches the value obtained using row operations.

---

### Final Answer

1. **Determinant value:**

$$
\det
\begin{pmatrix}
1 & 2 & 3 \\
1 & 3 & 4 \\
1 & 4 & 6 \\
\end{pmatrix}
= 1
$$

2. **Operations used and their effects:**
   The matrix was reduced to an upper triangular form $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ using the operations $R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - R_1$, and $R_3 \leftarrow R_3 - 2R_2$. These are all **row replacement operations**, which **do not change the determinant**[cite: 5, 6].
