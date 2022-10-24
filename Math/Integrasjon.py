# n = 1			# antall rektangler

import math as math

def integral(x_1: int, x_2: int):

	dx = 0.00001

	def f(x):
		return 4/(1+x**2)

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

def main():
	integral(0,1)


# Check if main
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()

