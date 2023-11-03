# Ejercicio 2.2.6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#
# *
# **
# ***
# ****
# *****


def bucle_asterisco(num):
    resultado = ""
    for i in range(1, num + 1):
        resultado = resultado + '\n' + '*' * i
    return resultado 


def main():
    num = int(input("Escibe un número: "))
    final = bucle_asterisco(num)
    print(final)

if __name__ == "__main__":
    main()