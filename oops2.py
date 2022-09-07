class computer:

    def __init__(self,cpu,ram): #init is used to initailse the variables and it will be called automatically 
            #above cpu and ram are passed as an argument to be a part of object we need to assign it an object
            #self is used to specify to which object should the pointer point to 
        self.cpu=cpu #hence the object here is self 
        self.ram=ram
        #self is the object here and we are assigning the cpu and ram to the object 
    def config(self): #we have to specifically call config to exectue its code unlike init
        print("config of comp is",self.cpu,self.ram) #here cpu an ram do not belong to this mehod they are just objects and hence we are linking it to self to fetch the values

#this is called oject creation an object comp is being created 
com1=computer("i5",16) #this will call init by itself here we are passing two arguments where we havw mentioned three in init thats cux when we are calling computer we are automatically passing com1 aka self as an argument 
com1.config()


