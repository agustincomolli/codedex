# pylint: disable=invalid-name
"""
🧑‍🚀 Pesos de los planetas
Es el año 2199... ¡nos hemos convertido en una especie interplanetaria y 
podemos viajar a otros planetas del sistema solar! 🚀

Crea un programa de conversión de peso que:

Pregunte al usuario cuál es su peso en la Tierra (como un valor flotante).
Pida al usuario un número de planeta (como un int).
Luego, use una declaración if/elif/else para calcular el peso del usuario en el 
planeta de destino.

Para calcular el peso del usuario:

Peso de destino = peso de la Tierra x gravedad relativa

Número Planeta Gravedad relativa
1 Mercurio 0,38
2 Venus 0,91
3 Marte 0,38
4 Júpiter 2,53
5 Saturno 1,07
6 Urano 0,89
7 Neptuno 1,14

Si el usuario ingresa un número de planeta que no esté entre 1 y 7, se 
imprimirá un mensaje que diga 'Número de planeta no válido'.
"""

print("🧑‍🚀 Pesos de los planetas\n")

MERCURY = 0.38
VENUS = 0.91
MARS = 0.38
JUPITER = 2.53
SATURN = 1.07
URANUS = 0.89
NEPTUNE = 1.14

earth_weight = float(input("¿Cuál es tu peso en la Tierra 🌎 ? "))
planet = int(input("Ingrese el número de planeta (1-7): "))

print("Tu peso ⚖️  en el planeta de destino será: ")

if planet == 1:
    print(earth_weight * MERCURY)
elif planet == 2:
    print(earth_weight * VENUS)
elif planet == 3:
    print(earth_weight * MARS)
elif planet == 4:
    print(earth_weight * JUPITER)
elif planet == 5:
    print(earth_weight * SATURN)
elif planet == 6:
    print(earth_weight * URANUS)
elif planet == 7:
    print(earth_weight * NEPTUNE)
else:
    print("Número de planeta no válido")
