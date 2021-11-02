n1=float(input("Ingrsee la nota 1 "))
n2=float(input("Ingrese la nota 2 "))
n3=float(input("Ingrese la nota 3 "))
n4=float(input("Ingrese la nota 4 "))
n5=float(input("Ingrese la nota 5 "))
N=((n1*15)/100)+((n2*20)/100)+((n3*15)/100)+((n4*30)/100)+((n5*20)/100)
if N<2:
    print("Lamento informarle que su nota de",N,"no le permite habilitar")
else:
    if N<3:
        print("Me veo obligado a informarle que con su nota de",N,"a reprobado la materia")
    else:
        if N>=3 and N<4.5:
            print("Con su nota de",N,"a aprobado la materia")
        else:
            print("Con su nota de",N,"a aprobado la materia con una alta calificacion, felicitaciones")
        