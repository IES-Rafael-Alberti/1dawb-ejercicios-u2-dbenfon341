# Ejercicio 2.1.2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
# introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def ejercicio():
    password = "asdf123456"
    check = input("Introduce la contraseña: ")

    if check == password:
        print ("Contraseña correcta.")
    else:
        print ("La contraseña es incorrecta.")
    return


ejercicio()