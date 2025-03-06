# pylint: disable=invalid-name

"""
Primero, pregúntele al usuario “¿Ya llegamos?” usando la función input() y 
guárdela en una variable answer.

Luego, utilice un bucle while que le pregunte al usuario "¿Ya llegamos?" una 
y otra vez hasta que responda "Sí".

El resultado podría verse así:

Are we there yet? One more hour
Are we there yet? Almost there
Are we there yet? Don't make me pull over
Are we there yet? Yes
"""

answer = input("Ya llegamos? ")
while answer != "Sí":
    answer = input("Ya llegamos? ")
