**Result:**

After the three row operations, the matrices are[cite: 9]

$$
\begin{aligned}
A_1 &= 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix}, 
&
A_2 &= 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix}, 
&
A_3 &= 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3 \\
\end{pmatrix}
\end{aligned}
$$[cite: 9]

The inverse operations, in the same order as the original operations they reverse, are:[cite: 9]

1. $R_2 \leftarrow R_2 + 2R_1$.[cite: 9]
2. $R_3 \leftarrow R_3 - R_1$.[cite: 9]
3. Interchange $R_2$ and $R_3$ again.[cite: 9]

**Steps & Detailed Explanation:**

Start with[cite: 9]

$$
A = 
\begin{pmatrix}
1 & 2 & -1 \\
2 & 4 & 1 \\
-1 & 1 & 3 \\
\end{pmatrix}
$$[cite: 9]

**Step 1: Replace $R_2$ by $R_2 - 2R_1$.** The first row stays unchanged. The new second row is[cite: 9]

$$
(2, 4, 1) - 2(1, 2, -1) = (2, 4, 1) - (2, 4, -2) = (0, 0, 3).
$$[cite: 9]

The third row is also unchanged, so[cite: 9]

$$
A_1 = 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix}
$$[cite: 9]

To reverse this operation, add $2R_1$ back to $R_2$: $R_2 \leftarrow R_2 + 2R_1$.[cite: 9]

**Step 2: Replace $R_3$ by $R_3 + R_1$.** The new third row is[cite: 9]

$$
(-1, 1, 3) + (1, 2, -1) = (0, 3, 2).
$$[cite: 9]

Therefore,[cite: 9]

$$
A_2 = 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix}
$$[cite: 9]

Subtracting $R_1$ from $R_3$ restores the previous third row, so the reverse is $R_3 \leftarrow R_3 - R_1$.[cite: 9]

**Step 3: Interchange $R_2$ and $R_3$.** This gives[cite: 9]

$$
A_3 = 
\begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3 \\
\end{pmatrix}
$$[cite: 9]

A swap reverses itself: swapping these two rows once more returns $A_2$.[cite: 9]

Each operation is reversible because adding a multiple of another row can be undone by subtracting that multiple, and an interchange can be undone by repeating it. These reversible changes are useful in elimination because they change a matrix's appearance without losing the ability to recover the previous matrix.[cite: 9]