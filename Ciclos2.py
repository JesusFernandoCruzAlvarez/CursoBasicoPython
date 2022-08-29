#while, listas, append, upper
#Escriba un programa que acepte una secuencia de lineas e imprima todas las lineas convertidas en 
#mayusculas por ejemplo si la entrada es: 
#de tal palo tal astilla, 
#en casa del herrero, asadon del palo
#a todo marrano le llega su nochebuena

#deje una linea en blanco para indicar que ha finalizado la entrada de lineas
#Entonces la salida seria:

#DE TAL PALO TAL ASTILLA, 
#EN CASA DEL HERRERO, ASADON DEL PALO
#A TODO MARRANO LE LLEGA SU NOCHEBUENA

lineas=[]
print("Escribe algunas lineas, deja una en blanco para indicar el final")
while True:
	s=input()
	if s:
		lineas.append(s.upper())
	else:
		break
for refran in lineas:
		print(refran)