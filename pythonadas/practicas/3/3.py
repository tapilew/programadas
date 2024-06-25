# 3.La suma de los tres ángulos de un triángulo es de 180 grados. Desarrolle un programa que lea
# valores correspondientes a tres ángulos y determine si ellos conforman o no un triángulo.
# Además, indique a que tipo de triangulo corresponde:
# a. Rectángulo: si tiene un ángulo recto (90 grados)
# b. Obtusángulo: tiene un ángulo obtuso (mayor que 90 pero menor que 180 grados)
# c. Acutángulo: los tres ángulos son agudos (menores que 90 grados).

"""
var
    Real: angulo_a, angulo_b, angulo_c
    Booleano: es_triangulo
    Cadena: tipo_triangulo
Inicio
Escribir "¿Cuántos grados tiene el ángulo A?: "
Leer angulo_a
Escribir "¿Cuántos grados tiene el ángulo B?: "
Leer angulo_b
Escribir "¿Cuántos grados tiene el ángulo C?: "
Leer angulo_c
Hacer es_triangulo <- (angulo_a + angulo_b + angulo_c) = 180
Si es_triangulo
    Si angulo_a = 90 o angulo_b = 90 o angulo_c = 90
        Hacer tipo_triangulo <- "Rectángulo"
    De otro modo si (angulo_a > 90 y angulo_a < 180) o (angulo_b > 90 y angulo_b < 180) o (angulo_c > 90 y angulo_c < 180)
        Hacer tipo_triangulo <- "Obtusángulo"
    De otro modo si angulo_a < 90 y angulo_b < 90 y angulo_c < 90
        Hacer tipo_triangulo <- "Acutángulo"
    Fin Si
    Si tipo_triangulo
        Escribir "Usted ingresó los ángulos de un Triángulo ", tipo_triangulo
    De otro modo
        Escribir "Los ángulos del tríangulo que ingresó no corresponden ni a un Triángulo Rectángulo, Obtusángulo ni Acutángulo"
    Fin Si
De otro modo
    Escribir "Los ángulos ingresados no corresponden a los de un triángulo"
Fin Si
Fin
"""


def es_obtuso(angulo):
    if angulo > 90 and angulo < 180:
        return True
    return False


def main():
    angulo_a = float(input("¿Cuántos grados tiene el ángulo A?: "))
    angulo_b = float(input("¿Cuántos grados tiene el ángulo B?: "))
    angulo_c = float(input("¿Cuántos grados tiene el ángulo C?: "))
    es_triangulo = (angulo_a + angulo_b + angulo_c) == 180
    tipo_triangulo = None
    if es_triangulo:
        if angulo_a == 90 or angulo_b == 90 or angulo_c == 90:
            tipo_triangulo = "Rectángulo"
        elif es_obtuso(angulo_a) or es_obtuso(angulo_b) or es_obtuso(angulo_c):
            tipo_triangulo = "Obtusángulo"
        elif angulo_a < 90 and angulo_b < 90 and angulo_c < 90:
            tipo_triangulo = "Acutángulo"
        if tipo_triangulo:
            print(
                f"Usted ingresó los ángulos de un Triángulo {tipo_triangulo}")
        else:
            print("Los ángulos del triángulo que ingresó no corresponden ni a un Triángulo Rectángulo, Obtusángulo ni Acutángulo.")
    else:
        print("Los ángulos ingresados no corresponden a los de un triángulo")


if __name__ == '__main__':
    main()
