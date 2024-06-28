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
    Real: ahorro, dias_mes
    Entero: dias_mes
Inicio
Hacer ahorro <- 0.00
Escribir "¿Cuántos días tiene este mes?: "
Leer dias_mes
Escribir "¿Cuánto desea ahorrar cada día?: "
Leer ahorro_diario
Repetir con dia desde 0 hasta menor que dias_mes
    Hacer ahorro <- ahorro + ahorro_diario
Fin Repetir
Escribir "¡Has ahorrado $", ahorro, " en el mes!"
Fin
"""

def main():
    ahorro = 0.00
    dias_mes = int(input("¿Cuántos días tiene este mes?: "))
    ahorro_diario = float(input("¿Cuánto estás dispuesto a ahorrar cada día del mes?: ")) 
    print()
    # ciclo - desde 1 hasta (dias_mes + 1) (day = 1; day < (dias_mes + 1))
    for dia in range(dias_mes):
        ahorro += ahorro_diario
    print(f"¡Has ahorrado ${ahorro} en el mes!")


if __name__ == "__main__":
    main()

