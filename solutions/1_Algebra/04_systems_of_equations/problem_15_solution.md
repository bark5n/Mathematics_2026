**Result:**

- **System 1:** Exactly one solution.
- **System 2:** Infinitely many solutions.
- **System 3:** No solution.

**Steps & Detailed Explanation:**

We use partial elimination to reveal the structure of each system without fully solving for $x$ and $y$.

**System 1:**
$$
\left( \begin{array}{cc|c}
1 & 1 & 2 \\
1 & -1 & 0
\end{array} \right)
$$
Apply $R_2 \leftarrow R_2 - R_1$:
$$
\left( \begin{array}{cc|c}
1 & 1 & 2 \\
0 & -2 & -2
\end{array} \right)
$$
The coefficient matrix has pivots in every column (both $x$ and $y$). There are no contradictions. This structure dictates **exactly one solution**.

**System 2:**
$$
\left( \begin{array}{cc|c}
1 & 1 & 2 \\
2 & 2 & 4
\end{array} \right)
$$
Apply $R_2 \leftarrow R_2 - 2R_1$:
$$
\left( \begin{array}{cc|c}
1 & 1 & 2 \\
0 & 0 & 0
\end{array} \right)
$$
The bottom row becomes $0 = 0$. The system is consistent, but column 2 has no pivot, meaning $y$ is a free variable. This structure dictates **infinitely many solutions**.

**System 3:**
$$
\left( \begin{array}{cc|c}
1 & 1 & 2 \\
2 & 2 & 5
\end{array} \right)
$$
Apply $R_2 \leftarrow R_2 - 2R_1$:
$$
\left( \begin{array}{cc|c}
1 & 1 & 2 \\
0 & 0 & 1
\end{array} \right)
$$
The bottom row reads $0 = 1$, which is a mathematical impossibility. This structure dictates **no solution**.