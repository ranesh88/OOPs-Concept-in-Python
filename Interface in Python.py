# Interface in Python

from abc import ABC , abstractmethod
class DefenceForce(ABC):
    def __init__(self):
        self.id = 101
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def gun(self):
        pass

class Army(DefenceForce):
    def gun(self):
        print("Child Class Army defining Abstract Method::")
        print("Gun = AK 47")

    def area(self):
        print("Army Area = Land")
        print()

class AirForce(DefenceForce):
    def gun(self):
        print("Child Class AirForce defining Abstract Method::")
        print("Gun = AK 42")

    def area(self):
        print("AirForce Area = sky")
        print()

class IndianNavy(DefenceForce):
    def gun(self):
        print("Child Class Indian Navy defining Abstract Method::")
        print("Gun = AK 43")

    def area(self):
        print("Indian Navy Area = Sea")
        print()

a=Army()
af = AirForce()
n = IndianNavy()

#a.gun()
#a.area()

#af.gun()
#af.area()

#n.gun()
#n.area()

class Father(ABC):
      @abstractmethod
      def disp(self):
          pass
class Child(Father):
    def disp(self):
        print("Child Class::")
        print("Defining Abstract Method")

c = Child()
#c.disp()


class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass

    @abstractmethod
    def disp2(self):
        pass


class Child(Father):
    def disp1(self):
        print("Child Class::")
        print("Disp1 Abstract Method")

class GrandChild(Child):
    def disp2(self):
        print("GrandChild Class::")
        print("Disp2 Abstract Method")

gc = GrandChild()
gc.disp1()
gc.disp2()