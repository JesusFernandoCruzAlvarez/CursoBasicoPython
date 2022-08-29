#Ejercicio2
#escribe un programa que acepte una secuencia de numeros binarios de cuatro digitos separados por comas 
#y cheque si son divisibles por 5 o no, los numeros divisibles por 5 serán impresos en una misma linea
#Separados por coma, ejemplo de entrada: 0100,0011,1010,1001 entonces la salida será: 1010
palabras=input("Escriba cantidades binarias de 4 digitos separadas por comas: ")
lista=palabras.split(',')
print (lista)
for i in lista:
	valor_d = int(i,2)
	if(valor_d%5==0):
		print(i)