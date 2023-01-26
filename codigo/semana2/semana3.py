import random

text = "mi lenguaje favorito es python"
print ("python" in text)

"""SLICING"""
print (text[0])
print (len(text))

size = len (text)
print (text [size - 1])

print (text [0:11])
print (text [3:])
print (text [:: -1])

"""JUEGO PIEDRA PAPEL O TIJERA"""

user_op = [piedra, papel, tijera]
computer_op = "piedra"

if user_op == computer_op :
    print ("empate")
elif user_op == "tijera":
    if computer_op == "piedra":
        print ("computer gana")
    else:
        print ("user gana")

 
"""JUEGO PIEDRA PAPEL O TIJERA RANDOM"""

import random
my_computer = ["piedra", "papel", "tijera"]
computer= random.choice (my_computer).lower()
useropcion= input ("ingrese piedra papel o tijera:").lower()

if computer == "piedra" and computer =="papel":
    print("Gano,papel a piedra ")
elif computer == "papel" and useropcion == "tijera!":
     print("Gano,tijera a papel ")
elif computer == "tijera" and useropcion == "piedra":
     print("Gano,piedra a tijera ")
if computer =="papel" and useropcion =="piedra":
     print("perdiste,La computadora gana papel a piedra ")
elif computer == "tijera" and useropcion == "papel":
    print("perdiste,la computadora gana tijera a papel ")
elif computer == "piedra" and useropcion == "tijera":
     print("perdiste,computadora gana piedra a tijera")
elif computer == useropcion:
    print("empate ")

"""ARREGLO DE NUMEROS"""

import random

numbers = [1,2,3,4,5]

fruits = ["manzana", "pera", "banana"]

new_list = numbers + fruits



numbers[0] = "banana"

numbers.append(700)
numbers.insert(0,0)
index=numbers.index(3)
numbers[index]= "change"
print(numbers)

print(random.choice(fruits))
print("mi primer arreglo =>", numbers)
numbers.pop()
numbers.remove(2)

my_random= random.choice(fruits)
print (random.choice(fruits))

# """DESCUENTOS: TRABAJO EN GRUPO"""

numero_escritorios = int(input("Ingrese la cantidad de escritorios: "))
valor_escritorio = int(650000)
valor_compra = (numero_escritorios*valor_escritorio)

if numero_escritorios < 5:
    print("El valor a pagar es",valor_compra - (valor_compra * 0.1))
else:
    if numero_escritorios >= 5 and numero_escritorios < 10:
        print("El valor a pagar es",valor_compra - (valor_compra * 0.2))
    else:
        if numero_escritorios >= 10:
            print("El valor a pagar es",valor_compra - (valor_compra * 0.4))



#CICLOS
#while
# count=0
# While count < 100:
#     count +=1
#     print (count)

# count = 0
# res = 0
# while count < 10:
#     count +=1
#     res = count + res
# print (count)

