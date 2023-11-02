class Employee():
    def __init__(self,name,age,salary,bonus):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__bonus
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def set_salary(self,salary):
        self.__salary = salary
    def set_bonus(self,bonus):
        self.__bonus = bonus
    def get_total_salary(self):
        return self.__salary + self.__bonus

emp = Employee("Марина",30,90000,15000)
emp.set_bonus(15000)
print("Имя: ",emp.get_name())
print("Возраст ",emp.get_age())
print("Зарплата ",emp.get_salary())
print("Бонус ",emp.get_bonus())
print("Итог ",emp.get_total_salary())

