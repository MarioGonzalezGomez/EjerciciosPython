# Haz un programa que adivine la talla de pie y la edad del usuario que lo ejecute. 
# Se basa en un sencillo truco matemático. El programa debe pedir al usuario que realice 
# las siguientes operaciones (las operaciones la tiene que realizar el de cabeza, no el programa):
# Pensar, escribir o apuntar su talla de zapato.
# Multiplicar ese número por 5.
# Sumarle 50.
# Multiplicarlo por 20.
# Sumarle 1022.
# Restarle el año de nacimiento.

# Después debes preguntarle el resultado y calcular su talla de zapato.
# Para obtener la talla, las dos primeras cifras corresponderán a la talla del zapato y 
# las dos siguientes a la edad del usuario.

print("""Piensa, escribe o apuntar tu talla de zapato.
#Multiplica ese número por 5.
#Sumarle 50.
#Multiplicalo por 20.
#Súmale 1022.
#Réstale el año de nacimiento. """)
resultado = input("¿Qué número has obtenido?")
print("Te edad es " + resultado[-2:])
print("Tu número de pie es "+ resultado[:2])