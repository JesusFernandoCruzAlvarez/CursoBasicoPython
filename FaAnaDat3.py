"""Fase 3 del análisis de datos
La agrupación de variables"""
import pandas as pd
import matplotlib.pyplot as plt  
df=pd.read_csv("peliculas_Fer_paso2.csv")
#Agrupar variables categoricas
def valores_unicos_cols(df):
	for columna in df:
		print("{} | {} | {} ".format(
			df[columna].name,
			len(df[columna].unique()),
			df[columna].dtype
			))
print("--- valores unicos por columnas ----")
valores_unicos_cols(df)	
#presupuesto
print("---valores de la columna presupuesto----")
print(df.año.unique())
print("--- categorias creadas para presupuesto----")
presupuesto_rico=['10000000','11000000','13000000']
presupuesto_pobre=['100000','200000']
presupuesto_raquitico=['7000']

df.loc[df['presupuesto'].isin(presupuesto_rico),'presupuesto_tipo']= 'Produccion Rica'
df.loc[df['presupuesto'].isin(presupuesto_pobre),'presupuesto_tipo']= 'Produccion Pobre'
df.loc[df['presupuesto'].isin(presupuesto_raquitico),'presupuesto_tipo']= 'Produccion region 4'

df.presupuesto_tipo=df.presupuesto_tipo.astype("category")
print(df.presupuesto_tipo.value_counts())   

#Año
print("---Valores de la columna año----")
print(df.año.unique())
print("---Categorias para la columna año----")
decada7=['1979', '1978', '1977', '1976', '1975', '1974', '1973', '1972','1971','1970']
decada8=['1989', '1988', '1987', '1986', '1985', '1984', '1983', '1982','1981','1980']
decada9=['1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992','1991','1990']

df.loc[df['año'].isin(decada7),'año_tipo']='decada7'
df.loc[df['año'].isin(decada8),'año_tipo']='decada8'
df.loc[df['año'].isin(decada9),'año_tipo']='decada9'

df.año_tipo=df.año_tipo.astype('category')
print(df.año_tipo.value_counts())

#agrupar variables numericas

print("--- valores de la variable año----")
lista=df.año.value_counts()
lista.sort_index(inplace=True)
print (lista)


print("--- categorias creadas para año----")
bins=[0,1970,1980,1990,2000,2010,2013]
names=[
	"setentas",
	"ochentas",
	"noventas",
	"dos mil",
	"dos mil diez",
	"dos mil trece"]

df["año_tipo"]=pd.cut(df["año"],bins,labels=names)
print(df.año_tipo.value_counts()) 

df.to_pickle("fer_producciones_por_año_paso3.pkl")
#el formato pickle nos permite guardar las variables categoricas.