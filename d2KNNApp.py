import pickle

modelo =pickle.load(open("d2_knn_modelo.pickle","rb"))
scaler =pickle.load(open("d2_knn_scaler.pickle","rb"))

while True:
	print ("--- sistema de prediccion de diabetes---")
	print("1.- Predecir")
	print("2.- Salir")
	opcion=int(input("Escriba su opcion:"))

	if opcion==1:
		embarazos=float(input("embarazos: "))
		glucosa =float(input ("Glucosa: "))
		presion =float(input ("presion: "))
		piel =float(input ("piel: "))
		insulina =float(input ("Insulina: "))
		IMC=float(input("IMC: "))
		herencia=float(input("Herencia: "))
		edad=float(input("Edad: "))
		datos=[embarazos,glucosa,presion,piel, insulina,IMC,herencia,edad]
		xdatos=scaler.transform([datos])
		talvez=modelo.predict(xdatos)
		print ("Diagnostico: {:.2f}".format(talvez[0]))


	if opcion==2:
		break;