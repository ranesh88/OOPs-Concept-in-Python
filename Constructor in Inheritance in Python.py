# Constructor in Inheritance in Python

class Father:
    def __init__(self, m):
        self.money = m
        print("Father Class Constructor")

    def show(self):
        print("Father Class Instance Method")


class Son(Father):
    def disp(self):
        print("Son Class Instance Method")
        print("Parent Class Instance variable ::", self.money)
        print("Manipulation on Parent Class Instance Variable ::", self.money+1000)

s = Son(1000)
print(s.money)
s.show()
s.disp()
