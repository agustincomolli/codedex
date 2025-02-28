# pylint: disable=invalid-name

"""
"99 botellas de cerveza" es una vieja canción que los niños molestos, o sea, 
todos, cantaban en viajes por carretera para pasar el tiempo.

Crea un programa 99_bottles.pyfor y usa un bucle y una range()función para 
imprimir todos los versos de "99 Botellas de Cerveza".

99 botellas de cerveza en la pared
99 botellas de cerveza
Toma una y pásala
98 botellas de cerveza en la pared

¡Y no olvides utilizar la interpolación de cadenas!
"""

BOTTLES = 99
for i in range(BOTTLES):
    print(f"{BOTTLES - i} botelllas de cerveza en la pared ")
    print(f"{BOTTLES - i} botelllas de cerveza")
    print("Toma una y pásala")
    print(f"{BOTTLES - i - 1} botelllas de cerveza en la pared ")
