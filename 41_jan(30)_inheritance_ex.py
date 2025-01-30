'''1. Real-time Applications Using Inheritance in Python
Inheritance allows you to create a new class based on an existing class, enabling code reusability and a hierarchical class structure. Some real-time applications include:

Banking System: Different types of accounts (savings, current, fixed deposit) can inherit from a base account class.

Online Shopping: Different user roles (buyer, seller, admin) can inherit from a base user class.

Game Development: Different game characters (player, enemy, NPC) can inherit from a base character class.

Content Management Systems: Different types of content (article, blog post, news) can inherit from a base content class.

Library Management System: Different types of items (books, magazines, journals) can inherit from a base item class.'''


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




'''
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