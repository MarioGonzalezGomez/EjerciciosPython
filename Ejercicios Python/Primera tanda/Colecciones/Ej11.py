# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Crear una nueva lista 
# con los nombres ordenados alfabéticamente e imprimirla por pantalla.

nombres=[]
for i in range(0,5):
    nombres.append(str(input("Introduce el nombre de la "+ str(i+1)+ "ª persona")))

print(nombres)
nombresOrdenados= nombres.copy()
nombresOrdenados.sort()
print(nombresOrdenados)