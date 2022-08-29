#Ejercicio 2
#Escriba un programa que acepte una secuencia de palabras separadas por comas si la entrada suministrada al 
#programa es la siguiente:
#saludos,hola,amigos,adios
#la salida será: adios,amigos,hola,saludos (las mismas palabras ordenadas alfabeticamente)
palabras=input("Escriba palabras separadas por comas: ")
lista=palabras.split(',')
lista.sort()
print(','.join(lista))
