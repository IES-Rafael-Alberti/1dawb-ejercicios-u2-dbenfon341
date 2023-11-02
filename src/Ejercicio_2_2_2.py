# Ejercicio 2.2.2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


def bucle_edad(edad):
    mensaje = ""
    año = 1
    while año <= edad:
        mensaje = mensaje + (f"{año}\n")
        año = año + 1
    return mensaje


def main():
    edad = int(input("Escribe tu edad: "))
    final = bucle_edad(edad)
    print(final)


if __name__ == "__main__":
    main()