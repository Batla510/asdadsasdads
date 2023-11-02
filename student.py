class Student:
    def __init__(self,name,age,grade,score):
        self.name = name
        self.age = age
        self.grade = grade
        self.score = score

    def display(self):
        print('Имя: ', self.name)
        print('Возраст: ', self.age)
        print('Класс: ', self.grade)
        print('Оценки: ', self.score)
    def avarage_score(self):
        a = sum(self.score)
        c = len(self.score)
        return f'Средний балл: {a / c}'

x = Student('Sasha','16',9,[5,2,1,3,4,2,5,2,3,4])
x.display()
print(x.avarage_score())