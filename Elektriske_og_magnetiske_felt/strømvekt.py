def main(m: float, I, l:float):
    utreining = (m*(10**(-3))*9.81)/(I*(l*10**(-2)))
    print(f'Utreiningen til F/Il = {utreining} N/am')
    

# Check main
if __name__ == '__main__':
     # This code won't run if this file is imported.
     main(0.80, 3.08, 3.2)