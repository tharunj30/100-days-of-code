nums=[1,2,3,34]
# print(nums)
# print(nums[-1])
# print(nums[2:])
names=['tharun','kumar','s j']
# print(names)
values=[9.8,'tharun',890]
mil=[nums,values]
print(mil)
nums.append(789)
# print(nums)
nums.insert(3,1890)
# print(nums)
nums.pop(2)
# print(nums)
nums.pop()#removes the last element 
# print(nums)
del nums[1:] #to delete muliple numbers
# print(nums)
#to add multiple numbers
nums.extend([29,390])
# print(nums)
# print(min(nums))
# print(max(nums))
nums.sort()
# print(nums)
#tuples are immutable whereas lsit are mutable
#iterations are faster in tuples than in lists

tup = (10,29,30)
# print(tup)
#sets uses concept called hash and hence we never know what is the output when we print the set
s = {22,3,34,546,6,23}
print(s)