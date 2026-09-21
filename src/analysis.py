import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/StudentsPerformance.csv")

print(df.head())
print("-"*20)
# Número de registros
print("Número de registros:", len(df))
print("-"*20)

# Número de columnas
print("Número de columnas:", len(df.columns))
print("-"*20)

# Nombre de las variables
print("Nombre de las variables:")
print(df.columns.tolist())
print("-"*20)

# Tipos de datos
print("Tipos de datos: ")
print(df.dtypes)
print("-"*20)

# Valores faltantes
print("Valores faltantes: ")
print(df.isnull().sum())
print("-"*20)

# Registros duplicados
print("Registros duplicados: ", df.duplicated().sum())
print("-"*20)

# Estadísticas descriptivas
print("Estadísticas descriptivas:")
print(df.describe())
print("-"*20)