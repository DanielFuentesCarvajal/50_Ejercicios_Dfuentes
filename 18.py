A=int(input("Ingrese los segundos que seran transformados a horas:minutos:segundos "))
H=(A//3600)
H1=A%3600
M=H1//60
M1=H1%60
S=M1
print(H,":", M, ":", S)