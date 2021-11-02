Z=int(input("Si desea ingresar el valor del IVA, escriba 0, si desea ingresar el precio del producto con IVA, escriba 1, y finalmente si desea ingresar el precio del producto sin IVA escriba 2: "))
if Z==0:
    A=int(input("Ingrese el valor del IVA del producto "))
    a=(A*100)/19
    AA=A+a
    print("El valor del producto sin IVA es ", a)
    print("El valor del producto con IVA es ", AA)
elif Z==1:
    B=int(input("Ingrese el precio del producto con IVA"))
    b=B/1.19
    BB=B/(119/19)
    print("El valor del prodcuto sin IVA es ", b)
    print("El valor del IVA es ", BB)
elif Z==2:  
  C=int(input("Ingrese el precio del producto sin IVA "))
  c=C*(19/100)
  CC=C+c
  print("El valor del IVA es:",c)
  print("El valor del producto con IVA incluido", CC)
else:
    print("Numero invalido, reinicie el codigo")
print("Gracias por usar mi programa, ten un buen dia o noche")
