from collections import deque

turno=deque(["0","X"])

tablero=[[" "," "," "],
		[" "," "," "],
		[" "," "," "]
]

def rotar_turno():
	turno.rotate()
	return turno[0]

def mostrar_tablero():
	print("")
	for fila in tablero:
		print(fila)
def procesar_posicion(posicion):
	fila,columna=posicion.split(',')
	return [int(fila)-1,int(columna)-1] 
def posicion_correcta(posicion):
	if 0 <=posicion[0]<=2 and 0<= posicion[1]<=2:
		if tablero[posicion[0]][posicion[1]]==" ":
			return True
		return False
def actualizar_tablero(posicion,jugador):
	tablero[posicion[0]][posicion[1]]=jugador
 
def ha_ganado(j):
	if tablero[0]==[j,j,j] or tablero[1]==[j,j,j]or tablero[2]==[j,j,j]:
		return True
	elif tablero[0][0]==j and tablero[1][0]==j and tablero[2][0]==j:
		return True
	elif tablero[0][1]==j and tablero[1][1]==j and tablero[2][1]==j:
		return True
	elif tablero[0][2]==j and tablero[1][2]==j and tablero[2][2]==j:
		return True
	elif tablero[0][0]==j and tablero[1][1]==j and tablero[2][2]==j:
		return True
	elif tablero[0][2]==j and tablero[1][1]==j and tablero[2][0]==j:
		return True 
	return False

def empate():
	print("van empatados")  		 


def juego():
	mostrar_tablero()
	jugador=rotar_turno()
	while True:
		posicion =input("Juega {}.  elige una posicion fila,columna de 1 a 3 ".format(jugador))
		if posicion=="salir":
			break
		
		try:
			posicion_l=procesar_posicion(posicion)
		except:
			print("error, posicion {} no es válida".format(posicion))
			continue  
		if posicion_correcta(posicion_l):
			print ("correcta")
			actualizar_tablero(posicion_l,jugador)
			mostrar_tablero()
			
			if ha_ganado(jugador):
				print("jugador de {} ha ganado!!!".format(jugador))
				break
			else:
				empate()
			jugador=rotar_turno()
		else:
			print ("posicion {} no es correcta".format(posicion))		
juego() 