# Ejercicio 2.2.13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


def palabras(palabras):
    lista = ""
    while palabras != "salir":
        lista = lista + palabras
        palabras = input("Introduce otra palabra: ")
    return lista


def main():
    introducePalabra = input("Introduce una palabra: ")
    final = palabras(introducePalabra)
    print (final)


if __name__ == "__main__":
    main()