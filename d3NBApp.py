import pickle
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import json

from sklearn.base import BaseEstimator
from scipy.sparse import issparse



class DenseTransformer(BaseEstimator):
    def __init__(self, return_copy=True):
        self.return_copy = return_copy
        self.is_fitted = False

    def transform(self, X, y=None):
        if issparse(X):
            return X.toarray()
        elif self.return_copy:
            return X.copy()
        else:
            return X

    def fit(self, X, y=None):
        self.is_fitted = True
        return self

    def fit_transform(self, X, y=None):
        return self.transform(X=X, y=y) 

        #crear un pipeline que integre los dos pasos anteriores e incluya clasificador NB con 
        #distribucion gaussiana



modelo =pickle.load(open("d3_NB_modelo.pickle","rb"))


while True:
	print ("--- sistema de clasificacion de textos---")
	print("1.- clasificar")
	print("2.- Salir")
	opcion=int(input("Escriba su noticia:"))

	if opcion==1:
		noticia=(input("noticia: "))
		datos=[noticia]
		#xdatos=scaler.transform([datos])
		talvez=modelo.predict(datos)
		print ("Diagnostico: "+(talvez[0]))


	if opcion==2:
		break;