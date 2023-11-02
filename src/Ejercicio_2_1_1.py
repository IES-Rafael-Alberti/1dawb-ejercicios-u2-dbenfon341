# Ejercicio 2.1.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


def comprobar_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad."
    else:
        return "No eres mayor de edad."


def main():
    edad = int(input(f"Por favor, introduce tu edad: "))
    resultado = comprobar_edad(edad)
    print(resultado)


if __name__ == "__main__":
    main()