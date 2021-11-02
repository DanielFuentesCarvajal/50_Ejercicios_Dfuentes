def Promedio(a):
    return sum(a)/len(a)

print("ingrese sus 3 numeros")
a=[]
for i in range(0,3):
    b=float(input())
    a.append(b)
promedio=Promedio(a)
print("El promedio de sus numeros es:",promedio)
