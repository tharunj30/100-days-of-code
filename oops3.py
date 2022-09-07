
#everytime an object is created a new address is allocated to it
class computer:
    def __init__(self):
        self.name='tharun'
        self.age=29
    
    def update(self):
        self.age=90
    
    def compare(self,other):
        if self.age==other.age:
           return True
        else:
            return False

c1=computer() #size of an object depends on the variables and size of variables assigned to it
#size allocation is done by constructor for this program computer() is the constructor
c2=computer()

print(c1.name)
# c1.update()
if c1.compare(c2):
    print("they are of same age")
else:
    print("not of same age")


