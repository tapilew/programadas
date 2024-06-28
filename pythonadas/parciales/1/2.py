"""
2. Debe crear un programa que le permita calcular tu color de nacimiento.
El color de nacimiento se calcula utilizando la siguiente tabla:
------------------------------------------------------------
|            | Año Par              | Año Impar            |
| Mes        |---------------------------------------------|
|            | Día Par  | Día Impar | Día Par  | Día Impar |
------------------------------------------------------------
| Enero      |          |           |          |           |
| Febrero    | Rojo     | Celeste   | Morado   | Negro     |
| Marzo      |          |           |          |           |
------------------------------------------------------------
| Abril      |          |           |          |           |
| Mayo       | Naranja  | Verde     | Turquesa | Gris      |
| Junio      |          |           |          |           |
------------------------------------------------------------
| Julio      |          |           |          |           |
| Agosto     | Marrón   | Fucsia    | Azul     | Amarillo  |
| Septiembre |          |           |          |           |
------------------------------------------------------------
| Octubre    |          |           |          |           |
| Noviembre  | Violeta  | Rosado    | Olivo    | Blanco    |
| Diciembre  |          |           |          |           |
------------------------------------------------------------

"""


def main():
    print("Ingresa tu fecha de nacimiento...")
    mes = int(input("Mes (1-12): "))
    dia = int(input("Día: "))
    anio = int(input("Año: "))
    color = None
    # enero, febrero o marzo
    if mes >= 1 and mes <= 3:
        # si el AÑO es PAR
        if anio % 2 == 0:
            # si el DÍA es PAR
            if dia % 2 == 0:
                color = "rojo"
            # si el DÍA es IMPAR
            else:
                color = "celeste"
        # si el AÑO es IMPAR
        else:
            # si el DÍA es PAR
            if dia % 2 == 0:
                color = "morado"
            # si el DÍA es IMPAR
            else:
                color = "negro"
    # abril, mayo o junio
    elif mes >= 4 and mes <= 6:
        # si el AÑO es PAR
        if anio % 2 == 0:
            # si el DÍA es PAR
            if dia % 2 == 0:
                color = "naranja"
            # si el DÍA es IMPAR
            else:
                color = "verde"
        # si el AÑO es IMPAR
        else:
            # si el DÍA es PAR
            if dia % 2 == 0:
                color = "turquesa"
            # si el DÍA es IMPAR
            else:
                color = "gris"
    # julio, agosto o septiembre
    elif mes >= 7 and mes <= 9:
        # si el AÑO es PAR
        if anio % 2 == 0:
            # si el DÍA es PAR
            if dia % 2 == 0:
                color = "marrón"
            # si el DÍA es IMPAR
            else:
                color = "fuscia"
        # si el AÑO es IMPAR
        else:
            # si el DÍA es PAR
            if dia % 2 == 0:
                color = "azul"
            # si el DÍA es IMPAR
            else:
                color = "amarillo"

    # octubre, noviembre o diciembre
    elif mes >= 10 and mes <= 12:
        # si el AÑO es PAR
        if anio % 2 == 0:
            # si el DÍA es PAR
            if dia % 2 == 0:
                color = "violeta"
            # si el DÍA es IMPAR
            else:
                color = "rosado"
        # si el AÑO es IMPAR
        else:
            # si el DÍA es PAR
            if dia % 2 == 0:
                color = "olivo"
            # si el DÍA es IMPAR
            else:
                color = "blanco"

    print(f"\n¡Tu color de nacimiento es el {color}!")


if __name__ == "__main__":
    main()
