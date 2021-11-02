from math import sqrt
class ecuacion():
    def __init__(self):
        self.interfaz()
    def calcular(self, A, B, C):
        if ((B**2)-4*A*C) < 0:
            print("La solución de la ecuación es con números complejos")
        else:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
            print("""\
Las soluciones de la ecuación son:
x1 = {}
x2 = {} """.format(x1, x2))
    def interfaz(self):
        print("Para la ecuación ax2 + bx + c")
        A = int(input("Ingrese a "))
        B = int(input("Ingrese b "))
        C = int(input("Ingrese c " ))
        
        self.calcular(A, B, C)
ecuacion()