# num = int(input('enter a num:'))
# if num <0:
#     print(num ,' is a negative number')
# elif num >0:
#     print(num, ' is a positive number')
# else:
#     print('Neutral')


m1 = int(input('enter marks of Maths:'))
m2 = int(input('enter marks of physics:'))
m3 = int(input('enter marks of chmistry:'))

total_marks = 600

percentage = ((m1+m2+m3)/total_marks)*100
print(f"percentage: {percentage:.2f}%")

if percentage<35:
    print('Fail')
#elif percentage in range(35,51):
elif percentage>=35 and percentage<=50:
    print('Grade-C')
elif percentage>50 and percentage<=90:
    print('Grade-B')
elif percentage>90 and percentage<=100:
    print('Grade-A')
else:
    print('Invalid percentage')
