grupo1={"Jhon","Paul","Ringo","George"}
grupo2={"Jhon","Yoko","Eric","Ringo"}

#operaciones con conjuntos
#pertenencia
print("Ken" in grupo1)
#union
unidos=grupo1.union(grupo2)
print (unidos)
#en los conjuntos no se permiten duplicados
#interseccion
comunes=grupo1.intersection(grupo2)
print(comunes)
#diferencia de conjuntos
resta=grupo1-grupo2
print ("diferencia: ",resta)
#diferencia simétrica
difsim=grupo1.symmetric_difference(grupo2)
print("diferencia simetrica",difsim)

#Agregar elementos
#add agrega solo un elemento
grupo2.add("Billy")
#remover elementos
grupo2.remove("Eric")
print("Agregar y remover: ",grupo2)
#AGREGAr varios elementos al mismo tiempo
grupo1.update(grupo2)
print("grupo1 nuevo: ",grupo1)
#eliminar elementos duplicados en la lista
grupo3={"juan","juan"}
print ("grupo3: ",grupo3)
#una lista si puede tener elementos repetidos
grupo3l=["juan","juan","maria"]
print("grupo 3 lista: ",grupo3l)
#convertir una lista a un conjunto
print ("Eliminar repetidos: ", list(set(grupo3l)))
#Comparar conjuntos
print("son iguales: ",grupo1==grupo2)
#convertir una cadena de caracteres en conjunto
palabra=set('manzana')
for letra in palabra:
	print(letra)
#un conjunto es una coleccion de elementos no ordenados
	 

