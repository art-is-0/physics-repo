
from pylab import plot, grid, legend, title, xlabel, ylabel, loadtxt

data = loadtxt("./Periodetid.txt")

tid = data[0,0]
leng = data[1,0]

tid2 = data[0,1]
leng2 = data[1,1]

tid3 = data[0,2]
leng3 = data[1,2]

plot(leng,tid,'bo', label = str(tid) + ' sek , 10 cm')
plot(leng2,tid2,'ro', label = str(tid2) + ' sek , 20 cm')
plot(leng3,tid3,'yo', label = str(tid3) + ' sek , 40 cm')

grid(1)
xlabel("Lengde på tråd")
ylabel("Tid")
title("Periode tid med et lodd")
legend()

