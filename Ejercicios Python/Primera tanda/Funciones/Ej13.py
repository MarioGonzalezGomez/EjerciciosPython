# Confeccionar un programa que calcule el factorial de un número introducido por teclado:
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

num= int(input("¿De qué número desea saber el factorial?"))
print(factorial(num))