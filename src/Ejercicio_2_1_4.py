# Ejercicio 2.1.4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


def numerit(num1):
    if num1 % 2 == 0:
        return print(f"El número es par.")
    else:
        return print(f"El número es impar.")


def main():
    numero = int(input(f"Introduce un número: "))
    numerit(numero)


if __name__ == "__main__":
    main()