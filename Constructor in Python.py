# Constructor in Python

#Constructor

class Mobile:
    def __init__(self):
        print("Mobile Constructor called")

realme=Mobile()

#Constructor without Parameter
class Mobile:
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        print("Model:",self.model)

realme=Mobile()
realme.show_model()

#Constructor with Parameter
class Mobile:
    #Constructor
    def __init__(self,m,v=80):
        self.model=m
        self.volume=v
    def show_model(self,p):
        price=p                  #Local Variable
        print("Model:",self.model,"Price:",price)
        print("Volume:",self.volume)

#Passing argument to Constructor
realme=Mobile("RealMe X",50)
#Accessing method from outside class
realme.show_model(1000)

#Passing argument to Constructor
redmi=Mobile("redmi 7s",55)
#Accessing method from outside class
redmi.show_model(1200)

