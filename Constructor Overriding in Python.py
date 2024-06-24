# Constructor Overriding in Python

# Constructor Overriding with Parameter
class Father:
    def __init__(self, m):
        self.money = m
        print("Father Class Constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self, r):
        self.money = r
        self.car = 'BMW'
        print("Son Class Constructor")
    def disp(self):
        print("Son Class Instance Method")

f = Father(5000)
s = Son(2000)
print(s.money)
print(s.car)
s.show()
s.disp()