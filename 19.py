D=int(input("Ingrese el dinero "))
D100=D//100000
d100=D%100000
D50=d100//50000
d50=d100%50000
D20=d50//20000
d20=d50%20000
D10=d20//10000
d10=d20%10000
D5=d10//5000
d5=d10%5000
D2=d5//2000
d2=d5%2000
D1=d2//1000
d1=d2%1000
print("El minimo numero de billetes de cada tipo para completar este valor seria de      : ",D100," Billetes de 100mil,",D50, "Billetes de 50mil,",D20,"Billetes de 20mil,",D10,"Billetes de 10mil,",D5,"Billetes de 5mil,",D2,"Billetes de 2mil y ",D1,"Billetes de mil")