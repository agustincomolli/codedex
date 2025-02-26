# pylint: disable=invalid-name
"""
El índice de masa corporal (IMC) fue creado por un matemático belga en la 
década de 1850 y lo utilizan los profesionales de la salud y la nutrición
 para estimar la grasa corporal humana en ciertas poblaciones.

Se calcula tomando el peso (masa) de un individuo en kilogramos y 
dividiéndolo por el cuadrado de su altura en metros.

IMC = peso / altura^2

Crea un programa bmi.py que calcule tu propio IMC.
"""

height = 1.62
weight = 65

bmi = weight / (height ** 2)

print(f"Tu IMC es {bmi:.2f} 💪")
