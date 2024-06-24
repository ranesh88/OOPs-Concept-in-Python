# Single Inheritance in Python

class Father:
    money = 1000
    def show(self):
        print("Parent Class Instance Method")

    @classmethod
    def showmoney(cls):
        print("Parent Class Class Method::", cls.money)

    @staticmethod
    def stat():
        a=10
        print("Parent Class Static Method::", a)

class Son(Father):
    def disp(self):
        print("Child Class Instance Method")

s = Son()
s.disp()
s.show()
s.showmoney()
s.stat()

print()

f = Father()
s.show()
s.showmoney()
s.stat()
#f.disp() AttributeError: 'Father' object has no attribute 'disp'

