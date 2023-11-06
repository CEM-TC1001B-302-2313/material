# Entradas -> Parámetros
# Salidas -> Valor de retorno

# Sin parámetros y sin valor de retorno
def suma1():
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

# Con parámetros y sin valor de retorno
def suma2(a : float, b : float) -> None:
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

# Con parámetros y con valor de retorno
def suma3(a : float, b : float) -> float:
    resultado = a + b
    return resultado

# suma1()
# suma2(63,2)
# x = float(input("Ingresa a: "))
# y = float(input("Ingresa b: "))
# suma2(x, y)
res = suma2("hola", "mundo")
print(res)
# res = suma3(53, 9)
# print(res)