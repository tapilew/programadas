"""
1. El Centro Educativo El Saber cuenta con una tabla para la escala de (A, B, C o D) y el
número de cursos, usted debe crear un programa que determine a cuánto asciende el
pago mensual de un determinado estudiante.

El monto a pagar que debe cancelar cada alumno se calcula de la siguiente forma:

Mensualidad = Cuota Fija + Cuota Variable
Donde la cuota fija es de B/.350.00
La cuota variable depende de la tabla:

----------------------------------------------------
| Escala de Pago | Número de Cursos      | Monto   |
----------------------------------------------------
|                | Entre 1 y 5 Inclusive | B/. 400 |
| A              | Entre 6 y 8 Inclusive | B/. 600 |  
|                | Más de 8              | B/. 900 |
----------------------------------------------------
|                | Entre 1 y 3 Inclusive | B/. 350 |
| B              | Entre 4 y 7 Inclusive | B/. 500 |
|                | Más de 7              | B/. 700 | 
----------------------------------------------------
|                | Entre 1 y 3 Inclusive | B/. 320 |
| C              | Entre 4 y 7 Inclusive | B/. 480 |
|                | Más de 7              | B/. 685 |
----------------------------------------------------
|                | Entre 1 y 4 Inclusive | B/. 310 |
| D              | Entre 5 y 8 Inclusive | B/. 475 |
|                | Más de 8              | B/. 680 |
----------------------------------------------------

"""


def main():
    escala = input("Ingrese la escala (A, B, C, D): ")
    num_mensual = int(input("Inserte el número de cursos: "))
    pago_mensual = float(input("¿Cuánto asciende el pago mensual?: "))

    cuota_fija = 0.00
    mensualidad = cuota_fija + 350.00

    if escala == "A":
        print()
        if num_mensual <= 5:
            cuota_fija = 400.00
        elif num_mensual <= 6:
            cuota_fija = 600.00
        else:
            cuota_fija = 900.00

    if escala == "B":
        print()
        if num_mensual <= 1:
            cuota_fija = 350.00
        elif num_mensual <= 4:
            cuota_fija = 500.00
        else:
            cuota_fija = 700.00
    
    if escala == "C":
        print()
        if num_mensual <= 1:
            cuota_fija = 320.00
        elif num_mensual <= 4:
            cuota_fija = 480.00
        else:
            cuota_fija = 680.00
    
    if escala == "D":
        print()
        if num_mensual <= 1:
            cuota_fija = 310.00
        elif num_mensual <= 5:
            cuota_fija = 475.00
        else:
            cuota_fija = 680.00


if __name__ == "__name__":
    main()

