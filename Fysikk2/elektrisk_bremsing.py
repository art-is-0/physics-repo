# Imports

# Main function
def bremsing(B, l, l_bredde, R, m, v0, T, s0, N):
    """
    B = Flukstetthet/Magnetfeltstyrke \r
    l = høyden på spole-siden \r
    l_bredde = bredden på spolen
    R = Motstand i ledningen \r
    m = Massen på bilen \r
    v0 = Start farten før magnetfeltet \r
    T = Tidsbegrensing
    s0 = Lengden før magnetfeltet
    N = Antall vindinger
    """

    import numpy as np
    import matplotlib.pyplot as plt

    # Definerer en liste med n tidverdier fra 0 til T.
    n = 1000
    t = np.linspace(0,T,n)
    dt = t[1] - t[0]

    # Lager lister for å lagre verdier.
    s = np.zeros(n)
    v = np.zeros(n)
    a = np.zeros(n)

    # Definerer startverdi for farten
    v[0] = v0

    # Definerer en funksjon for kraften som avhenger av posisjonen og farten til lederen.
    def F(s,v):
        # Før magnetfeltet
        if s < s0:
            return 0
        # På vei inn i magnetfeltet.
        elif s < s0 + l_bredde:
            return -(B*l)**2*N*v/R
        # Hele lederen er i feltet
        elif s < s0 + l_bredde*2:
            return 0
        # På vei ut av magnetfeltet.
        elif s < s0 + l_bredde*3:
            return -(B*l)**2*N*v/R
        # Etter magnetfeltet
        else:
            return 0
        
    # Beregner farten med eulermetoden. Akselerasjonen finner vi med
    # Newtons 2. lov for hver lille tidsteg.
    for i in range(n-1):
        a[i] = F(s[i],v[i])/m
        v[i+1] = v[i] + a[i]*dt
        s[i+1]= s[i] + v[i]*dt

    # Tegner akselerasjonsgrafen
    plt.figure(1)
    plt.plot(t[0:n-1], a[0:n-1], 'b-')
    plt.xlabel('$t$/s')
    plt.ylabel('m/s$^2$')
    plt.title('Akselerasjon')
    plt.grid()

    # Tegner fartsgrafen
    plt.figure(2)
    plt.plot(t, v, 'r-')
    plt.xlabel('$t$/s')
    plt.ylabel('(m/s)')
    plt.title('Fart')
    plt.grid()
    plt.show()

def main():
    bremsing(2, 1, 1, 3.0E-4, 1E4, 20, 0.3, 1, 5)
#   bremsing(B, l, l_b, R,     m,  v0, T, s0, N)


# Check main
if __name__ == '__main__':
     # This code won't run if this file is imported.
     main()