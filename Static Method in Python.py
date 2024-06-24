# Static Method in Python

# Static Method without Parameter
class Mobile:
    @staticmethod            # Decorator
    def show_model():        # Static Method
        print("RealMe X")

realme = Mobile()
Mobile.show_model()          # Calling Static Method

# Static Method with Class Variable
class Mobile:
    fp= 'Yes'
    @staticmethod            # Decorator
    def show_model():        # Static Method
        print("Finger Print ::", Mobile.fp)

realme = Mobile()
Mobile.show_model()          # Calling Static Method

# Static Method with Parameter

class Mobile:
    @staticmethod               # Decorator
    def show_model(m,p):        # Static Method
        model = m
        price = p
        print("Model ::", model ,"Price::", price)

realme = Mobile()
Mobile.show_model("Redmi Pro 6",4000)             # Calling Static Method
