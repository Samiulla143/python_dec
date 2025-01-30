'''
class customer:
    def __init__(self):
        self.name=Name
        self.ph=ph
        self.mail=mail
class platinumuser:
    def __init__(self,name,ph,mail):
        super().__init__(name,ph,mail)
        self.plat_id=plat_id
        
    def display(self):
        super().display_info()
        print(f"Platinum ID: {self.plat_id}")

# Example usage
customer1 = Customer("Alice", "1234567890", "alice@example.com")
platinum_user1 = PlatinumUser("Bob", "0987654321", "bob@example.com", "PLAT123")

customer1.display_info()
platinum_user1.display_info()
    
    
#polymorphism:one code in many ways

#method overloading : python never supports overloading
#method overriding :same method names  diffrent parameters is called as method overriding'''

# class Messenger:
#     def use_keyboard(self):
#         print('Using keyboard')

#     def send_message(self): 
#         print('Text message sent')

#     def receive_message(self): 
#         print('Text message received')

# class WhatsApp(Messenger):
#     def send_message(self): 
#         print('Text, video & audio sent using WA')

#     def receive_message(self):
#         print('Text, video & audio received using WA')

# class FacebookMessenger(Messenger):
#     def send_message(self): 
#         print('Text, video & audio sent using FB')

#     def receive_message(self): 
#         print('Text, video & audio received using FB')

# class InstaMessenger(Messenger):
#     def send_message(self): 
#         print('Text, video & audio sent using Insta')
#     def receive_message(self): 
#         print('Text, video & audio received using Insta')

# def use_message(ref):
#     ref.use_keyboard()
#     ref.send_message()
#     ref.receive_message()

# WA = WhatsApp()
# FB = FacebookMessenger()
# IM = InstaMessenger()

# use_message(WA)
# use_message(FB)
# use_message(IM)


# -------------------------------------------------------------------------------------------------------------------------

# class Messenger:

#     def use_keyboard(self): 
#         print('Using keyboard')

#     def send_message (self): 
#         print('Text messge sent')

#     def receive_message (self): 
#         print('Text messge received')

# class WhatsApp(Messenger):

#     def send_message (self): 
#         print('Text, video & audio sent using WA')

#     def receive_message (self): 
#         print('Text, video & audio receive using WA')

#     def send_live_location (self): 
#         print('Live location sent using WA')

# class FacebookMessenger(Messenger):

#     def send_message (self): 
#         print('Text, video & audio sent using FB')

#     def receive_message (self): 
#         print('Text, video & audio receive using FB')

#     def use_builtin_apps (self): 
#         print('Using biiltin apps using FB')

# class InstagramMessenger (Messenger):

#     def send_message (self):

#         print('Text, video & audio sent using Insta')

#     def receive_message (self): 
#         print('Text, video & audio receive using Insta')

#     def add_filters (self): 
#         print('Filters using Insta')

# def use_message (ref):

#     ref.use_keyboard()

#     ref.send_message()

#     ref.receive_message()

#     if type(ref) == WhatsApp:

#         ref.send_live_location()

#     if type(ref) == FacebookMessenger:

#         ref.use_builtin_apps()

#     if type(ref) == InstagramMessenger:

#         ref.add_filters()

# wa = WhatsApp()

# fb = FacebookMessenger()

# insta = InstagramMessenger()

# use_message(wa)

# use_message(fb)

# use_message(insta)






'''1.examples of real time application using inheritance in python.
2. python program using inheritance of the hotel application(customer,prime customer, staff).
3.how to achieve inheritance with the help of data base (sqlite3 and python connection)

1. Real-time Applications Using Inheritance in Python
Inheritance allows you to create a new class based on an existing class, enabling code reusability and a hierarchical class structure. Some real-time applications include:

Banking System: Different types of accounts (savings, current, fixed deposit) can inherit from a base account class.'''


'''Online Shopping: Different user roles (buyer, seller, admin) can inherit from a base user class.

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}, Email: {self.email}")

class Buyer(User):
    def __init__(self, username, email, cart):
        super().__init__(username, email)
        self.cart = cart

    def add_to_cart(self, item):
        self.cart.append(item)
        print(f"Added {item} to cart.")

class Seller(User):
    def __init__(self, username, email, store_name):
        super().__init__(username, email)
        self.store_name = store_name
        self.inventory = []

    def add_inventory(self, item):
        self.inventory.append(item)
        print(f"Added {item} to inventory.")

class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def manage_user(self, user):
        print(f"Managing user: {user.username}")

# Example usage
buyer = Buyer("buyer01", "buyer@example.com", [])
seller = Seller("seller01", "seller@example.com", "BestStore")
admin = Admin("admin01", "admin@example.com")

buyer.display_info()
buyer.add_to_cart("Laptop")

seller.display_info()
seller.add_inventory("Smartphone")

admin.display_info()
admin.manage_user(buyer)


Game Development: Different game characters (player, enemy, NPC) can inherit from a base character class.

Content Management Systems: Different types of content (article, blog post, news) can inherit from a base content class.

Library Management System: Different types of items (books, magazines, journals) can inherit from a base item class.

#2. Python Program Using Inheritance for a Hotel Application
class Customer:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class PrimeCustomer(Customer):
    def __init__(self, name, age, gender, membership_id):
        super().__init__(name, age, gender)
        self.membership_id = membership_id

    def display_info(self):
        super().display_info()
        print(f"Membership ID: {self.membership_id}")

class Staff:
    def __init__(self, name, age, gender, employee_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Employee ID: {self.employee_id}")

# Example usage
customer1 = Customer("Alice", 30, "Female")
prime_customer1 = PrimeCustomer("Bob", 40, "Male", "PM123")
staff1 = Staff("Charlie", 35, "Male", "ST456")

customer1.display_info()
prime_customer1.display_info()
staff1.display_info()





3. Achieving Inheritance with the Help of a Database To achieve inheritance with the help of a database, 
you can use object-relational mapping (ORM) tools like SQLAlchemy in Python. ORM allows you to map class
inheritance hierarchies to database tables. Here's a basic example:


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

class PrimeCustomer(Customer):
    __tablename__ = 'prime_customers'
    id = Column(Integer, primary_key=True)
    membership_id = Column(String)

# Setup the database engine
engine = create_engine('sqlite:///hotel.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a prime customer
prime_customer = PrimeCustomer(name="Bob", age=40, gender="Male", membership_id="PM123")
session.add(prime_customer)
session.commit()

# Query the database
for customer in session.query(Customer).all():
    print(customer.name, customer.age, customer.gender)

'''