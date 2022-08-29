import pandas as pd 
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error 

import numpy as np 
import pickle

#preparacion de datos
datos=pd.read_csv("comprar_alquilar.csv")

#entrenar el modelo
objetivo ="ahorros"
independientes=["ingresos"]

modelo =LinearRegression()
modelo.fit(X=datos[independientes],y=datos[objetivo])

#fase 3 evaluacion del modelo
#opcion a observar una muestra

y_pred =modelo.predict(datos[independientes])
datos["prediccion"]=y_pred

casos=datos[["ingresos","ahorros","prediccion","gastos_comunes","pago_coche","gastos_otros"]].head(30)

print (casos)

#opcion b observar graficamente
"""
import matplotlib as plt
casos.plot(kind="bar",figsize(18,8))
plt.show()
"""
#usar medida de error

print ("Error absoluto medio: {:.2f}".format(mean_absolute_error(datos[objetivo],y_pred)))

print ("Raiz cuadratico medio: {:.2f}".format(np.sqrt(mean_squared_error(datos[objetivo],y_pred))))

pickle.dump(modelo,open("comprar_modelo.pickle","wb"))
