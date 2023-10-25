# Ejercicio 2.1.3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


def ejercicio():
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    if num2 == 0:
        print("El divusir no puede ser 0.")
    else:
        print(f"La división es: {num1/num2}.")
    return


ejercicio()