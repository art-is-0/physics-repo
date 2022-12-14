from Integrasjon import omdreining
from math import exp


def main():
    omdreining(1,2, lambda x: exp(x**2))

# Check main
if __name__ == '__main__':
     # This code won't run if this file is imported.
     main()