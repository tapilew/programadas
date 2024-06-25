# 1. Una tienda de comercio electrónico gana el 30% de comisión sobre el precio de los
# productos que ofrece en su página web. Se necesita construir un algoritmo que
# calcule cuanto es la comisión de esta tienda por cada artículo que venda.
#  Debe
# imprimir el precio del producto y la comisión.

def main():
    num_producto = 0
    precio = 0
    while num_producto == 0 or precio > 0:
        num_producto += 1
        precio = float(input(f"Ingrese precio del producto {precio}: "))
        comision = float(precio) * .3
        print(precio)
        print(comision)


if __name__ == "__main__":
    main()
