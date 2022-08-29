def ejemplo():
	print("Esto es una funcion sin argumentos")

ejemplo()

def suma(a,b):
	resultado= a+b
	return resultado
print (suma(5,6))

def restar(actual,nacimiento):
	resultado=actual-nacimiento
	return resultado

edad_erronea=restar(1990,2020)
edad=restar(nacimiento=1990,actual=2020)
print (edad_erronea)
print (edad)

def dividir(dividendo,divisor=2):
	resultado=dividendo/divisor
	return resultado

cuarto=dividir(40,4)
print(cuarto)

mitad=dividir(40)
print (mitad)


