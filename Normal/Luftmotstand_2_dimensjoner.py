
# Program som regner ut bevegelen til en legeme som beveger seg med luftmotstand
# Positivt x retning er til høyre og positiv y retning er oppover

import matplotlib.pyplot as plt
import math as math

def two_dim(h_0: float, v0: float, degrees: float, luft: bool):
    g = -9.81    #(m/s^2)
    t_0 = 0
    t = 5
    dt = 0.001  # tidssteg(s)

    N = int(t/dt)    # antall utregninger

    # lister
    x_l = []
    y_l = []

    v_y = math.sin(degrees * math.pi / 180) * v0
    v_x = math.cos(degrees * math.pi / 180) * v0 

    if luft:
       # k, m = map(float, input('Enter the wind resistance variable and weight in kg = ').split()) # luftmotstandkoeffisient +  #(kg)
        k = 0.5
        m = 80
        g = 9.81    #(m/s^2)
        s = 1

        for i in range(0,N):
            L_x = -k*v_x*abs(v_x)      # resistance som alltid peker motsatt retning av fart
            sumF_x = L_x  # sum Force
            a_x = sumF_x / m    # N2L:
            ds = v_x*dt       # change in height
            dv_x = a_x * dt
            
            x_l.append(s)

            s = s + ds
            v_x = v_x + dv_x
        
        
            L_y = -k*v_y*abs(v_y)      # resistance som alltid peker motsatt retning av fart
            sumF_y = L_y - m*g  # sum Force
            a_y = sumF_y / m    # N2L:
            dh = v_y*dt       # change in height
            dv_y = a_y * dt
            
            y_l.append(h_0)

            h_0 = h_0 + dh
            v_y = v_y + dv_y


            

    else:
        def x(t):
            return v_x * t

        def y(t):

            return ((1/2)*g)*t**2 + v_y*t + h_0

        while y(t_0)>= 0:
            x_l.append(x(t_0))
            y_l.append(y(t_0))

            t_0 = t_0 + dt

    plt.figure(1)
    plt.plot(x_l, y_l, 'b-')
    plt.xlabel ('x (m)')
    plt.ylabel ('height (m)')
    plt.grid(1)
    plt.title('Movement')
    plt.show()


def main():
    two_dim(20,20,60,True)


# Check if main
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()