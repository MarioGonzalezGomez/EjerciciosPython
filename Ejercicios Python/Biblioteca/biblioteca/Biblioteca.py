class Biblioteca():
    
    def __init__(self, partners, books, books_available, books_on_loan):
        self.__partners=partners
        self.__books=books
        self.__books_avalaible= books_available
        self.__books_on_loan=books_on_loan

    @property
    def partners(self):
        return self.__partners
    
    
    @partners.setter
    def partners(self,a):
        self.__partners=a
    
    @property
    def books(self):
        return self.__books
    
    @books.setter
    def books(self,a):
        self.__books=a
    
    @property
    def books_available(self):
        return self.__books_available
    
    @books_available.setter
    def books_available(self,a):
        self.__books_available=a
    
    @property
    def books_on_loan(self):
        return self.__books_on_loan
    
    @books_on_loan.setter
    def books_on_loan(self,a):
        self.__books_on_loan=a
    
