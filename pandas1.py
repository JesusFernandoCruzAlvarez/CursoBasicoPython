#importar las librerias y cargar los datos

import pandas as pd 
from tabulate import tabulate
df=pd.read_csv("votos.csv")
#exploracion
print("Dimensiones: ",df.shape)

print("Tipos de datos")
print(df.dtypes)

#informacion sobre los datos
print("Datos estadísticos")
print(df.describe())
print("media: ")
print(df.mean())
print ("Informacion")
print(df.info())

#renombrar columnas y visualizar muestra
print("renombrar columnas")
df=df.rename(columns={
	"state_abbreviation":"ab",
	"fraction_votes":"%v"
	})
#visualizar muestras
print("primeras filas")
primeras=df.head(3)
print(tabulate(primeras,headers='keys')) 

print("ultimas filas")
ultimas=df.tail()
print(tabulate(ultimas,headers='keys'))

muestrax=df.sample(6)
print("Muestra aleatoria")
print(tabulate(muestrax,headers='keys'))
#indices
print(df.index)
print("registro localizado")
print(df.loc[0])

df2=df.set_index("county")
primeras2=df2.head(2)
print(tabulate(primeras2,headers='keys'))
print (df2.index)
print (df2.loc["Los Angeles"])
#Eliminar columnas de un dataset
print(df.columns)
df=df.drop('%v',1)#0 filas 1 columna
#otra forma df.drop('%v',1,inplace=True)
print(df.columns) 
#contar valores
contador=df.candidate.value_counts(sort=True,ascending=True)
print(contador)
print("El mas comun es: ",str(contador[0]))
print(contador.keys()[0])
#crear categorias qcut
"""lo podemos usar para discretizar una variable por ejemplo deseamos agregar una columna que 
contenga "muy pocos","pocos","considerable","muchos", considerando los votos obtenidos"""
clasificacion=["muy pocos","pocos","considerable","muchos"]
df["clasif"]=pd.qcut(df["votes"],4,clasificacion)
print(tabulate(df.sample(5),headers='keys'))

