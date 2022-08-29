#listas Ejercicio1
#Escriba un programa que encuentre lo numeros divisibles por 7 entre 2000 y 3200 inclusive
#los numeros obtenidos seran impresos en una sola lista, separados por comas

lista=[]
for i in range(2000,3201):
	if(i%7==0):
		lista.append(str(i)) 
print(lista)
print(','.join(lista)) 