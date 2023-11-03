# Actividad 1
# Ejercicio 1
# Aram Baruch González Pérez 57834
# Juan Arturo Nolasco Flores 486984

udf1 = float(input("Ingresa la calificación de tu udf1: "))
udf2 = float(input("Ingresa la calificación de tu udf2: "))
udf3 = float(input("Ingresa la calificación de tu udf3: "))
udf4 = float(input("Ingresa la calificación de tu udf4: "))
udf5 = float(input("Ingresa la calificación de tu udf5: "))
udf6 = float(input("Ingresa la calificación de tu udf6: "))
udf7 = float(input("Ingresa la calificación de tu udf7: "))
udf8 = float(input("Ingresa la calificación de tu udf8: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7 + udf8)/8

print("El promedio fue:", promedio, "Estudia más.")
print("El promedio fue: " + str(promedio) + " Estudia más.")
print("El promedio fue: {0} Estudia más.".format(promedio))
# f-strings
print(f"El promedio fue: {promedio} Estudia más.")

valor = 375938294.48872994
# : -> indica que usa un formato especial
# , -> indica que usamos el separador de miles
# .2 -> indica que queremos redondear a dos decimales
# f -> indica que queremos mostrarlo como número real
# y no como formato científico
print("El valor es: {0:,.2f}".format(valor))
print(f"El valor es: {valor:,.2f}")