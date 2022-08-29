print("comisiones")
cv=int(input("Ingrese la cantidad vendida"))
if cv<100000:
	comision=cv*.03
	print("la comision es: ",comision)
if cv>100000:
	if cv<150000:
		comision=cv*.05
		print("la comision es: ",comision)
