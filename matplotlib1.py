import pandas as pd
import matplotlib.pyplot as plt 

datos=pd.read_csv("casasboston.csv")

df=datos[["RM","CRIM","MEDV","TOWN","CHAS"]]
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
#histogramas para ver la distr. de una variable
#EJ ver la distribucion de la cantidad media de habitaciones
df.N_HABITACIONES_MEDIO.plot.hist()
plt.show()
#ver la distribucion del indice de crimen
df.INDICE_CRIMEN.plot.hist(bins=100,xlim=(0,20)) 
plt.show()
#grafico de dispersion sirve para representar la relacion entre dos variables
#EJ ver la relacion de indice de crimen y valor medio de las casas
df.plot.scatter(x="INDICE_CRIMEN",y="VALOR_MEDIANO",alpha=.20)
plt.show()
#Graficos de barras comparan una variable entre distintos grupos o categorias
#EJ mostrar el valor mediano por ciudad
valor_por_ciudad=df.groupby("CIUDAD")["VALOR_MEDIANO"].mean()
valor_por_ciudad.head(10).plot.bar()
plt.show()
valor_por_ciudad.head(10).plot.barh ()
plt.show()
#Diagrama de cajas
#util para presentar grupos de datos y compararlos, identifican de forma sencilla
#si la variable tiene outliers (valores atipicos), valores que se alejan de los
#frecuentes de dicha variable, EJ ver los valores atipicos de indice de crimen
#en los diferentes cuantiles de valor mediano

df["VALOR_CUANTILES"]=pd.qcut(df.VALOR_MEDIANO,5)
df.boxplot(column="INDICE_CRIMEN", by="VALOR_CUANTILES",figsize=(8,6))
plt.show()

"""Grafico circular se usa para mostrar la relacion porcentual entre las partes con
relacion a su conjunto"""
df.RIO_CHARLES.value_counts().plot.pie()
plt.show()