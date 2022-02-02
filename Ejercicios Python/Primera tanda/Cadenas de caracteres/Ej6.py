# Solicitar una oración por teclado y realizar las siguientes operaciones sobre ella:
# Mostrar longitud de la cadena.
# Mostrar espacios en blanco se ingresaron.
# Mostrar toda la oración en letras mayúsculas.
# Duplicar el contenido de la cadena.
# Dividir la cadena en una lista de palabras y recorrerla mostrándola y numerando cada palabra.

cadena = input("Introduce una cadena de texto")
print("Su longitud es de: "+ str(len(cadena)))
print("Tiene un número de espacios en blanco de: "+ str(cadena.count(" ")))
print("En mayus: "+ cadena.upper() )
print("Duplicada: "+ str(cadena*2))

cadena_split = cadena.split(" ")
contador=1
for i in cadena_split:
    
    print(" Palabra:" + str(contador) + " "+ i )
    contador+=1