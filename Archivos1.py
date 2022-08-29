"""Leer archivos de texto en python
1 Una lista, cada elemento es una linea del archivo
2 una lista, cada elemento es una palabra del archivo
3 una multilista, cada elemento es una lista que contiene una linea del archivo y donde cada elemento
es una palabra del archivo
"""
print("+++ 1 ++++")
datos=[]
with open("datos.txt") as fname:
	lineas=fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))
print(datos)
print("+++")

print("**** 2 ***")
datos2=[]
with open("datos.txt") as fname:
	for lineas in fname:
		datos2.extend(lineas.split())
print(datos2)
print ("***")

print("--- 3 ---")
datos3=[]
with open("datos.txt") as fname:
	for lineas in fname:
		datos3.append(lineas.split())
print(datos3)
print ("----")