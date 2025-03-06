# pylint: disable=invalid-name

"""
Utilice un for bucle y range() una función para mostrar el siguiente patrón en la 
terminal usando un grupo de asteriscos *:

*
* *
* * *
* * * *
* * * * *
# ... and so on

Debería verse así, pero con un total de 24 filas. La primera fila debería 
tener un asterisco y la última, 24.

Nota: Asegúrese de que haya un espacio vacío entre cada asterisco.


"""

for i in range(1, 25):
    print("* " * i)
