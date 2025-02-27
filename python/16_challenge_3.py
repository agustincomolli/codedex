# pylint: disable=invalid-name
"""
🤯 Datos sobre Snapple
Snapple es una famosa marca de té de Queens, Nueva York. Cada tapa de botella 
viene con un dato divertido y tonto.

Usa el módulo aleatorio para crear un número del 0 al 5.

Luego usa una declaración if/elif/else para imprimir uno de estos seis datos 
aleatorios sobre Snapple:

0 - 'Los flamencos se ponen rosados por comer camarones'.
1 - 'El único alimento que no se echa a perder es la miel'.
2 - 'Los camarones solo pueden nadar hacia atrás'.
3 - 'La vida útil de una papila gustativa es de aproximadamente 10 días'.
4 - 'Es imposible estornudar mientras se duerme'.
5 - 'Es ilegal cantar desafinado en Carolina del Norte'.
"""

import random

print("🤯 Datos sobre Snapple\n")

number = random.randint(0, 5)

if number == 0:
    print("Los flamencos se ponen rosados por comer camarones")
elif number == 1:
    print("El único alimento que no se echa a perder es la miel")
elif number == 2:
    print("Los camarones solo pueden nadar hacia atrás")
elif number == 3:
    print("La vida útil de una papila gustativa es de aproximadamente 10 días")
elif number == 4:
    print("Es imposible estornudar mientras se duerme")
else:
    print("Es ilegal cantar desafinado en Carolina del Norte")
