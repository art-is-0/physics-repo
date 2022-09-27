
# Program som regner ut bevegelen til en legeme som beveger seg med luftmotstand
# Positivt x retning er til høyre og positiv y retning er oppover

# Imports
import matplotlib.pyplot as plt
import math as math


def two_dim(h_0: float, v0: float, degrees: float, luft: bool, double: bool):

    '''
    A function that plots the movement of an object moving in two dimensions, \r
    it uses matplotlib.pyplot as plt and math as math to do the calculations. 

    The functions plots in degrees, and the speed is following the angle. \r
    h_0 adds a starting height for the movement, luft determains if there \r
    is wind resistance and double if you want to plot with and without \r
    air resistance on a single corrdinate system. 

    Note: for at double works, luft also must be true. 

    Example: two_dim(10, 25, 30, True, False), for a plot with only air \r
    resistance.

    Example: two_dim(10, 25, 30, True, True), for a plot with and without \r
    air resistance.
    '''

    # Values
    g = 9.81    #(m/s^2)
    dt = 0.001  # tidssteg(s)

    h_2 = h_0

    # lists
    x_l = []
    y_l = []
    x_l_2 = []
    y_l_2 = []

    # Speed
    v_y = math.sin(degrees * math.pi / 180) * v0
    v_x = math.cos(degrees * math.pi / 180) * v0 

    v_x_2 = v_x
    v_y_2 = v_y

    # A function that calculates and plots the movement with air resistance

    def luft_f(v_x, v_y, h_0):
       # k, m = map(float, input('Enter the wind resistance variable and weight in kg = ').split()) # luftmotstandkoeffisient +  #(kg)
        k = float(input('What is the air resistance koeffisient: '))
        m = float(input('What is the weight: '))
        s = 0

        while h_0 >= 0:
            L_x = k*v_x*abs(v_x)      # resistance som alltid peker motsatt retning av fart
            sumF_x = -L_x             # sum Force
            a_x = sumF_x / m          # N2L:
            ds = v_x*dt               # change in height
            dv_x = a_x * dt
            
            x_l.append(s)             # Puts the x-value in a list

            s = s + ds
            v_x = v_x + dv_x
        
        
            L_y = -k*v_y*abs(v_y)     # resistance som alltid peker motsatt retning av fart
            sumF_y = L_y - m*g        # sum Force
            a_y = sumF_y / m          # N2L:
            dh = v_y*dt               # change in height
            dv_y = a_y * dt
            
            y_l.append(h_0)           # Puts the y-value in a list

            h_0 = h_0 + dh
            v_y = v_y + dv_y

        # Plots the function with air resistance

        plt.figure(1)
        plt.plot(x_l, y_l, 'b-')
        plt.xlabel ('x (m)')
        plt.ylabel ('height (m)')
        plt.grid(1)
        plt.title('Movement')

    # A function that calculates and plots without air resistance

    def ligninger():       
        t_0 = 0 

        # A function for the x-values 

        def x(t_2):
            return v_x_2 * t_2

        # A function for the y-values 

        def y(t_2):
            return -((1/2)*g)*t_2**2 + v_y_2*t_2 + h_2

        # Adds values to a list until the y-value == 0

        while y(t_0)>= 0:
            x_l_2.append(x(t_0))
            y_l_2.append(y(t_0))

            t_0 = t_0 + dt

        # Plots the movement without air resistance

        plt.figure(1)
        plt.plot(x_l_2, y_l_2, 'r-')
        plt.xlabel ('x (m)')
        plt.ylabel ('height (m)')
        plt.grid(1)
        plt.title('Movement')


    # Simple code for luft and double chooses

    if luft:
        luft_f(v_x, v_y, h_0)

        if double:
            ligninger()

    else:
        ligninger()


    plt.show()


# Testing

def main():
    two_dim(20,20,30,True,True)


# Check if main
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()