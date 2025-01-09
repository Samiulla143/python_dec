# val1=[10,20,30,40,50]
# val2=val1[:]
# print(val1)
# print(val2)

'''global dictionary - used to reduce memory allocation'''

# a=10
# b=10
# print(a is b)
# print(id(a))
# print(id(b))

# list1=[[10,20],[30,40]]
# list2=list1
# list1[1][0]=300
# print(list1)
# print(list2)

'''shallow copy'''
import copy
# list1=[[10,20],[30,40]]
# list2=copy.copy(list1)
# list1[1][0]=300
# print(list1)
# print(list2)

'''deepcopy'''
# list1=[[10,20],[30,40]]
# list2=copy.deepcopy(list1)
# list1[1][0]=300
# print(list1)
# print(list2)

''' enumerate: gives postion and postion value'''
# lst=[10,20,30,40,50]
# for i,j in enumerate(lst):
#     print(i,j)
    
lst=[10,20,30,40,50,20]
print(lst.count(20))
print(lst.index(20))
print(lst.index(40))


