class student:
    def __init__(self,name,srn):
        self.name=name
        self.srn=srn
        self.lap=self.laptop()#outer classes will have a link to inner class

    
    def show(self):
        print(self.name,self.srn)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand='hp'
            self.ram=8
            self.strge=100
        
        def show(self):
            print(self.brand,self.ram,self.strge)

s1=student('thaurn',89)

'''lap1=s1.lap
print(id(lap1))

lap2=student.laptop()
print(lap2)#you can create object of inner class outside of the outer class provided that you use outer class name to call it'''
s1.show()