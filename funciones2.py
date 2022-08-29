def sumar(*args):
	resultado=0
	for valor in args:
		resultado+=valor
	return resultado

total=sumar(4,3,6,2)
print(total)