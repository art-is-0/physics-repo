

#Dette er et program som beregner bevegelsen til en gjenstand som faller
#med luftmotstand, f.eks en tennisball. 
#Positiv retning er oppover

from pylab import *

#initialbetingelser (startverdier)
t_0 = 1.0 #startid (s)
h_0 = 1 #starthøyde (m)
v_0 = -2.0 #startfart (m/s)
m = 1.0 #masse (kg)
g = 9.81 #tyngdeakselerasjon (m/s^2)
k = 0.20 #luftmotstandkoeffisient
vinkel = radians(20)
myy = 0.2

T = 2 #tid vi skal vise (s)
dt = 0.01 #tidssteg (s)
N = int(T/dt) #antall utregninger (oppløsning)

#lager variable
t = t_0
h = h_0
v = v_0

# lager lister som tar vare verdier
tid = [] #liste som lagrer tid
posisjon = []#liste som lagrer posisjon
fart = [] #liste som lagrer fart
akselerasjon = [] #liste som lagrer akselerasjon

#beregner bevegelsen i korte tidsteg
for i in range(0,N):
    L = -k*v**2*v/abs(v) #luftmotstand som alltid virker mot fartsretningen
    R = -m*g*cos(vinkel)*myy*(v/abs(v))
    sumF = L+m*g*sin(vinkel)+R #summen av kreftene på gjenstanden
    a = sumF/m #Newtons 2. lov
    dh = v * dt #endring i høyde
    dv = a * dt
    
    #lagre verdier i listene
    tid.append(t)
    posisjon.append(h)
    fart.append(v)
    akselerasjon.append(a)
    
    #endrer variablene før ny runde i løkka
    t = t + dt
    h = h + dh
    v = v + dv

figure(1) #setter inn en posisjonsgraf
plot(tid,posisjon)
#sette navn på akser
xlabel ('tid (s)')
ylabel ('høyde (m)')
grid()

"""
#Hente inn data fra forsøk
data=np.loadtxt("muffin.txt")
t_m=data[:,0]
s_m=data[:,1]
#plotte observerte data
plot(t_m,s_m,"ro")
"""

figure(2) #setter inn en fartsgraf
plot(tid,fart)
#sette navn på akser
xlabel ('tid (s)')
ylabel ('fart (m/s)')
grid()

figure(3) #setter inn en akselerasjonsgraf
plot(tid,akselerasjon)
#sette navn på akser
xlabel ('tid (s)')
ylabel ('akselerasjon (m/s^2)')
grid()

show()
