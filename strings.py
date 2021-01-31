name = "Siya"
age = 19

# Concatenate
print("Hello, My name is " +name+ " and I am " +str (age) )



# String Formating

# Arguments by Position
print("My name is {name} and I am {age}".format(name=name, age=age))

# F-Strings
print(f"Hello, My name is {name} and I am {age}")



# String Methods
s = "hello universe"

# Capitalize
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('universe', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('e'))

# Split into a list
print(s.split())

# Find position
print(s.find('e'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())