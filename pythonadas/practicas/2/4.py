# 4.Se desea un programa que lea el monto vendido durante el mes por un vendedor. El programa debe calcular
# la comisión a pagar al vendedor. El vendedor gana una comisión del 3% sobre el monto vendido. Al monto
# vendido se debe restar el monto en concepto de devoluciones o notas de crédito reportadas en el mes. En
# la solución presentada utilizar constante para manejar el porcentaje de comisión.

"""
var
    Real: PORCENTAJE_COMISION, monto_vendido, comision, ingreso_neto
Inicio
Hacer PORCENTAJE_COMISION <- 0.03
Escribir "Ingrese el total de ventas mensuales: $"
Leer monto_vendido
Hacer comision <- monto_vendido * PORCENTAJE_COMISION
Hacer ingreso_neto <- monto_vendido - comision
Escribir "Comisión pagada al vendedor (", (PORCENTAJE_COMISION * 100), "%) = $", comision)
Escribir "Ingreso neto = ", ingreso_neto
Fin
"""


def main():
    PORCENTAJE_COMISION = 0.03
    monto_vendido = float(input("Ingrese el total de ventas mensuales: $"))
    comision = monto_vendido * PORCENTAJE_COMISION
    ingreso_neto = monto_vendido - comision
    print(
        f"Comisión pagada al vendedor ({PORCENTAJE_COMISION * 100}%) = ${comision}")
    print(f"Ingreso neto = {ingreso_neto}")


if __name__ == "__main__":
    main()
