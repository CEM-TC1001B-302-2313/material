
#for i in range(5)

i = 0 # Asigna el valor inicial de i (variable de control - contador)
while i <= 4: # Condición de paro o de salida
    print(f"El valor de i es: {i}")
    i += 1 # Paso
    
print("-" * 20)

# for i in range(20, 10, -3)

i = 20
while i > 10:
    print(f"El valor de i es: {i}")
    i -= 3
    
print("-" * 20)

# for i in texto
texto = "hola mundo"
i = 0
while i < len(texto):
    print(f"i: {i} - texto[{i}]: {texto[i]}")
    i += 1
    
print("-" * 20)

lista = [1,5,7,True,"Hola",[False, "Nada"]]

# for i in lista:
i = 0
while i < len(lista):
    print(f"i: {i} - lista[{i}]: {lista[i]}")
    i += 1

print("-" * 20)

# Ciclo indefinido

centinela = "n"
while centinela != "s":
    centinela = input("¿Desea terminar? (s/n): ")

# Menú ciclado

opcion = 1
while opcion != 0:
    opcion = int(input("""Menú principal:
1) Opción 1
2) Opción 2
3) Opción 3
0) Salir
Ingrese la opción deseada: """))
    
    if opcion == 1:
        print("Haciendo algo...")
    elif opcion == 2:
        print("Ganaste.")
    elif opcion == 3:
        print("Perdiste.")
    elif opcion == 0:
        print("Hasta luego.")
    else:
        print("Debe elegir una opción válida.")
    
