# pylint: disable=invalid-name

"""
Ejemplo de bucle While
"""

print("BANCO DE CODEDEX 🏦")

pin = int(input("Ingrese su PIN: "))

while pin != 1234:
    pin = int(input("PIN incorrecto. Ingrese su PIN de nuevo: "))

if pin == 1234:
    print("\nPIN aceptado. ¡Bienvenido!")
