import matplotlib.pyplot as plt
import numpy as np

# Opplysninger:
m = 0.10 # kg
l = 0.20 # m
B = 1.0 # T
R = 0.40 # Ohm
g = 9.81 # m/s**2

def sumF_f(v: float) -> float:
    return m*g - (v * B**2 * l**2)/R

# Startbetingelser
s, v, t, a = 0, 0, 0, 0
s_l, v_l = [], []
# v_l = []
t_l = []
a_l = []
sumF_l = []
s_l.append(s)
v_l.append(v)
t_l.append(t)
a_l.append(a)
sumF_l.append(0)

# endring
dt = 0.001

while t < 8.0:
    sumF = sumF_f(v)
    a = sumF/m

    v += a*dt
    s += v*dt
    t += dt

    s_l.append(s)
    v_l.append(v)
    t_l.append(t)
    a_l.append(a)
    sumF_l.append(sumF)

print(s,v)

plt.figure(0)
plt.plot(t_l, s_l, 'b-')
plt.xlabel ('time (s)')
plt.ylabel ('height (m)')
plt.grid(1)
plt.title('Movement')

plt.figure(1)
plt.plot(t_l, v_l, 'b-')
plt.xlabel ('time (t)')
plt.ylabel ('velocity (m/s)')
plt.grid(1)
plt.title('Speed')

plt.figure(2)
plt.plot(t_l, a_l, 'b-')
plt.xlabel ('time (t)')
plt.ylabel ('acceleration (m/s**2)')
plt.grid(1)
plt.title('Acceleration')

plt.figure(3)
plt.plot(t_l, sumF_l, 'b-')
plt.xlabel ('time (t)')
plt.ylabel ('force (N)')
plt.grid(1)
plt.title('Sum of forces')


plt.show()
    


