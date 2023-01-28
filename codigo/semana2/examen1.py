print ("Articulos de Tecnologia")

print ("Elija la opción que desea comprar: Computadoras - Celulares - Mostrar")

producto = input("Nombre del producto: ").lower()

if producto == "computadoras":
    
    can_comp = int(input("Ingrese cantidad de computadoras: "))
    pre_comp= int(input("Ingrese precio de la computadora: "))
    val_comp = can_comp*pre_comp
    iva_comp= ((val_comp*12)/100)
    print ("EL valor a cancelar por computadoras es: ", val_comp + iva_comp )

elif producto == "celulares":
    
    can_cel = int(input("Ingrese cantidad de celulares: "))
    pre_cel= int(input("Ingrese precio del celular: "))
    val_cel = can_cel*pre_cel
    desc= ((val_cel*20)/100)
    iva_cel= (((val_cel-desc)*12)/100)
    print ("EL valor a cancelar por celulares es: ", ((val_cel -desc) + iva_cel) )

elif producto == "mostrar":
    
    can_comp = int(input("Ingrese cantidad de computadoras: "))
    pre_comp= int(input("Ingrese precio de la computadora: "))
    val_comp = can_comp*pre_comp
    iva_comp= ((val_comp*12)/100)
    
    can_cel = int(input("Ingrese cantidad de celulares: "))
    pre_cel= int(input("Ingrese precio del celular: "))
    val_cel = can_cel*pre_cel
    iva_cel= ((val_cel*12)/100)

    print ("EL valor a cancelar por computadoras y celulares es: ", val_comp +iva_comp + val_cel + iva_cel )

else: 
    print ("Ingrese una opcion valida") 
