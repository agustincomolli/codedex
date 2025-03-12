"""
Calculadora de Área (Area Calculator):

Objetivo: Crear un programa que calcule el área de diferentes figuras 
geométricas.

Requisitos:
El programa debe permitir al usuario elegir entre las siguientes figuras:
Círculo
Triángulo
Cuadrado
Rectángulo
Según la figura elegida, el programa debe solicitar al usuario los datos 
necesarios para calcular el área (radio, base, altura, lado, etc.).
El programa debe mostrar el resultado del cálculo con un mensaje claro.
El programa debe incluir validación de entrada para asegurarse de que el 
usuario ingresa datos numéricos válidos.

Ejemplo:
El usuario elige "Círculo".
El programa solicita el "Radio".
El usuario ingresa "5".
El programa muestra "El área del círculo es 78.54".
"""

MENU = "Elija una opción:\n"
MENU += "\t1: Círculo\n"
MENU += "\t2: Triángulo\n"
MENU += "\t3: Cuadrado\n"
MENU += "\t4: Rectángulo\n"
MENU += "\t5: Salir"

while True:
    area: float = 0
    print("*** CALCULADORA DE AREA ***\n")
    print(MENU)
    option = int(input("~> "))

    if option == 1:
        PI = 3.14159
        radio = int(input("Radio: "))
        area = PI * radio
    elif option == 2:
        base = int(input("Base: "))
        height = int(input("Altura: "))
        area = (base * height) / 2
    elif option == 3:
        side = int(input("Lado: "))
        area = side * side
    elif option == 4:
        base = int(input("Base: "))
        height = int(input("Altura: "))
        area = base * height
    elif option == 5:
        break
    elif option <= 0 or option > 5:
        continue

    print(f"El área es: {area:.2f}")

print("¡Hasta luego! 👋")
