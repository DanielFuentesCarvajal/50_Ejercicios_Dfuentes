a=int(input("Ingrese el año"))

if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print(a,"Es bisiesto")
else:
    print(a,"No es bisiesto")