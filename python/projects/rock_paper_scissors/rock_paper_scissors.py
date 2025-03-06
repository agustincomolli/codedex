"""
Piedra, Papel o Tijera (Rock Paper Scissors):

Objetivo: Crear un juego de Piedra, Papel o Tijera contra la computadora.

Requisitos:
El programa debe permitir al usuario elegir entre Piedra, Papel o Tijera.
La computadora debe elegir una opción al azar.
El programa debe determinar el ganador según las reglas del juego.
El programa debe mostrar la elección del usuario, la elección de la computadora
y el resultado del juego.
El programa debe llevar el conteo de los resultados, para que el usuario pueda 
saber cuantas veces a ganado, perdido o empatado.

Ejemplo:
El usuario elige "Piedra".
La computadora elige "Tijera".
El programa muestra "Elegiste Piedra. La computadora eligió Tijera. ¡Ganaste!".
"""
import random

MESSAGE = "Elige una opción:\n"
MESSAGE += "\t1: ✊ Piedra\n"
MESSAGE += "\t2: 🤚 Papel\n"
MESSAGE += "\t3: ✌️  Tijera\n"
MESSAGE += "~> "

wins: int = 0
ties: int = 0
losses: int = 0

while True:
    print("*** ¿PIEDRA, PAPEL O TIJERA? ***\n")

    user = int(input(MESSAGE))

    while user not in [1, 2, 3]:
        user = int(input(MESSAGE))

    machine = random.randint(1, 3)

    if user == 1:
        print("\nElegiste: ✊")
    elif user == 2:
        print("\nElegiste: 🤚")
    else:
        print("\nElegiste: ✌️")

    if machine == 1:
        print("Tu rival elije: ✊\n")
    elif machine == 2:
        print("Tu rival elije: 🤚\n")
    else:
        print("Tu rival elije: ✌️\n")

    if user == machine:
        print("¡Empate!")
        ties += 1
    elif user == 1 and machine == 3:
        print("¡Ganaste! 🥳")
        wins += 1
    elif user == 1 and machine == 2:
        print("¡Perdiste! 😣")
        losses += 1
    elif user == 2 and machine == 1:
        print("¡Ganaste! 🥳")
        wins += 1
    elif user == 2 and machine == 3:
        print("¡Perdiste! 😣")
        losses += 1
    elif user == 3 and machine == 2:
        print("¡Ganaste! 🥳")
        wins += 1
    else:
        print("¡Perdiste! 😣")
        losses += 1

    want_continue = input("¿Desea continuar? ")
    if want_continue in ["N", "n"]:
        break
    print()

print(f"Victorias: {wins}, Derrotas: {losses}, Empates: {ties}")
