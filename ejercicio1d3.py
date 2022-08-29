import pandas as fer
from tabulate import tabulate

air=fer.read_csv("peliculas.csv")
air2=air[[
	"year",
	"title",
	"budget",
]]

seleccion=(air2.query("budget!=0"))
print(seleccion.sort_values(by=("year"),ascending=False).head(5))
print(seleccion)


ambos=air2.title
ambos.to_csv("titulos_csv.csv", index=False)
print(ambos)
print("palabras repetidas")
contador=air2.title.value_counts()
print (contador)