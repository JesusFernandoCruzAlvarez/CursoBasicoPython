"""CREAR UNa funcion que dadas dos listas de elementos nos devuelva su coeficiente de jaccard, es
una medida de similaridad entre dos grupos, y se define como: la cardinalidad de la interseccion 
de ambos conjuntos divida por la cardinalidad de su union
"""
def  jaccard(grupo1, grupo2):
	interseccion=len(set(grupo1).intersection(set(grupo2)))
	union= len(set(grupo1).union(set(grupo2)))
	return interseccion/union

grupo_amigos1=["Manuel","Jesus","Rodrigo","Irving"]
grupo_amigos2=["Manuel","Alejandro","Fernando","Antonio","Jesus","Pablo"]

jaccard_amigos=jaccard(grupo_amigos1,grupo_amigos2)
print("porcentaje de similitud: {:.2f}".format(jaccard_amigos) )