"""Crear un CSV que contenga la informacion de las habitaciones con id (room_id): 29720,135493,232858,
337665"""
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

ambos=air2[air2.room_id.isin([29720,135493,232858,337665])]
ambos.to_csv("fer_csv.csv", index=False)
print(ambos)