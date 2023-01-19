"""numero par"""

num1 = int (input("Digite un numero:"))
if num1%2==0:
    print ("el numero es par")
else :
    print ("el numero no es par")

"""numero primo"""

numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1 
if contador > 0 :
  print("El número no es primo" )
else:
  print("El nÚmero es primo")