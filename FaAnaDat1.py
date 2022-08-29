"""Fases en el analisis de datos
Fase 1 Ingesta de datos"""
import pandas as pd 
datos=pd.read_csv("peliculas.csv")

#seleccionar columnas
df=datos[["year","title","budget","code"]]
#Renombrar columnas
df=df.rename(columns={
	"year":"año",
	"title":"titulo",
	"budget":"presupuesto",
	"code":"codigo"
	})
#ver tipos de datos
print(df.dtypes)
#mostrar dimension
print(df.shape)

df.to_csv("peliculas_Fer_paso1.csv",index=False)

