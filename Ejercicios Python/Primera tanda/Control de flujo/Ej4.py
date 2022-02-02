#Programa que adivine el numero en el que está pensando (entre 0 y 100) el usuario por tanteo 
# (preguntando sucesivamente si es mayor o menor que un número aleatorio de partida)
import random

tuNumero = False
intentos = 1
numMin = 0
numMax = 100

print("Piensa un número entre 0 y 100")
while tuNumero==False:
    resultado = random.randint(numMin,numMax)
    respuesta= input("¿Es "+ str(resultado)+ " tu número?")
    if respuesta=="Sí" or respuesta=="si" or respuesta=="sí":
        tuNumero=True
    else:
        intentos+=1
        mayor = input("¿El número es mayor que "+ str(resultado)+ "?")
        if mayor=="Sí" or mayor=="si" or mayor=="sí":
            numMin=resultado+1
        else:
            numMax=resultado

print("He necesitado " + str(intentos) + " para acertar tu número")
