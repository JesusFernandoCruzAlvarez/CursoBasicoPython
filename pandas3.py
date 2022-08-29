"""Un grupo de 5 amigos cuenta con 80 euros para su alojamiento desean una lista de 6 opciones
prefiriendo aquellas que tengan el mayor numero de habitaciones seguidos de aquellas con 
mejor puntuacion"""
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
amigos=air2.query("price<=80 & accommodates<=5")
print(amigos.sort_values(by=["bedrooms","overall_satisfaction"],ascending=False).head(6))

