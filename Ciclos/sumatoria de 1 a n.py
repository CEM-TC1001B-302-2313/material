# Ingresar un número n
# Calcular la sumatoria desde 1 hasta n
# Por ejemplo, si n = 5: 1+2+3+4+5 -> 15

n = int(input("Ingrese el valor de n: "))

resultado = 0
for i in range(1, n+1):
    resultado += i
print(f"La suma de 1 hasta {n} es: {resultado}")
    
# resultado + i -> resultado
# 0 + 1 -> 1
# 1 + 2 -> 3
# 3 + 3 -> 6
# 6 + 4 -> 10
# 10 + 5 -> 15