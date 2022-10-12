#n = 9**3			# antall rektangler

from math import exp, log

def integral(x_1: int, x_2: int):

	bredde = 0.00001

	def f(x):
		return 9.5*(1-exp(-1.6*x))

	arealN = 0
	arealØ = 0
	areal_l = []


	#bredde = (10 - 1)/n

	n = int((x_2 - x_1)/bredde)


	for i in range(n):

		hoydeN = f(x_1 + i*bredde)
		arealN = arealN + hoydeN*bredde

		hoydeØ = f(x_1+bredde + i*bredde)
		arealØ = arealØ + hoydeØ*bredde


	areal_l.append(round(arealN, 3))
	areal_l.append(round(arealØ, 3))

	print(areal_l)

def main():
	integral(4,5)


# Check if main
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()

