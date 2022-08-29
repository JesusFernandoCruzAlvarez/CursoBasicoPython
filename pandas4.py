#Filtrado
"""mostrar los lugares que cuenten con mas de 10 criticas (reviews) y con una puntuacion 
(overall_satisfaction) mayor a 4 ordenar los resultados de mejor a peor puntuacion
en caso de habitaciones con igual puntuacion, mostrar primero las que tengan mas criticas
mostrar 5 resultados"""
import pandas as pd
air=pd.read_csv("habitaciones.csv")
air2=air[[
	"reviews",
	"room_type",
	"overall_satisfaction",
	"accommodates",
	"bedrooms",
	"price"
]]

seleccion=air2.query(
	"reviews>=10 & overall_satisfaction>4")
print(seleccion.sort_values(
	 	by=["overall_satisfaction","reviews"],ascending=False).head(5)
	 	)

