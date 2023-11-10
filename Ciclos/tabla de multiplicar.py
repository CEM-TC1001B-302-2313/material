# Tabla de multiplicar
# Ingresar un valor n
# Mostrar su tabla de multiplicar de 1 hasta 10
# Si n = 3
# 1 x 3 = 3
# 2 x 3 = 6
# 3 x 3 = 9
# ...
# 10 x 3 = 30
n = int(input("Ingrese el valor de n: "))
for i in range(1, 11):
    resultado = i * n
    print(f"{i} x {n} = {resultado}")