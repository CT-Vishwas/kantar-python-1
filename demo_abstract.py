from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def calcualte_area(self):
        pass

    def describe(self):
        print("This is a 2D shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def calcualte_area(self):
        return self.width * self.height

rect = Rectangle(10,5)
print(f"Rectangle area: {rect.calcualte_area()}")
rect.describe()