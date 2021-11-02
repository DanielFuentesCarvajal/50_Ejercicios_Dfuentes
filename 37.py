a=int(input("Ingrese el primer numero "))
b=int(input("Ingrese el segundo numero "))
c=int(input("Ingrese el tercer numero "))
if b>a and c>b:
    print("Los numeros estan creciendo")
else:
    if b<a and c<b:
        print("Los numeros estan decreciendo")
    else:
        print("Los numeros no estan ni creciendo ni decreciendo")