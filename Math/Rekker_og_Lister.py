
n = 1

an = 3
extra = 6

# For en reklusiv formel


'''''''''
for i in range(0,10):
    print(f"Figurtall nr {n} er {an}")
    an = an + extra
    extra = extra + 3 
    n = n + 1
'''''''''

# For en eksplisit formel

for i in range(1,10):
    def eks(x):
        return x*2-1
    print(f"Figurtall nr {i} er {eks(i)}")
