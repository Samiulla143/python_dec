# num = int(input('enter a num:'))
# if num <0:
#     print(num ,' is a negative number')
# elif num >0:
#     print(num, ' is a positive number')
# else:
#     print('Neutral')

#-------------------------------------------------------

# m1 = int(input('enter marks of Maths:'))
# m2 = int(input('enter marks of physics:'))
# m3 = int(input('enter marks of chmistry:'))

# total_marks = 600

# percentage = ((m1+m2+m3)/total_marks)*100
# print(f"percentage: {percentage:.2f}%")

# if percentage<35:
#     print('Fail')
# elif percentage>=35 and percentage<=50:
#     print('Grade-C')
# elif percentage>50 and percentage<=90:
#     print('Grade-B')
# elif percentage>90 and percentage<=100:
#     print('Grade-A')
# else:
#     print('Invalid percentage')

#---------------------------------------------------------

usd_to_inr=84.89

try:
    age = int(input('Enter Your Age:'))
except ValueError:
    print('Enter valid age')
    exit()

if age>=18 and age<=30:
    usd_price = 5
elif age>=31 and age<=50:
    usd_price = 20
elif age>50:
    usd_price = 0
else:
    print(f'{age} is not eligible')
    exit()
    
Indian_Rupees = usd_price * usd_to_inr

if usd_price == 0: 
    print("The ticket is free!") 
elif usd_price==5: 
    print(f"The ticket price in Indian Rupees:",Indian_Rupees) 
else:
    print(f"The ticket price in Indian Rupees: ₹{Indian_Rupees:.2f}")
