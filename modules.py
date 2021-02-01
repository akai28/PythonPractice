# Core modules
from validator import validate_email
import validator
from camelcase import CamelCase
import datetime
from datetime import date
import time
from time import time


# Today's Date
import datetime

today = datetime.date.today()
print(today)

# Timestamp
today = date.today()
timestamp = time()

print(timestamp)

# Pip module
# Import custom module

c = CamelCase()
print(c.hump('hello there world'))

email = 'test#test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Invalid Email')
