import sys
import Biblioteca as bib
import Book as bo
import User as us


biblioteca = bib.Biblioteca()
lista_libros = []
lista_disponibles = []
lista_prestados =[]
lista_users = []

def crearUsuario():
    user = us.User()
    user.dni = input("Introduzca su dni")
    user.name = input("Introduzca su nombre")
    user.email = input("Introduzca su email")
    user.phone = input("Introduzca su número de teléfono")
    user.address = input("Introduzca su dirección")
    print("Usuario introducido con éxito")
    biblioteca.partners
        
        
def borrarUsuario(id):
    print(f"Usuario {id} eliminado con éxito")

def crearLibro():
    book = bo.Book()
    book.isbn = input("Introduzca el isbn del libro")
    book.title = input("Introduzca el título")
    book.author = input("Introduzca el autor")
    book.gender = input("Introduzca el género literario")
    book.cover = input("Introduzca la portada")
    book.synopsis = input("Introduzca la sinopsis")
    book.copies = input("De qué número de copias de dispone")

def opciones(respuesta):
    respuesta = int(respuesta)
    if(respuesta==1):
        crearUsuario()
    if(respuesta==2):
        borrarUsuario(input("Introduce el dni del usuario a borrar"))
    if(respuesta==3):
        crearLibro()

def main():
    respuesta = input ("""1.  Alta de socio
    2.  Baja de socio
    3.  Alta de libro
    4.  Baja de libro
    5.  Prestar libro
    6.  Devolver libro
    7.  Consultar libros
    8.  Consultar usuarios
    9.  Consultar prestamos
    10. Salir""")
    opciones(respuesta)


if __name__ == '__main__':
    main()