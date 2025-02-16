a=int(input('enter a number:'))
b=int(input('enter another number:'))
print('addition is:',a+b)



def rev_str(input_string):
    rev_str = ""
    for char in input_string:
        rev_str = char + rev_str
    return rev_str

original_string = input("Enter a string: ")
print("Reversed string:", rev_str(original_string))

