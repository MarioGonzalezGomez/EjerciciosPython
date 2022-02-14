from .book import Book
from .biblio import Biblio
from .user import User

biblioteca = Biblio()
map_libros = {}
map_disponibles = {}
map_prestados ={}
map_users = {}
user_books = []

salir=False

def crearUsuario():
    user = User()
    user.dni = input("Introduzca su dni")
    user.name = input("Introduzca su nombre")
    user.email = input("Introduzca su email")
    user.phone = input("Introduzca su número de teléfono")
    user.address = input("Introduzca su dirección")
    print("Usuario introducido con éxito")
    map_users.values(user.dni: user)
    map_users.setdefault(user.dni: user)
        
        
def borrarUsuario(dni):
   valor= map_users.pop(dni)
   if (str(valor)==None | str(valor)==""):
        print(f"Usuario {dni} eliminado con éxito")

def crearLibro():
    book = Book()
    book.isbn = input("Introduzca el isbn del libro")
    book.title = input("Introduzca el título")
    book.author = input("Introduzca el autor")
    book.gender = input("Introduzca el género literario")
    book.cover = input("Introduzca la portada")
    book.synopsis = input("Introduzca la sinopsis")
    book.copies = input("De qué número de copias de dispone")
    map_libros.setdefault({book.isbn:book})
    map_disponibles.setdefault({book.isbn:book})


def borrarLibro(isbn):
    valor= map_libros.pop(isbn)
    map_disponibles.pop(isbn)
    map_prestados.pop(isbn)
    if (str(valor)==None | str(valor)==""):
        print(f"Libro {isbn} eliminado con éxito")

def prestarLibro(isbn,dni):
   libro= map_disponibles.pop(isbn)
   map_prestados.setdefault(isbn,libro)
   user_books.append(libro)
   user = map_users.get(dni)
   user.books = user_books

def devolverLibro(isbn,dni):
    libro = map_prestados.pop(isbn)
    map_disponibles.setdefault(isbn,libro)
    user = map_users.get(dni)
    user.books.remove(libro)

def consultarLibros():
    print(map_libros.items)

def consultarUsuarios():
    print(map_users.items)

def consultarPrestamos():
    print(map_prestados.items)

def actualizarDatos():
    biblioteca.books=map_libros
    biblioteca.books_available= map_disponibles
    biblioteca.books_on_loan=map_prestados
    biblioteca.partners= map_users
    

def opciones(respuesta):
    respuesta = int(respuesta)
    if(respuesta==1):
        crearUsuario()
    if(respuesta==2):
        borrarUsuario(input("Introduce el dni del usuario a borrar"))
    if(respuesta==3):
        crearLibro()
    if(respuesta==4):
        borrarLibro(input("Introduce el isbn del libro a borrar"))
    if(respuesta==5):
        prestarLibro(input("Introduce el isbn del libro a prestar"), input("Introduce el dni del usuario que lo recibe"))
    if(respuesta==6):
        devolverLibro(input("Introduce el isbn del libro devuelto"), input("Introduce el dni del usuario que lo devuelve"))
    if(respuesta==7):
        consultarLibros()
    if(respuesta==8):
        consultarUsuarios()
    if(respuesta==9):
        consultarPrestamos()
    if(respuesta==10):
        salir=True
    actualizarDatos()

def main():
    while(salir==False):
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