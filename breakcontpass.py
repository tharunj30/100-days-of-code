'''av=5
# x=int(input('enter number of candies'))
i=1
while i<=x:
    if i>av:
        # print('out of candies')
        break
    # print('candy')
    i+=1'''



for x in range(0,100):
    if x%3==0 or x%5==0:
        continue
    print(x)
    
print('bye')

for x in range(0,100):
    if x%3==0 and x%5==0:
        continue
    print(x)
    
print('bye')

for x in range(0,100):
    if x%2!=0:
        pass
    else:
        print(x)
    
print('bye')