# text = "mi lenguaje favorito es python"
# print ("python" in text)

#Slicing
# print (text[0])
# print (len(text))

# size = len (text)
# print (text [size - 1])

# print (text [0:11])
# print (text [3:])
# print (text [:: -1])

#juego de piedra papel o tijera

# user_op = "piedra"
# computer_op = "piedra"

# if user_op == computer_op :
#     print ("empate")
# elif user_op == "tijera":
#     if computer_op == "piedra":
#         print ("computer gana")
#     else:
#         print ("user gana")

computer = "tijera"
useropcion= "tijera"
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