# pylint: disable=invalid-name
"""
El Sombrero Seleccionador es un sombrero mágico parlante del Colegio Hogwarts 
de Magia y Hechicería. El sombrero decide a cuál de las cuatro "Casas" va cada 
estudiante de primer año:

🦁Gryffindor
🦅 Ravenclaw
🦡Hufflepuff
🐍Slytherin

Escriba un programa que le haga algunas preguntas al usuario con las funciones 
int() y :input()

P1) ¿Te gusta el amanecer o el anochecer?
    1) El amanecer
    2) El anochecer

Si la respuesta es igual a 1, Gryffindor y Ravenclaw obtienen un +1.
De lo contrario, si la respuesta es igual a 2, Hufflepuff y Slytherin obtienen un +1.
De lo contrario, muestra el mensaje "Entrada incorrecta".

P2) Cuando esté muerto, quiero que la gente me recuerde como:
    1) El bueno
    2) El grande
    3) El sabio
    4) El valiente

Si la respuesta es 1, Hufflepuff +2.
De lo contrario, si la respuesta es 2, Slytherin +2.
De lo contrario, si la respuesta es 3, Ravenclaw +2.
De lo contrario, si la respuesta es 4, Gryffindor +2.
De lo contrario, muestra el mensaje "Entrada incorrecta".

P3) ¿Qué tipo de instrumento te agrada más?
    1) El violín
    2) La trompeta
    3) El piano
    4) La batería

Si la respuesta es 1, Slytherin +4.
De lo contrario, si la respuesta es 2, Hufflepuff +4.
De lo contrario, si la respuesta es 3, Ravenclaw +4.
De lo contrario, si la respuesta es 4, Gryffindor +4.
De lo contrario, muestra "Entrada incorrecta".
Por último, imprima la puntuación de cada casa.

Bono: Si quieres ir más allá, ¡mira si puedes descubrir cómo imprimir la casa 
con más puntos!
"""

print("El sombrero mágico 🎩")

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print() # Salto de sección
print("P1) ¿Te gusta el amanecer o el anochecer?")
print("    1) El amanecer ☀️")
print("    2) El anochecer 🌙")

answer = int(input("> "))

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    slytherin += 1
    hufflepuff += 1
else:
    print("Entrada incorrecta")

print()
print("P2) Cuando esté muerto, quiero que la gente me recuerde como:")
print("    1) El bueno ✌️")
print("    2) El grande 😎")
print("    3) El sabio 🤓")
print("    4) El valiente 💪")

answer = int(input("> "))

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Entrada incorrecta")

print()
print("P3) ¿Qué tipo de instrumento te agrada más?")
print("    1) El violín 🎻")
print("    2) La trompeta 🎺")
print("    3) El piano 🎹")
print("    4) La batería 🥁")

answer = int(input("> "))

if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Entrada incorrecta")

print()
print(f"🦁 Gryffindor: {gryffindor}")
print(f"🦅 Ravenclaw: {ravenclaw}")
print(f"🦡 Hufflepuff {hufflepuff}")
print(f"🐍Slytherin: {slytherin}")

winner = max(gryffindor, ravenclaw, hufflepuff, slytherin)

print()
if winner == gryffindor:
    print("🎩: ¡Has elegido 🦁 Gryffindor!")
elif winner == ravenclaw:
    print("🎩: ¡Has elegido 🦅 Ravenclaw!")
elif winner == hufflepuff:
    print("🎩: ¡Has elegido 🦡 Hufflepuff!")
else:
    print("🎩: ¡Has elegido 🐍Slytherin!")
