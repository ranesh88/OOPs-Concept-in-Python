# Instance Method in Python

# Instance Method without parameter
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'   # Instance Variable
    def show_model(self):        # Instance Method
        print("Model::", self.model)

realme = Mobile()
realme.show_model()

# Instance Method with parameter
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'   # Instance Variable
    def show_model(self,p):        # Instance Method
        self.price = p
        print("Model::", self.model , "Price ::" , self.price)

realme = Mobile()
realme.show_model(1000)

