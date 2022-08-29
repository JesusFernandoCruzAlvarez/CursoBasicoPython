import pandas as pd #1
import numpy as np

from sklearn.model_selection import train_test_split #2
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import confusion_matrix #2
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

import pickle

#preparacion de los datos
data=pd.read_csv("diabetes.csv")
zero=['Glucosa','PresionSanguinea','GrosorPiel','Insulina','IMC']
for col in zero:
	data[col]=data[col].replace(0,np.NaN)
	mean =int(data[col].mean(skipna=True))
	data[col]=data[col].replace(np.NaN, mean)

#2 Entrenar el modelo
objetivo="Resultado"
independientes=data.drop(objetivo,axis=1).columns
#Separar el data set en dos partes: entrenamiento y prueba

x_train, x_test, y_train, y_test =train_test_split(
	data[independientes],
	data[objetivo],
	test_size=.20,
	random_state=0,	
)
#estandarizar poner todo a una misma escala

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

clasificador=KNeighborsClassifier(n_neighbors=15,p=2, metric='chebyshev')
#p1=distancia manhattan 
#p2 =distancia euclidiana

clasificador.fit(x_train, y_train)

y_pred=clasificador.predict(x_test)
print(y_pred)

#3 evaluacion del modelo

conf_matrix=confusion_matrix(y_test,y_pred)
print ("matriz de confusion ")
print(conf_matrix)

print("Exactitud")
#porcentaje de predicciones correctas frente al total
print(accuracy_score(y_test,y_pred))

print ("presicion")
print(precision_score(y_test,y_pred))
#habilidad para clasificar como positivo lo que es positivo

print("Sensibilidad")
#Habilidad para encontrar los casos positivos
print(recall_score(y_test,y_pred))

print("F1 Score")
#F1 Score
print(f1_score(y_test,y_pred))


pickle.dump(clasificador,open("d2_knn_modelo.pickle","wb"))
pickle.dump(scaler,open("d2_knn_scaler.pickle","wb"))