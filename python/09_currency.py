# pylint: disable=invalid-name
"""
Acabamos de regresar de un viaje a Sudamérica, concretamente a Colombia, 
Perú y Brasil. Nos queda algo de efectivo en:

🇨🇴 pesos colombianos (4125,12  x dolar)
🇵🇪 Soles peruanos    (3,68 x dolar)
🇧🇷 reales brasileños (5,79 x dolar)

Crea un programa currency.py que le pide al usuario la cantidad que tiene 
en pesos, soles y reales y calcule el total en USD.
"""

PESOS = 4125.12
SOLES = 3.68
REAIS = 5.79

pesos_left = int(input("¿Cuántos pesos  te sobraron? "))
soles_left = int(input("¿Cuántos soles te sobraron? "))
reais_left = int(input("¿Cuántos reales te sobraron? "))

total = (pesos_left * PESOS) + (soles_left * SOLES) + (reais_left * REAIS)

print(f"Tenés u$s {total} en total. 💰")
