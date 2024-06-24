# Abstract Class Abstract Method and Concrete Method in Python

from abc import ABC , abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("Concrete Method")

#f = Father() TypeError: Can't instantiate abstract class Father without an implementation for abstract method 'disp'

class Child(Father):
    def disp(self):
        print("Child Class::")
        print("Defining Abstract Method")


c = Child()
#c.disp()
#c.show()


class DefenceForce(ABC):
    def __init__(self):
        self.id = 101
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun = AK 47", "ID::", self.id)

class Army(DefenceForce):
    def area(self):
        print("Army Area = Land")

class AirForce(DefenceForce):
    def area(self):
        print("AirForce Area = sky")

class IndianNavy(DefenceForce):
    def area(self):
        print("Indian Navy Area = Sea")

a=Army()
af = AirForce()
n = IndianNavy()

a.gun()
a.area()

af.gun()
af.area()

n.gun()
n.area()