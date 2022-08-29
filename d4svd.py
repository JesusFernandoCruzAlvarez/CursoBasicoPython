import numpy as np
import pandas as pd
import time

import pickle

print("cargando archivos: "+time.strftime("%H:%M:%S"))
puntuaciones=pd.io.parsers.read_csv("svd_ratings.dat",
	names=['user_id','movie_id','rating','time'],
	engine='python', delimiter='::'
	)
	
movie_data=pd.io.parsers.read_csv("svd_movies.dat",
	names=['movie_id','title','genre'],
	engine='python', delimiter='::'
	)
	
print ("ratings")
print(puntuaciones.shape)
print ("movies")
print(movie_data.shape)

print("creando matriz de puntuaciones"+time.strftime("%H:%M:%S"))
ratings_mat=np.ndarray(
	shape=(np.max(puntuaciones.movie_id.values),np.max(puntuaciones.user_id.values)),
	dtype=np.uint8
	)

ratings_mat[puntuaciones.movie_id.values-1,
puntuaciones.user_id.values-1]=puntuaciones.rating.values

print("matriz de puntuaciones")
print(ratings_mat.shape)

#print("normalizando matriz"+time.strftime("%H:%M:%S"))
#normalized_mat=ratings_mat-np.mean(ratings_mat,1)


print("normalizando matriz"+time.strftime("%H:%M:%S"))
normalized_mat=ratings_mat-np.asarray([(np.mean(ratings_mat,1))]).T
print("Matriz de ratings normalizada")
print(normalized_mat.shape)

print ("computando SVD "+time.strftime("%H:%M:%S"))
A=normalized_mat.T/np.sqrt(ratings_mat.shape[0]-1)
print("Matriz A")
print(A.shape)

U,S,V=np.linalg.svd(A)

print("SVD Finalizado"+time.strftime("%H:%M:%S"))

print ("Matriz U")
print(U.shape)
print ("Matriz S")
print(S.shape)
print ("Matriz V")
print(V.shape)

np.seterr(divide='ignore', invalid='ignore')
def similitud_coseno(data, movie_id,top_n=10):
	index=movie_id-1
	movie_row=data[index,:]
	magnitud=np.sqrt(np.einsum('ij,ij->i',data,data))
	similitud=np.dot(movie_row,data.T)/(magnitud[index]*magnitud)
	print("vector de similitud ")
	print(similitud.shape)
	sort_indexes=np.argsort(-similitud)
	return sort_indexes[:top_n]

def mostrar_similares(movie_data,movie_id,top_indexes):
	print("Recomendaciones para {}: \n".format(
		movie_data[movie_data.movie_id==movie_id].title.values[0]))
	for id in top_indexes+1:
		print(movie_data[movie_data.movie_id==id].title.values[0])

k=40
reducida=V.T[:,:k]
movie_id=19
top_n=10

np.savetxt('matriz_v.dat',reducida)

indexes=similitud_coseno(reducida,movie_id,top_n)
print (indexes)
mostrar_similares(movie_data,movie_id,indexes)

pickle.dump(reducida,open("d4_SVD_modelo.pickle","wb"))