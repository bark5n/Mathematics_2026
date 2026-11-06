### Essential Formulas

1. **Relation Between Velocity and Position:**
   Velocity is the instantaneous rate of change of position:

   $$
   v(t) = \frac{ds}{dt} \implies ds = v(t) \, dt
   $$

2. **Displacement (Net Change in Position):**

   $$
   \Delta s = s(t_2) - s(t_1) = \int_{t_1}^{t_2} v(t) \, dt
   $$

3. **Total Distance Traveled vs. Displacement:**
   * **Displacement:** $\int_{t_1}^{t_2} v(t) \, dt$ (accounts for direction; backwards motion cancels forward motion).
   * **Total Distance:** $\int_{t_1}^{t_2} |v(t)| \, dt$ (accumulates total path length non-negatively).
   * When $v(t) \ge 0$ everywhere on $[t_1, t_2]$, displacement and total distance are identical:

     $$
     v(t) \ge 0 \implies \int_{t_1}^{t_2} |v(t)| \, dt = \int_{t_1}^{t_2} v(t) \, dt
     $$

---

### Problem Statement

The velocity of a car during the first five seconds is described by the function

$$
v(t)=4t+2\quad [\mathrm{m/s}].
$$

Compute the distance traveled and explain why the integral of velocity gives the change in position.

Then answer what would have to be changed in the reasoning if the velocity also took negative values.

> **Why this problem:** it connects the integral with accumulation and distinguishes displacement from the actual distance traveled.

---

### Solution

**Step 1: Compute the distance traveled during the first five seconds**

The velocity is $v(t) = 4t + 2\ \mathrm{m/s}$ on the time interval $[0, 5]$.
For all $t \in [0, 5]$:

$$
t \ge 0 \implies 4t + 2 \ge 2 > 0
$$

Because the velocity is strictly positive throughout the entire $5$-second interval, the car moves exclusively forward in one direction. Therefore, the total distance traveled equals the net displacement:

$$
d = \int_0^5 (4t + 2) \, dt
$$

Compute the antiderivative:

$$
d = \left[ 2t^2 + 2t \right]_0^5
$$

Evaluate at the boundary limits:

$$
d = \left(2(5)^2 + 2(5)\right) - \left(2(0)^2 + 2(0)\right) = 2(25) + 10 - 0 = 50 + 10 = 60\ \mathrm{m}
$$

The car travels a distance of $60$ meters.

---

**Step 2: Explain why the integral of velocity gives the change in position**

1. **Velocity as a Differential Ratio:**
   By definition, velocity is the time derivative of the position function $s(t)$:

   $$
   v(t) = s'(t) = \frac{ds}{dt}
   $$

2. **Infinitesimal Displacements:**
   Over an infinitesimal time window of duration $dt$, the car moves by an infinitesimal spatial displacement:

   $$
   ds = v(t) \, dt
   $$

3. **Summation via the Integral:**
   The definite integral sums these uncountably many microscopic displacements across the continuous interval from $t = 0$ to $t = 5$. By the Fundamental Theorem of Calculus:

   $$
   \int_0^5 v(t) \, dt = \int_0^5 s'(t) \, dt = s(5) - s(0) = \Delta s
   $$

   The integral of the rate of change of position produces the net accumulated change in position.

---

**Step 3: What must be changed if velocity takes negative values**

1. **Displacement vs. Distance Distinction:**
   * If $v(t) < 0$ on some subinterval, the vehicle reverses direction and moves backwards toward the starting point.
   * The basic integral $\int_{t_1}^{t_2} v(t) \, dt$ continues to calculate **displacement** (the net vector separation between final position and initial position $s(t_2) - s(t_1)$). The backward motion subtracts from the forward motion.
2. **Adjustment for Total Distance:**
   * To measure **actual distance traveled** (what the vehicle's mechanical odometer records), the speed $|v(t)|$ must be integrated rather than the signed velocity:

     $$
     d_{\mathrm{total}} = \int_{t_1}^{t_2} |v(t)| \, dt
     $$

3. **Computational Procedure:**
   * We would solve $v(t) = 0$ to find the turnaround points where the vehicle reverses direction.
   * We would partition $[t_1, t_2]$ into intervals of positive and negative velocity.
   * On intervals where $v(t) < 0$, we would integrate $-v(t)$ so that the backward distance adds positively to the total:

     $$
     d_{\mathrm{total}} = \int_{v \ge 0} v(t) \, dt + \int_{v < 0} (-v(t)) \, dt
     $$

---

### Final Answer

1. **Distance Traveled:**

   $$
   d = \int_0^5 (4t + 2) \, dt = 60\ \mathrm{m}
   $$

2. **Why the Integral Yields Change in Position:**
   Because $v(t) = \frac{ds}{dt}$, the product $v(t) \, dt = ds$ is an infinitesimal displacement. Integrating these differentials from $t = 0$ to $t = 5$ sums all displacements to produce the net position change $\Delta s = s(5) - s(0)$.

3. **Adjustment for Negative Velocities:**
   * The integral $\int v(t) \, dt$ would give net displacement, allowing backward motion to cancel forward motion.
   * To find total distance traveled, one must integrate speed $|v(t)|$, splitting the integral at the stopping points $v(t) = 0$ and integrating $-v(t)$ when moving backwards.