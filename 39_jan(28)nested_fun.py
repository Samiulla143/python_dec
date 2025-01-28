# def add():
#     a,b=10,20
#     print(a+b)
#     def sub():
#         c=(a-b)
#         print(c)
#     sub()
# add()

# def add():
#     a,b=10,20
#     print(a+b)
# add()
# print(add) # gives address of it- hexdecimal value



def alpha(beta):  #carried the address of beta function
    print("alpha")
    beta() # calling beta function
def beta():
    print("beta")
alpha(beta) #sending address of beta function to alpha function

#output- #calling one function inside another function



#list=[1,2,5,6] get produt and the sum
prod=1
sum=0

for x in [1,2,5,6]:
    sum=sum+x
    prod=prod*x
print(sum)
print(prod)
