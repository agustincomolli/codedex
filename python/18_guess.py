# pylint: disable=invalid-name
"""
Crea un programa guess.py y escribe lo siguiente:

guess = 0

while guess != 6:
  guess = int(input("Guess the number:  "))

print("You got it!")

Ejecute el código varias veces para comprender lo que hace.

Hagámoslo de modo que sea el mismo juego de adivinanzas, pero con un nuevo 
límite en el número de intentos (antes era infinito).

Primero, introduzca una variable llamada tries en la parte superior y asígnele 
un valor de 0.

Luego, agrega la tries variable al while bucle usando un operador relacional 
(como lo hiciste con guess).
"""

TO_GUESS = 123
TOTAL_TRIES = 4
guess = 0
tries = 0

print("ADIVINA EL NUMERO 🔢")

while guess != TO_GUESS and tries < TOTAL_TRIES:
    guess = int(input("Adivina el número: "))
    tries += 1

if guess == TO_GUESS:
    print("¡Lo adivinaste, felicitaciones! 🥳")
else:
    print("¡Uh, mejor suerte para la próxima vez! 😣")
