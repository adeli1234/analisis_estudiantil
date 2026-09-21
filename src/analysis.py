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

# ¿Cuál de las tres areas tiene el promedio más alto?
average_math = df['math_score'].mean()
average_reading = df['reading_score'].mean()
average_writing = df['writing_score'].mean()

plt.figure(figsize=(8, 6))
plt.bar(['MATEMÁTICAS', 'LECTURA', 'ESCRITURA'], [average_math, average_reading, average_writing])
plt.xlabel('Área')
plt.ylabel('Promedio')
plt.title('Promedio de Puntajes por Área')
plt.savefig('outputs/resultados/promedio_areas.png')
plt.close()
plt.show()

print("El area con el promedio más alto es:", end=" ")
if average_math >= average_reading and average_math >= average_writing:
    print("Matemáticas")
elif average_reading >= average_writing:
    print("LECTURA")
else:
    print("ESCRITURA")

# ¿Qué porcentaje de estudiantes alcanzaron un rendimiento alto?
high_perform_students = df[df['rendimiento'] == 'Alto']
high_perform_stu_percentage = (len(high_perform_students) / len(df)) * 100
print(f"El porcentaje de estudiantes con rendimiento alto es: {high_perform_stu_percentage:.2f}%")

plt.figure(figsize=(8, 6))
plt.pie(df['rendimiento'].value_counts(), labels=df['rendimiento'].value_counts().index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Rendimiento de Estudiantes')
plt.savefig('outputs/resultados/distribucion_rendimiento.png')
plt.close()
plt.show()

# ¿Los estudiantes que realizaron el curso de preparación presentan mejores resultados?
prep_stu = df[df['test_preparation_course'] == 'completed']
print(f"El promedio de puntajes para estudiantes que realizaron el curso de preparación fue de: {prep_stu['average_score'].mean():.2f}")

# ¿Cuál es el promedio de puntajes para estudiantes que no realizaron el curso de preparación?
no_prep_stu = df[df['test_preparation_course'] == 'none']
print(f"El promedio de puntajes para estudiantes que no realizaron el curso de preparación fue de: {no_prep_stu['average_score'].mean():.2f}")

plt.figure(figsize=(8, 6))
plt.bar(['Curso de preparación completado', 'Curso de preparación no realizado'], [prep_stu['average_score'].mean(), no_prep_stu['average_score'].mean()])
plt.xlabel('Curso de preparación')
plt.ylabel('Promedio de puntajes')
plt.title('Comparación de Promedio de Puntajes según Curso de Preparación')
plt.savefig('outputs/resultados/comparacion_preparacion.png')
plt.close()
plt.show()