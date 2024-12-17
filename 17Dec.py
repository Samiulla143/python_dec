
name = input('enter Your name:')
exp = int(input(f'Enter {name} Experience:'))

if exp>=1:
    if exp>1 and exp<=5:
        print('Salary is 25k')
    elif exp>=6 and exp<=10:
        print('Salary is 50k')
    else:
        print('Salary is 75k')
else:
    print('Not Eligible')