#Programa que dibuje con asteriscos un triángulo rectángulo de N asteriscos de alto. 

alto = input("¿Qué altura tiene el triángulo?")
for i in range(1,int(alto)+1):
    print("*"*i)