# 2.Se desea un programa que dado el salario bruto de un empleado y el nombre del empleado calcule el salario
# neto. El programa debe calcular las deducciones de seguro social, seguro educativo. El programa debe escribir
# el nombre del empleado, el salario bruto, las deducciones y el salario neto. Adicional el programa debe dar
# el total de salario bruto, total de cada una de las deducciones y total del salario neto.
# Deducciones
# S. Social = S.Bruto * 9%
# S. Educativo = S.Bruto * 1.75%
# S.Neto = S.Bruto – (S.Social + S.Educativo)

'''
var
    Real salario_bruto, seguro_social, seguro_educativo, salario_neto
    Cadena nombre
Inicio
Escribir "Salario bruto del empleado: "
Leer salario_bruto
Hacer seguro_social <- salario_bruto * 0.09
Hacer seguro_educativo <- salario_bruto * 0.0175
Hacer salario_neto <- salario_bruto - seguro_social - seguro_educativo
Escribir "Salario de ", nombre
Escribir "Salario bruto = $", salario_bruto
Escribir "Seguro social = $", seguro_social
Escribir "Seguro educativo = $", seguro_educativo
Escribir "SALARIO NETO = $", salario_neto
Fin
'''


def main():
    salario_bruto = float(input("Salario bruto del empleado: "))
    nombre = input("Nombre del empleado: ")
    seguro_social = salario_bruto * 0.09
    seguro_educativo = salario_bruto * 0.0175
    salario_neto = salario_bruto - seguro_social - seguro_educativo
    print(f"\nSalario de {nombre}:")
    print(f"Salario bruto = ${salario_bruto}")
    print(f"Seguro social = ${seguro_social}")
    print(f"Seguro educativo = ${seguro_educativo}")
    print(f"SALARIO NETO = ${salario_neto}")


if __name__ == '__main__':
    main()
