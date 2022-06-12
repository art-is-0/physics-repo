from pylab import plot, grid, legend, figure
import numpy as np


data = np.loadtxt("./Globalvarme.txt")

år = data[:,0]
temp = data[:,1]

figure(1)
plot(år, temp, 'b-' )
grid(1)
legend()
