"""hacer un programa que lea un archivo de texto que contiene en cada linea nombres de peliculas
separados por comas, el programa determinará el porcentaje de similitud de la primera lista de 
peliculas con respecto a las demas. el programa seleccionará la lista con la que tenga mayor afinidad
el programa mostrará los nombres de las peliculas que estan en la lista con mayor afinidad y que no 
estan en la primera lista"""
print("+++ 1 ++++")
datos=[]
with open("peliculas.txt") as fname:
	lineas=fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n').split(","))

print(datos)
print("+++")

miriam=datos[0]
edith=datos[1]
anahi=datos[2]
print("lista 1: ", miriam)
print("lista 2: ",edith)
print("lista 3: ",anahi)

def  jaccard(grupo1, grupo2):
	interseccion=len(set(grupo1).intersection(set(grupo2)))
	union= len(set(grupo1).union(set(grupo2)))
	return interseccion/union

jaccard_amigos1=jaccard(miriam,edith)
print("porcentaje de similitud entre lista 1 y lista 2: {:.2f}".format(jaccard_amigos1) )

jaccard_amigos2=jaccard(miriam,anahi)
print("porcentaje de similitud entre lista 1 y lista 3: {:.2f}".format(jaccard_amigos2) )
Cmiriam=set(miriam)
Cedith=set(edith)
Canahi=set(anahi)

if (jaccard_amigos1>jaccard_amigos2):
	print("Lista 2 tiene la lista con mayor similitud")
	resta=Cedith-Cmiriam
	print ("y las peliculas que no estan en la lista 1 son: ",resta)
else:
	print("Lista 3 tiene la lista con mayor similitud")
	resta=Canahi-Cmiriam
	print ("y las peliculas que no estan en la lista 1 son: ",resta)