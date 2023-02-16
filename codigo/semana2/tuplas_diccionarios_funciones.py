#TUPLAS

opcion = ('piedra', 'papel', 'tijera')
print (opcion[0])
print (type(opcion))

print (opcion.count ('piedra'))
print (opcion.index ('piedra'))
#opcion [0] 'bomba'   #--no se puede realizar esta opcion

opcionv1 = list(opcion)
opcion [0] = 'bomba';

print (opcion[0])
print (opcionv1[0])
print (type(opcion))


#DICCIONARIOS

products = ['mantenimiento', 400, descripcion]


services ['id'] = 2

print (services.items ())
print (services.keys ())
print (services.values ())
print (services ['name'])

del services ['desarrollo de app']

services.pop ('id')
print (services ['tool'][1])

pasajero = [
     {'id':1, 'name': 'cristian', 'address': 'avenida falsa', 'fecha': '2023-02-11'},
     {'id':2, 'name': 'edison', 'address': 'calderon', 'fecha': '2023-02-11'},
     {'id':3, 'name': 'carlos', 'address': 'comite del pueblo', 'fecha': '2023-02-11'},
     {'id':4, 'name': 'josue', 'address': 'solanda', 'fecha': '2023-02-11'},
     {'id':5, 'name': 'david', 'address': 'san rafael', 'fecha': '2023-02-11'}
]


services = {
    'id': 1,
    'name' : 'desarrollo de app',
    'precio' : 400,
    'tool': ['laptop', 'servidores', 'pizarra digital']
 }

print ('id' in services) #busca y devuelve en valor boolean
services ['id'] = 2

services ['tool'].append ('celular') #agrega un campo a la lista tool
print (services)

options = ['pasajeros', 'rutas', 'viaje', 'trayecto', 'estacion' ];
pasajero = [
     {'id':1, 'name': 'cristian', 'address': 'avenida falsa', 'fecha': '2023-02-11'},
     {'id':2, 'name': 'edison', 'address': 'calderon', 'fecha': '2023-02-11'},
     {'id':3, 'name': 'carlos', 'address': 'comite del pueblo', 'fecha': '2023-02-11'},
     {'id':4, 'name': 'josue', 'address': 'solanda', 'fecha': '2023-02-11'},
     {'id':5, 'name': 'david', 'address': 'san rafael', 'fecha': '2023-02-11'}
]

#CICLO  FOR

for elemento in range (0,10):
   print (elemento) 
for elemento in range (1,10): 
    print (elemento)
for elemento in range (1,11):
    print (elemento)

#Ciclo que lee las opciones
for option in options: 
   print (option)

#   TABLA DE MULTIPLICAR

tabla_desde = 1 #tablas del 1...
tabla_hasta = 10 #...al 10
desde = 1 #multiplicaciones desde el 1...
hasta = 10 #...hasta el 10

#tabla de multiplicar
for factor1 in range(tabla_desde, tabla_hasta + 1):
 	print(f'Tabla de multiplicar del {factor1}:') #mostramos una cabecera para cada tabla
for factor2 in range(desde, hasta + 1):
     		print(f'{factor1} x {factor2} = {factor1 * factor2}')
print() #línea en blanco al final de cada tabla

#   MATRIZ
lista1 = [[1,3,5],[2,4,6],[1,2,3]];

for i in lista1:
    print (i)
    for j in i:
        print (j)

for key in pasajero.index():
    print (key['name'])


# FUNCIONES  DEF

num1 = 3;
num2 = 4;

res = num1 + num2
print (res)

def sum():
         print ('Esta es mi primera funcion')
sum();

def sum (n, v, iva=0.12):
     print (n + v + iva)
sum(3, 4);
sum (5,10, 0.14)

# SCOPE

num1 = 10;
res = 0;

def increment(res):  
     num1=0;
     num1 += 10
     print (num1)
 increment (res)

#-----------------------------------------------------------

def increment(res):  
     num1=0;
     res += 10
     return res

res_final = increment(res);
res_finalisima = increment(res_final)

print (res_finalisima)

#------------------------------------------------------------
def increment(res):  
     num1 = 20;
     res += 10
     return res, num1

res_final = increment(res);
res_finalisima = increment(res_final)
respuesta1, respuesta2 = increment(res)

print (respuesta2)

#  SERIE FIBONACCI

def pidenumero () :
  while True :
    n=(int(input("ingrese un numero mayor a 1 : ")))
    if n>1:
        return n

def generafibonacci (n):
    lista=[] 
    for i in range (0,n):
        if i==0 or i==1:
            lista.append(1)
        else:
            lista.append(lista[-2]+lista[-1])
    return lista

def muestralista (lista):
    for i in lista:
        if(i!=lista[-1]):
            print(f"{i}",end="+")
        else:
            print(f"{i}")

n=pidenumero()
lista=generafibonacci(n) 
muestralista(lista)     
