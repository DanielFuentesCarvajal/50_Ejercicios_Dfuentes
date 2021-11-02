K=int(input("Ingrese el numero de km a recorrer "))
D=int(input("Ingrse el numero de dias de estadia"))
if K>1000 and D>7:
    A=K*5000
    B=A-((A*15)/100)
    print("El precio de su boleto es de",B)
else:
    if K<=20:
        print("El precio de su boleto es de 100000")
    else:
        E=K*5000
        print("El precio de su boleto es de",E)