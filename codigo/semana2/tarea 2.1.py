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

"""numero mayor"""

num1= int(input ("Ingrese el primer numero:"))
num2= int(input ("Ingrese el segundo numero:"))
num3= int(input ("Ingrese el tercer numero:"))
if num2 < num1 > num3:
    print("El numero mayor es:", num1)
elif num1 < num2 > num3:
    print("El numero mayor es:", num2)
elif num1 < num3 > num2:
    print("El numero mayor es:", num3)
else:
     print("ingrese numeros diferentes")

"""ordenacion de tres numeros"""

num1= int(input ("Ingrese el primer numero:"))
num2= int(input ("Ingrese el segundo numero:"))
num3= int(input ("Ingrese el tercer numero:"))
if num1 > num2 and num2 > num3:
    print("El numero mayor es: ",num1, "  El numero medio es: ",num2, "  El numero menor es: ",num3)
elif num2 > num1 and num1 > num3:
    print("El numero mayor es: ",num2, "  El numero medio es: ",num1, "  El numero menor es: ",num3)
elif num3 > num1 and num1 > num2:
    print("El numero mayor es: ",num3, "  El numero medio es: ",num1, "  El numero menor es: ",num2)
elif num3 > num2 and num2 > num1:
    print("El numero mayor es: ",num3, "  El numero medio es: ",num2, "  El numero menor es: ",num1)
elif num1 > num3 and num3 > num2:
  print("El numero mayor es: ",num1, "  El numero medio es: ",num3, "  El numero menor es: ",num2)
elif num2 > num3 and num3 > num1:
  print("El numero mayor es: ",num2, "  El numero medio es: ",num3, "  El numero menor es: ",num1)
else:
     print("ingrese numeros diferentes")

"""numero multiplo de otro"""

num1= int(input ("Ingrese el primer numero:"))
num2= int(input ("Ingrese el segundo numero:"))
if num1 % num2 == 0:
  print ("El numero ", num2, "es multiplo de ", num1)
else:
  print ("El numero ", num2, "no es multiplo de ", num1)

"""año bisiesto"""

num1= int(input ("Ingrese un año: "))

if num1 % 4 == 0 and num1 % 100 !=0 or num1 % 100 == 0 and num1 % 400 == 0:
  print ("El año ", num1, "es bisiesto")
else:
  print ("El año ", num1, "no es bisiesto")
  