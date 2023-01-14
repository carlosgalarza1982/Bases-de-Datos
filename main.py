"""nombre = input ("ingrese su nombre:")
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
"""
igual, aux = 0, 0.
texto = input("Ingrese la palabra que desea evaluar: ")
for 
ind in reversed(range(0, len(texto))):
if texto[ind]. lower() == texto[aux]. lower():
igual += 1.
aux += 1.
if len(texto) == igual:
print("El texto es palindromo!")