class Book:
    def __init__(self,title,author,isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def set_title(self,title):
        self.__title = title

    def set_author(self,author):
        self.__author = author

    def set_isbn(self,isbn):
        self.__isbn = isbn
b = Book('title1', "Author",'ISBN1')
print(b.get_title())
b.set_title("asdasdads")
