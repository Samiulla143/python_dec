# class maths:
#     def __init__(self):
#         self.sub_name='maths'
#     def add(self):
#         a,b=10,20
#         print(a+b)
# m1=maths()
# m1.add()

class instagram:
    def __init__(self):
        self.instagram_version=2        #instance variable
        self.instagram_developer='md' #instance variable
    def authentication(self):           #local method name
        usr=input('enter username:')
        pas=int(input('enter password:'))
        # print(f'Username with 123: {usr}')

        if usr == 'sami123' and pas == 1234:
            print('Authentication successful.')
        else:
            print('Authentication failed. Username or password is incorrect.')

insta_app = instagram()
insta_app.authentication()
        
        
