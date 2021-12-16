# from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod

# class Shape(metaclass=ABCMeta):   - This can also be used but it is older syntax
class Shape(ABC):                  # - This is used in new version of python after version 3.4
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=7
        self.breadth=3

    def printarea(self):
        return self.length*self.breadth

rect1=Rectangle()
# rect2=Shape()  - cannot create object of abstract class