# pylint: disable=invalid-name
"""
🗓️ Estaciones del año
Ah, las cuatro estaciones del año: invierno, primavera, verano u otoño; ¡todo 
lo que tienes que hacer es llamar!

Pide al usuario el número de mes usando la función input().

Comprueba las cuatro estaciones usando una declaración if/elif/else y operadores 
lógicos:

month es 1, 2, 3, print 'Verano 🌻'
month es 4, 5, 6, print 'Otoño 🍂'
month es 7, 8, 9, print 'Invierno 🌨️'
month es 10, 11, 12, print 'Primavera 🌱'
Todo lo demás es 'Inválido'
Los operadores lógicos en Python incluyen las palabras clave and y or. 
¿Cuál deberías usar?
"""

print("🗓️  Estaciones del año\n")

month = int(input("Ingresa el número de mes: "))

if month == 1 or month == 2 or month == 3:
    print("Verano 🌻")
elif month == 4 or month == 5 or month == 6:
    print("Otoño 🍂")
elif month == 7 or month == 8 or month == 9:
    print("Invierno 🌨️")
elif month == 10 or month == 11 or month == 12:
    print("Primavera 🌱")
else:
    print("Inválido")
