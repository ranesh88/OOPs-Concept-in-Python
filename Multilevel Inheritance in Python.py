# Multilevel Inheritance in Python
class Father(object):
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self):
        super().__init__()               # Calling Father Class Constructor
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Instance Method")

class GrandSon(Son):
    def __init__(self):
        super().__init__()                   # Calling Son Class Constructor
        print("Grandson Class Constructor")
    def showG(self):
        print("GrandSon Class Instance Method")


g = GrandSon()
#g.showG()
#g.showS()
#g.showF()