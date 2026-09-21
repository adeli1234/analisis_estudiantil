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

'''
No se necesita de una limpieza o preprocesamiento tan extensos,
esto debido a que el dataset no cuenta con valores nulos o duplicados a los cuales se tenga que imputar o 
eliminar. Además las columnas manejan el tipo de datos que se espera,
por lo que no hay necesidad de hacer un cambio de tipo de datos.
'''

# Se normalizan los nombres de las columnas para que no tengan espacios y sean más fáciles de manejar
df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("/", "_")

print("Nombres de las columnas normalizados:")
print(df.columns.tolist())
print("-"*20)

# Se crea una variable llamada "average_Score"

df["average_score"] = ((df['math_score'] + df['reading_score'] + df['writing_score']) / 3).round(2)
print("Promedio de puntajes:")
print(df["average_score"].head())
print("-"*20)

# Codificación de calificaciones (clasificación de rendimiento)

labels = ['Bajo', 'Medio', 'Alto']
df['rendimiento'] = pd.cut(df['average_score'], bins=[0, 60, 80, 100], labels=labels, right=True)
print("Clasificación de rendimiento:")
print(df[['math_score', 'reading_score', 'writing_score', 'average_score', 'rendimiento']].head())
print("-"*20)