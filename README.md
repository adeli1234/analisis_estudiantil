# analisis_estudiantil
Este analisis sirve para demostrar cómo los factores socioeconómicos y académicos influyen en el desmpeño de los estudiantes ante evaluaciones de diversos tipos tales como de matemáticas, escritura y lectura.

## DATASET---

Nombre del dataset: "StudentsPerformance.csv"
Fuente: Se obtuvo la Kaggle
Descripción: El conjunto de datos tiene 1000 registros y 8 variables que describen factores socioeconómicos y sociodemográficos de los estudiantes junto con calificaciones de diversas pruebas.

## OBJETIVO---

El objetivo principal de estee proyecto es identificar y analizar c+omo influyen diferentes variables en relación a los estudiantes en el desempeño académico final por individual y por grupos.

## REQUISITOS---

- Python
- Las dependencias que se indican en el archivo 'requirements.txt' ('pandas', 'numpy', 'matplotlib', entre otros)

## INSTALACION---

git clone https://github.com/adeli1234/analisis_estudiantil.git

cd analisis_estudiantil

python -m venv .restaurant_rank

pip install -r requirements.txt

## EJECUCION---

python src/analysis.py

## ANALISIS---

- Se verificó el total de registros y columnas
- Se identificó el tipo de dato por variable
- Se realizó un diagnostico en busca de valores nulos o duplicados

- Se estandarizaron los nombres de las variables
- Se crearon variables derivadas

- Se evaluó la prueba con mayor promedio
- Se analizó el porcentaje de estudiantes con un nivel de rendimiento 'alto'
- Se verificó el impacto del exámen de preparación ante el rendimiento final

