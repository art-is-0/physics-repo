from pylab import plot, grid, legend, figure

km = float(input("How many km/h:  "))

def f(fart):
    return int(fart/3.6)


print(f"speed is {f(km)} m/s")


