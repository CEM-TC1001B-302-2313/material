# Adivinar un número entre 1 y 100
# Se debe generar un número entero aleatorio entre 1 y 100
# Preguntar por números al usuario hasta que atine al número generado
# Si falla, indicar si el número generado es menor o mayor
# Si gana, indicar cuántos intentos tardó

import random

numero_ganador = random.randint(1,100)
intentos = 0
numero_usuario = 0
while numero_usuario != numero_ganador and intentos < 5:
    numero_usuario = int(input("Ingresa tu número: "))
    if numero_usuario > numero_ganador:
        print("El número que buscas es más pequeño.")
    elif numero_usuario < numero_ganador:
        print("El número que buscas es más grande.")
    intentos += 1
if intentos <= 5:
    print(f"Has atinado al número y te tomó {intentos} intentos.")
else:
    print(f"Perdiste, el número era {numero_ganador}.")