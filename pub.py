class Publication:
    a = 'a'
    def __init__(self,title,author,year):
        self.__title = title
        self.__author = author
        self.__year = year

    def display(self):
        print('Название: ', self.__title)
        print(f'Автор: {self.__author}')
        print(f'Год издания: {self.__year}')

class Book(Publication):
    def __init__(self,title,author,year,isbn):
        super().__init__(title,author,year)
        self.isbn = isbn
    def display(self):
        super().display()
        print(f'ISBN: {self.isbn}')

class Magazine(Publication):
    def __init__(self,title,author,year,issue_number):
        super().__init__(title,author,year)
        self.issue_number = issue_number
    def display(self):
        super().display()
        print(f'Номер выпуска: {self.issue_number}')

# p = Publication('asdads','asdads','1231231233')
# p.display()
# b = Book('Чебурашка','народная',1995,123123123112121212312313123123123123131312123)
# b.display()
m = Magazine('Челвек паук',"Евгений Викторович",1975,5)
m.display()