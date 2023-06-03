t = 0
dt = 0.0001
g = 9.81
k = 4.878
s = 0
v = 0

while t < 0.4:    
    s = s + v*dt    
    a = g - k*v    
    v = v + a*dt
    t = t + dt

# while t < 2:    
#     s = s + v*dt    
#     a = g - k*v    
#     v = v + a*dt
#     if s >= 1.2:
#         print(t)
#         break
#     t = t + dt

C = 0.5*0.2/0.041
I = v*C
print(I)

print(s, v)