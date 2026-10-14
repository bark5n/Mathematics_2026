**Result:**

After the three row operations, the matrices are

$$
A_1=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3
\end{pmatrix}
,\qquad
A_2=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2
\end{pmatrix}
,\qquad
A_3=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3
\end{pmatrix}
.
$$

The inverse operations, in the same order as the original operations they reverse, are:

1. $R_2\leftarrow R_2+2R_1$.
2. $R_3\leftarrow R_3-R_1$.
3. Interchange $R_2$ and $R_3$ again.

**Steps & Detailed Explanation:**

Start with

$$
A=
\begin{pmatrix}
1 & 2 & -1 \\
2 & 4 & 1 \\
-1 & 1 & 3
\end{pmatrix}
.
$$

**Step 1: Replace $R_2$ by $R_2-2R_1$.** The first row stays unchanged. The new second row is

$$
(2,4,1)-2(1,2,-1)=(2,4,1)-(2,4,-2)=(0,0,3).
$$

The third row is also unchanged, so

$$
A_1=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix}
.
$$

To reverse this operation, add $2R_1$ back to $R_2$: $R_2\leftarrow R_2+2R_1$.

**Step 2: Replace $R_3$ by $R_3+R_1$.** The new third row is

$$
(-1,1,3)+(1,2,-1)=(0,3,2).
$$

Therefore,

$$
A_2=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix}
.
$$

Subtracting $R_1$ from $R_3$ restores the previous third row, so the reverse is $R_3\leftarrow R_3-R_1$.

**Step 3: Interchange $R_2$ and $R_3$.** This gives

$$
A_3=
\begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3 \\
\end{pmatrix}
.
$$

A swap reverses itself: swapping these two rows once more returns $A_2$.

Each operation is reversible because adding a multiple of another row can be undone by subtracting that multiple, and an interchange can be undone by repeating it. These reversible changes are useful in elimination because they change a matrix's appearance without losing the ability to recover the previous matrix.
