**Result:**

The system has infinitely many solutions: $x_1 = 2 + t$, $x_2 = 8 - t$, $x_3 = t$.

The third equation is not independently necessary. It can be derived entirely from the first two equations, meaning it adds no new information to the system.

**Steps & Detailed Explanation:**

Write the equations clearly:
$$
\begin{cases}
x_1 + x_2 = 10 \\
x_2 + x_3 = 8 \\
x_1 - x_3 = 2
\end{cases}
$$

Let's test if the third equation follows from the first two. Subtract the second equation from the first equation:

$$
(x_1 + x_2) - (x_2 + x_3) = 10 - 8
$$

Simplify the left side:

$$
x_1 + x_2 - x_2 - x_3 = 2 \implies x_1 - x_3 = 2
$$

This perfectly matches the third equation. Because the third equation is just a linear combination of the first two, it provides zero new mathematical constraints on the variables. 

We can solve the system using just the first two equations. There are $3$ variables but only $2$ independent equations, leaving $1$ free variable.
Let $x_3 = t$.
From equation 2: $x_2 + t = 8 \implies x_2 = 8 - t$.
From equation 1: $x_1 + (8 - t) = 10 \implies x_1 = 2 + t$.

This describes a line of solutions in 3D space. The third equation is completely redundant.