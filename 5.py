A=float(input("Ingrese el numero decimal "))
b=A%1
B=round(b,10)
C=A//1
if B == 0 and C!=0:
    print("La parte enteral de numero es:", C, "Y su numero no tiene parte decimal")
elif C == 0 and B!=0:
    print("Su numero no tiene parte entera", "Y su numero no tiene parte decimal", "porque su numero es",A)
else:
    print("La parte entera del numero es:", C,"Y su parte decimal es:", B)
print("Gracias por usar mi programa, ten un buen dia o noche")