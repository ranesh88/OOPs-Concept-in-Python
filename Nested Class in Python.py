# Nested Class in Python

class Army:
    def __init__(self):
        self.name = 'Rahul'
        #self.gn = self.Gun()    # Creating Inner Class Object
    def show(self):
        print("Name ::", self.name)

    class Gun:
        def __init__(self):
            self.name = 'AK 47'
            self.capacity = '75 Rounds'
            self.length = '34.3 In'
        def disp(self):
            print("Gun Name ::", self.name)
            print("Gun Capacity ::", self.capacity)
            print("Gun Length :: ", self.length)

a = Army()
print(a.name)
a.show()

g = Army().Gun()

#print(a.gn.name)
#print(a.gn.capacity)
#print(a.gn.length)

#a.gn.disp()
#g=a.gn

print(g.name)
print(g.capacity)
print(g.length)

g.disp()



