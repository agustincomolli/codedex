# pylint: disable=invalid-name

"""
Cree un programa grades.py que verifique si una calificación es superior o inferior a 55.

Comience creando una variable llamada gradey asígnele un valor entre 0 y 100.

Escriba una declaración if/ elsepara lo siguiente:

Si la calificación es mayor o igual a 55, entonces imprima "Aprobó".
De lo contrario, imprima "Falló".
"""

import random

# Generar una calificación aleatoria.
grade = random.randint(0, 100)

if grade >= 55:
    print("Aprobó 🥳")
else:
    print("Falló 😭")
