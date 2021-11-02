from math import sqrt
A=float(input("Ingrese la altura desde la que se lanza el objeto(en metros): "))
B=float(9.80665)
C=round((sqrt((2*A)/B)),4)
print("EL objeto tardara ",C, "segundos en caer")