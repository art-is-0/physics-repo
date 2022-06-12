    # Fysikk

Joe = float(input("Hvilken del vil du se? "))

        # variabler

tekststreng = "3.14"
desimaltall = float(tekststreng)

        # Print
def f(x):
    return 3**x
    
if Joe == 1:
    print(f"u weigh {round(f(2.5)*2, 3)} kg, but ur mom she is thick and weighs {f(30)} kg")

        # Input
        
if Joe == 2: 
    dis = float(input("Whut is za distonce? "))
    time =  float(input("Wwut is tha time? "))
    speed = dis/time
    print(f"Za speed was {round(speed, 3)} km/s")
    
        # List
                    # len() sier hvor mange ting det er i lista
                    
                    # print(talliste[0])    #Første element.
                        # print(tekstliste[2])  #Tredje element.
                        # print(tekstliste[-1]) #Siste element.
                        # print(talliste[-4])   #Fjerde siste element.

if Joe == 3:
    n = 0.5
    
    def f(x):
        return 10 /x
    
    List = ["joe", "mama", "thick", "yeet"]
    List2 = []
    while n < 4: 
        List2.append(round(f(n), 4))
        n = n + 1
    
    print(List)
    print(List2)
    
        # Løkke
        
if Joe == 4:
     for i in range(1,10):
         print("Jeg kan en sang som går deg på nervene.")
         print(f"Dette er det {i}. verset, nå er det bare {10-i} igjen!\n")
         
         
        # Funksjoner

if Joe == 5:
    def skrivTakk(navn):
        print(f"Takk, {navn}, for ditt arbeid!")

    skrivTakk("James")
    skrivTakk("Émilie")
    skrivTakk("Lise")

        # Import

if Joe == 6:
    
    import numpy as np
    print("Kvadratroten av 2 er", np.sqrt(2))



        # Lese datafiler
        
if Joe == 7:
    
    import numpy as np
    
    # Here we are assuming the file is stored at the same location from where our 
    # Python code will run (‘./’ represents current directory). If that is not the case
    #, we need to specify the complete path of the file 
    # (Ex: “C://Users/John/Desktop/weight_height_1.txt”)
    
    #Laster inn verdiene fra fil til variabelen data.
    data = np.loadtxt("./test.txt")

    #Regner ut gjennomsnittstemperaturen.
    gjennomsnitt = np.mean(data)
    print("Gjennomsnitt:", round(gjennomsnitt, 1), "grader")

    #Regner ut avviket.
    avvik = (np.max(data) - np.min(data)) / 2
    print("Avvik:", round(avvik, 1), "grader")

    #Finner antall temperaturmålinger
    antall = len(data)
    print("Antall:", antall)
    
    
    
if Joe == 8:
    
    import numpy as np
                        

    #Skilletegnet i datafila er komma og mellomrom.
    data = np.loadtxt("./test.txt", delimiter=", ")

        # : er lik kolone i en liste

    #ti = data[:,0]
    #tid = data[:,1]
    #tide = data[:,2]
    #print(ti, tid, tide)
    #Tiden er alle radene i kolonne 0 (python starter å telle på 0!)
    tid = data[:, 0]

    #Posisjonen er alle radene i kolonne 1.
    posisjon = data[:, 1]

    #print(f"Posisjonen etter {tid[5]} s var {posisjon[5]} m.")
    print(data[:,1])
    
    
    
if Joe == 9:
    from pylab import plot, grid, legend
    
    