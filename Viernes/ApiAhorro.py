import hug 
import pickle

modelo=pickle.load(open("comprar_modelo.pickle","rb"))
@hug.get()
def predecir(ingreso: hug.types.float_number):
	talvez=modelo.predict([[ingreso]])
	return {
		"ahorro":"{:.2f}".format(talvez[0])
	}

