# Ejercicio 2.1.5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos 
# mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def es_ingreso_suficiente(ingreso):
    if ingreso < 1000:
        return False
    else:
        return True
    

def es_mayor_de_edad(edad):
    if edad >= 16:
        return True
    else:
        return False
    

def main():
    ingresos = int(input(f"Introduce tus ingresos: "))
    edad_persona = int(input(f"Introduce tu edad: "))
    
    if es_ingreso_suficiente(ingresos) and es_mayor_de_edad(edad_persona):
        print(f"Tributas.")
    else:
        print(f"No tributas.")


if __name__ == "__main__":
    main()