
nombre = input ("ingrese su nombre:")
apellido = input ("ingrese su apellido:")
edad = input ("ingrese su edad:")

fullname = "Mi nombre es:   " + nombre +" Mi apellido es:   " + apellido + " y tengo una edad de:   " + edad
print (fullname)

name1 = "Carlos"
text = "hola como estas   "
nombre = input ("ingrese su nombre:")
print {name1 .upper()}

fulltext = text + nombre
print (fulltext)
fulltextv1 = f "{text} {nombre} ..!"
print (fulltext)
print (fulltextv1)

print {text (0:4)}
print {text (0:9)}

""""condicionales"""

if true : 
    #code
else 
    #code """

"""if anidados"""
elif true :
    #code
    elif true :
        #code
        elif true :
            #code
else 
    #code"""

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