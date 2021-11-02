from math import sqrt
print("Ingrese las coordenadas del primer punto")
x1=float(input("x: "))
y1=float(input("y: "))
print("Ingrese las coordenadas del segundo punto")
x2=float(input("x: "))
y2=float(input("y: "))
d=(sqrt(((x2-x1)**2)+((y2-y1)**2)))
print("La distancia entre los dos puntos en el plano cartesiano es de",d)