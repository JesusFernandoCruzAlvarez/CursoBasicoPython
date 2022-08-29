# Un ejemplo de multilistas en python
"""escriba un programa que tome dos digitos x,y como entrada y genere una multilista donde el valor 
de cada elemento sea el numero de fila.
una entrada seria:
3,3
la salida seria:
[[0,0,0][1,1,1][2,2,2]] """
input_str=input("Escriba dos numeros separados por comas: ")
dimension=[int(x) for x in input_str.split(',')]
rowNum=dimension[0]
colNum=dimension[1]
multilista=[[int(col*row) for col in range(colNum)]for row in range(rowNum)]
print (multilista)
