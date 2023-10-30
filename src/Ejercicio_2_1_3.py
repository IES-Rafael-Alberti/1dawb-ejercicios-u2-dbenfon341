# Ejercicio 2.1.3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


def numeritosDivision(num1, num2):
    if num2 == 0:
        return print(f"El divisor no debe ser cero.")
    else: 
        return num1 / num2


def main():
    num1 = int(input(f"Introduce un número: "))
    num2 = int(input(f"Introduce otro número: "))
    resultado = numeritosDivision(num1, num2)
    print (f"El resultado de la división es: {resultado}.")


if __name__ == "__main__":
    main()