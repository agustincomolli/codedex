# pylint: disable=invalid-name

"""
Un número está "al cuadrado" cuando se multiplica por sí mismo o se eleva a la 
segunda potencia (por ejemplo, 4² = 4 x 4 = 16).

Primero, se le pide al usuario un número entero int(input()) y se lo almacena 
en una variable number. Luego, se define una variable total con un valor inicial 
de 0.

Nota: Puedes pasar un mensaje de cadena a int(input()).

A continuación, utilice un bucle for y una función range() para calcular el total
de los cuadrados de todos los números enteros desde 1 hasta ese number.

Por último, imprima la salida como un valor entero.

Por ejemplo, si numberes 5, totaldebería ser 55 porque:

1^2 + 2^2 + 3^2 + 4^2 + 5^2
=1+4+9+16+25
=55
"""

number = int(input("Ingrese un número: "))
total = 0

for i in range(1, number + 1):
    total += i ** 2

print(total)
