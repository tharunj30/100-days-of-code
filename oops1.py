class computer: #class is a blue print of a phone i.e unique whereas the object is an instance
    def config(self):
        print("i5,1TB")
    #method in class is aka function
x=1
print(type(x))
com1=computer()
print(type(com1))

computer.config(com1)
#so here we are calling config method to call this we have to specify the class name and then pass the onject as a parameter
#we can also do this
com1.config()
#here in the bg com1 automatically belongs to computer class and hence calls computer and the method config is called more often the above way is used 
