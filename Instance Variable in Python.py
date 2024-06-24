#Instance Variable in Python

class Mobile:
    def __init__(self):
        self.model='Real Me X'       # Instance Variable
    def show_model(self):
        print(self.model)            # Accessing Instance Variable

realme=Mobile()
redmi=Mobile()
samsung=Mobile()

print(realme.model)
print(redmi.model)
print(samsung.model)

print()

redmi.model='Redmi 7s'
print(realme.model)
print(redmi.model)
print(samsung.model)

samsung.model='Samsung Galaxy Pro'
print(realme.model)
print(redmi.model)
print(samsung.model)

