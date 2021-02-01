# Create class
class User:

    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

        self._private = 1000

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

   # function for encap variable
    def print_encap(self):
        print(self._private)

# Extend class


class Customer(User):
    # Constructor
    def __init__(self, name, email, age):

        User.__init__(self, name, email, age)
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


#  Init user object
akai = User('Akanksha Tiwari', 'ak_tiwari@gmail.com', 19)
# Init customer object
utk = Customer('Utkarsh Tiwari', 'utk@yahoo.com', 25)

utk.set_balance(500)
print(utk.greeting())

akai.has_birthday()
print(akai.greeting())

# Encapsulation -->
akai.print_encap()
akai._private = 800
akai.print_encap()

# Method inherited from parent

utk.print_encap()
utk._private = 600
utk.print_encap()

akai.print_encap()
