# Ejercicio 2.1.2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
# introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


def comprobarPwd(pwd):
    if pwd == "contraseña":
        return print(f"¡Has acertado la contraseña!")
    else:
        return print(f"No has acertado.")


def main():
    pwd = input(f"Por favor, introduce la contraseña: ")
    pwd = pwd.lower()
    resultado = comprobarPwd(pwd)
    print(resultado)


if __name__ == "__main__":
    main()