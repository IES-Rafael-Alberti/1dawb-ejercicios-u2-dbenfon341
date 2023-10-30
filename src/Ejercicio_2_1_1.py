def comprobarEdad(edad):
    if edad >= 18:
        return "Eres mayor de edad."
    else:
        return "No eres mayor de edad."


def main():
    edad = int(input(f"Por favor, introduce tu edad: "))
    resultado = comprobarEdad(edad)
    print(resultado)


if __name__ == "__main__":
    main()