# Crea una clase “Saludo” que tenga los métodos: formal, informal y aleatorio. 
# Los métodos pueden aceptar un parámetro (nombre de la persona a saludar) o ninguno 
# (saludo genérico), el método aleatorio imprimirá un saludo aleatorio de una lista de saludos 
# almacenados en la clase
import random

class Saludo:
        
    saludos = ["Buenos días", "Cómo va todo", "Hola holita"]

    """Clase Saludo"""
    def informal(self, nom=""):
        print(f"Buenos días, es un honor contar con su presencia {nom}")
    
    def formal(self, nom=""):
        print(f"¿Qué pasa con la pasa {nom}?")

    def informal(self,sal=[], nom=""):
        saludo=sal[random(0,len(sal)-1)]
        print(f"{saludo} {nom}")