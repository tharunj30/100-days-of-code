
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other): ##here we are overriding the add operaor
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)

        return s3

    def __gt__(self,other): #here we are overriding the greater than operator'>' to compare things given as an input to the class student
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self): #here we are over riding the string method without this we will get the address instead of the string
        return '{} {} '.format(self.m1,self.m2)#we are using format here cuz we will get it as a string instead of the numbers
s1=student(12,13)
s2=student(14,14)
print(s1.__str__())
if s1>s2:
    print("s1 wins")
else:
    print('s2 wins')

 