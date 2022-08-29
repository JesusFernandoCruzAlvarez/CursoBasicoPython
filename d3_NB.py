import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import json

from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline

from sklearn.metrics import confusion_matrix #2
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from sklearn.model_selection import train_test_split #2

import pickle

noticias =pd.read_csv("noticias.csv")
with open ("stopwords-es.json") as fname:

	stopword_es=json.load(fname)

vectorizador=TfidfVectorizer(stop_words=stopword_es,strip_accents="unicode",max_features=25000)
strip_acents="unicode"
vectorizador.fit_transform(noticias.descripcion)

#crear un transformador para convertir la matriz dispersa en array

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

pipeline_gausiano=make_pipeline(
	vectorizador,
	DenseTransformer(),
	GaussianNB()
	)

x_train, x_test, y_train, y_test =train_test_split(
	noticias.descripcion,
	noticias.categoria,
	test_size=.20,
	random_state=0,	
)

pipeline_gausiano.fit(x_train,y_train)
y_pred=pipeline_gausiano.predict(x_test)

conf_matrix=confusion_matrix(y_test,y_pred)
print ("matriz de confusion ")
print(conf_matrix)

print("Exactitud")
#porcentaje de predicciones correctas frente al total
print(accuracy_score(y_test,y_pred))

print ("presicion")
print(precision_score(y_test,y_pred,average=None))
#habilidad para clasificar como positivo lo que es positivo

print("Sensibilidad")
#Habilidad para encontrar los casos positivos
print(recall_score(y_test,y_pred,average=None))

n1=[["Netflix estrena serie"],["la computacion en la nube"],["La vida en rosa"]]



for n in n1:
	r= pipeline_gausiano.predict(n)
	print("-----------------------")
	print ("noticia: "+ str(n))
	print ("Categoria probable: "+str(r))


pickle.dump(pipeline_gausiano,open("d3_NB_modelo.pickle","wb"))
#pickle.dump(scaler,open("d3_NB_scaler.pickle","wb"))