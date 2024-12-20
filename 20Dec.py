
#>>>>>>>>>>>>>>>>>>>> IN BUILT FUNCTIONS IN STRINGS <<<<<<<<<<<<<<<<<<<

# Upper,lower,swap case,title case, alpha numeric, all num, chr, 
# ordinal, split, r strip, l strip, strip, unicode, asciicode

# print('hello😍'.upper())
# print('HELLO😍'.lower())

# print('A','ord-->',ord('A'))
# print('a','ord-->',ord('a'))

# print(65,'chr-->',chr(65))
# print(97,'chr-->',chr(97))


# val= 'ABC'
# for x in val:
#     ord_val=ord(x)
#     conv_chr=ord_val+32
#     print(chr(conv_chr))

val='ABC$TuuO'
for x in val:
    ord_val=ord(x)
    if ord_val in range(65,91):
        print(chr(ord_val+32), end='')
    elif ord_val in range(97,123):
        print(chr(ord_val-32),end='')
    else:
        print(x,end='')