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
    mes_nacimiento = int(input("Inserte mes de nacimiento: "))
    anios = input("Inserte si el año de nacimiento es (año par, año impar): ")


if __name__ == "__main__":
    main()

