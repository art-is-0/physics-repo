l = 0.2
R = 0.004
B = 1
m1 = 0.25
m2 = 2
g = 9.81

s = 0
v=1.3
t=0

dt = 0.0001
G = m2*g


while s < 0.2:
    k = ((B*l)**2)/R
    sumF = G-v*k
    a = sumF/(m1+m2)

    v += a*dt
    s += v*dt
    t += dt

print(s,t)