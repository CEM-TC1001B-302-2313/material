import pandas as pd
# DataFrame
df = pd.read_csv("Student Stress Factors.csv")

print(df)

print(df.head(3))

print(df.tail(4))

# Estadísticas

print(df.info())

#variable_df["nombre columna"].función_estadística()
print(df["Stress levels"].sum()) # Suma total

print(df["Stress levels"].mean()) # Promedio

print(df["Stress levels"].median()) # Mediana

print(df["Stress levels"].max()) # Máximo

print(df["Stress levels"].min()) # Mínimo

print(df["Stress levels"].std()) # Desviación estándar

print(df["Stress levels"].var()) # Varianza

print(df["Timestamp"].mode()) # Moda (Object)