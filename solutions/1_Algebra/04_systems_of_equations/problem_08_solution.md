**Result:**

The sequence of row operations is identical for both systems because the operations are determined entirely by the coefficient matrix (the left side), which is the same in both cases. Only the numbers in the rightmost column differ.

**Steps & Detailed Explanation:**

Let's trace the elimination for both systems side by side.

**System 1 Augmented Matrix:**
$$
\begin{pmatrix}
2 & 1 & 5 \\
1 & -1 & 1
\end{pmatrix}
$$

**System 2 Augmented Matrix:**
$$
\begin{pmatrix}
2 & 1 & 1 \\
1 & -1 & 4
\end{pmatrix}
$$

To simplify elimination, it is standard practice to swap rows so the pivot is $1$. 

**Step 1:** $R_1 \leftrightarrow R_2$

System 1 becomes:
$$
\begin{pmatrix}
1 & -1 & 1 \\
2 & 1 & 5
\end{pmatrix}
$$

System 2 becomes:
$$
\begin{pmatrix}
1 & -1 & 4 \\
2 & 1 & 1
\end{pmatrix}
$$

**Step 2:** Eliminate the entry below the pivot using $R_2 \leftarrow R_2 - 2R_1$.

For System 1, the new second row is $(2, 1, 5) - (2, -2, 2) = (0, 3, 3)$. For System 2, the new second row is $(2, 1, 1) - (2, -2, 8) = (0, 3, -7)$.

At this point, the left sides of both matrices are exactly:
$$
\begin{pmatrix}
1 & -1 \\
0 & 3
\end{pmatrix}
$$
The elimination steps are dictated purely by the goal of placing zeros below the main diagonal of the coefficient matrix. The right-hand side acts as a passive passenger, undergoing the math but never dictating which row operation to apply.
