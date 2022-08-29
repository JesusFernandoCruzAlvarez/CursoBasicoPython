#Hacer una funcion que dado el nombre de un archivo, lo lea y devuelva la linea con mayor longitud

def linea_mas_larga(nombre):
	with open(nombre) as fname:
		lineas=[linea.strip('\n') for linea in fname.readlines()]
	lmaslarga=lineas[0]
	for linea in lineas:
		if len(linea)>len(lmaslarga):
			lmaslarga=linea 
	return lmaslarga

print("---------")
print("la linea con mayor longitud es: ")
print(linea_mas_larga("datos.txt"))