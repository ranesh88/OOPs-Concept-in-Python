# Class Method in Python

# Class Method without Parameter
class Mobile:
    @classmethod                      # Decorator
    def show_model(cls):              # Class Method
        print("RealMe X")

realme = Mobile()
Mobile.show_model()                   # Calling Class Method

# Class Method with Class Variable

class Mobile:
    fp = 'Yes'                        # Class Variable
    @classmethod                      # Decorator
    def show_model(cls):              # Class Method without Parameter
        print("Finger Print::", cls.fp)

realme = Mobile()
Mobile.show_model()                   # Calling Class Method

# Class Method with Parameter

class Mobile:
    fp = 'Yes'                             # Class Variable
    @classmethod                           # Decorator
    def show_model(cls , r):               # Class Method with Parameter
        cls.ram=r
        print("Finger Print::" , cls.fp)
        print("RAM size ::" , cls.ram)

realme = Mobile()
Mobile.show_model("4GB")                   # Calling Class Method