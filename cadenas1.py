#impresion de cadenas
print("hola mundo")
# imprimir dos cadenas 
print ("Saludos", "amigos") 
#imprimir cadenas con separador
print("Bienvenidos","al","curso",sep="-")
#las cadenas son arreglos en python
dato="Python "
print (dato[3])
#slicing
# imprimir desde el caracter que está en la posicion 2 al 4
print(dato[2:5])
print (dato[-4:-2])
# Metodos de cadenas
#Longitud de la cadena
print (len(dato))
#Convertir a minusculas
print(dato.lower())
#convertir a mayusculas
print(dato.upper())
#contar
print (dato.count("t"))
#Buscar
print(dato.find("o"))
#reemplazar
dato2=dato.replace("y","i")
print(dato2)
#remover espacios o caracteres al inicio o al final de la cadena
dato3=dato.strip()
print("dato con espacio eliminado:", dato3)
#operador in
print("p" in dato)

#convertir de numero a cadena
valor_cadena=str(1)
#convertir de cadena a numero
valor_numero=int("1")
#por default asume que tiene base 10 pero puede utilizar otra base
valor_d = int("1000",2)
print ("Valor convertido a base 2")
print (valor_d)

 #funcion format
nombre="Fernando"
curso="Python"
presentacion="Hola me llamo {} y estoy 	en curso de {}".format(nombre, curso)
print (presentacion)
import math
valor_pi="El valor de pi es {:.2f}".format(math.pi)
print (valor_pi)

#Entrada de datos en modo consola 
print("Dame un valor: ")
mi_valor=input()
#lo lee como cadena
print("Dame otro valor")
otro_valor=int(input())

#lo lee como entero


