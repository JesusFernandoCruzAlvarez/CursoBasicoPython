"""Ejercicio, utiliza una grafica para mostrar:
Distribucion de porcentaje de zona industrial
si existe correlacion entre n habitantes y valor mediano
los valores atipicos de porcentaje de clase baja en los diferentes cuantiles
de valor medio"""
import pandas as pd
import matplotlib.pyplot as plt 

datos=pd.read_csv("casasboston.csv")

df=datos[["RM","CRIM","MEDV","TOWN","CHAS","INDUS","LSTAT"]]
df=df.rename(columns={
	"TOWN":"CIUDAD",
	"CRIM":"INDICE_CRIMEN",
	"INDUS":"PCT_ZONA_INDUSTRIAL",
	"CHAS":"RIO_CHARLES",
	"RM":"N_HABITACIONES_MEDIO",
	"MEDV":"VALOR_MEDIANO",
	"LSTAT":"PCT_CLASE_BAJA"
	})
print(df.sample(5))

#ver la distribucion del porcentaje de zona industrial
df.PCT_ZONA_INDUSTRIAL.plot.hist()
plt.show()
df.plot.scatter(x="N_HABITACIONES_MEDIO",y="VALOR_MEDIANO",alpha=.20)
plt.show()

df["VALOR_CUANTILES"]=pd.qcut(df.VALOR_MEDIANO,5)
df.boxplot(column="PCT_CLASE_BAJA", by="VALOR_CUANTILES",figsize=(8,6))
plt.show()
