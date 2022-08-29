"""Fase 2 del analisis de datos
Diagnostico de la calidad de los datos
instalar las librerias numpy y scipy
pip install numpy
pip install scipy"""
#Fase 2 diagnóstico de la calidad de los datos
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("peliculas_Fer_paso1.csv")
print(df.shape)
#Dectectar repetidas
print("---- filas repetidas ---")
print(df[df.duplicated()].shape)
#Si hubiera filas repetidas y las quieres borrar
#df=df.drop_duplicates()

#Cardinalidad de las columnas
#que tantas veces se repite un mismo dato en una columna
n_registros=len(df)
def valores_duplicados_col(df):
	for columna in df:
		n_por_valor=df[columna].value_counts()
		mas_comun=n_por_valor.iloc[0]
		menos_comun=n_por_valor.iloc[-1]
		print(" {} | {} - {}|{} ".format(
			df[columna].name,
			round(mas_comun/(1.0*n_registros),3),
			round(menos_comun/(1.0*n_registros),3),
			df[columna].dtype
			)) 
print("---- Cardinalidad de las columnas ---")

valores_duplicados_col(df)

print (df.presupuesto.value_counts(normalize=True))
df.presupuesto.value_counts(normalize=True).plot.barh()
plt.show()
#revisar los valores nulos
n_registros=len(df)
def valores_inexistentes_col(df):
	for columna in df:
		print(" {} | {} | {} ".format(
			df[columna].name,
			len(df[df[columna].isnull()])/(1.0*n_registros),
			df[columna].dtype
			))

print("---revisar valores nulos----")

valores_inexistentes_col(df)
#revisar valores atipicos
from scipy import stats
import numpy as np
def atipicos_col(df):
	for columna in df:
		if df[columna].dtype !=np.object:
			n_atipicos= len(df[np.abs(stats.zscore(df[columna]))>3])
			print(" {} | {} | {} ".format(
				df[columna].name,
				n_atipicos,
				df[columna].dtype
				))
print("---revisar valores atipicos----")

atipicos_col(df)

#Otra forma de encontrar valores atípicos
df2=df[df.presupuesto<100000000]
df.boxplot(column='presupuesto')
plt.show()

df2.to_csv("peliculas_Fer_paso2.csv",index=False)