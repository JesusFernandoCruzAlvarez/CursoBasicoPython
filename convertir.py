import pandas as pd 
from sklearn.linear_model import LinearRegression

#fase 1 preparar los datos

datos =pd.read_csv("celsius_a_fahrenheit.csv")

#fase 2 entrenamiento del modelo

objetivo="Fahrenheit"
independientes=["Celsius"]

modelo=LinearRegression()
modelo.fit(X=datos[independientes] ,y=datos[objetivo])

#fase 4 prueba del modelo

temp_C=34
temp_F=modelo.predict([[temp_C]])

print ("Temperatura de prediccion: "+str(temp_F))