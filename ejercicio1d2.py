"""Escriba un programa que tome dos digitos x,y como entrada y genere una multilista donde el valor 
del elemento i,j (fila, columna) sea i*j
ejemplo, si la entrada fuese 3,5 la salida seria: [[0,0,0,0,0][0,1,2,3,4][0,2,4,6,8]]
imprima tambien la salida, una fila por linea
[0,0,0,0,0]
[0,1,2,3,4]
[0,2,4,6,8]"""
input_str=input("Escriba dos numeros separados por comas: ")
dimension=[int(x) for x in input_str.split(',')]
rowNum=dimension[0]
colNum=dimension[1]
multilista=[[int(row*col) for col in range(colNum)]for row in range(rowNum)]
print (multilista)
for i in multilista:
	print(i)