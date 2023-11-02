class Publisher:
    def __init__(self,location,name):
        self.name = name
        self.location = location
    def get_info(self):
        return f'Издательства: {self.name} \nПо адресу: {self.location}'
    def publish(self,message):
        self.message = message
        return f'Готовим {self.message} к публикации в {self.name} ({self.location})'
class BookPublisher(Publisher):
    def __init__(self,name,location,num_authors):
        super().__init__(name,location)
        self.num_authors = num_authors
    def publish(self,book,auther):
        return f'Передаем рукопись {book}, написанную автором {auther} в издательство {self.name} ({self.location})'
class NewspaperPublesher(Publisher):
    def __init__(self,name,location,num_pages):
        super().__init__(name,location)
        self.num_pages = num_pages
    def publish(self,message):
        return f'Печатаем свежий номер со статьей {message} на главной странице в издательстве {self.name} ({self.location})'


pub = Publisher('Omsk','asddad')
print(pub.get_info())
print(pub.publish("Справочник авпваппав"))
publisher = Publisher("АБВГД Пресс", "Москва")
print(publisher.publish("Справочник писателя"))

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
print(book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин"))

newspaper_publisher = NewspaperPublesher("Московские вести", "Москва", 12)
print(newspaper_publisher.publish("Новая версия Midjourney будет платной"))

