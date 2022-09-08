class A: #A is super class 
#MRo stands for method resoltion order that means it will run the left side first and then the right side 
    def __init__(self):
        print("init from class A")

    def feature1(self):
        print('feature 1 is working from class a')

    def feature2(self):
        print('feature 2 is working from class a')

class B():
    def __init__(self):
        super().__init__()
        print("init from class B")

    def feature3(self):
        print('feature 3 is working from class b')

    def feature4(self):
        print('feature 4 is working from class b')

class C(A,B):
    def __init__(self):
        super().__init__() #when we give a super class of both a and b we are baised towards a aka grandparent class
        print("init from class c")

    def feature5(self):
        print('feature 5 is working from class c')

    def feature6(self):
        print('feature 6 is working from class c')
    
b1=C()
# b1.feature3()
#the above is an example for multiple level inheritance
