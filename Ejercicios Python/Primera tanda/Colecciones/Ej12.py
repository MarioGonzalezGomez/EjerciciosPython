# Crear una lista con contenido [[50,34,70,20], [5,70,30,25], [10,5], [75,43,56,32,89], [[54,72]].
#  Imprimir la lista, asignar valor cero a todos los elementos mayores a 50 y volver a imprimir la 
# lista.

lista = [ [50,34,70,20] , [5,70,30,25] , [10,5] , [75,43,56,32,89] , [54,72] ]

print(lista)

for sublista in lista:
    for elemento in sublista:
        if elemento>50:
            sublista[sublista.index(elemento)]=0
print(lista)