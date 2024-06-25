# 4. Programa que lea números enteros hasta teclear 0, y nos muestre el máximo, el mínimo y la
# media de todos ellos. Piensa como debemos inicializar las variables.

"""
var
    Entero: max, min, num, contador, suma
Inicio
Hacer contador <- 0
Hacer suma <- 0
Escribir "Ingrese números enteros"
Escribir "Ingrese 0 para salir"
Mientras num != 0
    Escribir "Número entero: "
    Leer num
    Si num = 0
        break // salir del ciclo
    Fin Si
    Si contador = 0
        Hacer max <- num
        Hacer min <- num
    Fin Si
    Si num > max
        Hacer max <- num
    Fin Si
    Si num < min
        Hacer min <- num
    Fin Si
    Hacer contador <- contador + 1
    Hacer suma <- suma + num
Fin Mientras
Hacer media <- suma / contador
Escribir "Máximo = ", max
Escribir "Mínimo = ", min
Escribir "Media = ", media
Fin
"""


def main():
    max = None
    min = None
    num = None
    contador = 0
    suma = 0
    print("Ingrese números enteros")
    print("Ingrese 0 para salir\n")
    while num != 0:
        num = int(input("Número entero: "))
        if num == 0:
            break  # salir del ciclo
        if contador == 0:
            max = num
            min = num
        if num > max:
            max = num
        if num < min:
            min = num
        contador += 1
        suma += num
    media = suma / contador
    print(f"\nMáximo = {max}")
    print(f"Mínimo = {min}")
    print(f"Media = {media}")


if __name__ == "__main__":
    main()
