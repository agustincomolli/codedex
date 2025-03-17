"""
El proyecto "Terminal Adventure" consiste en crear un juego de aventura
basado en texto que se ejecuta en la terminal. El jugador navegará por
diferentes escenarios tomando decisiones que afectarán el desarrollo de la historia.

Objetivos:
Crear un juego interactivo donde el usuario puede tomar decisiones
Implementar múltiples caminos y finales posibles
Utilizar variables para seguir el progreso del jugador
Usar estructuras de control (if/elif/else) para manejar las decisiones
Implementar bucles para permitir que el juego continúe hasta que termine

Requisitos técnicos:
Utilizar variables para almacenar el nombre del jugador, ubicación actual,
objetos recolectados, etc.
Usar condicionales (if/elif/else) para manejar las diferentes opciones y caminos
Implementar bucles while/for para mantener el juego en ejecución
Utilizar la función input() para recibir decisiones del usuario
Usar print() para mostrar descripciones y opciones
"""

import random
import os
import time

TITLE = r"""
 _____         ____          ____   __    __    _____   __    __     ____   
(_   _)       (    )        / ___)  ) )  ( (   / ___/   ) )  ( (    (    )  
  | |         / /\ \       / /     ( (    ) ) ( (__    ( (    ) )   / /\ \  
  | |        ( (__) )     ( (       ) )  ( (   ) __)    \ \  / /   ( (__) ) 
  | |   __    )    (      ( (      ( (    ) ) ( (        \ \/ /     )    (  
__| |___) )  /  /\  \      \ \___   ) \__/ (   \ \___     \  /     /  /\  \ 
\________/  /__(  )__\      \____)  \______/    \____\     \/     /__(  )__\
"""

CAVE_LOGO = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠂⠉⠉⠉⠉⢁⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⣤⡠⠤⠴⠏⠀⠛⠀⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣼⣷⣷⡶⣶⠦⠀⠀⠀⢀⣀⣀⡀⠤⡎⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡖⠁⠀⣜⡹⠊⠁⠀⣀⣀⣠⠀⠀⠈⢑⡢⠈⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡾⠿⠓⠈⢀⡠⡴⠊⠉⠀⠀⠀⠙⡆⠀⠀⠀⠀⠀⠳⢴⡆⠀⠀⠀
⠀⠀⢀⡠⠋⠀⢠⠔⠂⣡⡞⢁⣠⣾⣿⣦⡀⠀⠱⡀⠀⠀⠀⠀⠀⢦⣇⢃⠀⠀
⠀⠀⡎⠀⠀⡠⢃⡔⢋⣰⣿⣿⣿⣿⣿⣿⣷⣤⡀⠙⡄⠀⠰⡟⠀⠈⡆⠏⡄⠀
⠀⡰⢻⠀⠙⢃⣾⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⠀⢀⣷⠰⣄⣴⠎⢹⡆
⢠⠁⢸⣄⠖⣮⢳⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣱⢀⡘⠘⠟⠯⡆⠀⢈⢷
⠧⡀⢠⠋⢀⠗⣾⣤⠜⢿⠿⠿⠛⠛⠛⠉⠉⠉⠉⣏⢀⣈⠧⣬⣀⣰⠧⣤⡼⠼
⠀⠀⢐⠖⢾⣄⣟⣀⠀⣀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⢄⣓⠚⠿⠏⠒⠃⠀⠀
⠀⠀⠈⠀⠀⣈⡀⠀⣹⠙⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

CAVE_ENTRANCE = r"""
                /\
               /**\
              /****\   /\
             /      \ /**\
            /  /\    /    \ 
           /  /  \  /      \     ( )   ( )
 0        /  / __ \/ /\     \   (   ) (   )
/|\      /  / |  | \/  \/\   \   ( )   ( )
/ \     /__/__|__|__\___\_\___\   |     |
"""

