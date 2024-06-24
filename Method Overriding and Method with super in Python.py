# Method Overriding and Method with super in Python

class Add:
    def result(self, x, y):
        print("Addition ::", x+y)

class Multi(Add):
    def result(self, a, b):
        super().result(30, 50)
        print("Multiplication ::", a*b)
    #pass

m = Multi()
m.result(10, 20)