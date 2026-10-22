**Result:**

$$
\begin{aligned}
RSx &= 
\begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}, 
&
SRx &= 
\begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
\end{aligned}
$$[cite: 10]

The results are different, so the order of the scaling and rotation matters for this vector.[cite: 10]

**Steps & Detailed Explanation:**

The vector is[cite: 10]

$$
x = 
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
$$[cite: 10]

and the matrices are[cite: 10]

$$
\begin{aligned}
S &= 
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}, 
&
R &= 
\begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\end{aligned}
$$[cite: 10]

For $RSx$, apply $S$ first because the rightmost matrix acts first:[cite: 10]

$$
Sx = 
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix} = 
\begin{pmatrix}
2 \\
2 \\
\end{pmatrix}
$$[cite: 10]

Then rotate the scaled vector counterclockwise by $90^\circ$:[cite: 10]

$$
RSx = R(Sx) = 
\begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
2 \\
2 \\
\end{pmatrix} = 
\begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}
$$[cite: 10]

For $SRx$, rotate first:[cite: 10]

$$
Rx = 
\begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix} = 
\begin{pmatrix}
-2 \\
1 \\
\end{pmatrix}
$$[cite: 10]

Next apply the scaling matrix. It doubles the first coordinate and leaves the second coordinate unchanged:[cite: 10]

$$
SRx = S(Rx) = 
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix}
\begin{pmatrix}
-2 \\
1 \\
\end{pmatrix} = 
\begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}
$$[cite: 10]

Geometrically, $S$ stretches horizontally while leaving vertical distances unchanged, whereas $R$ changes which direction is horizontal and which is vertical. If we stretch before rotating, the stretched horizontal component is rotated into the vertical direction. If we rotate first, the vector's horizontal component after rotation is the one that gets stretched. Thus these transformations do not commute: in general, $RS \ne SR$.[cite: 10]