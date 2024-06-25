# 1.Se desea un programa que lea 3 números enteros. El programa debe sumar los dos primeros números leídos
# y posteriormente el resultado obtenido multiplicarlo por el tercer número. El programa debe escribir el
# resultado.

'''
var
    Entero: int_a, int_b, int_c, suma, mult
Inicio
Escribir "Número entero A: "
Leer int_a
Escribir "Número entero B: "
Leer int_b
Escribir "Número entero C: "
Leer int_c
Hacer suma <- int_a + int_b
Hacer mult <- suma * int_c
Escribir int_a, " + ", int_b, " = ", suma
Escribir suma, " * "
Fin
'''


def main():
    int_a = int(input("Número entero A: "))
    int_b = int(input("Número entero B: "))
    int_c = int(input("Número entero C: "))
    suma = int_a + int_b
    mult = suma * int_c
    print(f"{int_a} + {int_b} = {suma}")
    print(f"{suma} * {int_c} = {mult}")


if __name__ == "__main__":
    main()
