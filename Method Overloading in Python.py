# Method Overloading in Python

class Myclass:
    def sum(self, a):
        print("1st Sum Method", a)
    def sum(self):
        print("2nd Sum Method")

obj = Myclass()
obj.sum()
#obj.sum(10) TypeError: Myclass.sum() takes 1 positional argument but 2 were given

# Method Overloading

class Myclass:
    def task(self, a=None, b=None, c=None):
        if(a!=None and b!=None and c!=None):
            s = a+b+c
        elif a!=None and b!=None:
            s = a*b
        else:
            s = "Please provide two numbers"
        return s
obj = Myclass()
print(obj.task(10, 20, 30))
print(obj.task(10, 20))
print(obj.task(10))
print(obj.task())
