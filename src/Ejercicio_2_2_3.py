# Ejercicio 2.2.3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


def bucle_impares(numero):
    impares = ""
    i = 1
    while i <= numero:
        if i != 1:
            impares = impares + ", "
        impares = impares + str(i)
        i = i + 2
    return impares


def main():
    num1 = int(input("Introduce un número entero positivo: "))
    buclefinal = bucle_impares(num1)
    print (buclefinal)


if __name__ == "__main__":
    main()