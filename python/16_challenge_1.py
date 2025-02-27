# pylint: disable=invalid-name
"""
En un sistema de evaluación de restaurantes de cinco estrellas (⭐️⭐️⭐️⭐️⭐️), 
las estrellas suelen representar los diferentes niveles de satisfacción.

Pero, ¿qué significa cada una de las estrellas?

Comience por crear una variable de calificación y configúrela como un número 
decimal.

Cree un sistema de calificación utilizando una declaración if/elif/else:

calificación mayor que 4,5, imprima 'Extraordinario'
calificación mayor que 4, imprima 'Excelente'
calificación mayor que 3, imprima 'Bueno'
calificación mayor que 2, imprima 'Regular'
Todo lo demás, imprima 'Malo'
"""

print("⭐ Calificaciones de alimentos")

RATING = 4.8

if RATING > 4.5:
    print("Extraordinario")
elif RATING > 4:
    print("Excelente")
elif RATING > 3:
    print("Bueno")
elif RATING > 2:
    print("Regular")
else:
    print("Malo")
