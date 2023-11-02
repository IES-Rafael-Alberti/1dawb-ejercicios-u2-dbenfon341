# Ejercicio 2.2.7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


def bucle_multiplicacion(num):
    resultado = 0
    i = 1
    while i < 11:
        resultado = i * num
        i = i + 1
        print (resultado)
    return resultado


def main():
    num = int(input("Introduce un número: "))
    bucle_multiplicacion(num)


if __name__ == "__main__":
    main()