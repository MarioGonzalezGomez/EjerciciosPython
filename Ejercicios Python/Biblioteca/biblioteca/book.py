class Book():

    def __init__(self, isbn="", title="", author="", gender="", cover="", synopsis="", copies=""):
        self.__isbn=isbn
        self.__title=title
        self.__author=author
        self.__gender=gender
        self.__cover=cover
        self.__synopsis=synopsis
        self.__copies=copies

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self,a):
        self.__isbn=a

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self,a):
        self.__title=a
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self,a):
        self.__author=a
    
    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self,a):
        self.__gender=a

    @property
    def cover(self):
        return self.__cover
    
    @cover.setter
    def cover(self,a):
        self.__cover=a
    
    @property
    def synopsis(self):
        return self.__synopsis
    
    @synopsis.setter
    def synopsis(self,a):
        self.__synopsis=a
    
    @property
    def copies(self):
        return self.__copies
    
    @copies.setter
    def copies(self,a):
        self.__copies=a