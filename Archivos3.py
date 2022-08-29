"""hacer una funcion que tenga como argumento un nombre de archivo y un numero n y que devuelva
las ultimas lineas"""

def leer_ultimas_lineas(nombre,n):
	with open(nombre)as fname:
		lineas=[lineas.strip('\n')for lineas in fname.readlines()] 
	return lineas[-n:]
print("+++++++")
print("Ultimas 2 lineas del archivo: ")
print(leer_ultimas_lineas("datos.txt",2))
