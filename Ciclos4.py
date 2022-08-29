import math
"""# elevar al cuadrado
#valor =3
#cuadrado=valor**2
#print (cuadrado)
# raiz cuadrada
#raiz=math.sqrt(15)
#print(raiz)
# redondear
#print(round(raiz)) 
Ejercicio a resolver: un robot se mueve en un plano, iniciando en el punto 0,0 el robot puede 
moverse UP, DOWN, LEFT, RIGHT, una serie de pasos indicados, escribe un programa que calcule la 
distancia entre la posicion del robot y el punto original.
ejemplo de entrada:
UP 5 DOWN 3 LEFT 3 RIGHT 2 entonces la salidad deberia ser: 2 considerando la formula para la 
distancia entre dos puntos, redondee en caso de decimales
d=round(math.sqrt(((x1-x2)**2)+((y1-y2)**2))
"""
x1=0
y1=0

print("Escribe el valor de UP: ")
up=int(input())
print("Escribe el valor de DOWN: ")
down=int(input())
y2=up-down

print("Escribe el valor de LEFT: ")
left=int(input())
print("Escribe el valor de RIGHT: ")
right=int(input())
x2=right-left
print("el valor de y es: ",y2)
print("el valor de x es: ",x2)
t1=((x1-x2)**2)
t2=((y1-y2)**2)
d=round(math.sqrt(t1+t2))
print("la distancia es ",d)
