import random

# Permite ingresar una opción entre águila y sol
# Simular un volado
# Avisar el resultado (gana o pierde)

# .strip() -> Quita los espacios vacíos del inicio y del final
# .lower() -> Convierte el contenido a minúsculas
# .upper() -> Convierte el contenido a mayúsuclas
# opcion = input("Elige entre águila y sol: ").strip().lower()
# if opcion == "águila" or opcion == "aguila":
#     print("Eligió águila.")
# elif opcion == "sol":
#     print("Eligió sol.")
# else:
#     print("Está mal.")

opcion = int(input("Elige 1 para águila y 2 para sol: "))
moneda = random.randint(1,2) # Genera un número entero entre 1 y 2
if moneda == 1:
    print("Cayó águila.")
else:
    print("Cayó sol.")
if opcion == moneda:
    print("Ganaste.")
else:
    print("Perdiste.")
    
    