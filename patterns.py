for i in range(4):
    for j in range(4):
        print('#',end='')
    print()

print('bye')
#to print hashtags in form of a triangle
for i in range(4):
    for j in range(i+1):
        print('#',end='')
    print()
print() 

#to print triangle in reverse order

for i in range(4):
    for j in range(4-i):
        print('#',end='')
    print()