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
    escala = input("Ingrese la escala de pago (A/B/C/D): ")
    cursos = int(input("Inserte el número de cursos: "))

    CUOTA_FIJA = 350.00
    cuota_variable = None
    print()

    match escala.strip().upper():
        case "A":
            if cursos >= 1 and cursos <= 5:
                cuota_variable = 400.00
            elif cursos >= 6 and cursos <= 8:
                cuota_variable = 600.00
            elif cursos > 8:
                cuota_variable = 900.00
        case "B":
            if cursos >= 1 and cursos <= 3:
                cuota_variable = 350.00
            elif cursos >= 4 and cursos <= 7:
                cuota_variable = 500.00
            elif cursos > 7:
                cuota_variable = 700.00
        case "C":
            if cursos >= 1 and cursos <= 3:
                cuota_variable = 320.00
            elif cursos >= 4 and cursos <= 7:
                cuota_variable = 480.00
            elif cursos > 7:
                cuota_variable = 685.00
        case "D":
            if cursos >= 1 and cursos <= 4:
                cuota_variable = 310.00
            elif cursos >= 5 and cursos <= 8:
                cuota_variable = 475.00
            elif cursos > 8:
                cuota_variable = 680.00

    mensualidad = CUOTA_FIJA + cuota_variable
    print(f"Su mensualidad es de ${mensualidad}")


if __name__ == "__main__":
    main()
