# Namespace in Python

# Class Variable
class Mobile:
    fp = 'Yes'                 # Class Variable
    @classmethod
    def is_fp(cls):           # Class Method
        print("Finger Print ::", cls.fp)         # Accessing Class Variable

realme = Mobile()
redmi = Mobile()
samsung = Mobile()

print("Class FP::", Mobile.fp)
print("RealMe FP::", realme.fp)
print("Redmi FP::", redmi.fp)
print("Samsung FP::", samsung.fp)
print()

Mobile.fp='No'
print("Class FP::", Mobile.fp)
print("RealMe FP::", realme.fp)
print("Redmi FP::", redmi.fp)
print("Samsung FP::", samsung.fp)
print()

realme.fp = 'Not Working'
print("Class FP::", Mobile.fp)
print("RealMe FP::", realme.fp)
print("Redmi FP::", redmi.fp)
print("Samsung FP::", samsung.fp)
