# Ejercicio 2.2.9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


def comprobar_pwd(pwd):
    while pwd != "contraseña":
        pwd = input("Inténtalo de nuevo: ")
    else:
        return "¡Has acertado!"


def main():
    pwd = input(f"Por favor, introduce la contraseña: ")
    pwd = pwd.lower()
    resultado = comprobar_pwd(pwd)
    print(resultado)


if __name__ == "__main__":
    main()