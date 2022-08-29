# while, split
#escribe un programa que administre una cuenta bancaria 
"""Usando un bitacora de operaciones, la bitacora de operaciones tiene la siguiente forma
D 100	significa que depositó 100 pesos
R 50	significa que retiró 50 pesos
ejemplo
D 200
D 200
R 100
D 50
introducir una linea vacia significa que ha finalizado la bitacora, la salida de este programa seria:
350"""
saldo=0
print("Escriba la bitacora de operaciones: ")
while True:
	s=input()
	if not s:
		break
	datos=s.split(" ")
	print(datos)
	operacion=datos[0]
	monto=int(datos[1])
	if operacion=='D':
		saldo+=monto
	elif operacion=='R':
		saldo-=monto

print(saldo)



