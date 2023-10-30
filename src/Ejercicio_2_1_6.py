# Ejercicio 2.1.6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


def pedirNombre(nombre):
    nombre = ""
    if nombre.startswith(('A','B','C','D','E','F','G','H','I','J','K','L','M')):
        return True
    elif nombre.startswith(('N','O','P','Q','R','S','T','U','V','W','X','Y','Z')):
        return False


def pedirGenero(sexo):
    if sexo == "hombre":
        return sexo == int(1)
    elif sexo == "mujer":
        return sexo == int(2)



def main():
    grupogenero = pedirGenero(int(input("Introduce tu género: ")))
    if grupogenero == (1):
        print("AAAA")
    else:
        print("BBBB")


main()