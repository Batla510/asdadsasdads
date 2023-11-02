class Shape:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def describe(self):
        print(f'Это геометрическая фигура, цвет - {self.color}')
class Circle(Shape):
    def __init__(self,name,color,radius):
        super().__init__(name,color)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f'Это окружность. Радиус - {self.radius} см, цвет - {self.color}.')
    def area(self):
        return 3.14*self.radius**2