# Multiple Inheritance and Method Resolution Order in Python

# Multiple Inheritance

class Father(object):
    def __init__(self):
        super().__init__()                  # Calling Parent Class Constructor
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Instance Method")

class Mother(object):
    def __init__(self):
        super().__init__()                     # Calling Parent Class Constructor
        print("Mother Class Constructor")
    def showM(self):
        print("Mother Class Instance Method")

class Son(Father, Mother):
    def __init__(self):
        super().__init__()                  # Calling Parent Class Constructor
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Instance Method")

s = Son()
# s.showF()
# s.showM()
# s.showS()


