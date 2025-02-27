# pylint: disable=invalid-name

"""
Crea un nuevo archivo llamado the_cyclone.py .

Pregúntele al usuario cuál es su altura y cuántos créditos tiene, y almacene 
los valores en una height variable y una credits variable.

Utilice una combinación de operadores relacionales y lógicos para crear las 
reglas:

Si son lo suficientemente altos y tienen suficientes créditos, imprima 
"¡Disfruta el viaje!"
De lo contrario, si tienen suficientes créditos, pero no son lo suficientemente 
altos, imprima "No eres lo suficientemente alto para viajar".
De lo contrario, si son lo suficientemente altos, pero no tienen suficientes 
créditos, imprima "No tiene suficientes créditos".
De lo contrario, imprima un mensaje indicando que no han cumplido ninguno de 
los requisitos.
"""

print("The Cyclone 🎢")

user_height = int(input("¿Cuál es tu altura en cm? "))
user_credits = int(input("¿Cuántos créditos tienes? "))

if user_height >= 137 and user_credits >= 10:
    print("¡Disfruta el viaje!")
elif user_height < 137 and user_credits >= 10:
    print("No eres lo suficientemente alto para viajar")
elif user_height >= 137 and user_credits < 10:
    print("No tienes suficientes créditos")
else:
    print("No cumples con ninguno de los requisitos")
