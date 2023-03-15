import numpy as np
from numpy.linalg import norm

def kurve_lengde(t_start: float, t_slutt: float):

    def f(t):
        return np.array([2*np.cos(1.2*t)-2, 2*np.sin(1.2*t), 15-0.11*t**2])
    
    lengde = 0
    i = t_start

    dx = 0.001
    # n = (x_slutt - x_start)/dx

    while i < t_slutt:

        vec_A = f(i)
        vec_B = f(i + dx)
        # print(vec_A)
        # print(vec_B)

        vec_AB = vec_B - vec_A

        lengde += norm(vec_AB)
        i += dx

    print(f'Lengden av kurven er {lengde}')
    return lengde


def main():
    kurve_lengde(0, 11.677)

# Check main
if __name__ == '__main__':
     # This code won't run if this file is imported.
     main()