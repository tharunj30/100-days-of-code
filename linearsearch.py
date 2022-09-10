
pos=-1
def search(list,n):
    i=0
    # while i <(len(list)):
    #     if list[i]==n:
    #         globals()['pos']=i
    #         return True
    #     i+=1
    # return False
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
    return False

list=[1,2,3,4,5,6,7,8,9,10,11,12]
n=10
if search(list,n):
    print('found at',pos+1)
else:
    print('not found')