CAVE = r"""
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',         Bifurcación         ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|==;                   ;==|.'.'.'.'.|
|.'.'.'.'.|::|', _____________ ,'|::|.'.'.'.'.|
|.'.'.'.'.|::|',|,',',',',',',|,'|::|.'.'.'.'.|
|.'.'.'.'.|--|'.|.'.'.'.'.'.'.|.'|--|.'.'.'.'.|
|.'.'.'.'.|::|'.|,',',',',',',|.'|::|.'.'.'.'.|
|,',',',',|--|',|.'.'.'.'.'.'.|,'|--|,',',',',|
|.'.'.'.'.|::|'.|,',',',',',',|.'|::|.'.'.'.'.|
|.'.'.'.'.|==:'    <-- ? -->    ':==|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;____________/%%%%%%%%%%%%%%%%%\____________;|
"""

LEFT_SWORD = r"""
+-----------------------------------------------------------------------------+
| |       |\                                           -~ /     \  /          |
|~~__     | \                                         | \/       /\          /|
|    --   |  \                                        | / \    /    \     /   |
|      |~_|   \                                       |/    \/         /      |
|--__  |   -- |\______________________________________|    /  \     /     \   |
|   |~~--__  |~_|____|____|____|____|____|_______|____|\ /      \/          \/|
|   |      |~--_|__|____|____|___    __|____|__|____|_|/ \    /   \       /   |
|___|______|__|_||___|____|____|  ()   ___|__|____|___|    \/       \  /      |
|  \~~~~ :   | _|__|____|____|    )(    ________|____||   /  \      /  \      |
|      | :_--~~ |_|_____|__|_  o======o  __|__|____|__|\/      \ /        \   |
|  __--| :  |  /                  ||                  | \     /  \          /\|
|~~  |   :  | /     espada -->    ||                  |  \  /      \      /   |
|    |      |/                    ||                  |  /\          \  /     |
|    |      /                ,c88888888b              |/   \          /\      |
|    |     /                ,88888888888b              -_   \       /    \    |
+-----------------------------------------------------------------------------+
"""

LEFT = r"""
+-----------------------------------------------------------------------------+
| |       |\                                           -~ /     \  /          |
|~~__     | \                                         | \/       /\          /|
|    --   |  \                                        | / \    /    \     /   |
|      |~_|   \                                       |/    \/         /      |
|--__  |   -- |\______________________________________|    /  \     /     \   |
|   |~~--__  |~_|____|____|____|____|____|____|____|__|\ /      \/          \/|
|   |      |~--_|__|____|____|____|____|____|____|____|/ \    /   \       /   |
|___|______|__|_||____|____|____|____|____|____|____|_|    \/       \  /      |
|  \~~~~ :   | _|___|____|____|____|____|____|____|___|   /  \      /  \      |
|      | :_--~~ |_|____|____|____|____|____|____|____||\/      \ /        \   |
|  __--| :  |  /                                      | \     /  \          /\|
|~~  |   :  | /                                       |  \  /      \      /   |
|    |      |/                                        |  /\          \  /     |
|    |      /                                         |/   \          /\      |
|    |     /                                           -_   \       /    \    |
+-----------------------------------------------------------------------------+
"""

KEY = r"""
  8 8          ,o. 
 d8o8azzzzzzzzd   b
               `o' 
"""

POTION = r"""
  |~|  
  | |  
.'   `.
`.___.'
"""

SWORD = r"""
 _         | |
| | _______| |---------------------------------------------\
|:-)_______|==[]============================================>
|_|        | |---------------------------------------------/
           |_|
"""

RIGHT = r"""
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|                         |.'.'.'.'.|
|.'.'.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
|.'.'.'.'.|---|'.|,  __.__  ,|.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|o  |  o|'|.'|:::|.'.'.'.'.|
|,',',',',|---|',|'|  -|-  |'|,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|o  |  o|'|.'|:::|.'.'.'.'.|
|.'.'.'.'.|---|',' --------- ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
|.'.'.'.'.|        /%%%%%%%\        |.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;___________________________________________;|
"""

