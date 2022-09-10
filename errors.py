#types of errors are 
#compile time=>syntax error as they are found during compiling time
#run time error is mainly cuz of it never stops running the program like zero division
#logical error =>code gets compiled we will get an output butthe output is wrong
a=5
b=2

try:
    print('resource opened')
    print(a/b)
    k=int(input("enter a number"))
    print(k)
    
except ZeroDivisionError as e:
    print("hey dont enter the number zero for division",e)
except Exception as e:
    print("something went wrong") 

finally:  #finally would be executed for sure 
    print('resource closed')