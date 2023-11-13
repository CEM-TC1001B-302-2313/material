
# total = 0
# precio = 0
# while precio >= 0:
#     total += precio
#     precio = float(input("Ingresa el precio del producto: "))
# print(f"El total a pagar es de: ${total:,.2f}")

total = 0
while (precio := float(input("Ingresa el precio del producto: "))) >= 0:
    total += precio
print(f"El total a pagar es de: ${total:,.2f}")