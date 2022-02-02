# Crear un programa que almacene nombres de personas, tras introducir un nombre nuevo mostrará un 
# conteo de los nombres que tienen 5 o más caracteres y preguntará si desea introducir un nuevo 
# nombre o salir del programa. Opcional: Cargar palabras a partir de un archivo txt.

salir= False
nombres =[]
while(salir==False):
    entrada= input("Introduce un nombre o escribe salir")
    if entrada=="salir":
        salir=True
    else:
        nombres.append(entrada)
        mas_de_5 = 0
        for i in nombres:
            if len(i)>=5:
                mas_de_5 += 1
        print("Actualmente hay " + str(mas_de_5)+ " nombres con más o 5 caracteres")

#Parte opcional

def leer_documento():
    with open ("ruta_fichero") as fichero:
	    datos=fichero.read()
        
def cargar_palabras(datos):
    for i in datos:
        nombres.append(i)