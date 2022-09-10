f=open('data.txt','r')
# print(f.read(),end='#')
print(f.readline())

f1=open('tharun','w')
for data in f:
    f1.write(data)

#python is boht complied and interpreted language
#first the code get compiled by complier and turn into byte code which is then interpreted by the interpretor 