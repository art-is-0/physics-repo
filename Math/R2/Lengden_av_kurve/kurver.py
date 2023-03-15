import numpy as np
from numpy.linalg import norm

def curve_length(t_start: float, t_end: float, x: any, y: any, z: any) -> float:
    """
    A function that returns the length of a parameter curve from a \r
    t-value to another t-value. You need to define the x, y and z  \r
    as three different lambda functions. 

    Example: curve_length(1.2, 5.7, lambda t: 2*np.cos(1.2*t)-2, lambda t: 1.2*t, lambda t: -0.11*t**2)

    """
    # Original function, inside of an array
    # def f(t):
    #     return np.array([2*np.cos(1.2*t)-2, 2*np.sin(1.2*t), 15-0.11*t**2])

    # A function to collect all the different lambda functions into a single array
    def f(t):
        return np.array([x(t), y(t), z(t)])
    
    # Values 
    length = 0
    i = t_start
    dx = 0.001          # determines how small the vectors are
    # n = (x_slutt - x_start)/dx

    # while function to collect all the data
    while i < t_end:
        # creating vectors to origo out of the function
        vec_A = f(i)
        vec_B = f(i + dx)

        # creates a vector out of the points
        vec_AB = vec_B - vec_A

        # norm finds the length of the vector and then gets put into a variable
        length += norm(vec_AB)
        i += dx         # increases the value

    return length


def main():
    print(curve_length(0, 11.677, lambda t: 2*np.cos(1.2*t)-2, lambda t: 2*np.sin(1.2*t), lambda t: 15-0.11*t**2))

# Check main
if __name__ == '__main__':
     # This code won't run if this file is imported.
     main()