# Ejercicio 2.1.6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


def comprobarGrupos(nombre, genero):
    if genero == 'F' and nombre < 'M' or genero == 'M' and nombre > 'N':
        return "A"
    else:
        return "B"


def main():
    nombre = input(f"Introduce tu nombre: ").upper()
    genero = input(f"Introduce tu género (F/M): ").upper()

    grupo = comprobarGrupos(nombre, genero)

    if genero == 'F' or genero == 'M':
        print(f"Perteneces al grupo: {grupo}")
    else:
        print(f"Introduce un género correcto.")


if __name__ == "__main__":
    main()
