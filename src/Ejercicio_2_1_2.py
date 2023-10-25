# Ejercicio 2.1.2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
# introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def pwd():
    password = "asdf123456"
    check = input("Introduce la contraseña: ")

    if check == password:
        print ("Contraseña correcta.")
    else:
        return print ("La contraseña es incorrecta.")


#def pwd(password):
#    password = input("Introduce una contraseña: ")
#    return password

#def probar_pwd():
    