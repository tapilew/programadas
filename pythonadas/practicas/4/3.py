# 3. Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la
# semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por
# las horas trabajadas.

"""
var
    Real: sueldo_hora, sueldo_semana
    Entero: horas_dia
Inicio
Escribir "¿Cuánto cobra el empleado por hora?: $"
Leer sueldo_hora
Hacer sueldo_semana <- 0.00
Escribir "Ingrese las horas trabajadas durante la semana..."
Repetir con dia desde 1 hasta menor que 7
    Escribir "'Cuántas horas trabajó el día ", dia, "?: "
    Leer horas_dia
    Hacer sueldo_semana <- sueldo_semana + (horas_dia * sueldo_hora)
Fin Repetir
Escribir "El sueldo del empleado por esta semana es de $", sueldo_semana
Fin
"""


def main():
    sueldo_hora = float(input("¿Cuánto cobra el empleado por hora?: $"))
    sueldo_semana = 0.00
    print("\nIngrese las horas trabajadas durante la semana...")
    # desde día 1 hasta día 6 (dia = 1; dia < 7)
    for dia in range(1, 7):
        sueldo_semana += float(
            input(f"¿Cúantas horas trabajó el día {dia}?: ")) * sueldo_hora
    print(f"\nEl sueldo del empleado por esta semana es de ${sueldo_semana}")


if __name__ == '__main__':
    main()
