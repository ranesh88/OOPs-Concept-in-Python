# Hierarchical Inheritance in Python

class Father(object):
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Instance Method")

class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter Class Constructor")
    def showD(self):
        print("Daughter Class Instance Method")

s = Son()
# s.showS()
# s.showF()
# s.showD()  AttributeError: 'Son' object has no attribute 'showD'.

d = Daughter()
# d.showD()
# d.showF()
# d.showS()  AttributeError: 'Daughter' object has no attribute 'showS'

