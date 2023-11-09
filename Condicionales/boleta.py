udf1 = float(input("Ingresa la calificación de tu udf1: "))
udf2 = float(input("Ingresa la calificación de tu udf2: "))
udf3 = float(input("Ingresa la calificación de tu udf3: "))
udf4 = float(input("Ingresa la calificación de tu udf4: "))
udf5 = float(input("Ingresa la calificación de tu udf5: "))
udf6 = float(input("Ingresa la calificación de tu udf6: "))
udf7 = float(input("Ingresa la calificación de tu udf7: "))
udf8 = float(input("Ingresa la calificación de tu udf8: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7 + udf8)/8

print(f"El promedio de tu semestre fue: {promedio}.")

if promedio < 70:
    print("¡¡¡Terrible, estudia más!!!")
elif promedio <= 85:
    print("No fue terrible, pero podría ser mejor.")
elif promedio <= 90:
    print("Decente.")
else:
    print("Excelente.")