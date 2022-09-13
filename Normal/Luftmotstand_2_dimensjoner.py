
# Program som regner ut bevegelen til en legeme som beveger seg med luftmotstand
# Positivt x retning er til høyre og positiv y retning er oppover

import matplotlib.pyplot as plt

def two_dim(t: int, h_0: float, v0_x: float, v0_y: float):
    m = 1       #(kg)
    g = -9.81    #(m/s^2)
    k = 0.5     # luftmotstandkoeffisient

    t_0 = 0
    dt = 0.1  # tidssteg(s)
    N = int(t/dt)    # antall utregninger

    # lister
    x_l = []
    y_l = []

    def x(t):
        return v0_x * t

    def y(t):
        return ((1/2)*g)*t**2 + h_0

    for i in range(0,N):
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
    two_dim(2,10,2,4)

# Check if main
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()