# Ejercicio 2.2.1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


def bucle_palabra(palabra):
    resultado = ""
    cont = 0
    while cont < 10:
        resultado = (resultado + palabra) + " \n"
        cont = cont + 1
    return resultado


def main():
    palabra = input("Introduce una palabra: ")
    final = bucle_palabra(palabra)
    print(final)


if __name__ == "__main__":
    main()