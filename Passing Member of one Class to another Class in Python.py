# Passing Member of one Class to another Class in Python

class Student:
    # Constructor
    def __init__(self,n,r):
        self.name = n
        self.roll = r
    # Instance Method
    def disp(self):
        print("Student Name ::", self.name)
        print("Student Roll ::", self.roll)

class User:
    # Static Method
    @staticmethod
    def show(s):
        print("User Name ::", s.name)
        print("User Roll ::", s.roll)
        s.disp()

# Creating object of Student Class
stu = Student("Rahul", 101)

User.show(stu)
