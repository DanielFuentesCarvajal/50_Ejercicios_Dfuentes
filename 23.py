A=float(input("Ingrese el numero: "))
if A>=0:
    if A%2==0:
       print(A,"es un numero par positivo")
    else: 
       print(A, "es un numero impar positivo")
else:
    if A%2==0:
       print(A,"es un numero par negativo")
    else: 
       print(A, "es un numero impar negativo")