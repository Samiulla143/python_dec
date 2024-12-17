#>>>>>>>>>>>>>>>>>>>>>>>NESTED IF<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# name = input('enter Your name:')
# exp = int(input(f'Enter {name} Experience:'))

# if exp>=1:
#     if exp>1 and exp<=5:
#         print('Salary is 25k')
#     elif exp>=6 and exp<=10:
#         print('Salary is 50k')
#     else:
#         print('Salary is 75k')
# else:
#     print('Not Eligible')
    
    
#>>>>>>>>>>>>>>>>>>>>>>>>BLUEPRINT OF PHONEPE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# while True:
#     print('1.Payment Filed')
#     print('2.Profile and Privacy')
#     print('3.Money Transfer')
#     print('4.exit')

#     user_inp=int(input('enter Your Choice:'))
#     if user_inp==1:
#         print('welcome to payment failed')
#     elif user_inp==2:
#         print('welcome to profile and privacy')
#     elif user_inp==3:
#         print('welcome to money transfer')
#     elif user_inp==4:
#         print('exit')
#         break


while True:
    print('1.Payment Filed')
    print('2.Profile and Privacy')
    print('3.Money Transfer')
    print('4.exit')

    user_inp=int(input('enter Your Choice:'))
    if user_inp==1:
        print('welcome to payment failed')
        print('1.Issues with failed payment')
        print('2.Issues with pending payment')
        print('3.Issues with succesful payment')
        print('4.Issues with payment made to merchants')
    elif user_inp==2:
        print('welcome to profile and privacy')
    elif user_inp==3:
        print('welcome to money transfer')
    elif user_inp==4:
        print('exit')
        break
