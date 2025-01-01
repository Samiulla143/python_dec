# tkts=[1,2,3,4,5]
# print('Available Tickets', tkts)
# user_inp = int(input('Enter quantity of tickets u wnanna buy:'))
# for x in range(user_inp):
#     ticket_num = int(input('enter ticket number:'))
#     tkts.remove(ticket_num)
# print('Available tkts', tkts)


# >>>>>>>>>>>>>>>>>> SETS<<<<<<<<<<<<<<<<<<<<<<<

# to get non duplicate values
# lst=[1,2,3,3,4,5,5,6]
# emp_list=[]
# for x in lst:
#     if x not in emp_list:
#         emp_list.append(x)
# print(emp_list)

# compressed form

# lst=[1,2,3,3,4,5,5,6]
# emp_list=[]
# [emp_list.append(x) for x in lst if x not in emp_list]
# print(emp_list)

# to get duplicate values
lst=[1,2,3,3,4,5,5,6]
emp_list=[]
dup_list=[]
for x in lst:
    if x in emp_list:
        dup_list.append(x)
    else:
        emp_list.append(x)
print(dup_list)