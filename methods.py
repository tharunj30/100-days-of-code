#variables store the data
#whereas the method gives us an explaination on how to work
#variables there are two class/static and instance 
#methods there are three class method static method and instance method
class student:
    school='tharun'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1
    
    def set_m1(self,value):
        self.m1=value 

    @classmethod

    def getSchool(cls):
        return cls.school

    @staticmethod

    def info():#leave the inside empty
        print("this is a staticmethod used")

s1=student(17,18,19)
s2=student(1,9,10)
# print(s1.avg())
# print(s2.avg())
print(student.getSchool()) #this owrks with class methods 
#if you want to fetch the values you will use the  accessors
#where if you want to modify the values you will use the mutators 
student.info()