lista_alumnos = ["Sofía", "Ana", "Arturo", "Roberto", "Juan"]
nombre = input("Ingresa el nombre del alumno a buscar: ")
alumno_encontrado = False
for i in lista_alumnos:
    if nombre.lower() == i.lower():
        alumno_encontrado = True
if alumno_encontrado:
    print("Alumno encontrado.")
else:
    print("El alumno no existe en la lista.")

# break -> Rompe el ciclo (termina el ciclo)
# continue -> Detiene la iteración actual y pasa a la siguiente
for i in lista_alumnos:
    if nombre.lower() == i.lower():
        print("Alumno encontrado.")
        break
else: # Se ejecuta si el ciclo no se detuvo con un break
    print("El alumno no existe en la lista.")
