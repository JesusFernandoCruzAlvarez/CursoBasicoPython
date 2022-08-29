import pandas as pd
air=pd.read_csv("habitaciones.csv")
#precio promedio, mas alto y mas bajo de una habitacion
datos=air.describe()
print (datos)
#solo la media de la columna precio
print(air["price"].mean())#max mas alto, min mas bajo
#ejemplo agrupamiento
#cuantas habitaciones hay disponibles por cada tipo de habitacion
#(room_type=Entire home/apt,Private room, Shared room)
#groupby
totales=air.groupby("room_type").count()#tambien se puede usar size()
print(totales)


