# 2.Se requiere el algoritmo para elaborar la planilla de un empleado. Para ello
# se dispone de sus horas laboradas en el mes, así como de la tarifa por hora.
# Imprima el monto de la planilla del empleado.

def main():
    horas_mes = int(input("Ingrese las horas laboradas en el mes: "))
    tarifa_hora = float(input("Ingrese la tarifa por hora: "))
    monto_planilla = horas_mes * tarifa_hora
    print(f"El monto de la planilla del empleado es ${monto_planilla}")


if __name__ == '__main__':
    main()
