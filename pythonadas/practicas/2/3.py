# 3. Construya un programa que resuelva el problema que tienen en una gasolinera. Los surtidores de esta
# registran lo que “surten” en galones, pero el precio de la gasolinera está fijado en litros. Cada galón tiene
# 3.785 litros y el precio por litro es 0.95. Si el cliente compra tanque lleno tiene un descuento del 2% sobre el
# monto final a pagar. El descuento solamente se otorga con tanque lleno.

'''
var
    Caracter: tanque_lleno
    Cadena: texto
    Real: galones, litros, PRECIO_LITRO, pago
Inicio
Escribir "¿Tanque lleno? (s/N): "
Leer input
Si input = 's'
    Hacer tanque_lleno <- Cierto
De otro modo
    Hacer tanque_lleno <- Falso
Fin si
Escribir "¿Cuántos galones llenará?: "
Leer galones
Hacer litros <- galones * 3.785
Hacer PRECIO_LITRO <- 0.95
Hacer pago <- litros * PRECIO_LITRO
Hacer texto <- ""
Si tanque_lleno
    Hacer pago <- pago - (pago * 0.02)
    Hacer texto <- "(2% de descuento por tanque lleno)"
Fin Si
Hacer texto <- "Costo a pagar por ", litros, " litros (", galones, " galones) = $", pago, " ", texto
Escribir texto
Fin
'''


def main():
    tanque_lleno = input("¿Tanque lleno? (s/N): ")
    if tanque_lleno.strip().lower() == "s":
        tanque_lleno = True
    else:
        tanque_lleno = False
    galones = float(input("¿Cuántos galones llenará?: "))
    litros = galones * 3.785
    PRECIO_LITRO = 0.95
    pago = litros * PRECIO_LITRO
    texto = ""
    if tanque_lleno:
        pago -= pago * 0.02
        texto = "(2% de descuento por tanque lleno)"
    texto = f"Costo a pagar por {litros} litros ({galones} galones) = ${pago} " + texto
    print(texto)


if __name__ == '__main__':
    main()
