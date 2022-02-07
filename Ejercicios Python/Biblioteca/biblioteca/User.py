class User():

    def __init__(self, dni, name, email, phone, address, books) -> None:
        self.__dni=dni
        self.__name=name
        self.__email=email
        self.__phone=phone
        self.__address=address
        self.__books=books

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,a):
        self.__dni=a

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,a):
        self.__name=a
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,a):
        self.__email=a
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self,a):
        self.__phone=a

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,a):
        self.__address=a
    
    @property
    def books(self):
        return self.__books
    
    @books.setter
    def books(self,a):
        self.__books=a