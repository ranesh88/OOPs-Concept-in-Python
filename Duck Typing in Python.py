# Duck Typing in Python

class Duck:
    def walk(self):
        print("Duck walking behaviour")

class Horse:
    def walk(self):
        print("Horse walking behaviour")

class Cat:
    def talk(self):
        print("Cat talking behaviour")

def myfunction(obj):
    obj.walk()

d = Duck()
h = Horse()
c= Cat()

myfunction(d)
myfunction(h)
#myfunction(c) AttributeError: 'Cat' object has no attribute 'walk'.