# Accessor or Getter Method and Mutator or Setter Method in Python

# Instance Method - Accessor or Getter Method

class Mobile:
    def __init__(self):
        self.model = 'RealMe X'         # Instance Variable
    def get_model(self):                # Instance Method
        return self.model

realme = Mobile()
m = realme.get_model()                  # Calling Access Method
print(m)

# Instance Method - Mutator or Setter Method without Parameter

class Mobile:
    def __init__(self):
        self.model = 'RealMe X'         # Instance Variable
    def set_model(self):                # Instance Method
        self.model = 'RealMe 2'

realme = Mobile()
#Before Setting
print(realme.model)
#After Setting
realme.set_model()                      # Calling Mutator Method
print(realme.model)

# Instance Method - Mutator or Setter Method with Parameter

class Mobile:
    def set_model(self, m):                # Instance Method
        self.model = m

realme = Mobile()
realme.set_model('Samsung Galaxy Pro')    # Calling Mutator Method
print(realme.model)



