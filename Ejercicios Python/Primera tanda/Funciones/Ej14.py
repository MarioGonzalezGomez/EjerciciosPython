# Escribe una función que tome una palabra y retorne con todas las letras en minúscula 
# menos la primera y la última.

def minus(a):
    a=str(a).capitalize()
    a=str(a)[:-1] + str(a)[-1:].upper()
    a=str(a)[0]+str(a)[1:-1].lower()+str(a)[-1:]
    return a

palabra=str(input("Introduce la palabra a transformar"))
print(minus(palabra))