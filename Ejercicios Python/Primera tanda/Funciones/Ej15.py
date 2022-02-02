# Reescribe el ejercicio 3 del apartado “Colecciones” utilizando una función 
# para presentar el menú y recibir la opción seleccionada.

import random

def mostrar_menu():
        return str( input(
 """    Introduzca 1 para agregar persona
    Introduzca 2 para obtener persona aleatoria
    Introduzca 3 para salir"""))

nombres= ["Juan", "Pepe"]
salir=False
while salir==False:
    resultado = mostrar_menu()
    if resultado==str(1):
        nombres.append(input("¿Cómo se llama la persona a introducir?"))
    if resultado==str(2):
        print(nombres[random.randint(0,len(nombres)-1)]) 
    if resultado==str(3):
        salir=True
        print("Adiós")   