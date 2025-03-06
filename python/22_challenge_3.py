# pylint: disable=invalid-name

"""
Supongamos que tenemos dos dados. 🎲 🎲

Crea un juego en el que uno adivine el valor total después de lanzar un par de 
dados una vez.

Cada dado tiene valores enteros del 1 al 6. Como hay dos dados, el rango de 
valores posibles está entre 2 y 12 (inclusive).

Utilice el randommódulo para “lanzar” los dados y almacenar los valores 
aleatorios de cada variable del dado en una nueva total variable.

Hasta que se adivine el valor correcto, utilice un while bucle para seguir 
solicitando al usuario un número.

Utilice whilebucles junto con los métodos del random módulo para resolver 
este desafío.

What is the total (2-12)? 10
What is the total (2-12)? 7
You got it!
"""

import random

print("🎲 Tirada de dados 🎲")

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
total = dice_1 + dice_2
answer = int(input("¿Cuál es el valor de los dados (2-12)? "))

while answer != total:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total = dice_1 + dice_2
    answer = int(input("¿Cuál es el valor de los dados (2-12)? "))

print("¡Lo adivinaste!")
