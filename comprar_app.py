import pickle

modelo =pickle.load(open("comprar_modelo.pickle","rb"))

while True:
	print ("*********** Sistema de prediccion de ahorro**************")
	print("1.- Predecir")
	print("2.- Salir")
	opcion=int (input("Escriba su opcion"))
	if opcion==1:
		xingreso=float (input("Escriba cuanto gana"))
		talvez=modelo.predict([[xingreso]])
		xgastos=float (input("Escriba sus gastos comunes"))
		talvez=modelo.predict([[xgastos]])
		xcoche=float (input("Escriba cuanto paga de su coche"))
		talvez=modelo.predict([[xcoche]])
		xogastos=float (input("Escriba sus otros gastos"))
		talvez=modelo.predict([[xogastos]])
		

		print("tal vez tiene ahorrado:{:.2f}".format(talvez[0]))
	if opcion==2:
		break;