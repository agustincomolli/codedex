# pylint: disable=invalid-name
"""
El teorema de Pitágoras es:
    c = (a^2 + b^2)^0.5
donde c es la hipotenusa mientras que a y b son los catetos.

Cree un programa hypotenuse.py que le pida al usuario dos números, ay b, y 
luego calcule la hipotenusa c.
"""
side_1 = int(input("Ingrese el primer cateto: "))
side_2 = int(input("Ingrese el segundo cateto: "))
hypotenuse = (side_1**2 + side_2**2)**0.5
print(f"La hipotenusa es: {hypotenuse} 📐")
