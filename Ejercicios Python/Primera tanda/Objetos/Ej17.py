# Reescribe el ejercicio 3 del apartado “Colecciones” con orientación a objetos. Opcional:
# Usa herencia para tener un diccionarios de al menos dos idiomas. Añade las opciones de importar
# o exportar el diccionario a un fichero.

import random

class Mostrador_de_nombres:

    def __init__(self, nombres= ["Juan", "Pepe"]) -> None:
        self.__nombres=nombres

    @property
    def nombres(self):
        return self.__nombres
    
    @nombres.setter
    def nombres(self,a):
        self.__nombres=a

    def mostrar_menu(self):
            return str( input(
    """        Introduzca 1 para agregar persona
        Introduzca 2 para obtener persona aleatoria
        Introduzca 3 para salir"""))


    def randomNames(self):
        salir=False
        while salir==False:
            resultado = self.mostrar_menu()
            if resultado==str(1):
                self.nombres.append(input("¿Cómo se llama la persona a introducir?"))
            if resultado==str(2):
                print(self.nombres[random.randint(0,len(self.nombres)-1)]) 
            if resultado==str(3):
                salir=True
                print("Adiós")   

class Main:
    mostrador= Mostrador_de_nombres()
    mostrador.randomNames()


#Parte opcional

def __leer_documento():
    with open("ruta_fichero") as fichero:
	    datos=fichero.read()

def importar(nombres):
    datos=__leer_documento()
    for i in datos:
        nombres.append(i)


def exportar(nombres):
    with open ("ruta_fichero") as fichero:
	    fichero.write(nombres)
