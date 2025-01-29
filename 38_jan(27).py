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





class User:
    def __init__(self, user_name, plan, user_id):
        self.user_name = user_name
        self.plan = plan
        self.user_id = user_id
        self.lst = [111, 222, 333]
        self.is_prime_user = self.check_prime_user()

    def check_prime_user(self):
        if self.plan == 'prime' and self.user_id in self.lst:
            print('You are a prime member')
            return True
        else:
            print('Invalid prime user')
            return False


class Booking(User):
    def __init__(self, user_name, plan, user_id):
        super().__init__(user_name, plan, user_id)
        self.tkt_available_on = [25, 26, 27, 28, 29]
        self.tickets = [1, 2, 3, 4, 5]

    def show_dates(self):
        print('Available travel dates:', self.tkt_available_on)

    def show_seats(self):
        print('Available seats:', self.tickets)

    def book_ticket(self):
        if self.is_prime_user:
            print('You are eligible for a 10% discount.')
        else:
            print('No discount available for your plan.')

        self.show_dates()

        # Loop until a valid date is entered
        while True:
            try:
                user_inp_date = int(input('Enter date of travel: '))
                if user_inp_date in self.tkt_available_on:
                    print('Date is available.')
                    break
                else:
                    print(f'Date not available, please select from {self.tkt_available_on}')
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        # Loop for ticket booking
        while True:
            try:
                user_inp = int(input('Enter quantity of tickets: '))
                if 1 <= user_inp <= len(self.tickets):
                    break
                else:
                    print(f'Invalid quantity. Available tickets: {len(self.tickets)}')
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        # Calculate cost and show discount if applicable
        total_cost = user_inp * 100  # Assuming each ticket costs 100 units
        if self.is_prime_user:
            discount = total_cost * 0.10
            total_cost -= discount
            print(f'Total cost after discount: {total_cost}')
        else:
            print(f'Total cost: {total_cost}')

        # Seat booking
        for _ in range(user_inp):
            while True:
                try:
                    ticket_num = int(input('Enter seat number: '))
                    if ticket_num in self.tickets:
                        print(f'Ticket {ticket_num} is booked.')
                        self.tickets.remove(ticket_num)
                        break
                    else:
                        print('Seat not available. Please choose another.')
                except ValueError:
                    print('Invalid input. Please enter a valid seat number.')

        # Show updated seat availability
        self.show_seats()


# Get user details and create a booking instance
user_name = input('Enter user name: ')
plan = input('Enter plan (normal, prime): ').lower()
try:
    user_id = int(input('Enter ID: '))
    ola = Booking(user_name, plan, user_id)
    ola.book_ticket()
except ValueError:
    print('Invalid ID. Please enter a numeric value.')










        

