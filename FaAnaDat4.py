"""Fase 4 distribucion de variables
se analizará la distribución de variables numéricas y categóricas y se analizará si
una columna sigue una distribución normal"""
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats

df=pd.read_pickle("fer_producciones_por_año_paso3.pkl")
print(df.dtypes)
#distribución de variables numéricas
df['año'].plot.hist()
plt.show()

#normalidad de una variable numérica
def normalidad_variable_numerica(col):
	stats.probplot(df[col],plot=plt)
	plt.xlabel('Diagrama de probabilidad (normal) de la variable {} '.format(col))
	plt.show()
normalidad_variable_numerica('año')
normalidad_variable_numerica('presupuesto')

#distribución de variables categoricas
columnas_numericas=df.select_dtypes(['int','float'])

for num_col in columnas_numericas: 
	
	_,pvalue= stats.normaltest(df[num_col])
	
	if (pvalue<0.05):
		print("Columna {} no sigue una distribución normal".format(num_col)).columns  
	else:
		print("Columna {} si sigue una distribución normal".format(num_col)).columns

#Distribucion de variables categoricas 
def distribucion_variable_categorica(col): 
	df[col].value_counts(ascending=True,normalize=True).tail(20).plot.barh()
	plt.xlabel('Distribucion de la variable categórica {}'.format(col))
	plt.show()
columnas_categoricas=df.select_dtypes('category').columns

for columna in columnas_categoricas:   
	distribucion_variable_categorica(columna)
