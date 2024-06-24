# Constructor with Super Method or Call Parent Class Constructor in Child Class in Python

# Constrictor with Super Method

class Father:
    def __init__(self,m):
        self.money = m
        print("Father Class Constructor")
    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)                 # Calling Parent Class Constructor
        self.job = j
        print("Son Class Constructor")
    def disp(self):
        print("Son Class Instance Method")
        print("Parent Class Instance Variable::", self.money)
        print("Son Class Instance Variable ::", self.job)

s = Son(2000,'SDE')
s.disp()

