A=int(input("Ingrese el valor del producto sin iva "))
if A>150000:
    B=A+((A*19)/100)
    b=B-((B*5)/100)
    print("El valor a pagar es: ",b)
else:
    C=A+((A*19)/100)
    print("El valor a pagar es: ", C)

