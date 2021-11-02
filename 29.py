A=float(input("Ingrese el primer numero "))
B=float(input("Ingrese el segundo numero "))
C=float(input("Ingrese el tercer numero "))
if A>B and A>C:
    if B>C:
        print("Los numeros organizados de mayor a menor son",A,B,C)
    else:
        print("Los numeros organizados de mayor a menor son",A,C,B)
else:
    if B>A and B>C:
        if A>C:
            print("Los numeros organizados de mayor a menor son",B,A,C)
        else:
            print("Los numeros organizados de mayor a menor son",B,C,A)
    else:
        if C>A and C>B:
            if A>B:
                print("Los numeros organizados de mayor a menor son",C,A,B)
            else:
                print("Los numeros organizados de mayor a menor son",C,B,A)