TREASURE = r"""
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
       %%%%
"""

DRAGON = r"""
            <>=======()
           (/\___   /|\\          ()==========<>_
                 \_/ | \\        //|\   ______/ \)
                   \_|  \\      // | \_/
                     \|\/|\_   //  /\/
                      (oo)\ \_//  /
                     //_/\_\/ /  |
                    @@/  |=\  \  |
                         \_=\_ \ |
                           \==\ \|\_
                        __(\===\(  )\
                       (((~) __(_/   |
                            (((~) \  /
                            ______/ /
                            '------'
"""

FOREST = r"""
        &&& &&  & &&              &&& &&  & &&
     && &\/&\|& ()|/ @, &&     && &\/&\|& ()|/ @, &&
     &\/(/&/&||/& /_/)_&/_&    &\/(/&/&||/& /_/)_&/_&
  &() &\/&|()|/&\/ '%" & ()  &() &\/&|()|/&\/ '%" & ()
 &_\_&&_\ |& |&&/&__%_/_& && &_\_&&_\ |& |&&/&__%_/_& &&
&&    && & &| &| /& & % ()& /&&   &&    && & &| &| /& & % ()& /&&
  ()&_---()&\&\|&&-&&--%---()~   ()&_---()&\&\|&&-&&--%---()~
   &&      \|||                &&      \|||
            |||                         |||
            |||           O             |||
            |||          /|\            |||
    , -=-~    .-^- _     / \     , -=-~    .-^- _
             `                       `
"""

RIP = r"""
 _____                        _____                
|  __ \                      |  _  |               
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   

                      -|-
                       |
                   .-'~~~`-.
                 .'         `.
                 |  R  I  P  |
                 |           |
                 |           |
               \\|           |//
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

VICTORY = r"""
   .
  / \
  | |
  |.|
  |.|
  |:|      __
