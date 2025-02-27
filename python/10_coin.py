# pylint: disable=invalid-name
"""
Control de flujo
"""

import random

coin = random.randint(0,1) # Generar un número aleatorio entre 0 y 1

if coin > 0.5:
    print("La moneda 🪙 salió cara. 😀")
else:
    print("La moneda 🪙 salió cruz. ❌")
