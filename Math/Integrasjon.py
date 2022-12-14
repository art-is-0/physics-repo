import math as math

def integral(x_1: int, x_2: int, f):
	"""
	integral(1, 2, lambda x: x**2)
	"""

	dx = 0.00001
	# n = 1		# antall rektangler

	arealN = 0
	arealØ = 0
	areal_l = []


	# dx = (x_2 - x_1)/n

	n = int((x_2 - x_1)/dx)


	for i in range(n):

		hoydeN = f(x_1 + i*dx)
		arealN += hoydeN * dx

		hoydeØ = f(x_1+dx + i*dx)
		arealØ += hoydeØ * dx


	areal_l.append(round(arealN, 3))
	areal_l.append(round(arealØ, 3))

	print(areal_l)


def omdreining(a:float, b:float, f):


    n = 10000

    dx = (b-a)/n

    summen = 0

    for i in range(n):
        r = dx * f(a+i*dx)
        summen += r

    print(summen*math.pi)


def main():
	integral(0,1, lambda x: x**2)


# Check if main
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()

