"""Se tiene 3 listas de peliculas, por ejemplo 
miriam=["","","","",]
edith=["","","","","","",]
anahi=["","","","","","","","",]

Escriba un programa que muestre la similitud de gustos entre pares de usuarios, por ejemplo:
Miriam_Edith
Miriam_Anahi
Edith_Anahi
"""
miriam=["Rapido y furioso","Interestelar","Todas caen","Spiderman",]
edith=["Como caido del cielo","Todas caen","Mireyes vs Godinez","X-man","Los increibles","Coco",]
anahi=["Coco","Rapido y furioso","Interestelar","Guadalupe reyes","El señor de los anillos","X-man","Cazafantasmas","Capitan america",]

def  jaccard(grupo1, grupo2):
	interseccion=len(set(grupo1).intersection(set(grupo2)))
	union= len(set(grupo1).union(set(grupo2)))
	return interseccion/union

jaccard_amigos=jaccard(miriam,edith)
print("porcentaje de similitud entre Miriam y Edith: {:.2f}".format(jaccard_amigos) )

jaccard_amigos=jaccard(miriam,anahi)
print("porcentaje de similitud entre Miriam y Anahi: {:.2f}".format(jaccard_amigos) )

jaccard_amigos=jaccard(edith,anahi)
print("porcentaje de similitud entre Edith y Anahi: {:.2f}".format(jaccard_amigos) )