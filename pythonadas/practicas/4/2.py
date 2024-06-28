
# 2. En una institución preescolar se desea ensenar a los niños mediante herramientas tecnológicas.
# Para matemáticas, se ha propuesto conseguir un programa que muestre los números que
# existen hasta una determinada cifra.
# Diseñe un programa que solicite un valor entero positivo y presente los números desde el uno
# hasta el valor ingresado de uno en uno.
# Por ejemplo, si es ingresado el 10 debe mostrar en la pantalla los números: 1, 2, 3, 4, 5, 6, 7, 8,
# 9 y 10.

"""
var
    Entero: numeros
Inicio
Escribir "¿Hasta qué número quieres contar?: "
Leer numeros
Repetir con num desde 1 hasta menor que (numeros + 1)
    Escribir num
Fin Repetir
Fin
"""


def main():
    numeros = int(input("¿Hasta qué número quieres contar?: "))
    print() 

    for num in range(1, numeros + 1):
        print(num)


if __name__ == "__main__":
    main()
