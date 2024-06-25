# 1. Lea un valor de temperatura t y un código p que puede ser 1 o 2. Si el código es 1 convierta la temperatura t de
# grados f a grados c con la fórmula c=5/9(t-32). Si el código es 2 convierta la temperatura t de grados c a f con la
# fórmula: f=32+9t/5, caso contrario muestre un mensaje de error.

"""
var
    Real: t
    Entero: p
Inicio
Escribir "Temperatura: "
Leer t
Escribir "Ingrese 1 (F a C) o 2 (C a F)"
Leer p
Segun p Hacer
    Caso 1:
        Hacer c <- 5 / 9 * (t - 32)
        Escribir p, " grados F = ", c, " grados C"
    Caso 2:
        Hacer f <- 32 + 9 * t / 5
        Escribir p, " grados C = ", f, " grados F"
    De lo contrario:
        Escribir "Usted ha ingresado un número equivocado (sólo se acepta 1 o 2)"
Fin Segun
Fin
"""

def main():
    t = float(input("Temperatura: "))
    p = int(input("Ingrese 1 (F a C) o 2 (C a F): "))

    match p:
        case 1:
            c = 5 / 9 * (t - 32)
            print(f"{p} grados F = {c} grados C")
        case 2:
            f = 32 + 9 * t / 5
            print(f"{p} grados C = {f} grados F")
        case _:
            print("Usted ha ingresado un número equivocado (sólo se acepta 1 o 2)")


if __name__ == "__main__":
    main()
