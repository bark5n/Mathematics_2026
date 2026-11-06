### Essential Formulas

1. **Total Accumulation from a Rate Function:**
   If $r(t)$ is the rate of arrival (units per unit time), the total accumulated quantity $R$ over the time interval $[a, b]$ is given by the definite integral:

   $$
   R = \int_a^b r(t) \, dt
   $$

2. **Average Rate of Arrival:**
   The continuous time-average of the rate function over $[a, b]$ is:

   $$
   r_{\mathrm{avg}} = \frac{1}{b - a} \int_a^b r(t) \, dt = \frac{R}{b - a}
   $$

3. **Trapezoidal Average of a Linear Function:**
   For any affine linear function $r(t) = m t + c$, the continuous average value equals the simple arithmetic mean of the endpoint values:

   $$
   r_{\mathrm{avg}} = \frac{r(a) + r(b)}{2}
   $$

---

### Problem Statement

The rate at which requests arrive at a server during the first 5 minutes is described by the function

$$
r(t)=100+20t\quad [\mathrm{requests/min}],\qquad 0\le t\le5.
$$

1. Compute the total number of requests that arrived during this time.
2. Compute the average rate of incoming requests over this interval.
3. Compare the average rate with the values $r(0)$ and $r(5)$.

> **Why this problem:** it shows the integral as summation of a varying rate in an example directly related to computer science.

---

### Solution

**Step 1: Compute the total number of requests during the first 5 minutes**

The arrival rate is $r(t) = 100 + 20t$ on the interval $[0, 5]$.
The total number of requests $R$ is the integral of the rate function:

$$
R = \int_0^5 (100 + 20t) \, dt
$$

Compute the antiderivative using the power rule:

$$
R = \left[ 100t + 10t^2 \right]_0^5
$$

Evaluate at the limits $t = 5$ and $t = 0$:

$$
R = \left(100(5) + 10(5^2)\right) - \left(100(0) + 10(0^2)\right)
$$

$$
R = 500 + 10(25) - 0 = 500 + 250 = 750
$$

A total of $750$ requests arrived at the server.

---

**Step 2: Compute the average rate of incoming requests**

The length of the time interval is:

$$
b - a = 5 - 0 = 5\ \mathrm{min}
$$

Apply the average value formula:

$$
r_{\mathrm{avg}} = \frac{1}{b - a} \int_a^b r(t) \, dt = \frac{R}{b - a}
$$

Substitute the total requests $R = 750$:

$$
r_{\mathrm{avg}} = \frac{750}{5} = 150\ \mathrm{requests/min}
$$

The average arrival rate over the 5-minute window is $150$ requests per minute.

---

**Step 3: Evaluate $r(0)$ and $r(5)$ and compare with $r_{\mathrm{avg}}$**

1. **Evaluate at the initial time $t = 0$:**

   $$
   r(0) = 100 + 20(0) = 100\ \mathrm{requests/min}
   $$

2. **Evaluate at the final time $t = 5$:**

   $$
   r(5) = 100 + 20(5) = 100 + 100 = 200\ \mathrm{requests/min}
   $$

3. **Compare with the average rate:**
   Calculate the arithmetic mean of the initial and final rates:

   $$
   \frac{r(0) + r(5)}{2} = \frac{100 + 200}{2} = \frac{300}{2} = 150\ \mathrm{requests/min}
   $$

   We observe that:

   $$
   r_{\mathrm{avg}} = \frac{r(0) + r(5)}{2} = 150\ \mathrm{requests/min}
   $$

4. **Mathematical Explanation:**
   Because the arrival rate $r(t) = 100 + 20t$ is a strictly linear function, its rate of growth is constant ($r'(t) = 20$). The region under the graph of $r(t)$ on $[0, 5]$ is a trapezoid with parallel vertical sides of lengths $100$ and $200$.
   The area of a trapezoid is:

   $$
   A_{\mathrm{trap}} = \frac{r(0) + r(5)}{2} \cdot 5 = \frac{100 + 200}{2} \cdot 5 = 150 \cdot 5 = 750
   $$

   Dividing by the width $5$ yields the arithmetic midpoint $150$. For any linear function, the integral average is identical to the average of the two endpoints.

---

### Final Answer

1. **Total Number of Requests:**

   $$
   R = \int_0^5 (100 + 20t) \, dt = 750\ \mathrm{requests}
   $$

2. **Average Rate of Arrival:**

   $$
   r_{\mathrm{avg}} = 150\ \mathrm{requests/min}
   $$

3. **Comparison with Endpoint Values:**
   * $r(0) = 100\ \mathrm{requests/min}$
   * $r(5) = 200\ \mathrm{requests/min}$
   * The average rate equals the arithmetic mean of the endpoints:

     $$
     r_{\mathrm{avg}} = \frac{r(0) + r(5)}{2} = \frac{100 + 200}{2} = 150\ \mathrm{requests/min}
     $$

     This holds generally for any linear rate function due to trapezoidal symmetry.