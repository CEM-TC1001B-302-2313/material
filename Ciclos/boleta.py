numero_udfs = int(input("Ingresa cuántas udfs cursaste: "))

promedio = 0
for i in range(1, numero_udfs + 1):
    udf = float(input(f"Ingresa la calificación de tu udf{i}: "))
    promedio += udf
promedio /= numero_udfs

print(f"El promedio de tu semestre fue: {promedio:,.2f}.")

if promedio < 70:
    print("¡¡¡Terrible, estudia más!!!")
elif promedio <= 85:
    print("No fue terrible, pero podría ser mejor.")
elif promedio <= 90:
    print("Decente.")
else:
    print("Excelente.")