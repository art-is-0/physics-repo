'''
Dette er et program som beregner bevegelsen til en gjenstand på 
et skråplan med luftmotstand og friksjon. 
Positiv retning er oppover skråplanet.
'''

from pylab import *
#Definerer konstanter
m = 75  #masse (kg)
g = 9.81 #tyngdeakselerasjon (m/s^2)
k = 10.67 #luftmotstandkoeffisient
mu=0 #friksjonstall
vinkel = radians(7)

#initialbetingelser (startverdier)
t_0 = 0 #startid (s)
s_0 = 0 #starthøyde (m)
v_0 = 8.4 #startfart (m/s)


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
posisjon = []#liste som lagrer posisjon
fart = [] #liste som lagrer fart
akselerasjon = [] #liste som lagrer akselerasjon

#beregner bevegelsen i korte tidsteg
for i in range(0,N):
    #Definere kreftene
    L = -k*v*(v/abs(v)) #luftmotstand som alltid virker mot fartsretningen
    R = -mu*m*g*cos(vinkel)*(v/abs(v)) #friksjon som alltid virker mot fartsretningen
    G = m*g    #summen av kreftene på gjenstanden og akselerasjon
    sumF = G*sin(vinkel)+L+R #summen av kreftene på gjenstanden
    a = sumF/m #Newtons 2. lov
    ds = v * dt #endring i høyde
    dv = a * dt
    
    #lagre verdier i listene
    tid.append(t)
    posisjon.append(s)
    fart.append(v)
    akselerasjon.append(a)
    
    #endrer variablene før ny runde i løkka
    t = t + dt
    s = s + ds
    v = v + dv

print(v)
figure(1) #setter inn en posisjonsgraf
plot(tid,posisjon)
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

