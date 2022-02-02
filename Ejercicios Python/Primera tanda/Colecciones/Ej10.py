# Crear un programa “Diccionario” que permita consultar definiciones, agregar nuevas palabras 
# con su definición o eliminar palabras.

salir=False
diccionario = {"hello":"hola", "goodbye":"adiós"}
while salir==False:
    resultado = input(
 """    Introduzca 1 para consultar definición
    Introduzca 2 para agregar palabras
    Introduzca 3 para eliminar palabras
    Introduzca 4 para salir""")
    if resultado==str(1):
       print(str(diccionario.get(input("Escriba la palabra en inglés para obtener su traducción"))))
    if resultado==str(2):
        clave= input("Introduzca la palabra en inglés")
        valor = input ("Introduzca su traducción al castellano")
        diccionario[clave]=valor
        print("Palabra introducida con éxito")
    if resultado==str(3):
        diccionario.pop(str(input("¿Qué palabra en inglés desea eliminar?")))
    if resultado==str(4):
        salir=True
        print("Adiós")

#Parte opcional

def leer_documento():
    with open ("ruta_fichero_csv") as fichero:
	    datos=fichero.read()
        
def cargar_palabras(datos):
    divididos= str(datos).split(";")
    claves=divididos[::2]
    valores=divididos[1::2]
    for i in range(0,len(claves)-1):
        diccionario.setdefault(claves[i],valores[i])