# atoms=[1,66,4,56,88,99]
# # print(atoms.sort())
# # print(atoms[0]+ atoms[-1])
# print(min(atoms))
# print(max(atoms))
# # print(atoms[0])


# val = [1,3,4,5,6,7]
# emp_list =[]
# for i in val:
#     if i%2==1:
#         emp_list.append(i)
#     else:
#         pass
# print(emp_list)

#resuced form of above pgm
print([x for x in [1,3,4,5,6,7] if x%2==1])

print([f'{x} is even' if x%2==0 else f'{x} is odd' for x in range(1,9)])


        