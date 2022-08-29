import pickle
import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import json
from sklearn.base import BaseEstimator
from scipy.sparse import issparse


modelo =pickle.load(open("d4_SVD_modelo.pickle","rb"))


while True:
	print ("--- sistema de recomendar peliculas---")
	print("1.- recomendar")
	print("2.- Salir")
	opcion=int(input("Escriba el id de la pelicula:"))

	if opcion==1:
		noticia=int(input("pelicula: "))
		datos=[noticia]
		#xdatos=scaler.transform([datos])
		talvez=datos
		print ("Recomendacion: "+str(talvez[0]))


	if opcion==2:
		break;