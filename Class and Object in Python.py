# Class and Object in Python

#Example 1

class Myclass(object):
    def show(self):
        print("I am a Method")


x=Myclass()
x.show()

#Example 1

class Myclass():
    def show(self):
        print("I am a Method")

x=Myclass()
x.show()

#Example 3
class Mobile():
    def __init__(self):
        self.model='RealMe X'

    def show_model(self):
        print("Model:",self.model)

realme = Mobile()
realme.show_model()
print(realme.model)
realme.model='Realme ProMax2'
print(realme.model)
realme.show_model()

#Example 4

class Mobile():
    def __init__(self):
        self.model='RealMe X'

    def show_model(self):
        price=10000
        print("Model:",self.model,"Price ::",price)

realme = Mobile()
realme.show_model()

#Example 5
class Mobile():
    def __init__(self,m):
        self.model=m

    def show_model(self,p):
        price=p
        print("Model:",self.model,"Price ::",price)

realme = Mobile('RealMe X')
realme.show_model(10000)


#Example 6
class Mobile():
    def __init__(self,m):
        self.model=m

    def show_model(self,p):
        price=p
        print("Model:",self.model,"Price ::",price)

redmi = Mobile('Redmi Pro')
redmi.show_model(10000)
print("id =",id(redmi))

vivo = Mobile('Vivo Max6')
vivo.show_model(15000)
print("id =",id(vivo))

samsung = Mobile('Samsung Galaxy Pro')
samsung.show_model(65000)
print("id =",id(samsung))

redmi1 = Mobile('Redmi Pro')
redmi1.show_model(10000)
print("id =",id(redmi1))



