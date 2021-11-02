def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero

numero = int(input("Ingrese el numero a invertir: "))
numero_invertido = invertir_numero(numero)
print(f"El número {numero} es {numero_invertido} al invertirse")