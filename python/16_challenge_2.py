# pylint: disable=invalid-name

"""
🎒 Calificaciones de la escuela secundaria
Las escuelas secundarias de EE. UU. suelen durar cuatro años, desde el primer 
año hasta el último año. 🚌💨

Primero, pídale al usuario que ingrese su calificación como un número entero.

Cree un sistema de calificaciones de la escuela secundaria de cuatro años 
utilizando una declaración if/elif/else:

la calificación es 9, imprime 'Freshman'
la calificación es 10, imprime 'Sophomore'
la calificación es 11, imprime 'Junior'
la calificación es 12, imprime 'Senior'
Todo lo demás es 'TBD'
"""

print("🎒 Calificaciones de la escuela secundaria")

grade = int(input("¿Cuál es tu nivel de grado? "))

if grade == 9:
    print("Freshman")
elif grade == 10:
    print("Sophomore")
elif grade == 11:
    print("Junior")
elif grade == 12:
    print("Senior")
else:
    print("TBD")
