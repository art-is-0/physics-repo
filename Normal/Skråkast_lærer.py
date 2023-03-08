from pylab import *
#Definerer konstanter
m = 0.06 #masse (kg)
g = 9.81 #tyngdeakselerasjon (m/s^2)
k = 0.0011 #luftmotstandkoeffisient
vinkel = radians(45)

#initialbetingelser (startverdier)
t_0 = 0 #startid (s)
v_0abs = 42 #startfart (m/s)
s_0 = array([0,0]) #startposisjon som vektor
v_0= array([v_0abs*cos(vinkel),v_0abs*sin(vinkel)]) #startfart som vektor


#Lager et tisdvindu og tidssteg
T = 5 #tid vi skal vise (s)
dt = 0.01 #tidssteg (s)
N = int(T/dt) #antall utregninger (oppløsning)

#lager variable
t = t_0
s = s_0
v = v_0

# lager lister som tar vare verdier
tid = [] #liste som lagrer tid
posisjon_x = []#liste som lagrer posisjon i x-retning
posisjon_y = []#liste som lagrer posisjon i y-retning
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
plot(posisjon_x,posisjon_y)
#sette navn på akser
xlabel ('posisjon x (m)')
ylabel ('posisjon y (m)')
grid()


# figure(2) #setter inn en fartsgraf
# plot(tid,fart)
# #sette navn på akser
# xlabel ('tid (s)')
# ylabel ('fart (m/s)')
# grid()

# figure(3) #setter inn en akselerasjonsgraf
# plot(tid,akselerasjon)
# #sette navn på akser
# xlabel ('tid (s)')
# ylabel ('akselerasjon (m/s^2)')
# grid()

show()
