
# range(final) -> Genera la secuencia de números que empieza
# en 0, termina antes de final y avanza de 1 en 1
# range(5) -> 0,1,2,3,4
print("Usando range(5)")
for i in range(5):
    print(f"El valor de i es: {i}")

print("-"*20)

# range(inicio, final) -> Genera la secuencia de números que
# empieza en inicio, termina antes de final y
# avanza de 1 en 1
print("Usando range(5,10)")
for i in range(5,10):
    print(f"El valor de i es: {i}")
    
print("-"*20)

# range(inicio, final, paso) -> Genera una secuencia de números
# que inicia en inicio, termina antes de final
# y avanza de paso en paso
print("Usando range(5,15,3)")
for i in range(5,14,3):
    print(f"El valor de i es: {i}")

print("-"*20)

for i in range(10,5):
    print(f"El valor de i es: {i}")
    
print("-"*20)

for i in range(10,5,-1):
    print(f"El valor de i es: {i}")
    
print("-"*20)

texto = "Hola mundo"
for i in texto:
    print(f"El valor de i es: {i}")
    
print("-"*20)

lista = [1, 6.7, True, [6,3], "hola"]
for i in lista:
    print(f"El valor de i es: {i}")
    
print("-"*20)

tupla = (1, 6.7, True, (6,3), "hola")
for i in tupla:
    print(f"El valor de i es: {i}")