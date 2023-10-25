# Ejercicio 2.1.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


def ejercicio():
    edad = int(input("Escribe tu edad: "))
    if edad < 18:
        print ("Eres menor de edad.")
    else:
        print ("Eres mayor de edad.")
    return


ejercicio()