# num = int (input('enter the amont:'))

# tax= num*(18/100)

# print('tax amount',tax)



#2nd Prog

ip1 = int(input('enter one num:'))
ip2 = int(input('enter second num:'))

add = ip1+ip2
sub = ip1-ip2
mul = ip1*ip2
div = ip1/ip2

operation = input('what do you wnat to calculate:'
                  'add'
                  'sub'
                  'mul'
                  'div')


if operation == add:
    print(add)
elif operation == sub:
    print(sub)
elif operation == mul:
    print(mul)
elif operation == div:
    print(div)
