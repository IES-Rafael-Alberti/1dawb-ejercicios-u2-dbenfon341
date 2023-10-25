# Ejercicio 2.1.4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


def ejercicio():
    num1 = int(input("Introduce un número: "))
    if num1 % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
    return


ejercicio()