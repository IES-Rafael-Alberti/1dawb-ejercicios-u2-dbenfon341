# Ejercicio 2.1.4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


def numero_par_impar(num1):
    if num1 % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."


def main():
    numero = int(input(f"Introduce un número: "))
    print (numero_par_impar(numero))


if __name__ == "__main__":
    main()