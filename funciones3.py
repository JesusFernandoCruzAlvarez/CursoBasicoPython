def cuadradoycubo(n):
	cuadrado=n**2
	cubo=n**3
	return [cuadrado, cubo]
print (cuadradoycubo(5)) #nos devuelve una tupla
c2,c3=cuadradoycubo(4)
print(c2)
print(c3)
lista=cuadradoycubo(3)
print(lista)
