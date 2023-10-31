# Ejercicio 2.2.1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def bucle_de_palabra(palabra):
    palabra_repetida = (palabra + " ") * 10
    return palabra_repetida
    

def main():
    palabra_input = input("Introduce una palabra: ")
    final = bucle_de_palabra(palabra_input)
    print(final)

if __name__ == "__main__":
    main()