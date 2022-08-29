#Listas
lista=[9.58,9.69,9.72]
print(lista)
#obtener la cantidad de elementos de una lista
cantidad_elementos=len(lista)
print(cantidad_elementos)
#Añadir un elemento al final
lista.append(8.99)
print (lista)
#añadir varios elementos
lista2=[7.52,7.89,7.44]
lista.extend(lista2)
print (lista)
#Concatenacion de listas
lista3=[8.65]
lista=lista+lista3
print(lista)
#Remover un elemento
lista.remove(9.58)
print (lista)
#Remover el ultimo elemento
lista.pop()
print (lista)
#contar cuantos elementos hay para un valor determinado 
print(lista.count(9.72))
#invertir la lista
print ("lista invertida")
lista.reverse()
print(lista)
