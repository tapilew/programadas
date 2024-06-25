# 4. El presidente de la república ha decidido estimular a todos los estudiantes de una universidad
# mediante la asignación de becas mensuales, para esto se tomarán en consideración los
# siguientes criterios:
# Para alumnos mayores de 18 años
# a. con promedio mayor o igual a 90, la beca será de B/.250.00;
# b. con promedio mayor o igual a 75, de B/.200.00;
# c. para los promedios menores de 75 pero mayores a 60, de B/.150.00;
# d. a los demás se les enviará una carta de invitación incitándolos a que estudien más en el
# próximo ciclo escolar.
# A los alumnos de 18 años o menores de esta edad
# a. con promedios mayores o iguales a 90, se les dará B/.300.00;
# b. con promedios menores a 90 pero mayores o iguales a 80, B/.200.00;
# c. para los alumnos con promedios menores a 80 pero mayores 60, se les dará B/.100.00,
# d. y a los alumnos que tengan promedios menores iguales a 60 se les enviará carta de
# invitación.
# Realice un programa que permita consultar el monto de la beca que obtendrá un estudiante de
# acuerdo a su edad y promedio.

"""
var
    Entero: edad
    Real: promedio, beca
Inicio
Escribir "¡Averigüemos el monto de beca que te corresponde!"
Escribir "Edad: "
Leer edad
Escribir "Promedio: "
Leer promedio
Hacer beca <- 0.00
Si edad > 18
    Si promedio >= 90
        Hacer beca <- 250.00
    De otro modo si promedio >= 75
        Hacer beca <- 200.00
    De otro modo si
        Hacer beca <- 150.00
    Fin Si
De otro modo
    Si promedio >= 90
        Hacer beca <- 300.00
    De otro modo si promedio >= 80
        Hacer beca <- 200.00
    De otro modo si promedio > 60
        Hacer beca <- 100.00
    Fin Si
Fin Si
Si beca > 0.00
    Escribir "¡Le corresponden $", beca, " mensuales por su beca!"
De otro modo
    Escribir "No ha alcanzado el puntaje requerido para una beca... ¡Ánimo, estudie más en el próximo ciclo escolar!"
Fin Si
Fin
"""


def main():
    print("¡Averigüemos el monto de beca que te corresponde!")
    edad = int(input("Edad: "))
    promedio = float(input("Promedio: "))
    beca = 0.00
    if edad > 18:
        if promedio >= 90:
            beca = 250.00
        elif promedio >= 75:
            beca = 200.00
        elif promedio > 60:
            beca = 150.00
    else:
        if promedio >= 90:
            beca = 300.00
        elif promedio >= 80:
            beca = 200.00
        elif promedio > 60:
            beca = 100.00
    if beca > 0.00:
        print(f"¡Le corresponden ${beca} mensuales por su beca!")
    else:
        print("No ha alcanzado el puntaje requerido para una beca... ¡Ánimo, estudie más en el próximo ciclo escolar!")


if __name__ == '__main__':
    main()
