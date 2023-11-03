# Ejercicio 2.2.3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


def bucle_numero(numero):
    mensaje = ""
    cont = 1
    while cont <= numero:
        mensaje = mensaje + (f"{cont}, ")
        cont = cont + 1
    return mensaje


def main():
    numero = int(input("Escribe un número: "))
    final = bucle_numero(numero)
    print(final)


if __name__ == "__main__":
    main()