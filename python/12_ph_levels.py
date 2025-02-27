# pylint: disable=invalid-name
"""
Cree un programa ph_levels.py que verifique si un nivel de pH es básico, ácido o neutro.

Primero, crea una phvariable y pídele al usuario un valor entre 0 y 14.

Escribe una ifdeclaración elifque elsediga que:

Si phes mayor que 7, salida "Básico".
Si phes menor que 7, salida "Ácido".
De lo contrario, salida "Neutral".
"""

ph = int(input("Ingrese el nivel de PH (0-14): "))

if ph > 7:
    print("Básico")
elif ph < 7:
    print("Acido")
else:
    print("Neutral")
