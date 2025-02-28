# pylint: disable=invalid-name

"""
Cree un programa fizz_buzz.py que genere números del 1 al 100.

Aquí está el truco:

Para múltiplos de 3, imprima "Fizz" en lugar del número.
Para múltiplos de 5, imprima "Buzz" en lugar del número.
Aquí viene la parte complicada: para múltiplos de 3 y 5, imprima "FizzBuzz".
"""

print("FIZZ BUZZ")

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
