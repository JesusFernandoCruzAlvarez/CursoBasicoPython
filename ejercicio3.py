#Ejercicio3
#Escriba un programa que encuentre todos los números entre 1000 y 3000 (inclusive) donde cada 
#uno de sus dígitos sea par, los números obtenidos serán impresos en una línea separados por comas.
lista=[]
nuevaLista=[]

for i in range(1000,3001):
	lista.append(i)
	d1=str(i)
	ev1=int(d1[0])
	if(ev1%2==0):
		ev2=int(d1[1])
		if(ev2%2==0):
			ev3=int(d1[2])
			if(ev3%2==0):
				ev4=int(d1[3])
				if(ev4%2==0):
					nuevaLista.append(i)
print(nuevaLista)

