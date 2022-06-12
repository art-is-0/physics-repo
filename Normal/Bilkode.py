from pylab import plot, grid, legend, figure, xlabel, ylabel, title
import numpy as np

data = np.loadtxt("./Bil.txt")

t = data[:,0]
p = data[:,1]

t2 = []
f = []
a = []

y = len(t)

for i in range (0,y):
    t2.append(t[i] - t[0])

# posisjonsgraf
figure(1)
plot(t2, p, 'b-')
grid()
xlabel("Time - s")
ylabel("Posision - m")
title("Movement of a toy car")

for i in range (0,y):
    f.append((p[i]-p[i-1])/(t2[i]-t2[i-1]))
    
# fartsgraf
figure(1)
plot(t2, f, 'r-')
grid()
xlabel("Time - s")
ylabel("Speed - m/s")
title("Speed of a toy car")

for i in range (0,y):
    a.append((f[i]-f[i-1])/(t2[i]-t2[i-1]))
    
# fartsgraf
figure(1)
plot(t2, a, 'y-', )
grid()
xlabel("Time - s")
ylabel("Acceleration - m/s^2")
title("Acceleration of a toy car")




