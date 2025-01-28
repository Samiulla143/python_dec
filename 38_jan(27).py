# class flipkart():
#     def __init__(self):
#         self.brand_name='wipro'
#         print(self.brand_name)
# f1=flipkart()
# f2=flipkart()
# f3=flipkart()
# f4=flipkart()

# class flipkart():
#     def __init__(self):
#         self.brand_name='wipro'
#         print(self.brand_name)
#     def show(self):
#         global price          #global variable
#         price=1000
#         print(price)
#     def add(self):
#         print(price)
# f1=flipkart()
# f1.show()
# f1.add()

tickets=[1,2,3,4,5]
def show():
    for x in tickets:
        print(x)
    
class booking:
    def book_ticket(self):
        show()
        user_inp = int(input('Enter quantity of ticket:'))
        for x in range(user_inp):
            ticket_num = int(input('enter seat number:'))
            if ticket_num in tickets:
                print('ticket is booked')
                tickets.remove(ticket_num)
            else:
                print('ticket not available')
        show()
        
ola=booking()
ola.book_ticket()







        

