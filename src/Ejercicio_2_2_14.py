# Ejercicio 2.2.14
# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.


def numeros(numero):
    lista = 0
    while numero != 0:
        lista = lista + numero
        numero = int(input("Introduce otro número: "))
    return lista


def main():
    introduceNumero = int(input("Introduce un número: "))
    final = numeros(introduceNumero)
    print (final)

if __name__ == "__main__":
    main()