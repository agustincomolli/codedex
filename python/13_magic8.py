# pylint: disable=invalid-name

"""
Cree un programa magic8.py que pueda responder a cualquier pregunta de Sí o No
 con una respuesta diferente cada vez que se ejecute.

La salida debe tener el siguiente formato:

Question:      [Question]
Magic 8 Ball:  [Answer]

Por ejemplo:

Question:      Is Codédex better than Udemy yet?
Magic 8 Ball:  Better not tell you now.
"""

import random

question = input("Pregunta ❓: ")
answer_number = random.randint(1, 9)

if answer_number == 1:
    print("Sí, definitivamente.")
elif answer_number == 2:
    print("Definitivamente es así.")
elif answer_number == 3:
    print("Sin duda.")
elif answer_number == 4:
    print("Respuesta confusa, inténtalo de nuevo.")
elif answer_number == 5:
    print("Vuelve a preguntar más tarde.")
elif answer_number == 6:
    print("Mejor no te lo digo ahora.")
elif answer_number == 7:
    print("Mis fuentes dicen que no.")
elif answer_number == 8:
    print("Las perspectivas no son muy buenas.")
else:
    print("Muy dudoso.")
