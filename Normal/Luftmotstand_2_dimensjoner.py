
# Program som regner ut bevegelen til en legeme som beveger seg med luftmotstand
# Positivt x retning er til høyre og positiv y retning er oppover

# Imports
import this
import matplotlib.pyplot as plt
import math as math
import numpy as np
from numpy.linalg import norm


def two_dim(h_0: float, s_y: float, v0: float, degrees: float, luft: bool, double: bool):

    '''
    A function that plots the movement of an object moving in two dimensions, \r
    it uses matplotlib.pyplot as plt and math as math to do the calculations. 

    The functions plots in degrees, and the speed is following the angle. \r
    h_0 adds a starting height for the movement, luft determains if there \r
    is wind resistance and double if you want to plot with and without \r
    air resistance on a single corrdinate system. 

    Note: for at double works, luft also must be true. 

    Example: two_dim(10, 0, 25, 30, True, False), for a plot with only air \r
    resistance.

    Example: two_dim(10, 0, 25, 30, True, True), for a plot with and without \r
    air resistance.
    '''

    # Values
    g = 9.81    #(m/s^2)
    dt = 0.001  # tidssteg(s)


    h_2 = h_0
    h_0_arr = np.array([0, h_0])

    # lists
    x_l = []
    y_l = []
    x_l_2 = []
    y_l_2 = []
    v_l = []
    a_l = []
    t_l = []

    # Speed
    v_y = math.sin(degrees * math.pi / 180) * v0
    v_x = math.cos(degrees * math.pi / 180) * v0 
    v_0 = np.array([v_x, v_y])
    v = v_0



    # A function that calculates and plots the movement with air resistance

    def luft_f(v, h_0):
       # k, m = map(float, input('Enter the wind resistance variable and weight in kg = ').split()) # luftmotstandkoeffisient +  #(kg)
        # k = float(input('What is the air resistance koeffisient: '))
        # m = float(input('What is the weight: '))
        k = 0.2
        m = 10
        s = 0
        t = 0
        s_0 = 0

        while h_0[1] >= s_0:
            L = -k*norm(v)*abs(norm(v))      # resistance som alltid peker motsatt retning av fart
            G = np.array([0,-m*g])
            sumF = G + L             # sum Force
            a = sumF / m          # N2L:

            dh = v*dt               # change in s
            dv = a * dt
            
            t_l.append(t)
            x_l.append(h_0[0])
            y_l.append(h_0[1])
            v_l.append(norm(v))
            a_l.append(norm(a))
            
            h_0 = h_0 + dh
            v = v + dv
            t += dt


            if h_0[1] < s_y and dh[1] <= 0:
                s_0 = s_y
        
        print(h_0[1])

        # Plots the function with air resistance

        plt.figure(1)
        plt.plot(x_l, y_l, 'b-')
        plt.xlabel ('x (m)')
        plt.ylabel ('height (m)')
        plt.grid(1)
        plt.title('Movement')

        plt.figure(2) #setter inn en fartsgraf
        plt.plot(t_l, v_l, 'b-')
        #sette navn på akser
        plt.xlabel ('time (s)')
        plt.ylabel ('speed (m/s)')
        plt.grid()
        plt.title('Speed')

        plt.figure(3) #setter inn en akselerasjonsgraf
        plt.plot(t_l, a_l)
        #sette navn på akser
        plt.xlabel ('time (s)')
        plt.ylabel ('acceleration (m/s^2)')
        plt.grid()
        plt.title('Acceleration')

    # A function that calculates and plots without air resistance

    def ligninger():       
        t_0 = 0 
        s_0 = 0

        # A function for the x-values 

        def x(t_2):
            return v_x * t_2

        # A function for the y-values 

        def y(t_2):
            return -((1/2)*g)*t_2**2 + v_y*t_2 + h_2

        # Adds values to a list until the y-value == 0

        while y(t_0)>= s_0:
            x_l_2.append(x(t_0))
            y_l_2.append(y(t_0))

            t_0 += dt

            if y(t_0) < s_y and y(t_0)-y(t_0 - 1) <= 0:
                s_0 = s_y

        # Plots the movement without air resistance

        plt.figure(1)
        plt.plot(x_l_2, y_l_2, 'r-')
        plt.xlabel ('x (m)')
        plt.ylabel ('height (m)')
        plt.grid(1)
        plt.title('Movement')


    # Simple code for luft and double chooses

    if luft:
        luft_f(v, h_0_arr)

        if double:
            ligninger()

    else:
        ligninger()


    plt.show()


# Testing

def main():
<<<<<<< HEAD
    two_dim(2,3,5,45,True,True)
=======
    two_dim(2,5,20,45,True,True)
>>>>>>> 0dd9444c2b87576aad069595eaa5730f90cc67b8


# Check if main
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()