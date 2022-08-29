#Recorrer listas con for
so=["windows","linux","mac","solaris","bsd","Unix"]
print (so)
for x in so:
	print(x)

#if dentro de un for
edades=[12,15,23,30,50]
cantidad=0
for num in edades:
	if(num%3==0):
		cantidad+=1
print(cantidad)
