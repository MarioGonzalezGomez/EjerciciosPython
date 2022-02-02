import secundaria as otro
import sys
#Podemos obtener los args[] con sys.args

def main():
    print("hola esto es el main")
    print(str(otro.funcion_retorna_numero())+", con rima y premio")

if __name__== '__main__':
    sys.exit(main())