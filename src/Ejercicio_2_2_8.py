# Ejercicio 2.2.8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1


def bucle_numero_piramide(n):
    piramide = ""
    for i in range(1, n + 1, 2):
        for j in range(i, 0, -2):
            piramide = piramide + str(j) + " "
        piramide = piramide + "\n"
    return piramide


def main():
    numero = int(input("Por favor, introduce un número entero: "))
    final = bucle_numero_piramide(numero)
    print(final)


if __name__ == "__main__":
    main()