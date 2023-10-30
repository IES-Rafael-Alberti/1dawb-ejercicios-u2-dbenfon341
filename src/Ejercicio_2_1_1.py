def comprobarEdad(edad):
    if edad >= 18:
        return print (f"Eres mayor de edad.")
    else:
        return print (f"No eres mayor de edad.")


def main():
    edad = int(input(f"Por favor, introduce tu edad: "))
    resultado = comprobarEdad(edad)
    print(resultado)


if __name__ == "__main__":
    main()