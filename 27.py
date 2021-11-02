A=float(input("Ingrese el primer numero: "))
B=float(input("Ingrese el segundo numero: "))
if A>B:
    print(A,"es mayor que ", B)
else:
    if A<B:
        print(B,"es mayor que",A)
    else:
        print(A,"y",B,"son el mismo numero")