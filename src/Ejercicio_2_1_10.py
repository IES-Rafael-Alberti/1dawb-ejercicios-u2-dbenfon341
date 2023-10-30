# Ejercicio 2.1.10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.



def tipoPizza(pizza):
    if pizza == 1:
        return True
    elif pizza == 2:
        return False
    

def pizzaVeg(ingrediente):
    if ingrediente == 1:
        return "Pimiento"
    elif ingrediente == 2:
        return "Tofu"
    
def pizzaNoveg(ingrediente):
    if ingrediente == 1:
        return "Peperoni"
    elif ingrediente == 2:
        return "Jamón"
    elif ingrediente == 3:
        return "Salmón"

def main():

    tipo_pizza = int(input("¡Bienvenido a Bella Napoli!\nTenemos pizzas vegetarianas y no vegetarianas.\n¿Qué tipo de pizza desea?\n1. Vegetariana\n2. No vegetariana\n"))
    if tipoPizza(tipo_pizza) == True:
        ingrediente = int((input(f"Has seleccionado una pizza vegetariana.\nLa pizza vegetariana puede incluir uno de los siguientes ingredientes:\n1. Pimiento\n2. Tofu.\n¿Qué ingrediente desea añadir?\n")))
        pizza = pizzaVeg(ingrediente)
        if pizza > 2:
            print(f"Introduce un ingrediente correcto.")
        else:
            print(f"Tu pizza vegetariana lleva {pizza}, Tomate y Mozzarella.")
    elif tipoPizza(tipo_pizza) == False:
        ingrediente = int((input(f"Has seleccionado una pizza no vegetariana.\nLa pizza no vegetariana puede incluir uno de los siguientes ingredientes:\n1. Peperoni\n2. Jamón\n3. Salmón.\n¿Que ingrediente desea añadir?\n")))
        pizza = pizzaNoveg(ingrediente)
        print(f"Tu pizza no vegetariana lleva {pizza}, Tomate y Mozzarella.")



    else:
        print("Seleccione un tipo correcto de pizza.")

    return

if __name__ == "__main__":
    main()