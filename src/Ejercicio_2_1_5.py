# Ejercicio 2.1.5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos 
# mensuales y muestre por pantalla si el usuario tiene que tributar o no.


def ejercicio(edad, ingresos):
    if edad < 16 or ingresos < 1000:
        print ("No tienes que tributar.")
    else:
        return print ("Tienes que tributar.")
    
    
ejercicio(int(input("Introduce tu edad: ")), int(input("Introduce tus ingresos mensuales: ")))