,_|:|_,   /  )
  (Oo    / _I_
   +\ \  || __|
      \ \||___|
        \ /.:.\-\
         |.:. /-----\
         |___|::oOo::|
         /   |:<_T_>:|
        |_____\ ::: /
         | |  \ \:/
         | |   | |
         \ /   | \___
         / |   \_____\
         `-'
"""

EXIT = r"""
               [     ]                      [     ]
              [_______][ ][ ][ ][][ ][ ][ ][_______]
               |     |  ,----------------,  |     |
               |     |/'    ____..____    '\|     |
               |     |    /'    ||    '\    |     |
               |     |   |o     ||     o|   |     |
               |  _  |   |     _||_     |   |  _  |
               | (_) |   |    (_||_)    |   | (_) |
               |     |   |     (||)     |   |     |
               |     |   |      ||      |   |     |
               |     |   |o     ||     o|   |     |
______________[_______]--'------''------'--[_______]_____________

"""


def main() -> None:
    """ Función principal del programa """
    state = {
        "location": "start",
        "health": 100,
        "is_playing": True,
        "has_key": False,
        "has_potion": False,
        "has_sword": False,
        "player_name": ""
    }

    # Limpiar la pantalla.
    clear()

    print(center_text(TITLE), end="")
    print(center_text(CAVE_LOGO))
    time.sleep(2)

    print_slowly("¡Bienvenido a Terminal Adventure: La Cueva Misteriosa!")
    state["player_name"] = input("\n¿Cuál es tu nombre, aventurero? > ")
    print(f"\n¡Saludos, {state["player_name"]}!\n")

    # Esperar un segundo.
    time.sleep(1)

    while state["is_playing"]:
        clear()
        if state["location"] == "start":
            show_start_location(state)
        elif state["location"] == "cave":
            show_cave_location(state)
        elif state["location"] == "left":
            show_left_location(state)
        elif state["location"] == "right":
            show_right_location(state)
        elif state["location"] == "treasure":
            show_treasure_location(state)
        elif state["location"] == "dragon":
            show_dragon_location(state)
        elif state["location"] == "forest":
            show_forest_location(state)
        elif state["location"] == "exit":
            show_exit_location(state)
        elif state["location"] == "death":
            show_death_location(state)


def clear() -> None:
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_slowly(text: str, speed: float = 0.03) -> None:
    """
    Imprime el texto dado en la terminal un carácter a la vez con un retraso.

    Args:
        text (str): El texto a imprimir lentamente.
        speed (float, optional): El retraso en segundos entre cada carácter. 
        El valor predeterminado es 0.03 segundos.

    Returns:
        None
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()


def center_text(text: str) -> str:
    """ Centra el texto en la consola.
    Args:
        text (str): El texto a centrar.

    Returns:
        str: El texto centrado.
    """
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    console_width = os.get_terminal_size().columns
    padding = (console_width - max_length) // 2
    centered_lines = [f"{' ' * padding}{line}" for line in lines]
    return '\n'.join(centered_lines)


def get_choice(options: list[str]) -> int:
    """
    Muestra una lista de opciones y solicita al usuario que haga una elección.

    Args:
        options (list[str]): Una lista de cadenas que representan las opciones disponibles.

    Returns:
        int: El índice (basado en 1) de la opción elegida.

    La función solicitará repetidamente al usuario hasta que se haga una elección válida.
    """
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i} - {option}")

        choice = input("\n¿Qué deseas hacer? > ")

        if choice.isdigit() and int(choice) >= 1 and int(choice) <= len(options):
            return int(choice)
        print("Opción no válida. Intenta de nuevo.\n")


def show_start_location(state: dict) -> dict:
    """
    Muestra la ubicación inicial del juego y presenta opciones al jugador.
    La función imprime una descripción de la ubicación inicial utilizando la función `print_slowly`.
    Luego, presenta al jugador tres opciones:
    1. Entrar a la cueva
    2. Explorar los alrededores
    3. Revisar tu inventario
    Dependiendo de la elección del jugador, la función retorna una cadena que indica la siguiente 
    ubicación:
    - "cave" si el jugador elige entrar a la cueva.
    - "forest" si el jugador elige explorar los alrededores.
    - "start" si el jugador elige revisar su inventario (después de mostrar el inventario).

    Returns:
        str: La siguiente ubicación basada en la elección del jugador.
    """
    print(center_text(CAVE_ENTRANCE))
    print_slowly("Te encuentras frente a la entrada de una misteriosa cueva.")
    print_slowly("Los lugareños hablan de un tesoro oculto en su interior, " +
                 "pero nadie ha regresado para contarlo.")
    print_slowly("El viento sopla suavemente, como si la cueva respirara...\n")

    options: list[str] = ["Entrar a la cueva",
                          "Explorar los alrededores",
                          "Revisar tu inventario",
                          "Salir del juego"]
    choice = get_choice(options)

    if choice == 1:
        state["location"] = "cave"
    elif choice == 2:
        state["location"] = "forest"
    elif choice == 3:
        show_inventory(state)
    else:
        state["is_playing"] = False

    return state


def show_inventory(state: dict) -> None:
    """
    Muestra el inventario del jugador en la terminal.
    Args:
        state (dict): Un diccionario que contiene el estado del jugador. 
                      Debe incluir las siguientes claves:
                      - "has_sword" (bool): Indica si el jugador tiene una espada.
                      - "has_key" (bool): Indica si el jugador tiene una llave.
                      - "has_potion" (bool): Indica si el jugador tiene una poción.
                      - "health" (int): La salud actual del jugador (0-100).
    Returns:
        None
    """
    sword: str = "Sí" if state["has_sword"] else "No"
    key: str = "Sí" if state["has_key"] else "No"
    potion: str = "Sí" if state["has_potion"] else "No"
    health: str = str(state["health"]) if state["health"] == 100 else str(
        state["health"]) + " "

    # Limpiar la pantalla.
    clear()
    inventory = rf"""
            \ ||| /
            ( o o )
 ~~~ooO~~~~~~ (_) ~~~~~~~~~~~~
|                             |
|          INVENTARIO         |
|          ~~~~~~~~~~         |
|                             |
|         Espada = {sword}         |
|         Llave = {key}          |
|         Poción = {potion}         |
|                             |
|         Salud = {health}         |
|                             |
 ~~~~~~~~~~~~~~~~~~~~~~~ooO~~~
          |____|____|
            ||   ||
           ooO   Ooo
"""
    print(center_text(inventory))
    input("Presione ENTER para continuar...")
    print()


def show_cave_location(state: dict) -> dict:
    """
    Muestra la ubicación de la cueva y permite al jugador elegir una acción.
    Args:
        state (dict): El estado actual del juego, que incluye la ubicación y otros datos relevantes.
    Returns:
        dict: El estado actualizado del juego después de la elección del jugador.
    """
    clear()
    print(center_text(CAVE))
    print_slowly("Entras a la cueva. Está oscuro y húmedo.")
    print_slowly("Tus pasos resuenan en las paredes rocosas.")
    print_slowly("A medida que tus ojos se adaptan a la oscuridad, " +
                 "notas que el camino se bifurca.\n")

    options = ["Ir hacia la izquierda", "Ir hacia la derecha",
               "Revisar tu inventario", "Volver a la entrada"]

    choice = get_choice(options)

    if choice == 1:
        state["location"] = "left"
    elif choice == 2:
        state["location"] = "right"
    elif choice == 3:
        show_inventory(state)
    else:
        state["location"] = "start"
    return state


def show_left_location(state: dict) -> dict:
    """
    Muestra la ubicación a la izquierda en la cueva y permite al jugador tomar decisiones.
    Args:
        state (dict): El estado actual del juego, que incluye información sobre 
                      si el jugador tiene la espada y la llave, y la ubicación actual.
    Return:
        dict: El estado actualizado del juego después de que el jugador haya tomado una decisión.    
    """
    if not state["has_sword"]:
        print(center_text(LEFT_SWORD))
        print_slowly("Sigues el camino de la izquierda, que desciende " +
                     "profundamente en la cueva.")
        print_slowly(
            "El aire se vuelve más frío y escuchas un sonido metálico.")
        print_slowly("¡Encuentras una espada antigua clavada en una roca!\n")
        options = ["Tomar la espada", "Dejarla e investigar más adelante",
                   "Revisar tu inventario", "Volver atrás"]

        choice = get_choice(options)
        if choice == 1:
            state["has_sword"] = True
            print(center_text(SWORD))
            print(center_text("¡Has obtenido una espada antigua!"))
        elif choice == 2:
            print_slowly("Decides dejar la espada por ahora.")
        elif choice == 3:
            show_inventory(state)
        else:
            state["location"] = "cave"
    else:
        print(center_text(LEFT))
        print_slowly("Sigues el camino de la izquierda, que desciende " +
                     "profundamente en la cueva.")
        print_slowly(
            "El aire se vuelve más frío y escuchas un sonido metálico.")
        print_slowly("Continúas por el camino y llegas a una pequeña cámara.")

        if not state["has_key"]:
            print_slowly(
                "¡En un rincón brillante, encuentras una llave dorada!\n")
            options = ["Tomar la llave", "Dejarla por ahora",
                       "Revisar tu inventario", "Volver atrás"]
            choice = get_choice(options)
            if choice == 1:
                state["has_key"] = True
                print(center_text(KEY))
                print("¡Has obtenido una Llave dorada!")
            elif choice == 2:
                print_slowly("Decides dejar la llave por ahora.")
            elif choice == 3:
                show_inventory(state)
            else:
                state["location"] = "cave"
        else:
            print_slowly(
                "No parece haber nada más interesante en esta cámara.\n")
            options = ["Revisar tu inventario", "Volver atrás"]
            choice = get_choice(options)
            if choice == 1:
                show_inventory(state)
            else:
                state["location"] = "cave"

    input("\nPresione ENTER para continuar...")
    return state


def show_right_location(state: dict) -> dict:
    """
    Muestra la ubicación a la derecha en la aventura y maneja las interacciones del jugador.
    Args:
        state (dict): El estado actual del juego, que incluye información sobre el 
                      inventario del jugador y su ubicación.
    Returns:
        dict: El estado actualizado del juego después de las interacciones del jugador 
              en esta ubicación.
    """
    print(center_text(RIGHT))
    print_slowly(
        "Sigues el camino de la derecha, que se estrecha cada vez más.")
    print_slowly(
        "Escuchas un goteo constante y percibes un brillo al final del túnel.")

    if not state["has_potion"]:
        print_slowly(
            "Encuentras un estante con una poción de color rojo brillante.\n")

        options = ["Tomar la poción", "Dejarla e investigar más adelante",
                   "Revisar tu inventario", "Volver atrás"]
        choice = get_choice(options)

        if choice == 1:
            state["has_potion"] = True
            print(center_text(POTION))
            print(center_text("¡Has obtenido una Poción curativa!"))
        elif choice == 2:
            print_slowly("Decides dejar la poción por ahora.")
        elif choice == 3:
            show_inventory(state)
        else:
            state["location"] = "cave"
    else:
        print_slowly("El brillo que veías al final del túnel proviene de " +
                     "una puerta dorada.")
        print_slowly("La puerta tiene una cerradura resplandeciente.")
        if not state["has_key"]:
            print_slowly("Necesitas una llave para abrir esta puerta.\n")

            options = ["Revisar tu inventario", "Volver atrás"]
            choice = get_choice(options)

            if choice == 1:
                show_inventory(state)
            else:
                state["location"] = "cave"
        else:
            print()
            options = ["Usar la llave dorada",
                       "Revisar tu inventario", "Volver atrás"]
            choice = get_choice(options)

            if choice == 1:
                print_slowly("¡La llave encaja perfectamente!")
                print_slowly("La puerta se abre lentamente...")
                state["location"] = "treasure"
            elif choice == 2:
                show_inventory(state)
            else:
                state["location"] = "cave"

    input("\nPresione ENTER para continuar...")
    return state


def show_treasure_location(state: dict) -> dict:
    """
    Muestra la ubicación del tesoro y permite al jugador tomar una decisión.
    Args:
        state (dict): El estado actual del juego.
    Returns:
        dict: El estado actualizado del juego después de la elección del jugador.    
    """
    print(center_text(TREASURE))
    print_slowly("¡Entras en una cámara llena de tesoros brillantes!")
    print_slowly("Oro, joyas y artefactos antiguos llenan la sala.")
    print_slowly("En el centro hay un cofre particularmente grande.\n")

    options = ["Abrir el cofre central", "Recoger algunas monedas",
               "Revisar tu inventario", "Salir de la cámara"]
    choice = get_choice(options)

    if choice == 1:
        print_slowly("Te acercas al cofre central con cautela...")
        print_slowly("Al abrirlo...")
        time.sleep(1.5)
        print_slowly("¡UN DRAGÓN DESPIERTA DETRÁS DE TI!")
        state["location"] = "dragon"
    elif choice == 2:
        print_slowly("Recoges algunas monedas de oro y las guardas.")
        print_slowly("Sientes tus bolsillos muy pesados...")
    elif choice == 3:
        show_inventory(state)
    else:
        state["location"] = "right"

    input("\nPresione ENTER para continuar...")
    return state


def show_dragon_location(state: dict) -> dict:
    """
    Muestra la ubicación del dragón y permite al jugador tomar decisiones
    basadas en su estado actual.
    Args:
        state (dict): El estado actual del juego, incluyendo la salud del jugador,
                      si tiene la espada antigua, si tiene pociones curativas, y
                      la ubicación actual.
    Returns:
        dict: El estado actualizado del juego después de la interacción con el dragón.
    """
    print(center_text(DRAGON))
    print_slowly("¡Un enorme dragón rojo se alza frente a ti!")
    print_slowly("Sus ojos amarillos te miran fijamente mientras exhala humo " +
                 "por sus fosas nasales.\n")

    if state["has_sword"]:
        options = ["Luchar con la espada antigua", "Huir",
                   "Usar poción curativa", "Revisar tu inventario"]
        choice = get_choice(options)

        if choice == 1:
            print_slowly(
                "¡Empuñas la espada antigua, que comienza a brillar con una luz azul!")
            print_slowly(
                "El dragón retrocede ante el brillo, parece temer a la espada.")
            print_slowly("Avanzas con determinación...")

            # Probabilidad de éxito del 70%
            if random.random() < 0.7:
                print_slowly(
                    "¡Con un movimiento rápido, logras herir al dragón!")
                print_slowly("La bestia ruge de dolor y se retira volando por una " +
                             "apertura en el techo.")
                print_slowly("¡Has derrotado al dragón y el tesoro es tuyo!")
                state["location"] = "exit"
            else:
                print_slowly(
                    "¡El dragón es demasiado rápido y te golpea con su cola!")
                state["health"] -= 50
                print_slowly("¡Has perdido 50 puntos de salud! " +
                             f"Salud actual: {state['health']}")
                if state["health"] <= 0:
                    print_slowly("El golpe es demasiado fuerte...")
                    print_slowly("Todo se vuelve oscuro...")
                    state["location"] = "death"
                else:
                    print_slowly("Te tambaleas pero logras mantenerte en pie.")
        elif choice == 2:
            print_slowly("Intentas huir del dragón...")
            # Probabilidad de éxito del 40%
            if random.random() < 0.4:
                print_slowly("¡Logras escabullirte mientras el dragón está " +
                             "distraído con el tesoro!")
                state["location"] = "right"
            else:
                print_slowly(
                    "¡El dragón te bloquea el paso y te ataca con sus garras!")
                state["health"] -= 60
                print_slowly("¡Has perdido 60 puntos de salud! " +
                             f"Salud actual: {state['health']}")

                if state["health"] <= 0:
                    print_slowly("El ataque es letal...")
                    state["location"] = "death"
        elif choice == 3:
            if state["has_potion"]:
                print_slowly("Bebes rápidamente la poción curativa.")
                state["health"] = min(100, state["health"] + 50)
                print_slowly(
                    f"¡Te has curado! Salud actual: {state['health']}")
                state["has_potion"] = False
            else:
                print_slowly("¡No tienes ninguna poción curativa!")
        else:
            show_inventory(state)
    else:
        print()
        options = ["Intentar huir", "Usar poción curativa",
                   "Revisar tu inventario"]
        choice = get_choice(options)

        if choice == 1:
            print_slowly("Intentas huir del dragón...")
            # Probabilidad baja de éxito sin espada
            if random.random() < 0.2:
                print_slowly("¡Por pura suerte logras escabullirte mientras el " +
                             "dragón está distraído!")
                state["location"] = "right"
            else:
                print_slowly(
                    "¡El dragón te bloquea el paso y te ataca con fuego!")
                state["health"] -= 70
                print_slowly(
                    f"¡Has perdido 70 puntos de salud! Salud actual: {state['health']}")

                if state["health"] <= 0:
                    print_slowly("Las llamas te consumen...")
                    state["location"] = "death"
        elif choice == 2:
            if state["has_potion"]:
                print_slowly("Bebes rápidamente la poción curativa.")
                state["health"] = min(100, state["health"] + 50)
                print_slowly(
                    f"¡Te has curado! Salud actual: {state['health']}")
                state["has_potion"] = False
            else:
                print_slowly("¡No tienes ninguna poción curativa!")
        else:
            show_inventory(state)

    input("\nPresione ENTER para continuar...")
    return state


def show_forest_location(state: dict) -> dict:
    """
    Muestra la ubicación del bosque y permite al jugador interactuar con el entorno.
    Args:
        state (dict): El estado actual del juego, que incluye información sobre el inventario 
                      y la ubicación del jugador.
    Returns:
        dict: El estado actualizado del juego después de la interacción del jugador en el bosque.
    """
    clear()
    print(center_text(FOREST))
    print_slowly("Te adentras en el bosque que rodea la cueva.")
    print_slowly("Los árboles son altos y el follaje es denso.")

    if not state["has_potion"]:
        print_slowly("Encuentras un arbusto con bayas rojas brillantes.\n")

        options = ["Recoger las bayas", "Ignorar las bayas",
                   "Revisar tu inventario", "Volver a la entrada de la cueva"]
        choice = get_choice(options)

        if choice == 1:
            print_slowly("Recoges las bayas y las mezclas con agua de " +
                         "un arroyo cercano.\n")
            print(center_text(POTION))
            print(center_text("¡Has creado una Poción curativa!"))
            state["has_potion"] = True
        elif choice == 2:
            print_slowly("Decides no tocar las bayas desconocidas.")
        elif choice == 3:
            show_inventory(state)
        else:
            state["location"] = "start"
    else:
        print_slowly("El bosque parece tranquilo, pero sientes que hay algo " +
                     "importante en la cueva.\n")

        options = ["Explorar más el bosque",
                   "Revisar tu inventario",
                   "Volver a la entrada de la cueva"]
        choice = get_choice(options)

        if choice == 1:
            print_slowly("Exploras más profundamente el bosque...")
            print_slowly("Después de un rato, te das cuenta de que estás " +
                         "dando vueltas en círculos.")
            print("Decides regresar al punto de partida.")
        elif choice == 2:
            show_inventory(state)
        else:
            state["location"] = "start"

    input("\nPresione ENTER para continuar...")
    return state


def show_exit_location(state: dict) -> dict:
    """
    Muestra el mensaje de victoria y finaliza el juego.

    Esta función imprime un mensaje de victoria, felicitando al jugador por
    haber conseguido el tesoro y derrotado al dragón. Luego, actualiza el
    estado del juego para indicar que el jugador ha terminado de jugar.

    Args:
        state (dict): El estado actual del juego, incluyendo el nombre del
                      jugador y si el juego está en curso.

    Returns:
        dict: El estado actualizado del juego, con 'is_playing' establecido
              en False.
    """
    print(center_text(VICTORY))
    print_slowly("¡Has conseguido el tesoro y derrotado al dragón!")
    print_slowly(f"Felicidades, {state['player_name']}! Tu valentía " +
                 "será recordada en las leyendas.")
    print_slowly("El tesoro del dragón contiene riquezas más allá " +
                 "de tus sueños.\n")
    print(center_text("--- FIN DE LA AVENTURA ---"))
    print_slowly("\n¡Has completado Terminal Adventure: La Cueva Misteriosa!")
    state["is_playing"] = False
    return state


def show_death_location(state: dict) -> dict:
    """
    Muestra un mensaje de muerte y finaliza el juego.

    Esta función imprime un mensaje indicando que el jugador ha muerto y
    que la aventura ha terminado. Actualiza el estado del juego para
    reflejar que el jugador ya no está jugando.

    Args:
        state (dict): El estado actual del juego, incluyendo el nombre
                      del jugador y si el juego está en curso.

    Returns:
        dict: El estado actualizado del juego con 'is_playing' establecido
              en False.
    """
    print(center_text(RIP))
    print_slowly("La oscuridad te envuelve...")
    print_slowly("Lamentablemente, tu aventura termina aquí, " +
                 f"{state['player_name']}.")
    print_slowly("Quizás otro aventurero tenga más suerte en el futuro.\n")
    print(center_text("--- FIN DE LA AVENTURA ---"))
    print_slowly("\n¡Has fracasado en Terminal Adventure: La Cueva Misteriosa!")
    state["is_playing"] = False
    return state


if __name__ == "__main__":
    main()
