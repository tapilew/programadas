# 1. Se desea crear un programa que permita calcular el ahorro de una persona durante un mes. Se le debe
# solicitar al usuario que ingrese la cantidad de días del mes y el monto a ahorrar por día. El programa debe
# mostrar el ahorro acumulado día a día hasta finalizar el mes.
# Ejemplo de cómo debe lucir la salida del programa:
#
# Dia | Ahorro
# 1 | 0.25
# 2 | 0.50
# 3 | 0.75
# 4 | 1.00
# 5 | 1.25
# 6 | 1.50
# . | .
# . | .
# . | .
# 30 | 7.50

"""
var
    Real: ahorro
    Entero: dias_mes
Inicio
Hacer ahorro <- 0.00
Escribir "¿Cuántos días tiene este mes?: "
Leer dias_mes
Repetir con dia desde 1 hasta menor que (dias_mes + 1)
    Hacer input <- 0
    Escribir "¿Cuánto has ahorrado el día ", dia, "?: $"
    Leer input
    Hacer ahorro <- ahorro + input
Fin Repetir
Escribir "¡Has ahorrado $", ahorro, " en el mes!"
Fin
"""

def main():
    ahorro = 0.00
    dias_mes = int(input("¿Cuántos días tiene este mes?: "))
    print()
    # ciclo - desde 1 hasta (dias_mes + 1) (day = 1; day < (dias_mes + 1))
    for dia in range(1, dias_mes + 1):
        ahorro += float(input(f"¿Cuánto has ahorrado el día {dia}?: $"))
    print(f"\n¡Has ahorrado ${ahorro} en el mes!")


if __name__ == "__main__":
    main()
