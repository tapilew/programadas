# 3. Se necesita elaborar un algoritmo que solicite el número de respuestas correctas,
# incorrectas y en blanco, correspondientes a postulantes, y muestre su puntaje final
# considerando que por cada respuesta correcta tendrá 3 puntos, respuestas
# incorrectas tendrá -1 y respuestas en blanco tendrá 0.

def main():
    correctas = int(input("Número de respuestas correctas: "))
    incorrectas = int(input("Número de respuestas incorrectas: "))
    en_blanco = int(input("Número de respuestas en blanco: "))
    puntos_maximos = (correctas + incorrectas + en_blanco) * 3
    puntaje_final = correctas * 3 - incorrectas
    print(f"Su puntaje final es {puntaje_final}/{puntos_maximos}")


if __name__ == '__main__':
    main()
