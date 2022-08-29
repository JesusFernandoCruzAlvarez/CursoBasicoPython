"""Ordenamiento multiple
se necesitan 10 habitaciones con un precio menor a 50 cada una que sean habitaciones compartidas 
mostrar primero las mas economicas y si hubiera precios iguales mostrar primero las de mejor
puntuacion"""

import pandas as pd
air=pd.read_csv("habitaciones.csv")
air2=air[[
	"reviews",
	"room_type",
	"overall_satisfaction",
	"accommodates",
	"bedrooms",
	"price",
	"room_id"
]]

seleccion=air2.query("price<50 & room_type=='Shared room'")
print(seleccion.sort_values(by=["price","overall_satisfaction"],ascending=[True,False]).head(10))