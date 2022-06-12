from math import sqrt, acos, pi, log


while True:
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    pp = x1*x2+y1*y2
    print(pp)

    if pp == 0:
        print("Vinkelen er vinkelrett")

    elif pp > 0:
        print("Vinkelen er spiss")

    else:
        print("Vinkelen er stump")

    u_l = sqrt(x1**2 + x2**2)
    v_l = sqrt(x2**2 + y2**2)

    cosverdi = pp/(u_l * v_l)
    vinkel = acos(cosverdi) *(360/(2*pi))
    print(round(vinkel,2))
