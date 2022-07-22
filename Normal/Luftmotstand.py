
# Program som regner ut bevegelsen til en gjenstand som faller med luftmotstant, fks en ball
# Positivt retning er oppover

from matplotlib.pyplot import *


# noe_0 = startnoe
t_0 = 0     #(s)
h_0 = 10  #(m)
v_0 = -2     #(m/s)
m = 1       #(kg)
g = 9.81    #(m/s^2)
k = 0.02    # luftmotstandkoeffisient

T = 10      # tid vi skal vise (s)
dt = 0.001  # tidssteg(s)
N = int(T/dt)    # antall utregninger

# variabler
t = t_0
h = h_0
v = v_0

# lister
t_l = []
p_l = []
v_l = []
a_l = []

for i in range(0,N):
    L = -k*v*abs(v)      # resistance som alltid peker motsatt retning av fart
    sumF = L - m*g  # sum Force
    a = sumF / m    # N2L:
    dh = v*dt       # change in height
    dv = a * dt
    
    t_l.append(t)
    p_l.append(h)
    v_l.append(v)
    a_l.append(a)
    
    t = t + dt
    h = h + dh
    v = v + dv
    
#data = np.loadtxt("./Muffinsformer.txt")

#time = data[:,0]
#posision = data[:,1]

#figure(1)
#plot(time, posision, 'ro')

figure(1)
plot(t_l, p_l, 'b-')
xlabel ('time (s)')
ylabel ('height (m)')
grid(1)
title('Height')


figure(2)
plot(t_l, v_l, 'r-')
xlabel ('time (s)')
ylabel ('velocity (m/s)')
grid(1)
title('Velocity')


figure(3)
plot(t_l, a_l, 'g-')
xlabel ('time (s)')
ylabel ('acceleration (m/s^2)')
grid(1)
title('Acceleration')
show()




