#Ejercicio
"""Escribe un programa que realice la siguiente operacion:
a+aa+aaa+aaaa
con un valor a dado por el usuario, por ejemplo si el usuario escribe
un 9, la operacion sería 9+99+999+9999
"""
x= input ("Dame un valor: ")
n1=x
n2=x+x
n3=x+x+x
n4=x+x+x+x
total=int(n1)+int(n2)+int(n3)+int(n4)
print("el total es: ",total)