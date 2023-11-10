# Factorial
# Ingresar un número entero n y calcularemos su factorial
# n! -> n * n-1 * n-2 ,.., 1
# 5! -> 5 * 4 * 3 * 2 * 1 = 120

n = int(input("Ingrese el valor de n: "))
resultado = 1
for i in range(1, n+1):
    resultado *= i
print(f"El factorial de {n} es: {resultado}")