"""Fase 5 comparaciones
Ahora crearemos recuentos y medias de multiples variables"""
#Recuento por multiples grupos
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_pickle("fer_producciones_por_año_paso3.pkl")   
plt.rcParams['figure.figsize']=(10,6)
print(df.dtypes)

#recuento por multiples grupos

#Generar un pivot_table (tabla dinámica)
def pivot_recuento(df,rows,columns,calc_field):
	df_pivot=df.pivot_table(values=calc_field,
							index=rows,
							columns=columns,
							aggfunc=np.size
							).dropna(axis=0,how='all')
	return df_pivot
recuento1=pivot_recuento(df,"año_tipo","presupuesto_tipo","titulo")
print(recuento1)
recuento2=pivot_recuento(df,"año_tipo","presupuesto_tipo","codigo")
print(recuento2)

#crear un heatmap o mapa de calor, es un diagrama que nos va a mostrar los mismos valores
#pero en forma grafica
def heatmap_recuento_tipos(df,col1,col2):
	pivot_table=pivot_recuento(df,col1,col2,"año")
	sns.heatmap(pivot_table, annot=True,fmt='g',cmap="YlGnBu") 
	plt.ylabel(col1)
	plt.xlabel(col2)
	plt.show()

heatmap_recuento_tipos(col1="año_tipo",col2="presupuesto_tipo",df=df)
# Medias por categorias
def medias_por_categoria(col_grupo,col_calculo):
	df.groupby(col_grupo)[col_calculo].mean().plot.barh()
	plt.ylabel(col_grupo)
	plt.xlabel('valores medios de {} '.format(col_calculo))
	plt.show()

medias_por_categoria(col_grupo="año_tipo", col_calculo="año")
# Medias por multiples grupos
def pivot_media(rows,columns,calc_field):
	df_pivot=df.pivot_table(values=calc_field,
							index=rows,
							columns=columns,
							aggfunc=np.mean
							).dropna(axis=0,how='all')
	return df_pivot

medias=pivot_media("año_tipo","presupuesto_tipo","año")
print (medias)

def heatmap_medias_tipos(col1,col2,col3):
	pivot_table=pivot_media(col1,col2,col3)
	sns.heatmap(pivot_table,annot=True,fmt='g')
	plt.ylabel(col1)
	plt.xlabel(col2)
	plt.show()

heatmap_medias_tipos("año_tipo","presupuesto_tipo","año" )
