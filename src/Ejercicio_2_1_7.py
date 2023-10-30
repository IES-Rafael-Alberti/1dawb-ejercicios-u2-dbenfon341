# Ejercicio 2.1.7
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#
# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.


def tipoRenta(renta):
    if renta < 10000:
        return "5"
    elif renta in range(10000, 20000):
        return "15"
    elif renta in range(20001, 35000):
        return "20"
    elif renta in range(35001, 60000):
        return "30"
    else:
        return "45"
    

def main():
    rentaAnual = int(input("Introduzca su renta anual: "))
    total = tipoRenta(rentaAnual)
    print (f"Su renta anual es de {total}%.")



if __name__ == "__main__":
    main()