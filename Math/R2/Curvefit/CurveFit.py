import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def trigonometrisk_modell(x_values, y_values):
    '''
    Du bruker regresjon for å lage en graf til de punktene du har gitt, \r
    a*sin(c*x+phi)+d
    '''

    # defining the function
    def f(x, a, c, phi, d):
        return a*np.sin(c*x+phi)+d

    # defining the constants
    [a,c,phi,d] = curve_fit(f, x_values, y_values)[0]

    print(f'a = {round(a,3)}, c = {round(c,3)}, phi = {round(phi,3)}, d = {round(d, 3)}' )

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[len(x_values)-1],200)
    plt.plot(x, f(x, a, c, phi, d), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()

def trigonometrisk_modell_med_c_og_delt_på_e(x_values, y_values, periode):
    '''
    '''
    c = (2*np.pi)/periode

    # defining the function
    def f(x, A, phi, d, a):
        return (A*np.sin(c*x+phi)+d)*np.exp(-a*x)

    # defining the constants
    [A,phi,d, a] = curve_fit(f, x_values, y_values)[0]

    print(f'A = {round(A,3)}, c = {round(c,3)}, phi = {round(phi,3)}, d = {round(d, 3)}, a = {round(a, 3)}' )

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[-1],500)
    plt.plot(x, f(x, A, phi, d, a), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()


def trigonometrisk_modell_med_c(x_values, y_values, periode):
    # defining the function
    c = (2*np.pi)/periode

    def f(x, a, phi, d):
        return a*np.sin(c*x+phi)+d



    # defining the constants
    [a,phi,d] = curve_fit(f, x_values, y_values)[0]

    print(f'a = {round(a,3)}, phi = {round(phi,3)}, d = {round(d, 3)}' )

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[-1],2000)
    plt.plot(x, f(x, a, phi, d), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()


def lineær_modell(x_values, y_values):
    # defining the function
    def f(x, a, b):
        return a*x + b

    # defining the constants
    [a,b] = curve_fit(f, x_values, y_values)[0]

    print(f'a = {round(a,3)}, b = {round(b, 3)}' )

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[-1],100)
    plt.plot(x, f(x, a, b), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()

def andregradsmodell(x_values, y_values):
    # defining the function
    def f(x, a, b, c):
        return a*x**2 + b*x + c

    # defining the constants
    [a,b,c] = curve_fit(f, x_values, y_values)[0]

    print(f'a = {round(a,3)}, b = {round(b, 3)}, c = {round(c,3)}')

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[-1],100)
    plt.plot(x, f(x, a, b, c), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()

def tredjegradsmodell(x_values, y_values):
    # defining the function
    def f(x, a, b, c, d):
        return a*x**3 + b*x**2 + c*x + d

    # defining the constants
    [a,b,c,d] = curve_fit(f, x_values, y_values)[0]

    print(f'a = {round(a,3)}, b = {round(b, 3)}, c = {round(c,3)}, d = {round(d,3)}')

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[-1],100)
    plt.plot(x, f(x, a, b, c, d), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()

def eksponentiell_modell(x_values, y_values):
    # defining the function
    def f(x, a, b):
        return a*b**x

    # defining the constants
    [a,b] = curve_fit(f, x_values, y_values)[0]

    print(f'a = {round(a,3)}, b = {round(b, 3)}')

    

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[-1],100)
    plt.plot(x, f(x, a, b), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()

def potens_modell(x_values, y_values):
    # defining the function
    def f(x, a, b):
        return a*x**b

    # defining the constants
    [a,b] = curve_fit(f, x_values, y_values)[0]

    def integral(x_1: float, x_2: float):
        dx = 0.00001
        arealN = 0
        areal_l = []
        areal_y = []
        areal_x = []

        n = int((x_2 - x_1)/dx)

        for i in range(n):
            hoydeN = f(x_1 + i*dx, a, b)
            arealN += hoydeN * dx
            areal_y.append(arealN)
            areal_x.append(i*dx+x_1)

        plt.plot(areal_x, areal_y, 'y')

        areal_l.append(round(arealN, 3))
        print(areal_l)

    print(f'a = {round(a,3)}, b = {round(b, 3)}')

    integral(x_values[0], x_values[-1])

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[-1],100)
    plt.plot(x, f(x, a, b), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()


def logistisk_modell(x_values, y_values):
    # defining the function
    def f(x, a, b, C):
        return C/(1 + a*np.exp(-b*x))

    # defining the constants
    [a,b,C] = curve_fit(f, x_values, y_values)[0]

    print(f'a = {round(a,3)}, b = {round(b, 3)}, C = {round(C, 3)}')

    # plotting the data
    plt.plot(x_values, y_values, 'o') 

    # plotting the modell
    x = np.linspace(x_values[0], x_values[-1],100)
    plt.plot(x, f(x, a, b, C), 'r')
    plt.xlabel('Diamenter (mm)')
    plt.ylabel('Resistans')
    plt.grid()
    plt.show()

