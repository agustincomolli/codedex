# pylint: disable=invalid-name

"""
¡Dale la bienvenida al Año Nuevo! Una fiesta de Nochevieja no estaría completa 
sin una cuenta regresiva del 10 al 1.

Utilice un forbucle y la range()función para una cuenta regresiva.

El resultado debería verse así:

10
9
8
7
6
5
4
3
2
1
Happy New Year! 🥳

Contando regresivamente del 10 al 1 en cada línea y luego un mensaje de Feliz 
Año Nuevo al final.
"""

for i in range(10, 0, -1):
    print(i)

print("Happy New Year! 🥳")
