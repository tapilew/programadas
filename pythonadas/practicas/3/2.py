# 2. Se requiere un programa para un restaurante el programa debe leer el tamaño de la pizza y el número de
# ingredientes adicionales y debe mostrar el precio que debe pagar.

"""
var
    Entero: tamanio, ingredientes
    Real: precio_por_ingrediente, precio
Inicio
Escribir "¿De qué tamaño quiere la pizza? (1/2/3): "
Leer tamanio
Escribir "¿Cuántos ingredientes desea?: "
Leer ingredientes
Hacer precio_por_ingrediente <- 0.00
Hacer precio <- 0.00
Segun tamanio Igual
    Caso 1:
        Hacer precio_por_ingrediente <- 5.00
    Caso 2:
        Hacer precio_por_ingrediente <- 9.00
    Caso 3:
        Hacer precio_por_ingrediente <- 20.00
    De lo contrario:
        Escribir "El tamaño que ingresó no es correcto."
Fin Segun
Hacer precio <- precio_por_ingrediente * ingredientes
Escribir "El precio por ingrediente es: ", precio_por_ingrediente
Escribir "Su precio a pagar es de: $", precio
Fin
"""

def main():
    tamanio = int(input("¿De qué tamaño quiere la pizza? (1/2/3): "))
    ingredientes = int(input("¿Cuántos ingredientes desea?: "))
    precio_por_ingrediente = 0.00
    precio = 0.00

    match tamanio:
        case 1:
            precio_por_ingrediente = 5.00
        case 2:
            precio_por_ingrediente = 9.00
        case 3:
            precio_por_ingrediente = 20.00
        case _:
            print("El tamaño que ingresó no es correcto.")

    precio = precio_por_ingrediente * ingredientes

    print(f"El precio por ingrediente es: {precio_por_ingrediente}")
    print(f"Su precio a pagar es de ${precio}")


if __name__ == "__main__":
    main()
