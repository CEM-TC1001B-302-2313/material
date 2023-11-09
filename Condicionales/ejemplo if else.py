edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
    print("Puedes votar.")
else:
    faltan = 18 - edad
    print("Aún eres menor de edad.")
    print(f"Te faltan {faltan} años para poder votar.")