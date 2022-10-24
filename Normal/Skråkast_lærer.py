"""
Spyder Editor


Created on Thu Nov 11 08:40:22 2021

@author: mattis

Dette er et program som beregner bevegelsen til en gjenstand på 
et skråplan med luftmotstand og friksjon. 
Positiv retning er oppover skråplanet.
"""

from pylab import *
#Definerer konstanter
m = 1.0 #masse (kg)
g = 9.81 #tyngdeakselerasjon (m/s^2)
k = 0.20 #luftmotstandkoeffisient
vinkel = radians(20)

#initialbetingelser (startverdier)
t_0 = 0 #startid (s)
s_0 = array([0,2]) #starthøyde (m)
v_0abs = 2 #startfart (m/s)
v_0 = array([v_0abs*cos(vinkel), v_0abs*sin(vinkel)])

#Lager et tisdvindu og tidssteg
T = 2 #tid vi skal vise (s)
dt = 0.01 #tidssteg (s)
N = int(T/dt) #antall utregninger (oppløsning)

#lager variable
t = t_0
s = s_0
v = v_0

# lager lister som tar vare verdier
tid = [] #liste som lagrer tid
posisjon_x = []#liste som lagrer posisjon
posisjon_y = []#liste som lagrer posisjon
fart = [] #liste som lagrer fart
akselerasjon = [] #liste som lagrer akselerasjon

#beregner bevegelsen i korte tidsteg
for i in range(0,N):
    #Definere kreftene
    L = -k*norm(v)**2*(v/norm(v)) #luftmotstand som alltid virker mot fartsretningen
    G = array([0,-m*g])
    #summen av kreftene på gjenstanden og akselerasjon
    sumF = G+L #summen av kreftene på gjenstanden
    a = sumF/m #Newtons 2. lov
    ds = v * dt #endring i høyde
    dv = a * dt
    
    #lagre verdier i listene
    tid.append(t)
    posisjon_x.append(s[0])
    posisjon_y.append(s[1])
    fart.append(norm(v))
    akselerasjon.append(norm(a))
    
    #endrer variablene før ny runde i løkka
    t = t + dt
    s = s + ds
    v = v + dv

figure(1) #setter inn en posisjonsgraf
plot(posisjon_x, posisjon_y)
#sette navn på akser
xlabel ('tid (s)')
ylabel ('posisjon (m)')
grid()


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