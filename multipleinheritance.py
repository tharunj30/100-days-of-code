class A: #A is super class 
    def feature1(self):
        print('feature 1 is working from class a')

    def feature2(self):
        print('feature 2 is working from class a')

class B():
    def feature3(self):
        print('feature 3 is working from class b')

    def feature4(self):
        print('feature 4 is working from class b')

class C(B,A):
    def feature5(self):
        print('feature 5 is working from class c')

    
c1=C()
c1.feature3()
#the above is an example for multiple level inheritance
