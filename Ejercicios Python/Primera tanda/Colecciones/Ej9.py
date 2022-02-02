# Crear un programa que almacene con dos opciones: 1. Agregar personas: permite introducir nombres 
# de personas de forma interactiva, 2. Sorteo: devuelve el nombre de una persona al azar.
import random

nombres= ["Juan", "Pepe"]
salir=False
while salir==False:
    resultado = input(
 """    Introduzca 1 para agregar persona
    Introduzca 2 para obtener persona aleatoria
    Introduzca 3 para salir""")
    if resultado==str(1):
        nombres.append(input("¿Cómo se llama la persona a introducir?"))
    if resultado==str(2):
        print(nombres[random.randint(0,len(nombres)-1)]) 
    if resultado==str(3):
        salir=True
        print("Adiós")   

#Parte opcional

def leer_documento():
    with open ("ruta_fichero_csv") as fichero:
	    datos=fichero.read()
        
def cargar_palabras(datos):
    divididos=str(datos).split(";")
    for i in divididos:
        nombres.append(i)