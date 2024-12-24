
#>>>>>>>>>>>>>>>>>> QUIZ APPLications <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

corr_ans=0
wrong_ans=0

print('1.what is the capital of india?')
inp=input('enter ans:').lower()
print(inp)
if inp=='delhi':
    corr_ans +=1
    print('Correct asn')
else:
    wrong_ans +=1
    print('wrong ans')
print('2.what is capital of karnataka?')
inp1=input('enter ans:').lower()
print(inp1)
if inp1=='bengaluru':
    corr_ans +=1
    print('correct ans')
else:
    wrong_ans +=1
    print('wrong ans')
print('percemtage',((corr_ans/(corr_ans+wrong_ans))*100))