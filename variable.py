# two types of variables instance variable and class/static varible
#namespace is a place where we create names and store names of variables
#types are class namespace where we store class variable
# and instance namespace  where we store instance variable
class car:
    #classes defined out of init we get class variables and it is common to all objects
    wheels=4 #examples of class variables
    def __init__(self):
        #beow both are instance variables which change everytime another car is changed 
        #variable defined inside init will be instance variable

        self.mil=10 #examples for instance variables
        self.brand="bmw"

c1=car()
c2=car()

print(c1.mil,c1.wheels)
c1.mil=7
#the above comments can be explained here
print(c1.mil,c2.wheels)

#now here we change the class variable which effects the entire set
car.wheels=10
print(c1.mil,c1.wheels)
print(c1.mil,c2.wheels)

