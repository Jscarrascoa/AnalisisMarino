# Comenzaremos leyendo el archivo AnalisisMarino.csv y luego realizaremos un análisis inicial de cada variable. Posteriormente, pasaremos al análisis exploratorio detallado del conjunto de datos.

#Instalar en el terminal si estas trabajando en Rstudio:
#como este ejemplo: pip3 install pandas

# Importando pandas y numpy para manejo y análisis de datos
import pandas as pd
import numpy as np

# Importando matplotlib y seaborn para visualización
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando estilos de seaborn para mejorar la estética de las visualizaciones
sns.set_style("whitegrid")

# Importando scikit-learn para técnicas de preprocesamiento y modelado
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Leyendo el archivo CSV
df_marino = pd.read_csv('AnalisisMarino.csv')

# Mostrando las primeras filas del DataFrame para tener una idea inicial de los datos
df_marino.head()

##Aquí está una vista previa de las primeras filas del conjunto de datos:

Contiene 26 columnas (variables) que abarcan desde la especie del pez, coordenadas geográficas, fecha de observación, características físicas, hasta detalles sobre el hábitat y comportamiento del pez.
Las variables incluyen tanto características numéricas como categóricas.
Para tener una mejor comprensión de los datos, vamos a realizar un análisis inicial de cada variable, comenzando con un resumen descriptivo de las variables numéricas y luego analizando la distribución de las variables categóricas.

# Resumen descriptivo de las variables numéricas
summary_numeric = df_marino.describe()

summary_numeric

jaosjdasd


