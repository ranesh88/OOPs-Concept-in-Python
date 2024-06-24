#Class Variable or Static Variable in Python

class Mobile:
    fp='Yes'                 # Class Variable
    @classmethod
    def is_fp(cls):
        print(cls.fp)         # Accessing Class Variable

realme = Mobile()

print(Mobile.fp)
Mobile.is_fp()

# Class Variable or Static Variable with Class Method
class Mobile:
    fp='Yes'                            # Class Variable
    def __init__(self):
        self.model='Real Me X'          # Instance Variable

    def show_model(self):               # Instance Method
        print("Model::",self.model)     # Accessing Instance Method

    @classmethod
    def is_fp(cls):                       # classMethod
        print("Finger Print ::",cls.fp)   # Accessing Class Variable

realme=Mobile()
realme.show_model()
realme.is_fp()
print()
Mobile.fp = 'No'                 # Modifying Class Variable
realme.is_fp()
print()


# Class Variable
class Mobile:
    fp='Yes'                 # Class Variable
    @classmethod
    def is_fp(cls):           # Class Method
        print("Finger Print ::",cls.fp)         # Accessing Class Variable

realme = Mobile()
redmi = Mobile()
samsung = Mobile()

print("RealMe::",Mobile.fp)
print("Redmi::",Mobile.fp)
print("Samsung::",Mobile.fp)
print()

Mobile.fp='No'                 # Modifying Class Variable
print("RealMe::",Mobile.fp)
print("Redmi::",Mobile.fp)
print("Samsung::",Mobile.fp)



